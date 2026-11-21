/* Fincal prepayment article: engine + calculator. Same monthly maths and HALF_UP rounding as loan.js.
   Amounts are integers in the smallest currency unit. */
(function () {
  "use strict";

  function roundHalfUp(v) { return Math.floor(v + 0.5); }
  function halfUpDiv(a, b) { var q = Math.floor(a / b), r = a - q * b; return r * 2 >= b ? q + 1 : q; }
  function annuityPayment(bal, rate, n) {
    var i = rate / 1200;
    if (i === 0) return halfUpDiv(bal, n);
    return roundHalfUp(bal * i / (1 - Math.pow(1 + i, -n)));
  }

  /** Runs a schedule. keep: fixed payment (annuity) or fixed principal (equal); when given, the loan
      simply ends earlier, otherwise the last of n months clears the balance. */
  function run(bal, rate, n, method, keep) {
    var i = rate / 1200, step = keep || (method === "annuity" ? annuityPayment(bal, rate, n) : halfUpDiv(bal, n));
    var pays = [], ends = [], interest = 0;
    for (var m = 1; bal > 0 && m <= n; m++) {
      var int = roundHalfUp(bal * i), p = method === "annuity" ? step - int : step;
      if (p > bal || m === n) p = bal;
      bal -= p; interest += int;
      pays.push(p + int); ends.push(bal);
    }
    return { months: pays.length, interest: interest, pays: pays, ends: ends, first: pays[0] || 0 };
  }

  /** Yearly rate earned by paying `cost` now to save the monthly differences between two schedules. */
  function yieldOf(cost, base, other) {
    function npv(r) {
      var s = -cost;
      for (var t = 0; t < base.pays.length; t++) s += (base.pays[t] - (other.pays[t] || 0)) / Math.pow(1 + r, t + 1);
      return s;
    }
    if (cost <= 0) return 0;
    var lo = -0.05, hi = 0.2;
    for (var k = 0; k < 100; k++) { var mid = (lo + hi) / 2; if (npv(mid) > 0) lo = mid; else hi = mid; }
    return (lo + hi) / 2 * 1200;
  }

  /** bal, extra in smallest units; rate yearly %; fee % of the amount prepaid. */
  function prepay(bal, rate, n, method, extra, feePct) {
    extra = Math.min(extra, bal);
    var fee = roundHalfUp(extra * feePct / 100), rest = bal - extra;
    var base = run(bal, rate, n, method);
    var keep = method === "annuity" ? annuityPayment(bal, rate, n) : halfUpDiv(bal, n);
    var shorter = run(rest, rate, n, method, keep), lower = run(rest, rate, n, method);
    function pack(x) {
      var saved = base.interest - x.interest;
      return { saved: saved, net: saved - fee, months: x.months, first: x.first, yield: yieldOf(extra + fee, base, x), ends: x.ends };
    }
    return { fee: fee, rest: rest, base: { interest: base.interest, months: base.months, first: base.first, ends: base.ends },
      shorter: pack(shorter), lower: pack(lower) };
  }

  if (typeof module !== "undefined" && module.exports) module.exports = { prepay: prepay };
  if (typeof document === "undefined") return;

  // ---- Calculator: locale and strings come from data-* on [data-prepay] ----
  var root = document.querySelector("[data-prepay]");
  if (!root) return;
  var ds = root.dataset, scale = Number(ds.scale) || 1, div = Number(ds.div) || 1;
  var $ = function (id) { return root.querySelector("#" + id); };
  var nf = new Intl.NumberFormat(ds.locale, { maximumFractionDigits: 0 });
  var nfm = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: Number(ds.dec), maximumFractionDigits: Number(ds.dec) });
  var nf1 = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  function money(v) {
    var s = nfm.format(v / scale);
    return !ds.cur ? s : ds.pre === "1" ? ds.cur + " " + s : s + " " + ds.cur;
  }
  function amount(el) { var d = String(el.value).replace(/\D/g, ""); return d ? Number(d) : NaN; }
  function num(el) { return parseFloat(String(el.value).replace(",", ".")); }
  function months(n) { return (n === 1 ? ds.m1 : ds.mn).replace("{n}", nf.format(n)); }
  ["pp-bal", "pp-extra"].forEach(function (id) {
    $(id).addEventListener("blur", function () { var v = amount(this); if (isFinite(v)) this.value = nf.format(v); });
  });

  function update() {
    var bal = amount($("pp-bal")), rate = num($("pp-rate")) * div, n = Math.floor(num($("pp-term")));
    var extra = amount($("pp-extra")), fee = num($("pp-fee")), method = $("pp-method").value;
    var ok = bal > 0 && bal <= 1e15 && rate >= 0 && rate <= 120 && n >= 1 && n <= 600 &&
      extra > 0 && fee >= 0 && fee <= 20;
    var outs = root.querySelectorAll("[data-out]");
    if (!ok) { outs.forEach(function (o) { o.textContent = "-"; }); return; }
    var r = prepay(bal * scale, rate, n, method, extra * scale, fee);
    var cut = n - r.shorter.months;
    var v = {
      fee: money(r.fee),
      "s-saved": money(r.shorter.saved), "l-saved": money(r.lower.saved),
      "s-net": money(r.shorter.net), "l-net": money(r.lower.net),
      "s-what": r.rest === 0 ? ds.paidoff : ds.cut.replace("{m}", months(cut)),
      "l-what": r.rest === 0 ? ds.paidoff : ds.newpay.replace("{v}", money(r.lower.first)),
      "s-yield": nf1.format(r.shorter.yield / div) + ds.sfx, "l-yield": nf1.format(r.lower.yield / div) + ds.sfx
    };
    outs.forEach(function (o) { o.textContent = v[o.getAttribute("data-out")]; });
    var link = $("pp-link");
    link.hidden = r.rest === 0;
    link.href = ds.path + "?amount=" + r.rest / scale + "&rate=" + +rate.toFixed(4) + "&term=" + n + "&unit=m&method=" + method;
  }
  root.querySelectorAll("input, select").forEach(function (el) { el.addEventListener("input", update); });
  update();
})();
