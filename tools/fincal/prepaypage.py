"""Article: paying a loan off early. Run: python3 -I prepaypage.py <site root>
Numbers come from fincal/calc/prepay.js (run through node) so they match the in-page calculator."""
import html
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loanpage import PLAY_SVG, APPLE_SVG, L as LOAN  # noqa: E402  (also regenerates the loan pages)
from complang import C as COMP  # noqa: E402
from prepaylang import A  # noqa: E402
from articles import CSS_HREF, nav, related  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
DATE = "2026-11-21"
ORDER = [k for k in ["en", "vi", "id", "th", "pt-BR", "ms"] if k in A]
e = lambda s: html.escape(s, quote=True)

JS = r"""
const {prepay}=require(process.argv[1]+"/fincal/calc/prepay.js");
const cfg=JSON.parse(process.argv[2]), res={};
for (const [lang,c] of Object.entries(cfg)) {
  const s=c.scale;
  res[lang]={ex: prepay(c.B*s,c.R,c.n,c.method,c.X*s,c.F),
    table: c.fees.map(f=>c.years.map(y=>prepay(c.B*s,c.R,y*12,c.method,c.X*s,f).lower.yield))};
}
console.log(JSON.stringify(res));
"""
cfg = {k: dict(B=A[k]["B"], R=A[k]["R"], n=A[k]["n"], method=A[k]["method"], X=A[k]["X"], F=A[k]["F"],
               fees=A[k]["fees"], years=A[k]["years"], scale=A[k]["fmt"]["scale"]) for k in ORDER}
D = json.loads(subprocess.run(["node", "-e", JS, ROOT, json.dumps(cfg)], capture_output=True, text=True, check=True).stdout)

W, H, Lm, Rm, T, B = 400, 210, 44, 10, 10, 26
pw, ph = W - Lm - Rm, H - T - B


class Lang:
    def __init__(self, lang):
        self.lang, self.t, self.d = lang, A[lang], D[lang]
        self.f = self.t["fmt"]

    def num(self, v, dec):
        s = f"{v:,.{dec}f}"
        if self.f["dc"]:
            s = s.replace(",", "\0").replace(".", ",").replace("\0", ".")
        return s

    def money(self, v):  # v in smallest units
        dec = self.f["dec"]
        n = self.num(round(v / self.f["scale"], dec), dec)
        return f'{self.f["cur"]} {n}' if self.f["pre"] else (f'{n} {self.f["cur"]}' if self.f["cur"] else n)

    def rate(self, y):
        return self.num(y / self.t["div"], 1) + self.t["sfx"]

    def short(self, v):
        v = v / self.f["scale"]
        if self.lang == "id":
            if v >= 1e9:
                return "Rp " + f"{v / 1e9:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " miliar"
            if v >= 1e6:
                return "Rp " + f"{v / 1e6:.1f}".rstrip("0").rstrip(".").replace(".", ",") + " juta"
            return self.money(v * self.f["scale"])
        if self.lang != "vi":
            return self.money(v * self.f["scale"])
        if v >= 1e9:
            return f"{v / 1e9:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " tỷ"
        if v >= 1e6:
            return f"{v / 1e6:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " triệu"
        return f"{v / 1e3:.0f} nghìn"

    def months(self, m):
        return (self.t["m1"] if m == 1 else self.t["mn"]).format(n=m)


def ychart(v, vmax):
    return T + ph - v / vmax * ph


