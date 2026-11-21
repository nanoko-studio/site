/* Fincal promo-then-floating rate article: engine + calculator. Same monthly maths and HALF_UP rounding as loan.js.
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

  /** n months; promo rate for the first k months, then the floating rate. Equal payments are worked out
      again on the remaining balance and term when the rate changes, as banks do. */
  function schedule(bal, n, method, promo, k, floating) {
    var start = bal, prin = halfUpDiv(bal, n), pay = annuityPayment(bal, promo, n);
    var pays = [], interest = 0, promoInterest = 0;
    for (var m = 1; m <= n && bal > 0; m++) {
      var rate = m <= k ? promo : floating;
      if (m === k + 1 && method === "annuity") pay = annuityPayment(bal, floating, n - k);
      var int = roundHalfUp(bal * rate / 1200), p = method === "annuity" ? pay - int : prin;
      if (p > bal || m === n) p = bal;
      bal -= p; interest += int; if (m <= k) promoInterest += int;
      pays.push(p + int);
    }
    var before = pays[Math.min(k, n) - 1] || 0, after = pays[k] || 0;
    return { pays: pays, interest: interest, promoInterest: promoInterest, first: pays[0], before: before, after: after,
      jump: after - before, total: start + interest };
  }

  if (typeof module !== "undefined" && module.exports) module.exports = { schedule: schedule };
  if (typeof document === "undefined") return;

  // ---- Calculator: locale and strings come from data-* on [data-teaser] ----
  var root = document.querySelector("[data-teaser]");
  if (!root) return;
  var ds = root.dataset, scale = Number(ds.scale) || 1, div = Number(ds.div) || 1;
  var $ = function (id) { return root.querySelector("#" + id); };
  var nf = new Intl.NumberFormat(ds.locale, { maximumFractionDigits: 0 });
  var nfm = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: Number(ds.dec), maximumFractionDigits: Number(ds.dec) });
  var nfp = new Intl.NumberFormat(ds.locale, { maximumFractionDigits: 0, signDisplay: "always" });
  function money(v) {
    var s = nfm.format(v / scale);
    return !ds.cur ? s : ds.pre === "1" ? ds.cur + " " + s : s + " " + ds.cur;
  }
  function amount(el) { var d = String(el.value).replace(/\D/g, ""); return d ? Number(d) : NaN; }
  function num(el) { return parseFloat(String(el.value).replace(",", ".")); }
  $("tz-amount").addEventListener("blur", function () { var v = amount(this); if (isFinite(v)) this.value = nf.format(v); });

  function update() {
    var bal = amount($("tz-amount")), n = Math.floor(num($("tz-term"))), method = $("tz-method").value;
    var promo = num($("tz-promo")) * div, k = Math.floor(num($("tz-months"))), fl = num($("tz-float")) * div;
    var ok = bal > 0 && bal <= 1e15 && n >= 2 && n <= 600 && k >= 1 && k < n &&
      promo >= 0 && promo <= 120 && fl >= 0 && fl <= 120;
    var outs = root.querySelectorAll("[data-out]");
    if (!ok) { outs.forEach(function (o) { o.textContent = "-"; }); return; }
    var r = schedule(bal * scale, n, method, promo, k, fl);
    var v = {
      before: money(r.before), after: money(r.after),
      jump: money(r.jump) + (r.before ? " (" + nfp.format(r.jump / r.before * 100) + "%)" : ""),
      interest: money(r.interest), total: money(r.total)
    };
    outs.forEach(function (o) { o.textContent = v[o.getAttribute("data-out")]; });
  }
  root.querySelectorAll("input, select").forEach(function (el) { el.addEventListener("input", update); });
  update();
})();
