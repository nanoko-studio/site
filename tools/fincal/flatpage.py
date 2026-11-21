"""Article: flat rate vs reducing balance, 6 languages. Run: python3 -I flatpage.py <site root>
Numbers come from fincal/calc/loan.js (run through node) so they match the calculator."""
import html
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loanpage import PLAY_SVG, APPLE_SVG, L as LOAN  # noqa: E402  (also regenerates the loan pages)
from complang import C as COMP  # noqa: E402
from flatlang import A  # noqa: E402
from articles import CSS_HREF, nav, related  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
DATE = "2026-11-20"
ORDER = ["en", "vi", "id", "th", "pt-BR", "ms"]
e = lambda s: html.escape(s, quote=True)

JS = r"""
const {calculate}=require(process.argv[1]+"/fincal/calc/loan.js");
const cfg=JSON.parse(process.argv[2]), res={};
for (const [lang,c] of Object.entries(cfg)) {
  const o={};
  for (const k of ["flat","equal","annuity"]) o[k]=calculate(c.P,c.rate,12,k);
  o.table=c.rates.map(r=>c.terms.map(m=>calculate(c.P,r,m,"flat").apr));
  o.small=calculate(c.P,c.small_rate,12,"flat").apr;
  res[lang]=o;
}
console.log(JSON.stringify(res));
"""
cfg = {k: {f: A[k][f] for f in ("P", "rate", "rates", "terms", "small_rate")} for k in ORDER}
D = json.loads(subprocess.run(["node", "-e", JS, ROOT, json.dumps(cfg)], capture_output=True, text=True, check=True).stdout)

W, H, Lm, Rm, T, B = 400, 210, 44, 6, 10, 26
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

    def money(self, v):
        n = self.num(round(v, self.f["dec"]), self.f["dec"])
        return f'{self.f["cur"]} {n}' if self.f["pre"] else (f'{n} {self.f["cur"]}' if self.f["cur"] else n)

    def pct(self, apr):  # apr is a nominal yearly %, shown per year or per month (pt-BR)
        return self.num(apr / self.t["div"], 1) + "%"

    def rate_txt(self, apr):
        return self.num(apr / self.t["div"], 1) + self.t["sfx"]

    def short(self, v):
        if self.lang != "vi":
            return self.money(v)
        if v >= 1e6:
            return f"{v / 1e6:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " triệu"
        return f"{v / 1e3:.0f} nghìn"


def ychart(v, vmax):
    return T + ph - v / vmax * ph


def bar(x, w, v, vmax, cls):
    y = ychart(v, vmax)
    r = min(4, w / 2, T + ph - y)
    d = (f"M{x:.1f},{T + ph:.1f}V{y + r:.1f}Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f}"
         f"H{x + w - r:.1f}Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f}V{T + ph:.1f}Z")
    return f'<path class="{cls}" d="{d}"/>'


def axes(vmax, labels):
    s = []
    for v, lbl in zip((0, vmax / 2, vmax), labels):
        y = ychart(v, vmax)
        s.append(f'<line class="grid" x1="{Lm}" x2="{W - Rm}" y1="{y:.1f}" y2="{y:.1f}"/>')
        s.append(f'<text class="tick" x="{Lm - 6}" y="{y + 4:.1f}" text-anchor="end">{e(lbl)}</text>')
    s.append(f'<line class="axis" x1="{Lm}" x2="{W - Rm}" y1="{T + ph}" y2="{T + ph}"/>')
    return s


def months_axis(t, gw):
    s = []
    for m in (1, 3, 6, 9, 12):
        cx = Lm + gw * (m - 0.5)
        lbl = (t["month_tick"] if m == 1 else t["month_tick_rest"]).format(m=m)
        s.append(f'<text class="tick" x="{cx:.1f}" y="{H - 8}" text-anchor="middle">{e(lbl)}</text>')
    return s


def svg(parts, label, sw):
    return (f'<svg class="achart" viewBox="0 0 {W} {H}" role="img" aria-label="{e(label)}" data-sw="{sw}">'
            + "".join(parts) + "</svg>")


def chart_interest(x):
    t, fp, ep = x.t, x.d["flat"]["periods"], x.d["equal"]["periods"]
    vmax = fp[0]["i"]
    gw = pw / 12
    bw = (gw - 2 - 6) / 2
    s, hits = axes(vmax, t["ticks1"]), []
    for m in range(12):
        fi, ei = fp[m]["i"], ep[m]["i"]
        x0 = Lm + gw * m + 3
        s.append(bar(x0, bw, fi, vmax, "s-flat"))
        s.append(bar(x0 + bw + 2, bw, ei, vmax, "s-equal"))
        tip = f'{t["month_tip"].format(m=m + 1)}|{t["names"]["flat"]}|{x.money(fi)}|{t["names"]["equal"]}|{x.money(ei)}'
        hits.append(f'<rect class="hit" x="{Lm + gw * m:.1f}" y="{T}" width="{gw:.1f}" height="{ph}" data-tip="{e(tip)}"/>')
    return s + months_axis(t, gw) + hits


