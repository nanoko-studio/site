"""Generate the Fincal loan calculator pages (VI + EN). Output is plain static HTML; edit the pages by hand afterwards if needed."""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loanlang import LANGS
from complang import C as COMP
from articles import CSS_HREF, nav, related  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
VI_PATH, EN_PATH = "/fincal/tinh-lai-vay/", "/fincal/loan-calculator/"
e = lambda s: html.escape(s, quote=True)

PLAY_SVG = ('<svg viewBox="0 0 512 512" aria-hidden="true"><path fill="#00d3ff" d="M47 24.7C40.2 30.1 36 39.3 36 51.6v408.8c0 12.3 4.2 21.5 11 26.9l1.6 1.4L277 259.7v-7.4L48.6 23.3 47 24.7z"/>'
            '<path fill="#ffce00" d="M353 336.1l-76-76.4v-7.4l76.1-76.4 1.7 1L445 232.4c25.7 14.6 25.7 38.6 0 53.2L354.7 335l-1.7 1.1z"/>'
            '<path fill="#ff3a44" d="M354.7 335L277 256 47 487.7c8.5 9 22.5 10.1 38.3 1.1L354.7 335z"/>'
            '<path fill="#00f076" d="M354.7 177L85.3 23.2C69.5 14.2 55.5 15.3 47 24.3L277 256l77.7-79z"/></svg>')
APPLE_SVG = ('<svg viewBox="0 0 384 512" aria-hidden="true"><path fill="#fff" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>')
WARN_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2 1 21h22L12 2zm1 15h-2v-2h2v2zm0-4h-2V9h2v4z"/></svg>'