def chart(x):
    t, d = x.t, x.d["ex"]
    n = t["n"]
    vmax = t["B"] * x.f["scale"]
    years = n // 12
    xm = lambda m: Lm + pw * m / n
    s = []
    for v, lbl in zip((0, vmax / 2, vmax), t["ticks"]):
        y = ychart(v, vmax)
        s.append(f'<line class="grid" x1="{Lm}" x2="{W - Rm}" y1="{y:.1f}" y2="{y:.1f}"/>')
        s.append(f'<text class="tick" x="{Lm - 6}" y="{y + 4:.1f}" text-anchor="end">{e(lbl)}</text>')
    s.append(f'<line class="axis" x1="{Lm}" x2="{W - Rm}" y1="{T + ph}" y2="{T + ph}"/>')
    series = {"base": [vmax] + d["base"]["ends"], "shorter": [d["rest"]] + d["shorter"]["ends"],
              "lower": [d["rest"]] + d["lower"]["ends"]}
    for k, cls in (("base", "s-flat"), ("lower", "s-annuity"), ("shorter", "s-equal")):
        pts = series[k]
        path = "M" + " L".join(f"{xm(m):.1f},{ychart(v, vmax):.1f}" for m, v in enumerate(pts))
        s.append(f'<path class="ln {cls}" d="{path}"/>')
    step = 5 if years > 8 else 1
    for yr in range(0, years + 1, step):
        lbl = t["year0"] if yr == 0 else t["year_tick"].format(y=yr)
        anchor = "start" if yr == 0 else ("end" if yr == years else "middle")
        s.append(f'<text class="tick" x="{xm(yr * 12):.1f}" y="{H - 8}" text-anchor="{anchor}">{e(lbl)}</text>')
    nm = t["names"]
    gw = pw / years
    for yr in range(years + 1):
        m = yr * 12
        val = lambda k: series[k][m] if m < len(series[k]) else 0
        title = t["year_tip0"] if yr == 0 else t["year_tip"].format(y=yr)
        tip = "|".join([title] + [p for k in ("base", "shorter", "lower") for p in (nm[k], x.money(val(k)))])
        x0 = max(Lm, xm(m) - gw / 2)
        x1 = min(W - Rm, xm(m) + gw / 2)
        s.append(f'<rect class="hit" x="{x0:.1f}" y="{T}" width="{x1 - x0:.1f}" height="{ph}" data-tip="{e(tip)}"/>')
    return (f'<svg class="achart" viewBox="0 0 {W} {H}" role="img" aria-label="{e(t["fig"][2])}" data-sw="s-flat s-equal s-annuity">'
            + "".join(s) + "</svg>")


def ytable(x):
    t = x.t
    head = "".join(f"<th scope='col'>{e(t['tbl_year'].format(y=y))}</th>" for y in t["years"])
    body = "".join(f"<tr><td>{x.num(f, 0)}%</td>" + "".join(f"<td>{x.num(v / t['div'], 1)}%</td>" for v in row) + "</tr>"
                   for f, row in zip(t["fees"], x.d["table"]))
    return (f'<div class="scrollx"><table class="cmp static ytable"><thead><tr><th scope="col">{e(t["tbl_head"])}</th>'
            f'<th colspan="{len(t["years"])}" scope="colgroup" class="grouphead">{e(t["tbl_group"])}</th></tr>'
            f'<tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table></div>')


