/* Fincal article: savings interest paid monthly vs at maturity. Engine + calculator, HALF_UP rounding.
   Amounts are integers in the smallest currency unit; interest counted by months (rate * months / 12). */
(function () {
  "use strict";

  function roundHalfUp(v) { return Math.floor(v + 0.5); }

  /** amount over t months. end: yearly % paid at maturity; mon: yearly % paid every month;
      re: yearly % earned by putting each monthly payment into a rolling 1-month deposit. */
  function deposit(amount, t, end, mon, re) {
    var endI = roundHalfUp(amount * end * t / 1200), each = roundHalfUp(amount * mon / 1200);
    var q = re / 1200, pot = 0, pots = [], ends = [], factor = 0;
    for (var m = 1; m <= t; m++) {
      pot += roundHalfUp(pot * q) + each;
      pots.push(pot); ends.push(m === t ? endI : 0);
      factor += Math.pow(1 + q, t - m);
    }
    return { endI: endI, each: each, paid: each * t, pot: pot, extra: pot - each * t, gap: endI - pot,
      breakeven: end * t / factor, pots: pots, ends: ends };
  }

  if (typeof module !== "undefined" && module.exports) module.exports = { deposit: deposit };
  if (typeof document === "undefined") return;

  // ---- Calculator: locale and strings come from data-* on [data-deposit] ----
  var root = document.querySelector("[data-deposit]");
  if (!root) return;
  var ds = root.dataset, scale = Number(ds.scale) || 1;
  var $ = function (id) { return root.querySelector("#" + id); };
  var nf = new Intl.NumberFormat(ds.locale, { maximumFractionDigits: 0 });
  var nfm = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: Number(ds.dec), maximumFractionDigits: Number(ds.dec) });
  var nf2 = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  function money(v) {
    var s = nfm.format(v / scale);
    return !ds.cur ? s : ds.pre === "1" ? ds.cur + " " + s : s + " " + ds.cur;
  }
  function amount(el) { var d = String(el.value).replace(/\D/g, ""); return d ? Number(d) : NaN; }
  function num(el) { return parseFloat(String(el.value).replace(",", ".")); }
  $("dp-amount").addEventListener("blur", function () { var v = amount(this); if (isFinite(v)) this.value = nf.format(v); });

  function update() {
    var a = amount($("dp-amount")), t = Math.floor(num($("dp-term")));
    var end = num($("dp-end")), mon = num($("dp-mon")), re = num($("dp-re"));
    var ok = a > 0 && a <= 1e15 && t >= 1 && t <= 120 && [end, mon, re].every(function (r) { return r >= 0 && r <= 50; });
    var outs = root.querySelectorAll("[data-out]");
    if (!ok) { outs.forEach(function (o) { o.textContent = "-"; }); return; }
    var r = deposit(a * scale, t, end, mon, re);
    var v = {
      end: money(r.endI), each: money(r.each), pot: money(r.pot),
      gap: r.gap === 0 ? ds.same : (r.gap > 0 ? ds.endwins : ds.monwins).replace("{v}", money(Math.abs(r.gap))),
      breakeven: nf2.format(r.breakeven) + ds.sfx
    };
    outs.forEach(function (o) { o.textContent = v[o.getAttribute("data-out")]; });
  }
  root.querySelectorAll("input").forEach(function (el) { el.addEventListener("input", update); });
  update();
})();