L = {
    "vi": dict(
        path=VI_PATH, og="vi_VN", faq_h="Câu hỏi thường gặp", name="Tiếng Việt", short="VI", cur_pre=False, sep=".", comma=True,
        title="Tính lãi vay ngân hàng - Lịch trả nợ hằng tháng | Fincal",
        desc="Máy tính lãi vay miễn phí: nhập số tiền, lãi suất, thời hạn để xem số tiền trả mỗi tháng, tổng lãi, biểu đồ và lịch trả nợ. So sánh dư nợ giảm dần, trả góp đều và lãi phẳng.",
        h1="Tính lãi vay ngân hàng",
        intro="Nhập số tiền vay, lãi suất và thời hạn để biết mỗi tháng phải trả bao nhiêu, tổng tiền lãi và lịch trả nợ. Tính ngay trên trình duyệt, không lưu hay gửi dữ liệu đi đâu.",
        crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="Tính lãi vay",
        amount="Số tiền vay", currency="đ", chips=[(100_000_000, "100 triệu"), (500_000_000, "500 triệu"), (1_000_000_000, "1 tỷ"), (3_000_000_000, "3 tỷ")],
        rate="Lãi suất", rate_unit="%/năm", term="Thời hạn vay", years="năm", months="tháng",
        method="Cách tính lãi",
        methods=[("equal", "Dư nợ giảm dần (gốc đều)", "Trả gốc bằng nhau, lãi tính trên dư nợ còn lại. Tháng đầu trả nhiều nhất."),
                 ("annuity", "Trả góp đều hằng tháng", "Mỗi tháng trả một số tiền như nhau (niên kim)."),
                 ("flat", "Lãi phẳng (dư nợ ban đầu)", "Lãi luôn tính trên số tiền vay ban đầu. Hay gặp ở vay tiêu dùng, trả góp.")],
        default=dict(amount=1_000_000_000, rate=10.5, term=20, unit="y", method="equal"),
        interest="Tổng tiền lãi", lbl_i="Tiền lãi", total="Tổng phải trả", principal="Tiền gốc",
        cmp_title="So sánh 3 cách tính", cmp_note="Cùng số tiền, lãi suất và thời hạn. Bấm một dòng để xem chi tiết.",
        cmp_method="Cách tính", cmp_first="Tháng đầu trả", cmp_interest="Tổng lãi",
        cmp_names={"equal": "Dư nợ giảm dần", "annuity": "Trả góp đều", "flat": "Lãi phẳng"},
        chart_title="Gốc và lãi theo thời gian", chart_note="Mỗi cột là số tiền trả trong năm (hoặc tháng, với khoản vay ngắn). Chạm vào cột để xem chi tiết.",
        sched_title="Lịch trả nợ", sched_cols=["Gốc", "Lãi", "Tổng trả", "Dư nợ còn lại"],
        sched_more="Năm đầu có chi tiết từng tháng. Lịch trả nợ từng tháng cho mọi năm có trong app Fincal.",
        promo_title="Khoản vay của bạn phức tạp hơn?",
        promo_lead="App Fincal tính được những thứ ngân hàng thật sự áp dụng:",
        promo_items=[("Lãi suất theo giai đoạn", "ưu đãi những tháng đầu, sau đó đổi sang lãi suất mới, bao nhiêu giai đoạn cũng được"),
                     ("Trả nợ trước hạn", "một lần hoặc định kỳ, tính cả phí phạt, xem tiết kiệm được bao nhiêu lãi và bớt bao nhiêu tháng"),
                     ("Lưu kịch bản", "đặt tên, mở lại, nhân bản để thử phương án khác; lịch sử tính toán tự lưu"),
                     ("Lịch trả nợ từng tháng", "cho mọi năm, chia sẻ kết quả kèm biểu đồ dưới dạng ảnh")],
        get_on="TẢI TRÊN", dl_on="TẢI TRÊN", ct="web-fincal-calc-loan-vi",
        apr_label="Lãi suất thực tế", footer_privacy="Quyền riêng tư", footer_support="Hỗ trợ",
        article=None, faq=None,
    ),
    "en": dict(
        path=EN_PATH, og="en_US", faq_h="Frequently asked questions", name="English", short="EN", cur_pre=False, sep=",", comma=False,
        title="Loan Calculator - Monthly Payment and Amortization Schedule | Fincal",
        desc="Free loan calculator: enter the amount, rate and term to see your monthly payment, total interest, a chart and the repayment schedule. Compare annuity, equal principal and flat-rate loans.",
        h1="Loan calculator",
        intro="Enter the loan amount, interest rate and term to see your monthly payment, total interest and repayment schedule. Everything runs in your browser - nothing is stored or sent anywhere.",
        crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="Loan calculator",
        amount="Loan amount", currency="", chips=[(10_000, "10K"), (50_000, "50K"), (250_000, "250K"), (500_000, "500K")],
        rate="Interest rate", rate_unit="% a year", term="Loan term", years="years", months="months",
        method="Repayment method",
        methods=[("annuity", "Equal monthly payments", "The same payment every month (annuity). Most mortgages and car loans."),
                 ("equal", "Equal principal", "Same principal each month, interest on the remaining balance. Highest payment first."),
                 ("flat", "Flat rate", "Interest is always charged on the original amount. Common for personal and installment loans.")],
        default=dict(amount=300_000, rate=6.5, term=30, unit="y", method="annuity"),
        interest="Total interest", lbl_i="Interest", total="Total paid", principal="Principal",
        cmp_title="Compare the 3 methods", cmp_note="Same amount, rate and term. Tap a row to see its details.",
        cmp_method="Method", cmp_first="First payment", cmp_interest="Total interest",
        cmp_names={"equal": "Equal principal", "annuity": "Equal payments", "flat": "Flat rate"},
        chart_title="Principal and interest over time", chart_note="Each bar is what you pay in a year (or a month, for short loans). Tap a bar for details.",
        sched_title="Repayment schedule", sched_cols=["Principal", "Interest", "Total paid", "Balance left"],
        sched_more="The first year is broken down by month. The monthly schedule for every year is in the Fincal app.",
        promo_title="Is your loan more complicated?",
        promo_lead="The Fincal app handles what lenders actually do:",
        promo_items=[("Rate changes", "an intro rate for the first months, then a new rate - as many periods as you need"),
                     ("Prepayments", "one-off or recurring, with fees; see the interest saved and months cut"),
                     ("Saved scenarios", "name, reopen and duplicate them to try other options; history is saved automatically"),
                     ("Monthly schedule", "for every year, and share the result with its charts as an image")],
        get_on="GET IT ON", dl_on="DOWNLOAD ON THE", ct="web-fincal-calc-loan",
        apr_label="Real rate", footer_privacy="Privacy Policy", footer_support="Support",
        article=None, faq=None,
    ),
}