def build(lang):
    x = Lang(lang)
    t, d, lt = x.t, x.d["ex"], LOAN[lang]
    url = BASE + t["path"]
    nm = t["names"]
    sc = x.f["scale"]
    base, sh, lo = d["base"], d["shorter"], d["lower"]
    ex_link = f'{lt["path"]}?amount={t["B"]}&amp;rate={t["R"]}&amp;term={t["n"]}&amp;unit=m&amp;method={t["method"]}'
    flat = [v for row in x.d["table"] for v in row]
    i5 = t["years"].index(5)
    y5 = [row[j] for row in x.d["table"] for j in range(i5, len(t["years"]))]
    keep = base["first"] if t["method"] == "annuity" else round(t["B"] * sc / t["n"])
    V = dict(fee=x.money(d["fee"]), keep=x.short(keep), s_saved=x.short(sh["saved"]), l_saved=x.short(lo["saved"]),
             s_yield=x.rate(sh["yield"]), l_yield=x.rate(lo["yield"]), y5_lo=x.num(min(y5) / t["div"], 1), y5_hi=x.rate(max(y5)),
             y1_lo=x.rate(min(row[0] for row in x.d["table"])), ex_link=ex_link,
             cut=x.months(t["n"] - sh["months"]), newpay=x.short(lo["first"]), basepay=x.short(base["first"]),
             drop=x.short(base["first"] - lo["first"]))
    rows = [r.format(fee=x.short(d["fee"])) for r in t["ex_rows"]]
    cols = [(base, None), (sh, sh), (lo, lo)]
    td = lambda v: f"<td>{v}</td>"
    V["EXTABLE"] = f"""<div class="scrollx"><table class="cmp static ex3">
<thead><tr><th></th><th scope="col">{e(nm["base"])}</th><th scope="col">{e(nm["shorter"])}</th><th scope="col">{e(nm["lower"])}</th></tr></thead>
<tbody>
<tr><td>{e(rows[0])}</td>{"".join(td(x.short(c["first"])) for c, _ in cols)}</tr>
<tr><td>{e(rows[1])}</td>{"".join(td(x.months(c["months"])) for c, _ in cols)}</tr>
<tr><td>{e(rows[2])}</td>{td(x.short(base["interest"]))}{td(x.short(base["interest"] - sh["saved"]))}{td(x.short(base["interest"] - lo["saved"]))}</tr>
<tr><td>{e(rows[3])}</td><td>-</td>{td(x.short(sh["saved"]))}{td(x.short(lo["saved"]))}</tr>
{"" if not t["F"] else f'<tr class="on"><td>{e(rows[4])}</td><td>-</td>{td(x.short(sh["net"]))}{td(x.short(lo["net"]))}</tr>'}
</tbody></table></div>"""
    TI = {"base": base["interest"], "shorter": base["interest"] - sh["saved"], "lower": base["interest"] - lo["saved"]}
    mx = max(TI.values())
    cls = {"base": "s-flat", "shorter": "s-equal", "lower": "s-annuity"}
    V["HBARS"] = (f'<div class="hbars" role="img" aria-label="{e(t["ex_rows"][2])}">' + "".join(
        f'<div class="hrow"><span class="hname">{e(nm[k])}</span><span class="htrack"><i class="{cls[k]}" '
        f'style="width:{TI[k] / mx * 100:.1f}%"></i></span><b>{x.money(TI[k])}</b></div>'
        for k in ("base", "lower", "shorter")) + "</div>")
    f = t["fig"]
    legend = "".join(f'<span><i class="sw {cls[k]}"></i>{e(nm[k])}</span>' for k in ("base", "shorter", "lower"))
    V["FIG"] = f"""<figure class="card fig">
  <figcaption><h3>{e(f[0])}</h3><p class="note">{e(f[1])}</p></figcaption>
  <div class="legend">{legend}</div>
  <div class="chartbox">{chart(x)}<div class="tip" hidden></div></div>
</figure>"""
    V["YTABLE"] = ytable(x)
    c, fm = t["calc"], x.f
    num0 = lambda v: x.num(v, 0)
    numr = lambda v: x.num(v, 1).rstrip("0").rstrip(",.")
    unit = e(fm["cur"])
    money_box = lambda i, v: (f'<div class="box">' + (f'<span class="unit pre">{unit}</span>' if fm["pre"] else "")
                              + f'<input id="{i}" inputmode="numeric" value="{num0(v)}">'
                              + ("" if fm["pre"] else f'<span class="unit">{unit}</span>') + "</div>")
    opts = "".join(f'<option value="{k}"' + (" selected" if k == t["method"] else "") + f'>{e(v)}</option>'
                   for k, v in t["methods"].items())
    out_row = lambda i, k: f'<tr><td>{e(c["rows"][i])}</td><td data-out="s-{k}">-</td><td data-out="l-{k}">-</td></tr>'
    V["CALC"] = f"""<section class="card conv prepay" data-prepay data-locale="{fm["intl"]}" data-dec="{fm["dec"]}" data-cur="{unit}" data-pre="{1 if fm["pre"] else 0}" data-scale="{sc}" data-div="{t["div"]}" data-sfx="{e(t["sfx"])}" data-path="{lt["path"]}" data-m1="{e(t["m1"])}" data-mn="{e(t["mn"])}" data-cut="{e(c["cut"])}" data-newpay="{e(c["newpay"])}" data-paidoff="{e(c["paidoff"])}">
  <h3>{e(c["title"])}</h3>
  <div class="convin">
    <div class="field wide"><label for="pp-bal">{e(c["bal"])}</label>{money_box("pp-bal", t["B"])}</div>
    <div class="field"><label for="pp-rate">{e(c["rate"])}</label><div class="box"><input id="pp-rate" inputmode="decimal" value="{numr(t["R"] / t["div"])}"><span class="unit">{e(c["rate_unit"])}</span></div></div>
    <div class="field"><label for="pp-term">{e(c["term"])}</label><div class="box"><input id="pp-term" inputmode="numeric" value="{t["n"]}"><span class="unit">{e(c["term_unit"])}</span></div></div>
    <div class="field wide"><label for="pp-method">{e(c["method"])}</label><div class="box"><select id="pp-method">{opts}</select></div></div>
    <div class="field wide"><label for="pp-extra">{e(c["extra"])}</label>{money_box("pp-extra", t["X"])}</div>
    <div class="field"><label for="pp-fee">{e(c["fee"])}</label><div class="box"><input id="pp-fee" inputmode="decimal" value="{numr(t["F"])}"><span class="unit">{e(c["fee_unit"])}</span></div></div>
  </div>
  <p class="ppfee">{e(c["fee_line"])} <b data-out="fee">-</b></p>
  <div class="scrollx"><table class="cmp static ppout" aria-live="polite">
    <thead><tr><th></th><th scope="col">{e(nm["shorter"])}</th><th scope="col">{e(nm["lower"])}</th></tr></thead>
    <tbody>{out_row(0, "saved")}{out_row(1, "net")}{out_row(2, "what")}{out_row(3, "yield").replace("<tr>", '<tr class="on">', 1)}</tbody>
  </table></div>
  <p class="more"><a id="pp-link" href="{ex_link}">{e(c["more"])}</a></p>
</section>"""
    body = t["body"].format_map(V).strip()
    faq = t["faq"]
    faq_html = "".join(f"<details><summary>{e(q)}</summary><div>{e(a)}</div></details>" for q, a in faq)
    pt, plead, pitems = t["promo"]
    promo_items = "".join(f"<li><b>{e(a)}</b>: {e(b)}</li>" for a, b in pitems)
    play = (f"https://play.google.com/store/apps/details?id=com.namnoit.fincal&amp;referrer=utm_source%3Dnanoko.app"
            f"%26utm_medium%3Dwebsite%26utm_campaign%3D{t['ct']}")
    apple = f"https://apps.apple.com/app/apple-store/id6783214662?pt=128952050&amp;ct={t['ct']}&amp;mt=8"
    stores = (f'<div class="stores">'
              f'<a class="store" href="{play}" target="_blank" rel="noopener">{PLAY_SVG}<span><small>{lt["get_on"]}</small><strong>Google Play</strong></span></a>'
              f'<a class="store" href="{apple}" target="_blank" rel="noopener">{APPLE_SVG}<span><small>{lt["dl_on"]}</small><strong>App Store</strong></span></a></div>')
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{A[k]["path"]}">' for k in ORDER)
    if "en" in A:
        hreflang += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{A["en"]["path"]}">'
    langs = ""
    if len(ORDER) > 1:
        menu = "".join(f'<a href="{A[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "")
                       + f'>{e(LOAN[k]["name"])}</a>' for k in ORDER)
        langs = f'<details class="langs"><summary aria-label="{e(lt["name"])}">{e(lt["name"])}</summary><nav class="langmenu">{menu}</nav></details>'
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": t["h1"], "description": t["desc"], "inLanguage": lang, "url": url,
         "mainEntityOfPage": url, "datePublished": DATE, "dateModified": DATE,
         "image": BASE + "/fincal/ic_launcher-playstore.png",
         "author": {"@type": "Organization", "name": "Nanoko Studio", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "Nanoko Studio", "url": BASE + "/",
                       "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon-512.png"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Nanoko Studio", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Fincal", "item": BASE + "/fincal/"},
            {"@type": "ListItem", "position": 3, "name": lt["crumb_page"], "item": BASE + lt["path"]},
            {"@type": "ListItem", "position": 4, "name": t["crumb"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]}, ensure_ascii=False)
    tile_s = t["tile_shorter"].format(cut=x.months(t["n"] - sh["months"]))
    tile_l = t["tile_lower"].format(drop=x.short(base["first"] - lo["first"]))
    hero_val = "≈ " + x.rate(lo["yield"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{url}">
{hreflang}
<meta property="og:type" content="article">
<meta property="og:site_name" content="Fincal">
<meta property="og:locale" content="{lt["og"]}">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/fincal/ic_launcher-playstore.png">
<meta property="article:published_time" content="{DATE}">
<meta property="article:modified_time" content="{DATE}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f6f6f1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15171a" media="(prefers-color-scheme: dark)">
<meta name="apple-itunes-app" content="app-id=6783214662">
<link rel="icon" type="image/png" href="/fincal/ic_launcher-playstore.png">
<link rel="stylesheet" href="{CSS_HREF}">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="topbar"><div class="wrap">
<a class="brand" href="/fincal/"><img src="/fincal/ic_launcher-playstore.png" alt="" width="32" height="32">Fincal</a>
<span class="spacer"></span>
{nav(lang)}
{langs}
</div></header>

<main class="wrap">
<article class="article post">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Nanoko Studio</a> › <a href="/fincal/">Fincal</a> › <a href="{lt["path"]}">{e(lt["crumb_page"])}</a></nav>
<h1>{e(t["h1"])}</h1>
<p class="byline">{e(t["byline"])}</p>

<section class="card tldr" aria-label="{e(t["summary"])}">
  <p>{t["tldr"]}</p>
  <div class="tiles">
    <div class="tile"><span><i class="sw s-equal"></i>{e(nm["shorter"])}</span><b>{e(x.short(sh["saved"]))}</b><small>{e(tile_s)}</small></div>
    <div class="tile"><span><i class="sw s-annuity"></i>{e(nm["lower"])}</span><b>{e(x.short(lo["saved"]))}</b><small>{e(tile_l)}</small></div>
    <div class="tile hero"><span>{e(t["hero"])}</span><b>{e(hero_val)}</b><small>{e(t["hero_small"])}</small></div>
  </div>
</section>

{body}

<h2>{e(lt["faq_h"])}</h2>
<div class="faq">{faq_html}</div>

<section class="card promo">
  <img src="/fincal/ic_launcher-playstore.png" alt="Fincal" width="56" height="56" loading="lazy">
  <div>
    <h2>{e(pt)}</h2>
    <p class="note" style="margin:0">{e(plead)}</p>
    <ul>{promo_items}</ul>
    {stores}
  </div>
</section>

<p class="calc-links"><a href="{lt["path"]}">{e(COMP[lang]["loan_link"])} →</a><a href="{COMP[lang]["path"]}">{e(COMP[lang]["compound_name"])} →</a></p>
{related(lang, t["path"], "loan")}
</article>
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(lt["footer_privacy"])}</a><a href="/fincal/support/">{e(lt["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
<script src="/fincal/calc/article.js" defer></script>
<script src="/fincal/calc/prepay.js" defer></script>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, A[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(build(lang))
    print(lang, A[lang]["path"])
