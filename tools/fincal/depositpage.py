"""Article: savings interest monthly vs at maturity. Run: python3 -I depositpage.py <site root>
Numbers come from fincal/calc/deposit.js (run through node) so they match the in-page calculator."""
import html
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loanpage import PLAY_SVG, APPLE_SVG, L as LOAN  # noqa: E402  (also regenerates the loan pages)
from complang import C as COMP  # noqa: E402
from depositlang import D as T  # noqa: E402
from articles import CSS_HREF, nav, related  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
DATE = "2026-11-21"
ORDER = [k for k in ["en", "vi", "id", "th", "pt-BR", "ms"] if k in T]
e = lambda s: html.escape(s, quote=True)

JS = r"""
const {deposit}=require(process.argv[1]+"/fincal/calc/deposit.js");
const cfg=JSON.parse(process.argv[2]), res={};
for (const [lang,c] of Object.entries(cfg)) {
  const A=c.A*c.scale;
  res[lang]={main: deposit(A,c.t,c.E,c.M,c.R), idle: deposit(A,c.t,c.E,c.M,c.res[0]),
    res: c.res.map(r=>deposit(A,c.t,c.E,c.M,r)), terms: c.terms.map(t=>deposit(A,t,c.E,c.M,c.R))};
}
console.log(JSON.stringify(res));
"""
cfg = {k: dict(A=T[k]["A"], t=T[k]["t"], E=T[k]["E"], M=T[k]["M"], R=T[k]["R"], res=T[k]["res"], terms=T[k]["terms"],
               scale=T[k]["fmt"]["scale"]) for k in ORDER}
D = json.loads(subprocess.run(["node", "-e", JS, ROOT, json.dumps(cfg)], capture_output=True, text=True, check=True).stdout)

W, H, Lm, Rm, Tp, Bm = 400, 210, 44, 10, 10, 26
pw, ph = W - Lm - Rm, H - Tp - Bm
CLS = ["s-annuity", "s-equal"]


class Lang:
    def __init__(self, lang):
        self.lang, self.t, self.d = lang, T[lang], D[lang]
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

    def rate(self, y, dec=1):
        v = self.num(y, dec)
        return (v[:-2] if v[-2:] in (",0", ".0") else v) + self.t["sfx"]

    def short(self, v):
        v = v / self.f["scale"]
        if self.lang == "id":
            if v >= 1e9:
                return "Rp " + f"{v / 1e9:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " miliar"
            if v >= 1e6:
                return "Rp " + f"{v / 1e6:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " juta"
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




def chart(x):
    t, d = x.t, x.d["main"]
    n, vmax = t["t"], t["tick_max"] * x.f["scale"]
    xm = lambda m: Lm + pw * m / n
    ym = lambda v: Tp + ph - min(v, vmax) / vmax * ph
    s = []
    for v, lbl in zip((0, vmax / 2, vmax), t["ticks"]):
        s.append(f'<line class="grid" x1="{Lm}" x2="{W - Rm}" y1="{ym(v):.1f}" y2="{ym(v):.1f}"/>')
        s.append(f'<text class="tick" x="{Lm - 6}" y="{ym(v) + 4:.1f}" text-anchor="end">{e(lbl)}</text>')
    s.append(f'<line class="axis" x1="{Lm}" x2="{W - Rm}" y1="{Tp + ph}" y2="{Tp + ph}"/>')
    for vals, cls in zip((d["pots"], d["ends"]), CLS):
        pts, prev = [f"{xm(0):.1f},{ym(0):.1f}"], 0
        for m, v in enumerate(vals, 1):
            pts += [f"{xm(m):.1f},{ym(prev):.1f}", f"{xm(m):.1f},{ym(v):.1f}"]
            prev = v
        s.append(f'<path class="ln {cls}" d="M' + " L".join(pts) + '"/>')
    for m in range(0, n + 1, 3 if n > 6 else 1):
        lbl = t["month_tick"].format(m=m) if m else "0"
        anchor = "start" if m == 0 else ("end" if m == n else "middle")
        s.append(f'<text class="tick" x="{xm(m):.1f}" y="{H - 8}" text-anchor="{anchor}">{e(lbl)}</text>')
    for m in range(1, n + 1):
        tip = "|".join([t["month_tip"].format(m=m), t["series"][0], x.money(d["pots"][m - 1]), t["series"][1], x.money(d["ends"][m - 1])])
        s.append(f'<rect class="hit" x="{xm(m - 1):.1f}" y="{Tp}" width="{pw / n:.1f}" height="{ph}" data-tip="{e(tip)}"/>')
    return (f'<svg class="achart" viewBox="0 0 {W} {H}" role="img" aria-label="{e(t["fig"][2])}" data-sw="{" ".join(CLS)}">'
            + "".join(s) + "</svg>")


