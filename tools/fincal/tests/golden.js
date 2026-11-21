const fs = require("fs"), path = require("path");
const { calculate } = require(process.argv[2]);
const M = { ANNUITY: "annuity", EQUAL_PRINCIPAL: "equal", FLAT: "flat" };
let pass = 0, fail = 0, skip = 0;
for (const f of fs.readdirSync(process.argv[3]).filter(f => f.includes("loan_"))) {
  const lines = fs.readFileSync(path.join(process.argv[3], f), "utf8").split(/\r?\n/);
  const kv = {}; const rows = []; let header = null; const sum = {};
  for (const l of lines) {
    const c = (l.match(/("[^"]*"|[^,]*)(,|$)/g) || []).map(x => x.replace(/,$/, "").replace(/^"|"$/g, "")).map(x => /^\$?[\d,]+(\.\d+)?$/.test(x) && x.includes("$") ? x.replace(/[$,]/g, "").replace(/\.00$/, "") : x);
    if (!c[0] || l.startsWith("#")) continue;
    if (c[0] === "index") { header = c; continue; }
    if (!header) kv[c[0]] = c[1];
    else if (/^\d+$/.test(c[0])) rows.push(Object.fromEntries(header.map((h, i) => [h, c[i]])));
    else sum[c[0]] = c[1];
  }
  const segs = (kv.rateSchedule || "").split(";").filter(Boolean);
  if (segs.length !== 1 || (kv.prepayments && kv.prepayments.trim())) { skip++; console.log("skip", kv.id); continue; }
  const r = calculate(+kv.principal, +segs[0].split(":")[1], +kv.termMonths, M[kv.method]);
  const errs = [];
  for (const e of rows) {
    const p = r.periods[+e.index - 1] || { p: 0, i: 0, pay: 0, end: 0 };
    if (p.pay != +e.payment || p.p != +e.principalPaid || p.i != +e.interestPaid || p.end != +e.endingBalance) errs.push(e.index);
  }
  if (sum.totalInterest && r.totalInterest != +sum.totalInterest) errs.push("totalInterest " + r.totalInterest + " vs " + sum.totalInterest);
  if (sum.effectiveAnnualRatePct && Math.abs(r.apr - +sum.effectiveAnnualRatePct) > 0.01) errs.push("apr " + r.apr + " vs " + sum.effectiveAnnualRatePct);
  if (errs.length) { fail++; console.log("FAIL", kv.id, errs.slice(0, 5)); } else { pass++; console.log("ok  ", kv.id, rows.length + " periods checked", sum.effectiveAnnualRatePct ? "apr " + r.apr.toFixed(4) : ""); }
}
console.log({ pass, fail, skip });
