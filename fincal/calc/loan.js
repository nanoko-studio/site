/* Fincal loan calculator for the web. Single fixed rate; same maths and rounding as the Fincal app
   engine (HALF_UP to the smallest currency unit at every period). Floating rates, prepayments,
   saved loans and exports live in the app. */
(function () {
  "use strict";

  // ---------- Engine (amounts are integers in the smallest unit: dong, or cents) ----------
  function roundHalfUp(v) { return Math.floor(v + 0.5); }
  function halfUpDiv(a, b) { var q = Math.floor(a / b), r = a - q * b; return r * 2 >= b ? q + 1 : q; }

  function annuityPayment(balance, annualRate, months) {
    if (balance <= 0 || months <= 0) return 0;
    var i = annualRate / 100 / 12;
    if (i === 0) return halfUpDiv(balance, months);
    return roundHalfUp(balance * i / (1 - Math.pow(1 + i, -months)));
  }

  function solveEffectiveRate(principal, payment, months) {
    if (principal <= 0 || months <= 0 || payment <= 0 || payment * months <= principal) return 0;
    var lo = 0, hi = 1;
    for (var k = 0; k < 200; k++) {
      var mid = (lo + hi) / 2;
      var pmt = principal * mid / (1 - Math.pow(1 + mid, -months));
      if (pmt > payment) hi = mid; else lo = mid;
    }
    return (lo + hi) / 2 * 12 * 100;
  }

  /** method: "annuity" | "equal" | "flat". Returns { periods: [{p, i, pay, end}], totalInterest, totalPaid, apr }. */
  function calculate(principal, annualRate, months, method) {
    var i = annualRate / 100 / 12, bal = principal, periods = [], totalInterest = 0, apr = 0, m;
    if (method === "annuity") {
      var pmt = annuityPayment(principal, annualRate, months);
      for (m = 1; m <= months && bal > 0; m++) {
        var int1 = roundHalfUp(bal * i), sched = pmt - int1;
        var pp = (sched >= bal || m === months) ? bal : sched;
        bal -= pp; totalInterest += int1;
        periods.push({ p: pp, i: int1, pay: pp + int1, end: bal });
      }
    } else {
      var base = halfUpDiv(principal, months);
      var flatInt = roundHalfUp(principal * i);
      if (method === "flat") apr = solveEffectiveRate(principal, base + flatInt, months);
      for (m = 1; m <= months && bal > 0; m++) {
        var int2 = method === "flat" ? flatInt : roundHalfUp(bal * i);
        var p2 = m === months ? bal : Math.min(base, bal);
        bal -= p2; totalInterest += int2;
        periods.push({ p: p2, i: int2, pay: p2 + int2, end: bal });
      }
    }
    return { periods: periods, totalInterest: totalInterest, totalPaid: principal + totalInterest, apr: apr };
  }

  if (typeof module !== "undefined" && module.exports) { module.exports = { calculate: calculate }; }
  if (typeof document === "undefined") return;

  // ---------- UI ----------
  var root = document.querySelector("[data-loan-calc]");
  if (!root) return;
  // Per-language settings: number locale, minor-unit scale, currency affixes and UI strings.
  var LANG = document.documentElement.lang || "en";
  var C = {
    vi: { loc: "vi-VN", scale: 1, pre: "", suf: " đ", max: 1e12, comma: true },
    id: { loc: "id-ID", scale: 1, pre: "Rp ", suf: "", max: 1e14, comma: true },
    th: { loc: "th-TH", scale: 100, pre: "", suf: " ฿", max: 1e10, comma: false },
    "pt-BR": { loc: "pt-BR", scale: 100, pre: "R$ ", suf: "", max: 1e9, comma: true },
    ms: { loc: "ms-MY", scale: 100, pre: "RM ", suf: "", max: 1e9, comma: false },
    en: { loc: "en-US", scale: 100, pre: "", suf: "", max: 1e8, comma: false }
  }[LANG] || { loc: "en-US", scale: 100, pre: "", suf: "", max: 1e8, comma: false };
  var SCALE = C.scale; // VND and IDR are computed in whole units, other currencies in cents
  var nf = new Intl.NumberFormat(C.loc, { maximumFractionDigits: 0 });
  var nf2 = new Intl.NumberFormat(C.loc, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var pf = new Intl.NumberFormat(C.loc, { maximumFractionDigits: 2 });
  var plain = function (word) { return function (n) { return nf.format(n) + " " + word; }; };
  var T = {
    vi: {
      perMonth: "Trả mỗi tháng", firstMonth: "Tháng đầu", lastMonth: "tháng cuối", downTo: "giảm dần còn",
      year: "Năm", month: "Tháng", principal: "Gốc", interest: "Lãi", balance: "Dư nợ còn lại",
      periods: plain("kỳ"), yearN: function (n) { return "Năm " + n; }, monthN: function (n) { return "Tháng " + n; },
      aprNote: function (r) { return "Lãi phẳng " + r + "%/năm tương đương lãi suất thực tế khoảng"; },
      words: [[1e9, "tỷ"], [1e6, "triệu"], [1e3, "nghìn"]], unitWord: "đồng"
    },
    id: {
      perMonth: "Cicilan per bulan", firstMonth: "Cicilan pertama", lastMonth: "di bulan terakhir", downTo: "turun menjadi",
      year: "Tahun", month: "Bulan", principal: "Pokok", interest: "Bunga", balance: "Sisa pinjaman",
      periods: plain("cicilan"), yearN: function (n) { return "Tahun " + n; }, monthN: function (n) { return "Bulan " + n; },
      aprNote: function (r) { return "Bunga flat " + r + "% per tahun setara dengan bunga efektif sekitar"; },
      words: [[1e12, "triliun"], [1e9, "miliar"], [1e6, "juta"], [1e3, "ribu"]], unitWord: "rupiah"
    },
    th: {
      perMonth: "ค่างวดต่อเดือน", firstMonth: "งวดแรก", lastMonth: "ในงวดสุดท้าย", downTo: "ลดลงเหลือ",
      year: "ปี", month: "เดือน", principal: "เงินต้น", interest: "ดอกเบี้ย", balance: "ยอดคงเหลือ",
      periods: plain("งวด"), yearN: function (n) { return "ปีที่ " + n; }, monthN: function (n) { return "งวดที่ " + n; },
      aprNote: function (r) { return "ดอกเบี้ยคงที่ " + r + "% ต่อปี เทียบเท่าดอกเบี้ยแบบลดต้นลดดอกประมาณ"; }
    },
    "pt-BR": {
      perMonth: "Parcela mensal", firstMonth: "Primeira parcela", lastMonth: "na última", downTo: "caindo para",
      year: "Ano", month: "Mês", principal: "Amortização", interest: "Juros", balance: "Saldo devedor",
      periods: function (n) { return nf.format(n) + (n === 1 ? " parcela" : " parcelas"); },
      yearN: function (n) { return "Ano " + n; }, monthN: function (n) { return "Mês " + n; },
      aprNote: function (r) { return "Uma taxa flat de " + r + "% ao ano equivale a uma taxa sobre o saldo devedor de cerca de"; }
    },
    ms: {
      perMonth: "Ansuran bulanan", firstMonth: "Ansuran pertama", lastMonth: "pada bulan terakhir", downTo: "turun kepada",
      year: "Tahun", month: "Bulan", principal: "Pokok", interest: "Faedah", balance: "Baki pinjaman",
      periods: plain("ansuran"), yearN: function (n) { return "Tahun " + n; }, monthN: function (n) { return "Bulan " + n; },
      aprNote: function (r) { return "Kadar rata " + r + "% setahun bersamaan dengan kadar efektif (baki berkurangan) kira-kira"; }
    },
    en: {
      perMonth: "Monthly payment", firstMonth: "First month", lastMonth: "last month", downTo: "falling to",
      year: "Year", month: "Month", principal: "Principal", interest: "Interest", balance: "Balance left",
      periods: function (n) { return nf.format(n) + (n === 1 ? " payment" : " payments"); },
      yearN: function (n) { return "Year " + n; }, monthN: function (n) { return "Month " + n; },
      aprNote: function (r) { return "A flat rate of " + r + "% a year is about the same as a reducing-balance rate of"; }
    }
  }[LANG] || null;
  if (!T) T = { perMonth: "Monthly payment", firstMonth: "First month", lastMonth: "last month", downTo: "falling to",
    year: "Year", month: "Month", principal: "Principal", interest: "Interest", balance: "Balance left",
    periods: plain("payments"), yearN: function (n) { return "Year " + n; }, monthN: function (n) { return "Month " + n; },
    aprNote: function (r) { return "A flat rate of " + r + "% a year is about the same as a reducing-balance rate of"; } };

  var $ = function (sel) { return root.querySelector(sel); };
  var amountEl = $("#amount"), rateEl = $("#rate"), rateRange = $("#rate-range"), termEl = $("#term"),
      termRange = $("#term-range"), unitEl = $("#unit"), wordsEl = $("#amount-words");
  var MAX_AMOUNT = C.max;

  function money(units) { return C.pre + (SCALE === 1 ? nf.format(units) : nf2.format(units / SCALE)) + C.suf; }
  function moneyShort(units) { return nf.format(Math.round(units / SCALE)); }
  function parseAmount(s) { var d = String(s).replace(/[^\d]/g, ""); return d ? Math.min(Number(d), MAX_AMOUNT) : 0; }
  function parseRate(s) { var v = parseFloat(String(s).replace(",", ".")); return isFinite(v) ? Math.min(Math.max(v, 0), 100) : 0; }
  function showRate(v) { return C.comma ? String(v).replace(".", ",") : String(v); }
  function method() { var c = root.querySelector('input[name="method"]:checked'); return c ? c.value : "annuity"; }
  function months() {
    var n = Math.max(0, Math.floor(Number(termEl.value) || 0));
    return Math.min(unitEl.value === "y" ? n * 12 : n, 600);
  }

  // Amount in words, for currencies where amounts run into millions and billions (VND, IDR).
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

  // Keep the caret on the same digit while thousands separators are inserted.
  function formatAmountInput() {
    var el = amountEl, pos = el.selectionStart || 0;
    var digitsBefore = el.value.slice(0, pos).replace(/[^\d]/g, "").length;
    var v = parseAmount(el.value);
    var out = v ? nf.format(v) : "";
    el.value = out;
    var seen = 0, p = 0;
    while (p < out.length && seen < digitsBefore) { if (/\d/.test(out[p])) seen++; p++; }
    try { el.setSelectionRange(p, p); } catch (e) {}
  }

  var urlTimer;
  function saveUrl() {
    clearTimeout(urlTimer);
    urlTimer = setTimeout(function () {
      var q = new URLSearchParams({ amount: parseAmount(amountEl.value), rate: parseRate(rateEl.value),
        term: termEl.value, unit: unitEl.value, method: method() });
      try { history.replaceState(null, "", "?" + q.toString()); } catch (e) {}
    }, 400);
  }

  function loadUrl() {
    var q = new URLSearchParams(location.search);
    if (q.get("amount")) amountEl.value = nf.format(parseAmount(q.get("amount")));
    if (q.get("rate")) rateEl.value = showRate(parseRate(q.get("rate")));
    if (q.get("unit") === "m" || q.get("unit") === "y") unitEl.value = q.get("unit");
    if (q.get("term")) termEl.value = Math.max(1, Math.min(600, Math.floor(Number(q.get("term")) || 1)));
    var m = q.get("method"), r = m && root.querySelector('input[name="method"][value="' + m.replace(/[^a-z]/g, "") + '"]');
    if (r) r.checked = true;
  }

  function syncRanges() {
    rateRange.value = Math.min(parseRate(rateEl.value), Number(rateRange.max));
    termRange.max = unitEl.value === "y" ? 35 : 420;
    termRange.value = Math.min(Number(termEl.value) || 0, Number(termRange.max));
  }

  // ---------- Rendering ----------
  function group(periods) {
    var byYear = periods.length > 36, out = [];
    periods.forEach(function (pr, idx) {
      var k = byYear ? Math.floor(idx / 12) : idx;
      if (!out[k]) out[k] = { label: byYear ? T.yearN(k + 1) : T.monthN(idx + 1), short: String(k + 1), p: 0, i: 0, end: 0 };
      out[k].p += pr.p; out[k].i += pr.i; out[k].end = pr.end;
    });
    return { rows: out, byYear: byYear };
  }

  var lastGroup = null, resizeTimer;
  var SVGNS = "http://www.w3.org/2000/svg";
  function el(tag, attrs) { var e = document.createElementNS(SVGNS, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); return e; }

  function niceMax(v) {
    if (v <= 0) return 1;
    var p = Math.pow(10, Math.floor(Math.log10(v))), n = v / p;
    return (n <= 1 ? 1 : n <= 2 ? 2 : n <= 2.5 ? 2.5 : n <= 5 ? 5 : 10) * p;
  }

  function drawChart(g) {
    var svg = $("#chart"), tip = $("#chart-tip");
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    lastGroup = g;
    var rows = g.rows, W = Math.round(svg.getBoundingClientRect().width) || 640, L = 4, R = 4, Tp = 12, B = 24;
    if (W < 280) W = 280;
    var H = W < 500 ? 230 : 270;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    if (!rows.length) return;
    var max = niceMax(Math.max.apply(null, rows.map(function (r) { return r.p + r.i; })));
    var plotW = W - L - R, plotH = H - Tp - B, slot = plotW / rows.length;
    var bw = Math.max(2, Math.min(28, slot - Math.max(2, slot * 0.28)));
    var y = function (v) { return Tp + plotH - v / max * plotH; };
    [0.5, 1].forEach(function (f) {
      svg.appendChild(el("line", { x1: L, x2: W - R, y1: y(max * f), y2: y(max * f), "class": "grid" }));
    });
    svg.appendChild(el("line", { x1: L, x2: W - R, y1: y(0), y2: y(0), "class": "axis" }));
    var every = Math.ceil(rows.length / (W < 500 ? 6 : 12));
    rows.forEach(function (r, k) {
      var cx = L + slot * k + slot / 2, x = cx - bw / 2;
      var hp = r.p / max * plotH, hi = r.i / max * plotH, gap = hi > 0 && hp > 0 ? 2 : 0;
      var rad = Math.min(4, bw / 2);
      svg.appendChild(el("rect", { x: x, y: y(0) - hp, width: bw, height: Math.max(0, hp), "class": "bar-p" }));
      if (hi > 0) {
        var top = y(0) - hp - gap - hi;
        svg.appendChild(el("path", { "class": "bar-i", d: roundTop(x, top, bw, hi, Math.min(rad, hi)) }));
      }
      if (k % every === 0 || k === rows.length - 1 && rows.length <= 12) {
        var t = el("text", { x: cx, y: H - 8, "class": "tick", "text-anchor": "middle" }); t.textContent = r.short; svg.appendChild(t);
      }
      var hit = el("rect", { x: L + slot * k, y: Tp, width: slot, height: plotH, "class": "hit", tabindex: "-1" });
      hit.addEventListener("pointerenter", function () { showTip(k); });
      hit.addEventListener("pointerdown", function () { showTip(k); });
      svg.appendChild(hit);
    });
    function showTip(k) {
      var r = rows[k];
      tip.innerHTML = "<b>" + r.label + "</b>" +
        "<span><i class='sw sw-p'></i>" + T.principal + "<em>" + moneyShort(r.p) + "</em></span>" +
        "<span><i class='sw sw-i'></i>" + T.interest + "<em>" + moneyShort(r.i) + "</em></span>" +
        "<span>" + T.balance + "<em>" + moneyShort(r.end) + "</em></span>";
      tip.hidden = false;
      var box = svg.getBoundingClientRect(), frac = (L + slot * k + slot / 2) / W;
      var left = frac * box.width, tw = tip.offsetWidth;
      tip.style.left = Math.max(0, Math.min(box.width - tw, left - tw / 2)) + "px";
      svg.querySelectorAll(".hit").forEach(function (h, j) { h.classList.toggle("on", j === k); });
    }
    svg.onpointerleave = function (e) { if (e.pointerType === "mouse") { tip.hidden = true; svg.querySelectorAll(".hit.on").forEach(function (h) { h.classList.remove("on"); }); } };
  }

  function roundTop(x, y, w, h, r) {
    return "M" + x + "," + (y + h) + "V" + (y + r) + "Q" + x + "," + y + " " + (x + r) + "," + y +
      "H" + (x + w - r) + "Q" + (x + w) + "," + y + " " + (x + w) + "," + (y + r) + "V" + (y + h) + "Z";
  }

  function renderTable(g, periods) {
    var head = $("#sched-head"), body = $("#sched-body");
    head.textContent = g.byYear ? T.year : T.month;
    $("#sched-count").textContent = T.periods(periods.length);
    var html = "";
    g.rows.forEach(function (r, k) {
      html += "<tr><th scope='row'>" + r.short + "</th><td>" + money(r.p) + "</td><td>" + money(r.i) +
        "</td><td>" + money(r.p + r.i) + "</td><td>" + money(r.end) + "</td></tr>";
      if (g.byYear && k === 0) {
        periods.slice(0, 12).forEach(function (pr, j) {
          html += "<tr class='sub'><th scope='row'>" + T.monthN(j + 1) + "</th><td>" + money(pr.p) + "</td><td>" +
            money(pr.i) + "</td><td>" + money(pr.pay) + "</td><td>" + money(pr.end) + "</td></tr>";
        });
      }
    });
    body.innerHTML = html;
  }

  // A full 50-year schedule for all three methods takes well under a millisecond, so render synchronously.
  function update() { render(); }

  function render() {
    var P = parseAmount(amountEl.value) * SCALE, rate = parseRate(rateEl.value), n = months(), m = method();
    if (wordsEl) wordsEl.textContent = amountWords(parseAmount(amountEl.value));
    var ok = P > 0 && n > 0;
    root.classList.toggle("empty", !ok);
    if (!ok) return;
    var res = calculate(P, rate, n, m), ps = res.periods;

    var head = $("#res-payment"), sub = $("#res-payment-sub"), label = $("#res-payment-label");
    if (m === "equal" && ps.length > 1) {
      label.textContent = T.firstMonth;
      head.textContent = money(ps[0].pay);
      sub.textContent = T.downTo + " " + money(ps[ps.length - 1].pay) + " " + T.lastMonth;
    } else {
      label.textContent = T.perMonth;
      head.textContent = money(ps[0].pay);
      sub.textContent = "";
    }
    var mini = $("#mini");
    if (mini) { $("#mini-label").textContent = label.textContent; $("#mini-val").textContent = head.textContent; }
    $("#res-interest").textContent = money(res.totalInterest);
    $("#res-total").textContent = money(res.totalPaid);
    $("#res-principal").textContent = money(P);
    var share = res.totalPaid ? P / res.totalPaid * 100 : 100;
    $("#split-p").style.width = share + "%";
    $("#split-p-pct").textContent = pf.format(share) + "%";
    $("#split-i-pct").textContent = pf.format(100 - share) + "%";

    var aprBox = $("#res-apr");
    if (m === "flat" && res.apr > 0) {
      aprBox.hidden = false;
      $("#res-apr-text").textContent = T.aprNote(pf.format(rate));
      $("#res-apr-val").textContent = pf.format(res.apr) + "%";
    } else aprBox.hidden = true;

    // Compare the three methods on the same inputs.
    ["annuity", "equal", "flat"].forEach(function (mm) {
      var r = mm === m ? res : calculate(P, rate, n, mm);
      $("#cmp-" + mm).textContent = money(r.totalInterest);
      $("#cmp-" + mm + "-pay").textContent = money(r.periods[0].pay);
      var row = $("#cmprow-" + mm); row.classList.toggle("on", mm === m);
    });

    var g = group(ps);
    drawChart(g);
    renderTable(g, ps);
    $("#chart-tip").hidden = true;
    saveUrl();
  }

  // ---------- Wiring ----------
  amountEl.addEventListener("input", function () { formatAmountInput(); update(); });
  rateEl.addEventListener("input", function () { syncRanges(); update(); });
  rateRange.addEventListener("input", function () { rateEl.value = showRate(rateRange.value); update(); });
  termEl.addEventListener("input", function () { syncRanges(); update(); });
  termRange.addEventListener("input", function () { termEl.value = termRange.value; update(); });
  unitEl.addEventListener("change", function () {
    var v = Number(termEl.value) || 0;
    termEl.value = unitEl.value === "m" ? v * 12 : Math.max(1, Math.round(v / 12));
    syncRanges(); update();
  });
  root.querySelectorAll('input[name="method"]').forEach(function (r) { r.addEventListener("change", update); });
  root.querySelectorAll("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () { amountEl.value = nf.format(Number(b.getAttribute("data-amount"))); update(); });
  });
  root.querySelectorAll("[data-pick]").forEach(function (row) {
    row.addEventListener("click", function () {
      var r = root.querySelector('input[name="method"][value="' + row.getAttribute("data-pick") + '"]');
      if (r) { r.checked = true; update(); }
    });
  });
  window.addEventListener("resize", function () {
    $("#chart-tip").hidden = true;
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () { if (lastGroup) drawChart(lastGroup); }, 120);
  });

  // Show the floating summary only while the inputs are on screen and the results are not.
  var mini = $("#mini");
  if (mini && "IntersectionObserver" in window) {
    var formIn = false, resIn = false;
    var setMini = function () { mini.classList.toggle("off", !(formIn && !resIn) || root.classList.contains("empty")); };
    new IntersectionObserver(function (es) { es.forEach(function (e) { formIn = e.isIntersecting; }); setMini(); }).observe($(".inputs"));
    new IntersectionObserver(function (es) { es.forEach(function (e) { resIn = e.isIntersecting; }); setMini(); }).observe($("#res-payment"));
  }

  // Close the language menu when tapping elsewhere.
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details.langs[open]").forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
  });

  loadUrl();
  syncRanges();
  render();
})();
