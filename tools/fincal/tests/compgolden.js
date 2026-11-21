const fs = require("fs"), path = require("path");
const { calculate } = require(process.argv[2]);
const F = { MONTHLY: "m", QUARTERLY: "q", YEARLY: "y" };
let pass = 0, fail = 0;
for (const f of fs.readdirSync(process.argv[3]).filter(f => f.includes("comp_"))) {
  const lines = fs.readFileSync(path.join(process.argv[3], f), "utf8").split(/\r?\n/);
  const kv = {}, years = [], sum = {}; let header = null;
  for (const l of lines) {
    const c = l.split(",").map(x => x.replace(/^"|"$/g, ""));
    if (c[0] === "index") { header = c; continue; }
    if (!header) { if (c[0]) kv[c[0]] = c[1]; continue; }
    if (c[9] && /^\d+$/.test(c[9])) years.push({ year: +c[9], contributed: +c[10], interest: +c[11], endValue: +c[12] });
    if (c[0] && !/^\d+$/.test(c[0])) sum[c[0]] = c[1];
  }
  const r = calculate(+kv.initial, +kv.contribution, F[kv.contributionFrequency], F[kv.compoundFrequency], kv.contributionTiming === "BEGIN" ? "begin" : "end", +kv.annualRatePercent, +kv.years);
  const errs = [];
  years.forEach(e => { const g = r.byYear[e.year - 1]; if (!g || g.contributed !== e.contributed || g.interest !== e.interest || g.endValue !== e.endValue) errs.push(e.year); });
  if (sum.futureValue && r.futureValue != +sum.futureValue) errs.push("fv " + r.futureValue + " vs " + sum.futureValue);
  if (sum.totalInterest && r.totalInterest != +sum.totalInterest) errs.push("ti");
  if (errs.length) { fail++; console.log("FAIL", kv.id, errs.slice(0, 5)); } else { pass++; console.log("ok  ", kv.id, years.length + " years", sum.futureValue ? "fv " + sum.futureValue : ""); }
}
console.log({ pass, fail });