L["vi"]["article"] = """
<h2>Cách tính lãi vay theo dư nợ giảm dần</h2>
<p>Đây là cách phần lớn ngân hàng ở Việt Nam dùng cho vay mua nhà, mua xe và vay thế chấp. Tiền gốc được chia đều cho số tháng, còn tiền lãi chỉ tính trên số dư nợ còn lại, nên càng về sau càng trả ít.</p>
<div class="formula">Gốc mỗi tháng = Số tiền vay ÷ Số tháng<br>Lãi tháng này = Dư nợ còn lại × Lãi suất năm ÷ 12</div>
<h2>Cách tính trả góp đều hằng tháng</h2>
<p>Mỗi tháng trả một số tiền bằng nhau, gồm cả gốc và lãi (phương pháp niên kim). Những tháng đầu phần lớn là tiền lãi, càng về sau phần gốc càng nhiều. Dễ lên kế hoạch chi tiêu, nhưng tổng lãi cao hơn dư nợ giảm dần.</p>
<div class="formula">Tiền trả mỗi tháng = P × r ÷ (1 − (1 + r)<sup>−n</sup>)<br>P: số tiền vay · r: lãi suất năm ÷ 12 · n: số tháng</div>
<h2>Lãi phẳng là gì, vì sao cần cẩn thận</h2>
<p>Với lãi phẳng, tiền lãi luôn tính trên số tiền vay ban đầu, kể cả khi bạn đã trả bớt gốc. Vì vậy cùng một con số lãi suất, lãi phẳng đắt hơn nhiều so với dư nợ giảm dần. Ví dụ vay 100 triệu trong 24 tháng với lãi phẳng 12%/năm thì tổng lãi là 24 triệu, tương đương lãi suất dư nợ giảm dần khoảng <b>21,57%/năm</b>. Máy tính phía trên hiện con số quy đổi này khi bạn chọn lãi phẳng. <a href="/fincal/lai-phang-va-lai-giam-dan/">Xem giải thích chi tiết và bảng quy đổi →</a></p>
<h2>Ví dụ: vay 1 tỷ, lãi suất 10,5%/năm trong 20 năm</h2>
<table class="cmp">
<thead><tr><th>Cách tính</th><th>Tháng đầu trả</th><th>Tổng lãi</th></tr></thead>
<tbody>
<tr><td>Dư nợ giảm dần</td><td>12.916.667 đ</td><td>1.054.374.917 đ</td></tr>
<tr><td>Trả góp đều</td><td>9.983.799 đ</td><td>1.396.111.658 đ</td></tr>
<tr><td>Lãi phẳng</td><td>12.916.667 đ</td><td>2.100.000.000 đ</td></tr>
</tbody></table>
<p>Trả góp đều nhẹ hơn khoảng 2,9 triệu mỗi tháng lúc đầu, nhưng tổng lãi cao hơn khoảng 342 triệu so với dư nợ giảm dần.</p>
<h2>Trả nợ trước hạn có lợi không?</h2>
<p>Trả bớt nợ giúp giảm tiền lãi, nhưng thường phải chịu phí phạt 1-3% số tiền trả trước, và bạn sẽ được hỏi muốn giảm kỳ hạn hay giảm số tiền trả hằng tháng. <a href="/fincal/tra-no-truoc-han/">Xem ví dụ và tính phí phạt có đáng không →</a></p>
<h2>Hết lãi ưu đãi, tiền trả tăng bao nhiêu?</h2>
<p>Phần lớn khoản vay mua nhà có lãi ưu đãi 1-3 năm đầu rồi chuyển sang thả nổi, và tiền trả hằng tháng có thể tăng hơn một phần tư ngay tháng đầu tiên. <a href="/fincal/lai-uu-dai-va-tha-noi/">Xem ví dụ và cách chọn gói ưu đãi →</a></p>
"""
L["vi"]["faq"] = [
    ("Nên chọn dư nợ giảm dần hay trả góp đều?",
     "Dư nợ giảm dần có tổng lãi thấp hơn nhưng những tháng đầu phải trả nhiều. Trả góp đều nhẹ hơn lúc đầu và dễ lên kế hoạch, đổi lại tổng lãi cao hơn. Nếu thu nhập đủ để trả mức tháng đầu, dư nợ giảm dần thường rẻ hơn."),
    ("Lãi suất 1%/tháng là bao nhiêu một năm?",
     "1%/tháng tương đương 12%/năm. Nếu đó là lãi phẳng, lãi suất thực tế theo dư nợ giảm dần cao hơn nhiều, khoảng 21-22%/năm với khoản vay 2 năm. Chọn \"Lãi phẳng\" ở trên để xem con số chính xác cho khoản vay của bạn."),
    ("Kết quả có giống ngân hàng tính không?",
     "Máy tính làm tròn đến từng đồng mỗi kỳ và tính lãi theo tháng (lãi suất năm chia 12), giống app Fincal. Một số ngân hàng tính lãi theo số ngày thực tế trong tháng, nên có thể chênh vài nghìn đồng mỗi kỳ."),
    ("Lãi suất thay đổi hoặc trả nợ trước hạn thì tính thế nào?",
     "Trang này dùng một mức lãi suất cố định. Để tính lãi ưu đãi những tháng đầu rồi đổi sang lãi suất mới, hoặc trả trước hạn có phí phạt, hãy dùng app Fincal miễn phí trên Android và iOS."),
    ("Dữ liệu tôi nhập có bị gửi đi không?",
     "Không. Mọi phép tính chạy ngay trên trình duyệt của bạn. Các con số chỉ nằm trên đường dẫn của trang để bạn chia sẻ lại được kết quả."),
]
L["en"]["article"] = """
<h2>How equal monthly payments are calculated</h2>
<p>Most mortgages and car loans use equal monthly payments (an annuity). Each payment is the same, but early payments are mostly interest and later ones mostly principal.</p>
<div class="formula">Monthly payment = P × r ÷ (1 − (1 + r)<sup>−n</sup>)<br>P: loan amount · r: annual rate ÷ 12 · n: number of months</div>
<h2>How equal principal works</h2>
<p>The principal is split evenly across all months and interest is charged only on the remaining balance, so payments start high and fall every month. Total interest is lower than with equal payments.</p>
<div class="formula">Principal each month = Loan amount ÷ Months<br>Interest this month = Remaining balance × Annual rate ÷ 12</div>
<h2>Why flat-rate loans cost more than they look</h2>
<p>With a flat rate, interest is always charged on the original amount, even after you have repaid part of it. A 2-year loan of 25,000 at a 12% flat rate costs 6,000 in interest - the same as a reducing-balance rate of about <b>21.57%</b>. The calculator shows this real rate when you pick Flat rate. <a href="/fincal/flat-rate-vs-reducing-balance/">Read the full explanation and conversion table →</a></p>
<h2>Example: 300,000 at 6.5% for 30 years</h2>
<table class="cmp">
<thead><tr><th>Method</th><th>First payment</th><th>Total interest</th></tr></thead>
<tbody>
<tr><td>Equal payments</td><td>1,896.20</td><td>382,636.71</td></tr>
<tr><td>Equal principal</td><td>2,458.33</td><td>293,313.66</td></tr>
<tr><td>Flat rate</td><td>2,458.33</td><td>585,000.00</td></tr>
</tbody></table>
<p>Equal payments start about 562 lower each month, but cost about 89,000 more in interest over the life of the loan.</p>
<h2>Is it worth paying off early?</h2>
<p>Paying part of the loan off early cuts the interest, but there may be a fee, and you will be asked whether you want a shorter term or a lower monthly payment. <a href="/fincal/paying-off-a-loan-early/">See an example and check whether the fee is worth it →</a></p>
"""
L["en"]["faq"] = [
    ("Which is cheaper, equal payments or equal principal?",
     "Equal principal always costs less interest, because you repay principal faster. Equal payments are easier to budget for and start lower. If you can afford the higher first payments, equal principal is usually cheaper."),
    ("Does it work for any currency?",
     "Yes. Enter the amount in your currency; results are rounded to the cent every month."),
    ("Will my lender's numbers match exactly?",
     "The calculator charges interest monthly (annual rate ÷ 12) and rounds every period, the same as the Fincal app. Lenders that charge interest by the actual number of days can differ slightly."),
    ("What about rate changes or extra payments?",
     "This page uses a single fixed rate. For an intro rate followed by a new rate, or prepayments with fees, use the free Fincal app on Android and iOS."),
    ("Is what I type sent anywhere?",
     "No. Every calculation runs in your browser. The numbers only appear in the page address so you can share your result."),
]