def chart_base(x):
    t, ep, P = x.t, x.d["equal"]["periods"], x.t["P"]
    gw = pw / 12
    s, hits = axes(P, t["ticks2"]), []
    for m in range(12):
        bal = ep[m]["end"] + ep[m]["p"]
        s.append(bar(Lm + gw * m + 2, gw - 4, bal, P, "s-equal"))
        tip = f'{t["month_tip"].format(m=m + 1)}|{t["tip_bal"]}|{x.money(bal)}|{t["tip_base"]}|{x.money(P)}'
        hits.append(f'<rect class="hit" x="{Lm + gw * m:.1f}" y="{T}" width="{gw:.1f}" height="{ph}" data-tip="{e(tip)}"/>')
    y = ychart(P, P)
    s.append(f'<line class="flatline" x1="{Lm}" x2="{W - Rm}" y1="{y:.1f}" y2="{y:.1f}"/>')
    return s + months_axis(t, gw) + hits


def hbars(x, TI):
    n = x.t["names"]
    mx = max(TI.values())
    out = [f'<div class="hrow"><span class="hname">{e(n[k])}</span>'
           f'<span class="htrack"><i class="s-{k}" style="width:{TI[k] / mx * 100:.1f}%"></i></span>'
           f'<b>{x.money(TI[k])}</b></div>' for k in ("flat", "annuity", "equal")]
    return f'<div class="hbars" role="img" aria-label="{e(x.t["hbars_aria"])}">' + "".join(out) + "</div>"


def apr_table(x):
    t = x.t
    head = "".join(f"<th scope='col'>{m}</th>" for m in t["terms"])
    body = ""
    for r, row in zip(t["rates"], x.d["table"]):
        label = t["row"].format(m=x.num(r / 12, 1).rstrip("0").rstrip(",."), y=x.num(r, 1).rstrip("0").rstrip(",."))
        body += f"<tr><td>{label}</td>" + "".join(f"<td>{x.pct(v)}</td>" for v in row) + "</tr>"
    return (f'<div class="scrollx"><table class="cmp static"><thead><tr><th scope="col">{e(t["names"]["flat"])}</th>'
            f'<th colspan="{len(t["terms"])}" scope="colgroup" class="grouphead">{e(t["tbl_group"])}</th></tr>'
            f'<tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table></div>')


def ratio_range(x):
    rs = [v / r for r, row in zip(x.t["rates"], x.d["table"]) for v in row]
    lo, hi = min(rs), max(rs)
    return x.num(round(lo, 1), 1), x.num(round(hi, 1), 1)


