"""Single list of Fincal articles and calculators.

Adding an article: write its <x>lang.py + <x>page.py, then add one entry to ARTICLES below.
The blog pages, the "Related articles" block on every page, the header Blog link and
sitemap.xml are all built from this list (run tools/fincal/build.py).
No side effects on import: page generators import this module.
"""
import hashlib
import html
import os

from complang import C as COMP
from loanlang import LANGS as LOAN_LANGS
from flatlang import A as FLAT
from prepaylang import A as PREPAY
from teaserlang import T as TEASER
from depositlang import D as DEPOSIT

ORDER = ["en", "vi", "id", "th", "pt-BR", "ms"]
e = lambda s: html.escape(s, quote=True)

# calc.css?v=<hash>: a changed stylesheet gets a new URL, so browsers never pair new HTML with an old cached CSS.
_CSS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fincal", "calc", "calc.css")
CSS_HREF = "/fincal/calc/calc.css?v=" + hashlib.sha256(open(_CSS, "rb").read()).hexdigest()[:8]

# Topic of each article; the blog page groups by topic in this order.
TOPICS = ["loan", "save"]

# Newest first. "t" maps language -> that language's text dict (needs path, h1, desc).
ARTICLES = [
    dict(key="deposit", topic="save", date="2026-11-21", t=DEPOSIT),
    dict(key="prepay", topic="loan", date="2026-11-21", t=PREPAY),
    dict(key="teaser", topic="loan", date="2026-11-21", t=TEASER),
    dict(key="flat", topic="loan", date="2026-11-20", t=FLAT),
]

# Language menu label and footer words (same as on the calculator pages).
UI = {
    "en": dict(name="English", short="EN", footer_privacy="Privacy Policy", footer_support="Support"),
    "vi": dict(name="Tiếng Việt", short="VI", footer_privacy="Quyền riêng tư", footer_support="Hỗ trợ"),
    **{k: {f: v[f] for f in ("name", "short", "footer_privacy", "footer_support")} for k, v in LOAN_LANGS.items()},
}

LOAN_PATH = {"en": "/fincal/loan-calculator/", "vi": "/fincal/tinh-lai-vay/", **{k: v["path"] for k, v in LOAN_LANGS.items()}}
# Calculator for each topic: language -> (path, name).
CALCS = {
    "loan": {k: (LOAN_PATH[k], COMP[k]["loan_link"]) for k in ORDER},
    "save": {k: (COMP[k]["path"], COMP[k]["compound_name"]) for k in ORDER},
}

BLOG = {
    "en": dict(path="/fincal/blog/", nav="Blog", title="Blog - loan and savings interest guides | Fincal",
               desc="Guides to loan and savings interest with worked examples: flat vs reducing balance, paying off a loan early, monthly interest vs at maturity.",
               intro="Guides to loan and savings interest, with worked numbers and a calculator to try your own.", related="Related articles", all="All articles"),
    "vi": dict(path="/fincal/blog/vi/", nav="Blog", title="Blog - hướng dẫn lãi vay và lãi tiết kiệm | Fincal",
               desc="Bài viết về lãi vay và lãi tiết kiệm kèm ví dụ tính sẵn: lãi phẳng và lãi giảm dần, trả nợ trước hạn, lãi ưu đãi và thả nổi, nhận lãi hằng tháng hay cuối kỳ.",
               intro="Bài viết giải thích lãi vay và lãi tiết kiệm, có số liệu tính sẵn và công cụ để bạn thử với con số của mình.", related="Bài liên quan", all="Xem tất cả bài viết"),
    "id": dict(path="/fincal/blog/id/", nav="Blog", title="Blog - panduan bunga pinjaman dan deposito | Fincal",
               desc="Panduan bunga pinjaman dan deposito dengan contoh hitungan: bunga flat vs efektif, pelunasan dipercepat, bunga deposito bulanan atau saat jatuh tempo.",
               intro="Panduan bunga pinjaman dan tabungan, lengkap dengan contoh hitungan dan kalkulator untuk mencoba angka Anda sendiri.", related="Artikel terkait", all="Semua artikel"),
    "th": dict(path="/fincal/blog/th/", nav="บล็อก", title="บล็อก - คู่มือดอกเบี้ยเงินกู้และเงินฝาก | Fincal",
               desc="บทความเรื่องดอกเบี้ยเงินกู้และเงินฝากพร้อมตัวอย่างคำนวณ: flat rate กับลดต้นลดดอก โปะหนี้บ้าน ฝากประจำรับดอกเบี้ยรายเดือนหรือครบกำหนด",
               intro="บทความอธิบายดอกเบี้ยเงินกู้และเงินออม พร้อมตัวเลขตัวอย่างและเครื่องคำนวณให้ลองกับตัวเลขของคุณเอง", related="บทความที่เกี่ยวข้อง", all="บทความทั้งหมด"),
    "pt-BR": dict(path="/fincal/blog/pt-br/", nav="Blog", title="Blog - guias de juros de empréstimos e investimentos | Fincal",
                  desc="Guias sobre juros de empréstimos e investimentos com exemplos calculados: taxa flat x saldo devedor, amortização antecipada, juros mensais ou no vencimento.",
                  intro="Guias sobre juros de empréstimos e investimentos, com exemplos calculados e uma calculadora para testar os seus números.", related="Artigos relacionados", all="Todos os artigos"),
    "ms": dict(path="/fincal/blog/ms/", nav="Blog", title="Blog - panduan faedah pinjaman dan simpanan | Fincal",
               desc="Panduan faedah pinjaman dan simpanan dengan contoh kiraan: kadar rata vs baki berkurangan, bayar pinjaman lebih awal, faedah bulanan atau semasa matang.",
               intro="Panduan faedah pinjaman dan simpanan, dengan contoh kiraan dan kalkulator untuk mencuba angka anda sendiri.", related="Artikel berkaitan", all="Semua artikel"),
}