L.update(LANGS)
ORDER = ["en", "vi", "id", "th", "pt-BR", "ms"]


def stores(t):
    play = (f"https://play.google.com/store/apps/details?id=com.namnoit.fincal&amp;referrer=utm_source%3Dnanoko.app"
            f"%26utm_medium%3Dwebsite%26utm_campaign%3D{t['ct']}")
    apple = f"https://apps.apple.com/app/apple-store/id6783214662?pt=128952050&amp;ct={t['ct']}&amp;mt=8"
    return (f'<div class="stores">'
            f'<a class="store" href="{play}" target="_blank" rel="noopener">{PLAY_SVG}<span><small>{t["get_on"]}</small><strong>Google Play</strong></span></a>'
            f'<a class="store" href="{apple}" target="_blank" rel="noopener">{APPLE_SVG}<span><small>{t["dl_on"]}</small><strong>App Store</strong></span></a>'
            f'</div>')


def jsonld(lang, t):
    url = BASE + t["path"]
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": t["h1"] + " - Fincal", "url": url, "inLanguage": lang,
         "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "description": t["desc"],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": "Nanoko Studio", "url": BASE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": t["crumb_home"], "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": t["crumb_app"], "item": BASE + "/fincal/"},
            {"@type": "ListItem", "position": 3, "name": t["crumb_page"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
    ]}, ensure_ascii=False)


