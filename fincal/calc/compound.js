/* Fincal compound interest calculator for the web. Same engine as the Fincal app: simulated month by
   month in whole minor units (dong, or cents), contributions earn interest for the share of the
   compounding period they are present, interest is capitalized (HALF_UP) at each compounding boundary. */
(function () {
  "use strict";

  // ---------- Engine ----------
  var FREQ_MONTHS = { m: 1, q: 3, y: 12 };
  function roundHalfUp(v) { return Math.floor(v + 0.5); }

  /** initial, contribution: integers in the smallest unit. cf/kf: "m" | "q" | "y". timing: "end" | "begin".
      Returns { futureValue, totalContributions, totalInterest, byYear: [{year, contributed, interest, endValue}] }. */
  function calculate(initial, contribution, cf, kf, timing, annualRate, years) {
    var km = FREQ_MONTHS[kf] || 1, cm = FREQ_MONTHS[cf] || 1;
    var periodRate = annualRate / 100 / (12 / km), begin = timing === "begin";
    var balance = initial, totalC = 0, totalI = 0, byYear = [], yC = 0, yI = 0;
    var periodStart = balance, weighted = 0, total = years * 12;
    for (var month = 1; month <= total; month++) {
      var periodEnd = (Math.floor((month - 1) / km) + 1) * km, contributes, present;
      if (begin) { contributes = (month - 1) % cm === 0; present = periodEnd - (month - 1); }
      else { contributes = month % cm === 0; present = periodEnd - month; }
      if (contributes && contribution) {
        balance += contribution; yC += contribution; totalC += contribution;
        weighted += contribution * present / km;
      }
      if (month % km === 0) {
        var interest = roundHalfUp((periodStart + weighted) * periodRate);
        balance += interest; yI += interest; totalI += interest;
        periodStart = balance; weighted = 0;
      }
      if (month % 12 === 0) {
        byYear.push({ year: month / 12, contributed: yC, interest: yI, endValue: balance });
        yC = 0; yI = 0;
      }
    }
    return { futureValue: balance, totalContributions: totalC, totalInterest: totalI, byYear: byYear };
  }

  if (typeof module !== "undefined" && module.exports) { module.exports = { calculate: calculate }; }
  if (typeof document === "undefined") return;

  // ---------- UI ----------
  var root = document.querySelector("[data-compound-calc]");
  if (!root) return;
  var LANG = document.documentElement.lang || "en";
  var C = {
    vi: { loc: "vi-VN", scale: 1, pre: "", suf: " đ", max: 1e12, comma: true },
    id: { loc: "id-ID", scale: 1, pre: "Rp ", suf: "", max: 1e14, comma: true },
    th: { loc: "th-TH", scale: 100, pre: "", suf: " ฿", max: 1e10, comma: false },
    "pt-BR": { loc: "pt-BR", scale: 100, pre: "R$ ", suf: "", max: 1e9, comma: true },
    ms: { loc: "ms-MY", scale: 100, pre: "RM ", suf: "", max: 1e9, comma: false },
    en: { loc: "en-US", scale: 100, pre: "", suf: "", max: 1e8, comma: false }
  }[LANG] || { loc: "en-US", scale: 100, pre: "", suf: "", max: 1e8, comma: false };
  var SCALE = C.scale;
  var LIMIT = 9e15; // stay inside exact integer range
  var nf = new Intl.NumberFormat(C.loc, { maximumFractionDigits: 0 });
  var nf2 = new Intl.NumberFormat(C.loc, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var pf = new Intl.NumberFormat(C.loc, { maximumFractionDigits: 2 });
  var xf = new Intl.NumberFormat(C.loc, { maximumFractionDigits: 1 });
  var T = {
    vi: { fv: "Giá trị sau", yrs: function (n) { return n + " năm"; }, times: function (x) { return "gấp " + x + " lần số tiền bỏ vào"; },
      initial: "Vốn ban đầu", contrib: "Tiền góp", interest: "Lãi", total: "Tổng", yearN: function (n) { return "Năm " + n; },
      rows: function (n) { return n + " năm"; }, tooLarge: "Số quá lớn để tính", words: [[1e9, "tỷ"], [1e6, "triệu"], [1e3, "nghìn"]], unitWord: "đồng" },
    id: { fv: "Nilai setelah", yrs: function (n) { return n + " tahun"; }, times: function (x) { return x + " kali total dana yang disetor"; },
      initial: "Investasi awal", contrib: "Setoran", interest: "Bunga", total: "Total", yearN: function (n) { return "Tahun " + n; },
      rows: function (n) { return n + " tahun"; }, tooLarge: "Nilai terlalu besar untuk dihitung", words: [[1e12, "triliun"], [1e9, "miliar"], [1e6, "juta"], [1e3, "ribu"]], unitWord: "rupiah" },
    th: { fv: "มูลค่าเมื่อครบ", yrs: function (n) { return n + " ปี"; }, times: function (x) { return "เป็น " + x + " เท่าของเงินที่ลงไป"; },
      initial: "เงินลงทุนเริ่มต้น", contrib: "เงินสมทบ", interest: "ดอกเบี้ย", total: "รวม", yearN: function (n) { return "ปีที่ " + n; },
      rows: function (n) { return n + " ปี"; }, tooLarge: "ตัวเลขใหญ่เกินกว่าจะคำนวณได้" },
    "pt-BR": { fv: "Valor em", yrs: function (n) { return n + (n === 1 ? " ano" : " anos"); }, times: function (x) { return x + " vezes o total investido"; },
      initial: "Investimento inicial", contrib: "Aportes", interest: "Juros", total: "Total", yearN: function (n) { return "Ano " + n; },
      rows: function (n) { return n + (n === 1 ? " ano" : " anos"); }, tooLarge: "Valor grande demais para calcular" },
    ms: { fv: "Nilai selepas", yrs: function (n) { return n + " tahun"; }, times: function (x) { return x + " kali jumlah yang dilaburkan"; },
      initial: "Pelaburan permulaan", contrib: "Sumbangan", interest: "Faedah", total: "Jumlah", yearN: function (n) { return "Tahun " + n; },
      rows: function (n) { return n + " tahun"; }, tooLarge: "Nilai terlalu besar untuk dikira" },
    en: { fv: "Value after", yrs: function (n) { return n + (n === 1 ? " year" : " years"); }, times: function (x) { return x + "× what you put in"; },
      initial: "Initial investment", contrib: "Contributions", interest: "Interest", total: "Total", yearN: function (n) { return "Year " + n; },
      rows: function (n) { return n + (n === 1 ? " year" : " years"); }, tooLarge: "Value too large to calculate" }
  };
  T = T[LANG] || T.en;

  var $ = function (sel) { return root.querySelector(sel); };
  var initialEl = $("#initial"), contribEl = $("#contrib"), cfreqEl = $("#cfreq"), rateEl = $("#rate"),
      rateRange = $("#rate-range"), yearsEl = $("#years"), yearsRange = $("#years-range"), kfreqEl = $("#kfreq");

  function money(units) { return C.pre + (SCALE === 1 ? nf.format(units) : nf2.format(units / SCALE)) + C.suf; }
  function moneyShort(units) { return C.pre + nf.format(Math.round(units / SCALE)) + C.suf; }
  function parseAmount(s) { var d = String(s).replace(/[^\d]/g, ""); return d ? Math.min(Number(d), C.max) : 0; }
  function parseRate(s) { var v = parseFloat(String(s).replace(",", ".")); return isFinite(v) ? Math.min(Math.max(v, 0), 100) : 0; }
  function showRate(v) { return C.comma ? String(v).replace(".", ",") : String(v); }
  function years() { return Math.min(100, Math.max(0, Math.floor(Number(yearsEl.value) || 0))); }
  function timing() { var c = root.querySelector('input[name="timing"]:checked'); return c ? c.value : "end"; }

  function amountWords(v) {
    if (!v || !T.words) return "";
    var parts = [], rest = v;
    T.words.forEach(function (w, k) {
      var q = Math.floor(rest / w[0]);
      if (q) { parts.push((k === 0 ? nf.format(q) : q) + " " + w[1]); rest -= q * w[0]; }
    });
    if (rest) parts.push(rest);
    return parts.join(" ") + " " + T.unitWord;
  }

  function formatAmountInput(el) {
    var pos = el.selectionStart || 0;
    var digitsBefore = el.value.slice(0, pos).replace(/[^\d]/g, "").length;
    var v = parseAmount(el.value), out = v ? nf.format(v) : "";
    el.value = out;
    var seen = 0, p = 0;
    while (p < out.length && seen < digitsBefore) { if (/\d/.test(out[p])) seen++; p++; }
    try { el.setSelectionRange(p, p); } catch (e) {}
  }

  var urlTimer;
  function saveUrl() {
    clearTimeout(urlTimer);
    urlTimer = setTimeout(function () {
      var q = new URLSearchParams({ initial: parseAmount(initialEl.value), contrib: parseAmount(contribEl.value), every: cfreqEl.value,
        rate: parseRate(rateEl.value), years: years(), compound: kfreqEl.value, timing: timing() });
      try { history.replaceState(null, "", "?" + q.toString()); } catch (e) {}
    }, 400);
  }

  function loadUrl() {
    var q = new URLSearchParams(location.search), f = /^[mqy]$/;
    if (q.has("initial")) initialEl.value = parseAmount(q.get("initial")) ? nf.format(parseAmount(q.get("initial"))) : "";
    if (q.has("contrib")) contribEl.value = parseAmount(q.get("contrib")) ? nf.format(parseAmount(q.get("contrib"))) : "";
    if (f.test(q.get("every"))) cfreqEl.value = q.get("every");
    if (f.test(q.get("compound"))) kfreqEl.value = q.get("compound");
    if (q.get("rate")) rateEl.value = showRate(parseRate(q.get("rate")));
    if (q.get("years")) yearsEl.value = Math.max(1, Math.min(100, Math.floor(Number(q.get("years")) || 1)));
    var t = q.get("timing");
    if (t === "begin" || t === "end") root.querySelector('input[name="timing"][value="' + t + '"]').checked = true;
    if (kfreqEl.value !== "m" || timing() !== "end") $("#adv").open = true;
  }

  function syncRanges() {
    rateRange.value = Math.min(parseRate(rateEl.value), Number(rateRange.max));
    yearsRange.value = Math.min(years(), Number(yearsRange.max));
  }

  // ---------- Chart: stacked bars per year (initial, contributions so far, interest so far) ----------
  var SVGNS = "http://www.w3.org/2000/svg", lastRows = null, resizeTimer;
  function el(tag, attrs) { var e = document.createElementNS(SVGNS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); return e; }
  function niceMax(v) {
    if (v <= 0) return 1;
    var p = Math.pow(10, Math.floor(Math.log10(v))), n = v / p;
    return (n <= 1 ? 1 : n <= 2 ? 2 : n <= 2.5 ? 2.5 : n <= 5 ? 5 : 10) * p;
  }
  function roundTop(x, y, w, h, r) {
    return "M" + x + "," + (y + h) + "V" + (y + r) + "Q" + x + "," + y + " " + (x + r) + "," + y +
      "H" + (x + w - r) + "Q" + (x + w) + "," + y + " " + (x + w) + "," + (y + r) + "V" + (y + h) + "Z";
  }

  function drawChart(rows) {
    var svg = $("#chart"), tip = $("#chart-tip");
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    lastRows = rows;
    var W = Math.round(svg.getBoundingClientRect().width) || 640, L = 4, R = 4, Tp = 12, B = 24;
    if (W < 280) W = 280;
    var H = W < 500 ? 230 : 270;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    if (!rows.length) return;
    var max = niceMax(rows[rows.length - 1].total);
    var plotW = W - L - R, plotH = H - Tp - B, slot = plotW / rows.length;
    var bw = Math.max(2, Math.min(28, slot - Math.max(1, slot * 0.28)));
    var y = function (v) { return Tp + plotH - v / max * plotH; };
    [0.5, 1].forEach(function (f) { svg.appendChild(el("line", { x1: L, x2: W - R, y1: y(max * f), y2: y(max * f), "class": "grid" })); });
    svg.appendChild(el("line", { x1: L, x2: W - R, y1: y(0), y2: y(0), "class": "axis" }));
    var every = Math.ceil(rows.length / (W < 500 ? 6 : 12)), gapPx = bw >= 6 ? 2 : 1;
    rows.forEach(function (r, k) {
      var cx = L + slot * k + slot / 2, x = cx - bw / 2, base = y(0);
      var segs = [["bar-p", r.initial], ["bar-c", r.contrib], ["bar-i", r.interest]].filter(function (s) { return s[1] > 0; });
      segs.forEach(function (s, j) {
        var h = s[1] / max * plotH, g = j < segs.length - 1 && h > gapPx * 2 ? gapPx : 0;
        if (j === segs.length - 1) svg.appendChild(el("path", { "class": s[0], d: roundTop(x, base - h, bw, h, Math.min(4, bw / 2, h)) }));
        else svg.appendChild(el("rect", { x: x, y: base - h + g, width: bw, height: Math.max(0, h - g), "class": s[0] }));
        base -= h;
      });
      if (k % every === every - 1 || k === rows.length - 1 && rows.length <= 12 || every === 1) {
        var t = el("text", { x: cx, y: H - 8, "class": "tick", "text-anchor": "middle" }); t.textContent = r.year; svg.appendChild(t);
      }
      var hit = el("rect", { x: L + slot * k, y: Tp, width: slot, height: plotH, "class": "hit" });
      hit.addEventListener("pointerenter", function () { showTip(k); });
      hit.addEventListener("pointerdown", function () { showTip(k); });
      svg.appendChild(hit);
    });
    function showTip(k) {
      var r = rows[k];
      tip.innerHTML = "<b>" + T.yearN(r.year) + "</b>" +
        (r.initial ? "<span><i class='sw sw-p'></i>" + T.initial + "<em>" + moneyShort(r.initial) + "</em></span>" : "") +
        (r.contrib ? "<span><i class='sw sw-c'></i>" + T.contrib + "<em>" + moneyShort(r.contrib) + "</em></span>" : "") +
        "<span><i class='sw sw-i'></i>" + T.interest + "<em>" + moneyShort(r.interest) + "</em></span>" +
        "<span>" + T.total + "<em>" + moneyShort(r.total) + "</em></span>";
      tip.hidden = false;
      var box = svg.getBoundingClientRect(), left = (L + slot * k + slot / 2) / W * box.width, tw = tip.offsetWidth;
      tip.style.left = Math.max(0, Math.min(box.width - tw, left - tw / 2)) + "px";
      svg.querySelectorAll(".hit").forEach(function (h, j) { h.classList.toggle("on", j === k); });
    }
    svg.onpointerleave = function (e) { if (e.pointerType === "mouse") { tip.hidden = true; svg.querySelectorAll(".hit.on").forEach(function (h) { h.classList.remove("on"); }); } };
  }

  function renderTable(byYear) {
    $("#sched-count").textContent = T.rows(byYear.length);
    var html = "";
    byYear.forEach(function (r) {
      html += "<tr><th scope='row'>" + r.year + "</th><td>" + money(r.contributed) + "</td><td>" + money(r.interest) +
        "</td><td>" + money(r.endValue) + "</td></tr>";
    });
    $("#sched-body").innerHTML = html;
  }

  function render() {
    var P = parseAmount(initialEl.value) * SCALE, A = parseAmount(contribEl.value) * SCALE, rate = parseRate(rateEl.value),
        n = years(), cf = cfreqEl.value, kf = kfreqEl.value, tm = timing();
    $("#initial-words").textContent = amountWords(parseAmount(initialEl.value));
    $("#contrib-words").textContent = amountWords(parseAmount(contribEl.value));
    var ok = (P > 0 || A > 0) && n > 0, res = ok ? calculate(P, A, cf, kf, tm, rate, n) : null;
    var tooBig = res && !(res.futureValue < LIMIT);
    root.classList.toggle("empty", !ok || tooBig);
    $("#res-err").hidden = !tooBig;
    if (!ok || tooBig) { if (tooBig) $("#res-err").textContent = T.tooLarge; return; }

    var put = P + res.totalContributions, fv = res.futureValue;
    $("#res-fv-label").textContent = T.fv + " " + T.yrs(n);
    $("#res-fv").textContent = money(fv);
    $("#res-fv-sub").textContent = put > 0 && fv > put ? T.times(xf.format(fv / put)) : "";
    $("#mini-label").textContent = $("#res-fv-label").textContent;
    $("#mini-val").textContent = money(fv);
    $("#res-put").textContent = money(put);
    $("#res-interest").textContent = money(res.totalInterest);
    var pct = function (v) { return fv ? v / fv * 100 : 0; };
    $("#split-p").style.width = pct(P) + "%";
    $("#split-c").style.width = pct(res.totalContributions) + "%";
    $("#split-p").hidden = !P; $("#split-c").hidden = !res.totalContributions;
    $("#lg-p").hidden = !P; $("#lg-c").hidden = !res.totalContributions;
    $("#res-initial").textContent = money(P);
    $("#res-contrib").textContent = money(res.totalContributions);
    $("#res-int2").textContent = money(res.totalInterest);
    $("#pct-p").textContent = pf.format(pct(P)) + "%";
    $("#pct-c").textContent = pf.format(pct(res.totalContributions)) + "%";
    $("#pct-i").textContent = pf.format(pct(res.totalInterest)) + "%";

    // Same inputs, each compounding frequency.
    ["m", "q", "y"].forEach(function (k) {
      var r = k === kf ? res : calculate(P, A, cf, k, tm, rate, n);
      $("#cmp-" + k).textContent = money(r.futureValue);
      $("#cmp-" + k + "-i").textContent = money(r.totalInterest);
      $("#cmprow-" + k).classList.toggle("on", k === kf);
    });

    var cum = 0, rows = res.byYear.map(function (r) {
      cum += r.contributed;
      return { year: r.year, initial: P, contrib: cum, interest: r.endValue - P - cum, total: r.endValue };
    });
    drawChart(rows);
    renderTable(res.byYear);
    $("#chart-tip").hidden = true;
    saveUrl();
  }

  // ---------- Wiring ----------
  [initialEl, contribEl].forEach(function (inp) { inp.addEventListener("input", function () { formatAmountInput(inp); render(); }); });
  rateEl.addEventListener("input", function () { syncRanges(); render(); });
  rateRange.addEventListener("input", function () { rateEl.value = showRate(rateRange.value); render(); });
  yearsEl.addEventListener("input", function () { syncRanges(); render(); });
  yearsRange.addEventListener("input", function () { yearsEl.value = yearsRange.value; render(); });
  [cfreqEl, kfreqEl].forEach(function (s) { s.addEventListener("change", render); });
  root.querySelectorAll('input[name="timing"]').forEach(function (r) { r.addEventListener("change", render); });
  root.querySelectorAll("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () { initialEl.value = nf.format(Number(b.getAttribute("data-amount"))); render(); });
  });
  root.querySelectorAll("[data-pick]").forEach(function (row) {
    row.addEventListener("click", function () { kfreqEl.value = row.getAttribute("data-pick"); render(); });
  });
  window.addEventListener("resize", function () {
    $("#chart-tip").hidden = true;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { if (lastRows) drawChart(lastRows); }, 120);
  });

  var mini = $("#mini");
  if (mini && "IntersectionObserver" in window) {
    var formIn = false, resIn = false;
    var setMini = function () { mini.classList.toggle("off", !(formIn && !resIn) || root.classList.contains("empty")); };
    new IntersectionObserver(function (es) { es.forEach(function (e) { formIn = e.isIntersecting; }); setMini(); }).observe($(".inputs"));
    new IntersectionObserver(function (es) { es.forEach(function (e) { resIn = e.isIntersecting; }); setMini(); }).observe($("#res-fv"));
  }

  document.addEventListener("click", function (e) {
    document.querySelectorAll("details.langs[open]").forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
  });

  loadUrl();
  syncRanges();
  render();
})();
