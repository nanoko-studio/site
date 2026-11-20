/* Fincal guide pages: chart tooltips and the flat-rate converter. Runs in the browser only. */
(function () {
  "use strict";

  // ---- Tooltips: each .hit rect carries "Title|label|value|label|value" ----
  document.querySelectorAll(".chartbox").forEach(function (box) {
    var svg = box.querySelector("svg"), tip = box.querySelector(".tip"), on = null;
    if (!svg || !tip) return;
    function hide() { tip.hidden = true; if (on) on.classList.remove("on"); on = null; }
    function show(hit) {
      if (on === hit) return;
      if (on) on.classList.remove("on");
      on = hit; hit.classList.add("on");
      var p = hit.getAttribute("data-tip").split("|"), cls = (svg.getAttribute("data-sw") || "").split(" ");
      tip.textContent = "";
      var b = document.createElement("b"); b.textContent = p[0]; tip.appendChild(b);
      for (var k = 1; k + 1 < p.length; k += 2) {
        var s = document.createElement("span"), sw = document.createElement("i"), em = document.createElement("em");
        sw.className = "sw " + (cls[(k - 1) / 2] || "");
        s.appendChild(sw); s.appendChild(document.createTextNode(p[k])); em.textContent = p[k + 1]; s.appendChild(em);
        tip.appendChild(s);
      }
      tip.hidden = false;
      var br = box.getBoundingClientRect(), hr = hit.getBoundingClientRect();
      var x = hr.left - br.left + hr.width / 2 - tip.offsetWidth / 2;
      tip.style.left = Math.max(0, Math.min(x, box.clientWidth - tip.offsetWidth)) + "px";
      tip.style.top = (-tip.offsetHeight - 6) + "px";
    }
    svg.querySelectorAll(".hit").forEach(function (h) {
      h.addEventListener("pointerenter", function () { show(h); });
      h.addEventListener("click", function () { show(h); });
    });
    svg.addEventListener("pointerleave", function (ev) { if (ev.pointerType === "mouse") hide(); });
    document.addEventListener("click", function (ev) { if (!box.contains(ev.target)) hide(); });
  });

  // ---- Flat rate -> effective (reducing balance) rate; locale settings come from data-* ----
  var conv = document.querySelector("[data-flat-conv]");
  if (!conv) return;
  var ds = conv.dataset, rateEl = conv.querySelector("#cv-rate"), termEl = conv.querySelector("#cv-term");
  var P = Number(ds.p), dec = Number(ds.dec), perMonth = ds.unit === "m", div = Number(ds.div) || 1;
  var nfm = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: dec, maximumFractionDigits: dec });
  var nf1 = new Intl.NumberFormat(ds.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  function annuity(r, n) { return r === 0 ? P / n : P * r / (1 - Math.pow(1 + r, -n)); }
  function solve(pay, n) {
    if (pay * n <= P) return 0;
    var lo = 0, hi = 1;
    for (var k = 0; k < 100; k++) { var mid = (lo + hi) / 2; if (annuity(mid, n) > pay) hi = mid; else lo = mid; }
    return (lo + hi) / 2;
  }
  function money(v) {
    var s = nfm.format(v);
    return !ds.cur ? s : ds.pre === "1" ? ds.cur + " " + s : s + " " + ds.cur;
  }
  function update() {
    var v = parseFloat(String(rateEl.value).replace(",", ".")), n = Math.floor(Number(termEl.value));
    var ok = isFinite(v) && v >= 0 && v <= (perMonth ? 10 : 120) && n >= 1 && n <= 360;
    if (!ok) { ["cv-apr", "cv-flat", "cv-equal"].forEach(function (id) { conv.querySelector("#" + id).textContent = "-"; }); return; }
    var i = perMonth ? v / 100 : v / 1200, yearly = i * 1200;
    var apr = solve(P / n + P * i, n) * 1200;
    conv.querySelector("#cv-apr").textContent = nf1.format(apr / div) + ds.sfx;
    conv.querySelector("#cv-flat").textContent = money(P * i * n);
    conv.querySelector("#cv-equal").textContent = money(P * i * (n + 1) / 2);
    conv.querySelector("#cv-link").href = ds.path + "?amount=" + P + "&rate=" + +yearly.toFixed(4) +
      "&term=" + n + "&unit=m&method=flat";
  }
  rateEl.addEventListener("input", update);
  termEl.addEventListener("input", update);
  update();
})();