def page(lang):
    t = L[lang]
    d = t["default"]
    fmt = lambda v: f"{v:,}".replace(",", t["sep"])
    chips = "".join(f'<button type="button" data-amount="{v}">{e(lbl)}</button>' for v, lbl in t["chips"])
    methods = "".join(
        f'<label><input type="radio" name="method" value="{v}"{" checked" if v == d["method"] else ""}>'
        f'<span><b>{e(n)}</b><small>{e(s)}</small></span></label>' for v, n, s in t["methods"])
    order = [m[0] for m in t["methods"]]
    cmp_rows = "".join(
        f'<tr id="cmprow-{m}" data-pick="{m}"><td>{e(t["cmp_names"][m])}</td><td id="cmp-{m}-pay">-</td><td id="cmp-{m}">-</td></tr>'
        for m in order)
    cols = "".join(f"<th scope='col'>{e(c)}</th>" for c in t["sched_cols"])
    faq = "".join(f"<details><summary>{e(q)}</summary><div>{e(a)}</div></details>" for q, a in t["faq"])
    promo = "".join(f"<li><b>{e(a)}</b>: {e(b)}</li>" for a, b in t["promo_items"])
    cur = f'<span class="unit">{t["currency"]}</span>' if t["currency"] and not t["cur_pre"] else ""
    cur_pre = f'<span class="unit pre">{t["currency"]}</span>' if t["cur_pre"] else ""
    rate_val = str(d["rate"]).replace(".", ",") if t["comma"] else str(d["rate"])
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{L[k]["path"]}">' for k in ORDER)
    langmenu = "".join(
        f'<a href="{L[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "") + f'>{e(L[k]["name"])}</a>'
        for k in ORDER)
    url = BASE + t["path"]
    faq_h = t["faq_h"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{url}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{BASE}{EN_PATH}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fincal">
<meta property="og:locale" content="{t["og"]}">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/fincal/ic_launcher-playstore.png">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f6f6f1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15171a" media="(prefers-color-scheme: dark)">
<meta name="apple-itunes-app" content="app-id=6783214662">
<link rel="icon" type="image/png" href="/fincal/ic_launcher-playstore.png">
<link rel="stylesheet" href="{CSS_HREF}">
<script type="application/ld+json">{jsonld(lang, t)}</script>
</head>
<body>
<header class="topbar"><div class="wrap">
<a class="brand" href="/fincal/"><img src="/fincal/ic_launcher-playstore.png" alt="" width="32" height="32">Fincal</a>
<span class="spacer"></span>
{nav(lang)}
<details class="langs"><summary aria-label="{e(t["name"])}">{e(t["name"])}</summary><nav class="langmenu">{langmenu}</nav></details>
</div></header>

<main class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">{e(t["crumb_home"])}</a> › <a href="/fincal/">{e(t["crumb_app"])}</a> › <span>{e(t["crumb_page"])}</span></nav>
<h1>{e(t["h1"])}</h1>
<p class="intro">{e(t["intro"])}</p>

<div class="calc" data-loan-calc>
<form class="card inputs" onsubmit="return false" autocomplete="off">
  <div class="field">
    <label for="amount">{e(t["amount"])}</label>
    <div class="box">{cur_pre}<input id="amount" inputmode="numeric" value="{fmt(d["amount"])}" aria-describedby="amount-words">{cur}</div>
    <p class="hint" id="amount-words" aria-live="polite"></p>
    <div class="chips">{chips}</div>
  </div>
  <div class="field">
    <label for="rate">{e(t["rate"])}</label>
    <div class="box"><input id="rate" inputmode="decimal" value="{rate_val}"><span class="unit">{e(t["rate_unit"])}</span></div>
    <input id="rate-range" type="range" min="0" max="30" step="0.1" value="{d["rate"]}" aria-label="{e(t["rate"])}">
  </div>
  <div class="field">
    <label for="term">{e(t["term"])}</label>
    <div class="box"><input id="term" inputmode="numeric" value="{d["term"]}">
      <select id="unit" aria-label="{e(t["term"])}"><option value="y" selected>{e(t["years"])}</option><option value="m">{e(t["months"])}</option></select></div>
    <input id="term-range" type="range" min="1" max="35" step="1" value="{d["term"]}" aria-label="{e(t["term"])}">
  </div>
  <fieldset class="field" style="border:0;padding:0;margin:0">
    <legend class="label" style="font-size:14px;font-weight:600;margin:0 0 6px;padding:0">{e(t["method"])}</legend>
    <div class="seg">{methods}</div>
  </fieldset>
</form>

<a class="mini off" id="mini" href="#results" aria-hidden="true" tabindex="-1"><span id="mini-label"></span><b id="mini-val"></b><i>↓</i></a>
<div class="results" id="results" aria-live="polite">
  <section class="card">
    <div class="headline">
      <div class="main"><div class="label" id="res-payment-label"></div><div class="big" id="res-payment">-</div><div class="sub" id="res-payment-sub"></div></div>
      <div class="stat"><div class="label">{e(t["total"])}</div><b id="res-total">-</b></div>
      <div class="stat"><div class="label">{e(t["interest"])}</div><b id="res-interest">-</b></div>
    </div>
    <div class="split">
      <div class="bar" role="img" aria-label="{e(t["principal"])} / {e(t["interest"])}"><span class="p" id="split-p" style="width:60%"></span><span class="i"></span></div>
      <div class="legend"><span><i class="sw sw-p"></i>{e(t["principal"])} <b id="res-principal"></b> · <span id="split-p-pct"></span></span><span><i class="sw sw-i"></i>{e(t["lbl_i"])} · <span id="split-i-pct"></span></span></div>
    </div>
    <div class="apr" id="res-apr" hidden>{WARN_SVG}<span id="res-apr-text"></span><b id="res-apr-val"></b></div>
  </section>

  <section class="card">
    <h2>{e(t["cmp_title"])}</h2>
    <p class="note">{e(t["cmp_note"])}</p>
    <table class="cmp"><thead><tr><th scope="col">{e(t["cmp_method"])}</th><th scope="col">{e(t["cmp_first"])}</th><th scope="col">{e(t["cmp_interest"])}</th></tr></thead>
    <tbody>{cmp_rows}</tbody></table>
  </section>

  <section class="card">
    <h2>{e(t["chart_title"])}</h2>
    <p class="note">{e(t["chart_note"])}</p>
    <div class="legend" style="margin:0 0 8px"><span><i class="sw sw-p"></i>{e(t["principal"])}</span><span><i class="sw sw-i"></i>{e(t["lbl_i"])}</span></div>
    <div class="chartbox"><svg id="chart" role="img" aria-label="{e(t["chart_title"])}" viewBox="0 0 640 260"></svg><div class="tip" id="chart-tip" hidden></div></div>
  </section>

  <section class="card promo">
    <img src="/fincal/ic_launcher-playstore.png" alt="Fincal" width="56" height="56" loading="lazy">
    <div>
      <h2>{e(t["promo_title"])}</h2>
      <p class="note" style="margin:0">{e(t["promo_lead"])}</p>
      <ul>{promo}</ul>
      {stores(t)}
    </div>
  </section>

  <details class="card fold">
    <summary><h2>{e(t["sched_title"])}</h2><span class="fold-hint" id="sched-count"></span></summary>
    <div class="tablewrap"><table class="sched"><thead><tr><th scope="col" id="sched-head"></th>{cols}</tr></thead><tbody id="sched-body"></tbody></table></div>
    <p class="more">{e(t["sched_more"])}</p>
  </details>
</div>
</div>

<article class="article">
{t["article"].strip()}
<h2>{faq_h}</h2>
<div class="faq">{faq}</div>
<p class="calc-links"><a href="{COMP[lang]["path"]}">{e(COMP[lang]["compound_name"])} →</a></p>
{related(lang, t["path"], "loan")}
</article>
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(t["footer_privacy"])}</a><a href="/fincal/support/">{e(t["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
<script src="/fincal/calc/loan.js" defer></script>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, L[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(page(lang))
    print(p)
