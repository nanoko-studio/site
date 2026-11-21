"""Article: promo rate then floating rate. Run: python3 -I teaserpage.py <site root>
Numbers come from fincal/calc/teaser.js (run through node) so they match the in-page calculator."""
import html
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loanpage import PLAY_SVG, APPLE_SVG, L as LOAN  # noqa: E402  (also regenerates the loan pages)
from complang import C as COMP  # noqa: E402
from teaserlang import T  # noqa: E402
from articles import CSS_HREF, nav, related  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
DATE = "2026-11-21"
ORDER = [k for k in ["en", "vi", "id", "th", "pt-BR", "ms"] if k in T]
e = lambda s: html.escape(s, quote=True)

JS = r"""
const {schedule}=require(process.argv[1]+"/fincal/calc/teaser.js");
const cfg=JSON.parse(process.argv[2]), res={};
for (const [lang,c] of Object.entries(cfg)) {
  const s=c.scale, B=c.B*s, run=(p,k,f)=>schedule(B,c.n,c.method,p,k,f);
  res[lang]={main: run(c.P,c.k,c.F), noPromo: run(c.F,c.k,c.F).interest,
    floats: c.floats.map(f=>{const r=run(c.P,c.k,f); return {after:r.after, jump:r.jump, interest:r.interest};}),
    chart: c.chart_floats.map(f=>run(c.P,c.k,f).pays),
    pkgs: c.packages.map(([p,k])=>c.pkg_floats.map(f=>run(p,k,f).interest))};
}
console.log(JSON.stringify(res));
"""
cfg = {k: dict(B=T[k]["B"], n=T[k]["n"], method=T[k]["method"], P=T[k]["P"], k=T[k]["k"], F=T[k]["F"],
               floats=T[k]["floats"], chart_floats=T[k]["chart_floats"], packages=T[k]["packages"],
               pkg_floats=T[k]["pkg_floats"], scale=T[k]["fmt"]["scale"]) for k in ORDER}
D = json.loads(subprocess.run(["node", "-e", JS, ROOT, json.dumps(cfg)], capture_output=True, text=True, check=True).stdout)

W, H, Lm, Rm, Tp, Bm = 400, 210, 44, 10, 10, 26
pw, ph = W - Lm - Rm, H - Tp - Bm
CLS = ["s-annuity", "s-equal", "s-flat"]


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

    def rate(self, y):
        v = self.num(y / self.t["div"], 1)
        return (v[:-2] if v[-2:] in (",0", ".0") else v) + self.t["sfx"]

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



def chart(x):
    t = x.t
    n, vmax = t["n"], t["tick_max"] * x.f["scale"]
    years = n // 12
    xm = lambda m: Lm + pw * m / n
    ym = lambda v: Tp + ph - min(v, vmax) / vmax * ph
    s = []
    for v, lbl in zip((0, vmax / 2, vmax), t["ticks"]):
        s.append(f'<line class="grid" x1="{Lm}" x2="{W - Rm}" y1="{ym(v):.1f}" y2="{ym(v):.1f}"/>')
        s.append(f'<text class="tick" x="{Lm - 6}" y="{ym(v) + 4:.1f}" text-anchor="end">{e(lbl)}</text>')
    s.append(f'<line class="axis" x1="{Lm}" x2="{W - Rm}" y1="{Tp + ph}" y2="{Tp + ph}"/>')
    for pays, cls in zip(x.d["chart"], CLS):
        path = "M" + " L".join(f"{xm(m):.1f},{ym(v):.1f} {xm(m + 1):.1f},{ym(v):.1f}" for m, v in enumerate(pays))
        s.append(f'<path class="ln {cls}" d="{path}"/>')
    step = 5 if years > 8 else 1
    for yr in range(0, years + 1, step):
        lbl = t["year0"] if yr == 0 else t["year_tick"].format(y=yr)
        anchor = "start" if yr == 0 else ("end" if yr == years else "middle")
        s.append(f'<text class="tick" x="{xm(yr * 12):.1f}" y="{H - 8}" text-anchor="{anchor}">{e(lbl)}</text>')
    marks = sorted(set(list(range(0, n, 12)) + [t["k"] - 1]))
    names = [t["series"].format(r=x.rate(f)) for f in t["chart_floats"]]
    for i, m in enumerate(marks):
        tip = "|".join([t["month_tip"].format(m=m + 1)] + [p for nm, pays in zip(names, x.d["chart"]) for p in (nm, x.money(pays[m]))])
        x0 = xm(m) if i == 0 else (xm(marks[i - 1]) + xm(m)) / 2
        x1 = xm(n) if i == len(marks) - 1 else (xm(m) + xm(marks[i + 1])) / 2
        s.append(f'<rect class="hit" x="{x0:.1f}" y="{Tp}" width="{x1 - x0:.1f}" height="{ph}" data-tip="{e(tip)}"/>')
    return (f'<svg class="achart" viewBox="0 0 {W} {H}" role="img" aria-label="{e(t["fig"][2])}" data-sw="{" ".join(CLS)}">'
            + "".join(s) + "</svg>")