def table(heads, rows):
    return ('<div class="scrollx"><table class="cmp static ex3"><thead><tr>' + "".join(f'<th scope="col">{e(h)}</th>' for h in heads)
            + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")


def build(lang):
    x = Lang(lang)
    t, d, lt, ct = x.t, x.d, LOAN[lang], COMP[lang]
    url = BASE + t["path"]
    sc = x.f["scale"]
    mn = d["main"]
    V = dict(end=x.short(mn["endI"]), each=x.short(mn["each"]), paid=x.short(mn["paid"]), extra=x.short(mn["extra"]),
             pot=x.short(mn["pot"]), gap=x.short(mn["gap"]), idle=x.short(d["idle"]["gap"]))
    V["RTABLE"] = table(t["rtbl"], [f'<tr{" class=on" if r == t["R"] else ""}><td>{e(t["re_name"][r])}</td><td>{x.short(o["pot"])}</td>'
                                    f'<td>{x.short(o["gap"]) if o["gap"] >= 0 else e(t["rwin"].format(v=x.short(-o["gap"])))}</td></tr>' for r, o in zip(t["res"], d["res"])])
    V["TTABLE"] = table(t["ttbl"], [f'<tr{" class=on" if m == t["t"] else ""}><td>{e(x.months(m))}</td><td>{x.short(o["endI"])}</td>'
                                    f'<td>{x.rate(o["breakeven"], 2)}</td></tr>' for m, o in zip(t["terms"], d["terms"])])
    f = t["fig"]
    legend = "".join(f'<span><i class="sw {c}"></i>{e(nm)}</span>' for nm, c in zip(t["series"], CLS))
    V["FIG"] = f"""<figure class="card fig">
  <figcaption><h3>{e(f[0])}</h3><p class="note">{e(f[1])}</p></figcaption>
  <div class="legend">{legend}</div>
  <div class="chartbox">{chart(x)}<div class="tip" hidden></div></div>
</figure>"""
    c, fm = t["calc"], x.f
    numr = lambda v: x.num(v, 2).rstrip("0").rstrip(",.")
    unit = e(fm["cur"])
    money_box = lambda i, v: (f'<div class="box">' + (f'<span class="unit pre">{unit}</span>' if fm["pre"] else "")
                              + f'<input id="{i}" inputmode="numeric" value="{x.num(v, 0)}">'
                              + ("" if fm["pre"] else f'<span class="unit">{unit}</span>') + "</div>")
    rate_box = lambda i, v: f'<div class="box"><input id="{i}" inputmode="decimal" value="{numr(v)}"><span class="unit">{e(c["rate_unit"])}</span></div>'
    outs = ["end", "each", "pot", "gap", "breakeven"]
    orows = "".join(f'<tr{" class=on" if k == "gap" else ""}><td>{e(c["rows"][i])}</td><td data-out="{k}">-</td></tr>' for i, k in enumerate(outs))
    V["CALC"] = f"""<section class="card conv prepay" data-deposit data-locale="{fm["intl"]}" data-dec="{fm["dec"]}" data-cur="{unit}" data-pre="{1 if fm["pre"] else 0}" data-scale="{sc}" data-sfx="{e(t["sfx"])}" data-endwins="{e(c["endwins"])}" data-monwins="{e(c["monwins"])}" data-same="{e(c["same"])}">
  <h3>{e(c["title"])}</h3>
  <div class="convin">
    <div class="field wide"><label for="dp-amount">{e(c["amount"])}</label>{money_box("dp-amount", t["A"])}</div>
    <div class="field"><label for="dp-term">{e(c["term"])}</label><div class="box"><input id="dp-term" inputmode="numeric" value="{t["t"]}"><span class="unit">{e(c["term_unit"])}</span></div></div>
    <div class="field"><label for="dp-end">{e(c["end"])}</label>{rate_box("dp-end", t["E"])}</div>
    <div class="field"><label for="dp-mon">{e(c["mon"])}</label>{rate_box("dp-mon", t["M"])}</div>
    <div class="field"><label for="dp-re">{e(c["re"])}</label>{rate_box("dp-re", t["R"])}</div>
  </div>
  <div class="scrollx"><table class="cmp static ppout" aria-live="polite"><tbody>{orows}</tbody></table></div>
</section>"""
    body = t["body"].format_map(V).strip()
    faq = t["faq"]
    faq_html = "".join(f"<details><summary>{e(q)}</summary><div>{e(a)}</div></details>" for q, a in faq)
    pt, plead, pitems = t["promo_title"], ct["promo_lead"], ct["promo_items"]
    promo_items = "".join(f"<li><b>{e(a)}</b>: {e(b)}</li>" for a, b in pitems)
    play = (f"https://play.google.com/store/apps/details?id=com.namnoit.fincal&amp;referrer=utm_source%3Dnanoko.app"
            f"%26utm_medium%3Dwebsite%26utm_campaign%3D{t['ct']}")
    apple = f"https://apps.apple.com/app/apple-store/id6783214662?pt=128952050&amp;ct={t['ct']}&amp;mt=8"
    stores = (f'<div class="stores">'
              f'<a class="store" href="{play}" target="_blank" rel="noopener">{PLAY_SVG}<span><small>{lt["get_on"]}</small><strong>Google Play</strong></span></a>'
              f'<a class="store" href="{apple}" target="_blank" rel="noopener">{APPLE_SVG}<span><small>{lt["dl_on"]}</small><strong>App Store</strong></span></a></div>')
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{T[k]["path"]}">' for k in ORDER)
    if "en" in T:
        hreflang += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{T["en"]["path"]}">'
    langs = ""
    if len(ORDER) > 1:
        menu = "".join(f'<a href="{T[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "")
                       + f'>{e(LOAN[k]["name"])}</a>' for k in ORDER)
        langs = f'<details class="langs"><summary aria-label="{e(lt["name"])}">{lt["short"]}</summary><nav class="langmenu">{menu}</nav></details>'
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
            {"@type": "ListItem", "position": 3, "name": ct["crumb_page"], "item": BASE + ct["path"]},
            {"@type": "ListItem", "position": 4, "name": t["crumb"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]}, ensure_ascii=False)
    tiles = (f'<div class="tile"><span>{e(t["calc"]["rows"][0])}</span><b>{e(x.short(mn["endI"]))}</b><small>{e(t["tile_end"])}</small></div>'
             f'<div class="tile"><span>{e(t["calc"]["rows"][2])}</span><b>{e(x.short(mn["pot"]))}</b><small>{e(t["tile_mon"])}</small></div>'
             f'<div class="tile hero"><span>{e(t["hero"])}</span><b>+{e(x.short(mn["gap"]))}</b><small>{e(t["hero_small"].format(idle=V["idle"]))}</small></div>')
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
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Nanoko Studio</a> › <a href="/fincal/">Fincal</a> › <a href="{ct["path"]}">{e(ct["crumb_page"])}</a></nav>
<h1>{e(t["h1"])}</h1>
<p class="byline">{e(t["byline"])}</p>

<section class="card tldr" aria-label="{e(t["summary"])}">
  <p>{t["tldr"]}</p>
  <div class="tiles">{tiles}</div>
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

<p class="calc-links"><a href="{ct["path"]}">{e(ct["compound_name"])} →</a><a href="{lt["path"]}">{e(ct["loan_link"])} →</a></p>
{related(lang, t["path"], "save")}
</article>
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(lt["footer_privacy"])}</a><a href="/fincal/support/">{e(lt["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
<script src="/fincal/calc/article.js" defer></script>
<script src="/fincal/calc/deposit.js" defer></script>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, T[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(build(lang))
    print(lang, T[lang]["path"])