def build(lang):
    x = Lang(lang)
    t, d, lt = x.t, x.d, LOAN[lang]
    url = BASE + t["path"]
    fp, ep, ap = d["flat"]["periods"], d["equal"]["periods"], d["annuity"]["periods"]
    TI = {k: d[k]["totalInterest"] for k in ("flat", "equal", "annuity")}
    n = t["names"]
    loan_rate = t["rate"]
    ex_link = f'{lt["path"]}?amount={t["P"]}&amp;rate={loan_rate}&amp;term=12&amp;unit=m&amp;method=flat'
    lo, hi = ratio_range(x)
    V = dict(P=x.money(t["P"]), flat_i=x.money(fp[0]["i"]), last_bal=x.money(ep[11]["p"] + ep[11]["end"]),
             last_bal_s=x.short(ep[11]["p"] + ep[11]["end"]), flat_i12_s=x.short(fp[11]["i"]),
             eq_i12_s=x.short(ep[11]["i"]), ex_link=ex_link, lo=lo, hi=hi)
    f1, f2, ct = t["fig1"], t["fig2"], t["conv_t"]
    legend2 = (f'<div class="legend"><span><i class="sw s-flat"></i>{e(n["flat"])}</span>'
               f'<span><i class="sw s-equal"></i>{e(n["equal"])}</span></div>')
    V["FIG1"] = f"""<figure class="card fig">
  <figcaption><h3>{e(f1[0])}</h3><p class="note">{e(f1[1])}</p></figcaption>
  {legend2}
  <div class="chartbox">{svg(chart_interest(x), f1[3], "s-flat s-equal")}<div class="tip" hidden></div></div>
  <p class="fignote">{f1[2].format_map(V)}</p>
</figure>"""
    V["FIG2"] = f"""<figure class="card fig">
  <figcaption><h3>{e(f2[0])}</h3><p class="note">{e(f2[1])}</p></figcaption>
  <div class="legend"><span><i class="sw s-equal"></i>{e(f2[2])}</span><span><i class="sw dash"></i>{e(f2[3])}</span></div>
  <div class="chartbox">{svg(chart_base(x), f2[4], "s-equal dash")}<div class="tip" hidden></div></div>
</figure>"""
    rows = t["ex_rows"]
    V["EXTABLE"] = f"""<div class="scrollx"><table class="cmp static">
<thead><tr><th></th><th scope="col">{e(n["flat"])}</th><th scope="col">{e(n["equal"])}</th><th scope="col">{e(n["annuity"])}</th></tr></thead>
<tbody>
<tr><td>{e(rows[0])}</td><td>{x.money(fp[0]["pay"])}</td><td>{x.money(ep[0]["pay"])}</td><td>{x.money(ap[0]["pay"])}</td></tr>
<tr><td>{e(rows[1])}</td><td>{x.money(fp[11]["pay"])}</td><td>{x.money(ep[11]["pay"])}</td><td>{x.money(ap[11]["pay"])}</td></tr>
<tr class="on"><td>{e(rows[2])}</td><td>{x.money(TI["flat"])}</td><td>{x.money(TI["equal"])}</td><td>{x.money(TI["annuity"])}</td></tr>
</tbody></table></div>"""
    V["HBARS"] = hbars(x, TI)
    V["APRTABLE"] = apr_table(x)
    cr, cn = t["conv"]
    f = x.f
    V["CONV"] = f"""<section class="card conv" data-flat-conv data-p="{t["P"]}" data-locale="{f["intl"]}" data-dec="{f["dec"]}" data-cur="{e(f["cur"])}" data-pre="{1 if f["pre"] else 0}" data-unit="{t["unit"]}" data-div="{t["div"]}" data-sfx="{e(t["sfx"])}" data-path="{lt["path"]}">
  <h3>{e(ct["title"])}</h3>
  <div class="convin">
    <div class="field"><label for="cv-rate">{e(ct["rate"])}</label><div class="box"><input id="cv-rate" inputmode="decimal" value="{x.num(cr, 1).rstrip("0").rstrip(",.")}"><span class="unit">{e(ct["rate_unit"])}</span></div></div>
    <div class="field"><label for="cv-term">{e(ct["term"])}</label><div class="box"><input id="cv-term" inputmode="numeric" value="{cn}"><span class="unit">{e(ct["term_unit"])}</span></div></div>
  </div>
  <div class="convout" aria-live="polite">
    <div><span>{e(ct["apr"])}</span><b id="cv-apr">-</b></div>
    <div><span>{e(ct["flat"])}</span><b id="cv-flat">-</b></div>
    <div><span>{e(ct["equal"])}</span><b id="cv-equal">-</b></div>
  </div>
  <p class="more"><a id="cv-link" href="{ex_link}">{e(ct["more"])}</a></p>
</section>"""
    body = t["body"].format_map(V).strip()
    faq = [(q, a.format(small=x.rate_txt(d["small"]))) for q, a in t["faq"]]
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
    langmenu = "".join(f'<a href="{A[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "")
                       + f'>{e(LOAN[k]["name"])}</a>' for k in ORDER)
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
    hero_val = "≈ " + x.rate_txt(d["flat"]["apr"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{url}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{BASE}{A["en"]["path"]}">
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
<details class="langs"><summary aria-label="{e(lt["name"])}">{e(lt["name"])}</summary><nav class="langmenu">{langmenu}</nav></details>
</div></header>

<main class="wrap">
<article class="article post">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Nanoko Studio</a> › <a href="/fincal/">Fincal</a> › <a href="{lt["path"]}">{e(lt["crumb_page"])}</a></nav>
<h1>{e(t["h1"])}</h1>
<p class="byline">{e(t["byline"])}</p>

<section class="card tldr" aria-label="{e(t["summary"])}">
  <p>{t["tldr"]}</p>
  <div class="tiles">
    <div class="tile"><span><i class="sw s-flat"></i>{e(n["flat"])}</span><b>{x.money(TI["flat"])}</b><small>{e(t["tile_small"])}</small></div>
    <div class="tile"><span><i class="sw s-equal"></i>{e(n["equal"])}</span><b>{x.money(TI["equal"])}</b><small>{e(t["tile_small"])}</small></div>
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
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, A[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(build(lang))
    x = Lang(lang)
    print(lang, A[lang]["path"], x.rate_txt(D[lang]["flat"]["apr"]), ratio_range(x), x.rate_txt(D[lang]["small"]))