def articles(lang, topic=None):
    """Articles available in this language (newest first): list of (entry, text dict)."""
    return [(a, a["t"][lang]) for a in ARTICLES if lang in a["t"] and (topic is None or a["topic"] == topic)]


def nav(lang, current=False):
    """Header link to the blog; goes right after <span class="spacer"></span>."""
    b = BLOG[lang]
    cur = ' aria-current="page"' if current else ""
    return f'<a class="navlink" href="{b["path"]}"{cur}>{e(b["nav"])}</a>'


# Default thumbnails, one per topic, drawn inline so they follow light/dark colors.
# An article can set img="/fincal/blog/img/<name>.webp" (4:3) to use its own picture instead.
THUMBS = {
    # Loan: monthly payments, principal and interest; interest shrinks as the balance falls.
    "loan": '<svg viewBox="0 0 120 90" aria-hidden="true">' + "".join(
        f'<rect class="tp" x="{14 + i * 16}" y="{78 - 34}" width="10" height="34" rx="2"/>'
        f'<rect class="ti" x="{14 + i * 16}" y="{78 - 34 - h - 2}" width="10" height="{h}" rx="2"/>'
        for i, h in enumerate([26, 22, 18, 14, 10, 6])) + '</svg>',
    # Savings: balance growing faster over time.
    "save": '<svg viewBox="0 0 120 90" aria-hidden="true">'
            '<path class="ta" d="M12 78 L12 70 C40 68 64 60 82 46 C94 37 102 27 108 16 L108 78 Z"/>'
            '<path class="tl" d="M12 70 C40 68 64 60 82 46 C94 37 102 27 108 16"/>'
            '<circle class="td" cx="108" cy="16" r="4.5"/></svg>',
}


_S = '<svg viewBox="0 0 120 90" aria-hidden="true">'
THUMBS.update({
    # Flat rate stays on the original amount (dashed, level) while reducing balance falls.
    "flat": _S + '<path class="tg" d="M14 78 H106"/><path class="tf" d="M14 30 H106"/>'
                 '<path class="tl" d="M14 30 L106 70"/><circle class="td" cx="106" cy="30" r="4.5"/></svg>',
    # Prepayment: one big extra payment, then the loan ends early (remaining months ghosted).
    "prepay": _S + "".join(f'<rect class="tp" x="{12 + i * 14}" y="54" width="9" height="24" rx="2"/>' for i in range(3))
                 + '<rect class="ti" x="54" y="16" width="9" height="62" rx="2"/>'
                 + "".join(f'<rect class="tp" x="{68 + i * 14}" y="56" width="9" height="22" rx="2"/>' for i in range(2))
                 + '<rect class="tx" x="96" y="56" width="9" height="22" rx="2"/></svg>',
    # Teaser rate: low for a while, then a step up to the floating rate.
    "teaser": _S + '<path class="ta" d="M12 78 V60 H50 V30 H108 V78 Z"/>'
                   '<path class="tl" d="M12 60 H50 V30 H108"/><circle class="td" cx="50" cy="30" r="4.5"/></svg>',
    # Monthly interest (small bars every month) vs one payout at maturity.
    "deposit": _S + "".join(f'<rect class="tp" x="{12 + i * 8}" y="70" width="5" height="8" rx="1.5"/>' for i in range(11))
                    + '<rect class="ti" x="102" y="18" width="8" height="60" rx="2"/></svg>',
})


def thumb(a):
    if a.get("img"):
        return f'<span class="thumb"><img src="{a["img"]}" alt="" width="120" height="90" loading="lazy"></span>'
    return f'<span class="thumb">{THUMBS.get(a["key"], THUMBS[a["topic"]])}</span>'


def postlist(items):
    li = "".join(
        f'<li><a href="{t["path"]}">{thumb(a)}<span class="pl-text"><b>{e(t["h1"])}</b> '
        f'<span class="pl-desc">{e(t["desc"])}</span></span></a></li>' for a, t in items)
    return f'<ul class="postlist">{li}</ul>'


def related(lang, path, topic, limit=3):
    """'Related articles' block for the end of a page: same topic first, then the rest, newest first."""
    others = [x for x in articles(lang) if x[1]["path"] != path]
    others.sort(key=lambda x: x[0]["topic"] != topic)  # stable: keeps newest-first inside each group
    if not others:
        return ""
    b = BLOG[lang]
    return (f'<section class="related"><h2>{e(b["related"])}</h2>{postlist(others[:limit])}'
            f'<p class="calc-links"><a href="{b["path"]}">{e(b["all"])} →</a></p></section>')


def site_urls():
    """Every Fincal page built from this list, for sitemap.xml."""
    urls = [BLOG[k]["path"] for k in ORDER]
    for topic in TOPICS:
        urls += [CALCS[topic][k][0] for k in ORDER]
    for a in ARTICLES:
        urls += [a["t"][k]["path"] for k in ORDER if k in a["t"]]
    return urls