def build(lang):
    x = Lang(lang)
    t, d, lt = x.t, x.d, LOAN[lang]
    url = BASE + t["path"]
    sc = x.f["scale"]
    mn = d["main"]
    pct = lambda a, b: x.num(a / b * 100, 1) + "%"
    fi = t["floats"].index(t["F"])
    jumps = [r["after"] for r in d["floats"]]
    tots = [r["interest"] for r in d["floats"]]
    pk = d["pkgs"]
    pfi = t["pkg_floats"].index(t["F"])
    V = dict(prin=x.short(round(t["B"] * sc / t["n"])), first=x.short(mn["first"]), before=x.short(mn["before"]),
             after=x.short(mn["after"]), jump=x.short(mn["jump"]), pct=pct(mn["jump"], mn["before"]),
             step1=x.short((jumps[-1] - jumps[0]) / (len(jumps) - 1)), step_total=x.short((tots[-1] - tots[0]) / (len(tots) - 1)),
             no_promo=x.short(d["noPromo"]), promo_saving=x.short(d["noPromo"] - mn["interest"]),
             pkg_gap=x.short(pk[0][pfi] - pk[-1][pfi]))
    ft = t["ftbl"]
    rows = "".join(f'<tr{" class=on" if f == t["F"] else ""}><td>{x.rate(f)}</td><td>{x.short(r["after"])}</td>'
                   f'<td>+{x.short(r["jump"])}</td><td>{x.short(r["interest"])}</td></tr>' for f, r in zip(t["floats"], d["floats"]))
    V["FTABLE"] = (f'<div class="scrollx"><table class="cmp static ex3"><thead><tr>' + "".join(f'<th scope="col">{e(h)}</th>' for h in ft)
                   + f'</tr></thead><tbody>{rows}</tbody></table></div>')
    pt_ = t["ptbl"]
    best = [min(range(len(pk)), key=lambda i: pk[i][j]) for j in range(len(t["pkg_floats"]))]
    prow = "".join(f'<tr><td>{e(t["pkg_name"].format(p=x.num(p, 1).rstrip("0").rstrip(",."), k=k))}</td>'
                   + "".join(f'<td>{"<b>" if best[j] == i else ""}{x.short(v)}{"</b>" if best[j] == i else ""}</td>' for j, v in enumerate(pk[i])) + "</tr>"
                   for i, (p, k) in enumerate(t["packages"]))
    V["PTABLE"] = (f'<div class="scrollx"><table class="cmp static ex3 pkg"><thead><tr><th scope="col">{e(pt_[0])}</th>'
                   f'<th colspan="{len(t["pkg_floats"])}" scope="colgroup" class="grouphead">{e(pt_[1])}</th></tr><tr><th></th>'
                   + "".join(f'<th scope="col">{e(pt_[2].format(r=x.num(f, 1).rstrip("0").rstrip(",.")))}</th>' for f in t["pkg_floats"])
                   + f'</tr></thead><tbody>{prow}</tbody></table></div>')
    f = t["fig"]
    legend = "".join(f'<span><i class="sw {c}"></i>{e(t["series"].format(r=x.rate(r)))}</span>' for r, c in zip(t["chart_floats"], CLS))
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
    opts = "".join(f'<option value="{k}"' + (" selected" if k == t["method"] else "") + f'>{e(v)}</option>' for k, v in t["methods"].items())
    rate_box = lambda i, v: f'<div class="box"><input id="{i}" inputmode="decimal" value="{numr(v / t["div"])}"><span class="unit">{e(c["rate_unit"])}</span></div>'
    mon_box = lambda i, v: f'<div class="box"><input id="{i}" inputmode="numeric" value="{v}"><span class="unit">{e(c["term_unit"])}</span></div>'
    outs = ["before", "after", "jump", "interest", "total"]
    orows = "".join(f'<tr{" class=on" if k == "jump" else ""}><td>{e(c["rows"][i])}</td><td data-out="{k}">-</td></tr>' for i, k in enumerate(outs))
    V["CALC"] = f"""<section class="card conv prepay" data-teaser data-locale="{fm["intl"]}" data-dec="{fm["dec"]}" data-cur="{unit}" data-pre="{1 if fm["pre"] else 0}" data-scale="{sc}" data-div="{t["div"]}">
  <h3>{e(c["title"])}</h3>
  <div class="convin">
    <div class="field wide"><label for="tz-amount">{e(c["amount"])}</label>{money_box("tz-amount", t["B"])}</div>
    <div class="field"><label for="tz-term">{e(c["term"])}</label>{mon_box("tz-term", t["n"])}</div>
    <div class="field wide"><label for="tz-method">{e(c["method"])}</label><div class="box"><select id="tz-method">{opts}</select></div></div>
    <div class="field"><label for="tz-promo">{e(c["promo"])}</label>{rate_box("tz-promo", t["P"])}</div>
    <div class="field"><label for="tz-months">{e(c["promo_months"])}</label>{mon_box("tz-months", t["k"])}</div>
    <div class="field"><label for="tz-float">{e(c["floating"])}</label>{rate_box("tz-float", t["F"])}</div>
  </div>
  <div class="scrollx"><table class="cmp static ppout" aria-live="polite"><tbody>{orows}</tbody></table></div>
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
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{T[k]["path"]}">' for k in ORDER)
    if "en" in T:
        hreflang += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{T["en"]["path"]}">'
    langs = ""
    if len(ORDER) > 1:
        menu = "".join(f'<a href="{T[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "")
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
    k = t["k"]
    tiles = (f'<div class="tile"><span>{e(t["month_tip"].format(m=k))}</span><b>{e(x.short(mn["before"]))}</b><small>{e(t["tile_before"])}</small></div>'
             f'<div class="tile"><span>{e(t["month_tip"].format(m=k + 1))}</span><b>{e(x.short(mn["after"]))}</b><small>{e(t["tile_after"])}</small></div>'
             f'<div class="tile hero"><span>{e(t["hero"])}</span><b>+{e(x.short(mn["jump"]))}</b><small>{e(t["hero_small"].format(pct=V["pct"]))}</small></div>')
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

<p class="calc-links"><a href="{lt["path"]}">{e(COMP[lang]["loan_link"])} →</a><a href="{COMP[lang]["path"]}">{e(COMP[lang]["compound_name"])} →</a></p>
{related(lang, t["path"], "loan")}
</article>
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(lt["footer_privacy"])}</a><a href="/fincal/support/">{e(lt["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
<script src="/fincal/calc/article.js" defer></script>
<script src="/fincal/calc/teaser.js" defer></script>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, T[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(build(lang))
    print(lang, T[lang]["path"])
