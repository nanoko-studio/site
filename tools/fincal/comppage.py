"""Generate the Fincal compound interest calculator pages (6 languages). Run: python3 -I comppage.py <site root>"""
import html
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from complang import C
from loanlang import LANGS
from compsav import SAV
from articles import CSS_HREF, nav, related  # noqa: E402

for _k, _s in SAV.items():
    for _f in ("title", "desc"):
        if _f in _s:
            C[_k][_f] = _s[_f]
    if "faq" in _s:
        C[_k]["faq"].insert(1, _s["faq"])

ROOT = sys.argv[1]
BASE = "https://nanoko.app"
ORDER = ["en", "vi", "id", "th", "pt-BR", "ms"]
LOAN_PATH = {"en": "/fincal/loan-calculator/", "vi": "/fincal/tinh-lai-vay/", **{k: v["path"] for k, v in LANGS.items()}}
e = lambda s: html.escape(s, quote=True)

# Shared per-language bits (same as the loan pages).
COMMON = {
    "en": dict(name="English", short="EN", faq_h="Frequently asked questions", currency="", cur_pre=False, sep=",", comma=False,
               get_on="GET IT ON", dl_on="DOWNLOAD ON THE", footer_privacy="Privacy Policy", footer_support="Support"),
    "vi": dict(name="Tiếng Việt", short="VI", faq_h="Câu hỏi thường gặp", currency="đ", cur_pre=False, sep=".", comma=True,
               get_on="TẢI TRÊN", dl_on="TẢI TRÊN", footer_privacy="Quyền riêng tư", footer_support="Hỗ trợ"),
}
for k, v in LANGS.items():
    COMMON[k] = {f: v[f] for f in ("name", "short", "faq_h", "currency", "cur_pre", "sep", "comma", "get_on", "dl_on", "footer_privacy", "footer_support")}
SCALE = {"vi": 1, "id": 1}

PLAY_SVG = ('<svg viewBox="0 0 512 512" aria-hidden="true"><path fill="#00d3ff" d="M47 24.7C40.2 30.1 36 39.3 36 51.6v408.8c0 12.3 4.2 21.5 11 26.9l1.6 1.4L277 259.7v-7.4L48.6 23.3 47 24.7z"/>'
            '<path fill="#ffce00" d="M353 336.1l-76-76.4v-7.4l76.1-76.4 1.7 1L445 232.4c25.7 14.6 25.7 38.6 0 53.2L354.7 335l-1.7 1.1z"/>'
            '<path fill="#ff3a44" d="M354.7 335L277 256 47 487.7c8.5 9 22.5 10.1 38.3 1.1L354.7 335z"/>'
            '<path fill="#00f076" d="M354.7 177L85.3 23.2C69.5 14.2 55.5 15.3 47 24.3L277 256l77.7-79z"/></svg>')
APPLE_SVG = ('<svg viewBox="0 0 384 512" aria-hidden="true"><path fill="#fff" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"/></svg>')


# ---------- Engine (port of compound.js, used to fill the article numbers) ----------
def calculate(initial, contribution, cf, kf, timing, rate, years):
    FM = {"m": 1, "q": 3, "y": 12}
    km, cm = FM[kf], FM[cf]
    pr = rate / 100 / (12 / km)
    bal, tc, ti, ps, w = initial, 0, 0, initial, 0.0
    for month in range(1, years * 12 + 1):
        pe = ((month - 1) // km + 1) * km
        if timing == "begin":
            con, pres = (month - 1) % cm == 0, pe - (month - 1)
        else:
            con, pres = month % cm == 0, pe - month
        if con and contribution:
            bal += contribution; tc += contribution; w += contribution * pres / km
        if month % km == 0:
            i = math.floor((ps + w) * pr + 0.5)
            bal += i; ti += i; ps = bal; w = 0.0
    return dict(fv=bal, tc=tc, ti=ti)


def money(lang, units):
    c, s = COMMON[lang], SCALE.get(lang, 100)
    v = units / s
    txt = f"{v:,.0f}" if s == 1 else f"{v:,.2f}"
    if c["sep"] == ".":
        txt = txt.replace(",", "\0").replace(".", ",").replace("\0", ".")
    if lang == "en":
        return txt
    return f"{c['currency']} {txt}" if c["cur_pre"] else f"{txt} {c['currency']}"


def numbers(lang):
    d, s = C[lang]["default"], SCALE.get(lang, 100)
    P, A = d["initial"] * s, d["contrib"] * s
    r = calculate(P, A, d["every"], "m", "end", d["rate"], d["years"])
    early = calculate(P, A, d["every"], "m", "end", d["rate"], d["years"] + 10)
    out = dict(fv=money(lang, r["fv"]), put=money(lang, P + r["tc"]), int=money(lang, r["ti"]),
               early=money(lang, early["fv"]), early_put=money(lang, P + early["tc"]))
    for k in "mqy":
        out["kf_" + k] = money(lang, calculate(P, A, d["every"], k, "end", d["rate"], d["years"])["fv"])
    return out


def savings(lang):
    s, sc = SAV[lang], SCALE.get(lang, 100)
    P = s["initial"] * sc
    r = calculate(P, 0, "m", s["kf"], "end", s["rate"], s["years"])
    simple = round(P * s["rate"] / 100 * s["years"])
    link = (f'{C[lang]["path"]}?initial={s["initial"]}&amp;contrib=0&amp;rate={s["rate"]}'
            f'&amp;years={s["years"]}&amp;compound={s["kf"]}')
    return s["html"].strip().format(sv_fv=money(lang, r["fv"]), sv_int=money(lang, r["ti"]),
                                    sv_simple=money(lang, simple), sv_link=link)


def stores(t, c):
    play = (f"https://play.google.com/store/apps/details?id=com.namnoit.fincal&amp;referrer=utm_source%3Dnanoko.app"
            f"%26utm_medium%3Dwebsite%26utm_campaign%3D{t['ct']}")
    apple = f"https://apps.apple.com/app/apple-store/id6783214662?pt=128952050&amp;ct={t['ct']}&amp;mt=8"
    return (f'<div class="stores">'
            f'<a class="store" href="{play}" target="_blank" rel="noopener">{PLAY_SVG}<span><small>{c["get_on"]}</small><strong>Google Play</strong></span></a>'
            f'<a class="store" href="{apple}" target="_blank" rel="noopener">{APPLE_SVG}<span><small>{c["dl_on"]}</small><strong>App Store</strong></span></a>'
            f'</div>')


def jsonld(lang, t):
    url = BASE + t["path"]
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": t["h1"] + " - Fincal", "url": url, "inLanguage": lang,
         "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "description": t["desc"],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": "Nanoko Studio", "url": BASE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Nanoko Studio", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Fincal", "item": BASE + "/fincal/"},
            {"@type": "ListItem", "position": 3, "name": t["crumb_page"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
    ]}, ensure_ascii=False)


def page(lang):
    t, c = C[lang], COMMON[lang]
    d = t["default"]
    fmt = lambda v: f"{v:,}".replace(",", c["sep"])
    rate_val = str(d["rate"]).replace(".", ",") if c["comma"] else str(d["rate"])
    chips = "".join(f'<button type="button" data-amount="{v}">{e(lbl)}</button>' for v, lbl in t["chips"])
    pre = f'<span class="unit pre">{c["currency"]}</span>' if c["cur_pre"] else ""
    suf = f'<span class="unit">{c["currency"]}</span>' if c["currency"] and not c["cur_pre"] else ""
    every = "".join(f'<option value="{k}"{" selected" if k == d["every"] else ""}>{e(t["every"][k])}</option>' for k in "mqy")
    kfreq = "".join(f'<option value="{k}"{" selected" if k == "m" else ""}>{e(t["freq"][k])}</option>' for k in "mqy")
    timings = "".join(f'<label><input type="radio" name="timing" value="{k}"{" checked" if k == "end" else ""}><span><b>{e(t["timings"][k])}</b></span></label>' for k in ("end", "begin"))
    cmp_rows = "".join(f'<tr id="cmprow-{k}" data-pick="{k}"><td>{e(t["freq"][k])}</td><td id="cmp-{k}">-</td><td id="cmp-{k}-i">-</td></tr>' for k in "mqy")
    cols = "".join(f"<th scope='col'>{e(x)}</th>" for x in t["sched_cols"])
    faq = "".join(f"<details><summary>{e(q)}</summary><div>{e(a)}</div></details>" for q, a in t["faq"])
    promo = "".join(f"<li><b>{e(a)}</b>: {e(b)}</li>" for a, b in t["promo_items"])
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{C[k]["path"]}">' for k in ORDER)
    langmenu = "".join(
        f'<a href="{C[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "") + f'>{e(COMMON[k]["name"])}</a>'
        for k in ORDER)
    url = BASE + t["path"]
    article = t["article"].strip().format(**numbers(lang))
    # Savings example goes before the rule-of-72 section.
    sv = savings(lang)
    cut = article.rfind("<h2>", 0, article.find("72"))
    article = article[:cut] + sv + "\n" + article[cut:]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{url}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{BASE}{C["en"]["path"]}">
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
<details class="langs"><summary aria-label="{e(c["name"])}">{c["short"]}</summary><nav class="langmenu">{langmenu}</nav></details>
</div></header>

<main class="wrap">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Nanoko Studio</a> › <a href="/fincal/">Fincal</a> › <span>{e(t["crumb_page"])}</span></nav>
<h1>{e(t["h1"])}</h1>
<p class="intro">{e(t["intro"])}</p>

<div class="calc" data-compound-calc>
<form class="card inputs" onsubmit="return false" autocomplete="off">
  <div class="field">
    <label for="initial">{e(t["initial"])}</label>
    <div class="box">{pre}<input id="initial" inputmode="numeric" value="{fmt(d["initial"])}" aria-describedby="initial-words">{suf}</div>
    <p class="hint" id="initial-words" aria-live="polite"></p>
    <div class="chips">{chips}</div>
  </div>
  <div class="field">
    <label for="contrib">{e(t["contrib"])}</label>
    <div class="box pair">{pre}<input id="contrib" inputmode="numeric" value="{fmt(d["contrib"])}" aria-describedby="contrib-words">{suf}
      <select id="cfreq" aria-label="{e(t["contrib"])}">{every}</select></div>
    <p class="hint" id="contrib-words" aria-live="polite"></p>
  </div>
  <div class="field">
    <label for="rate">{e(t["rate"])}</label>
    <div class="box"><input id="rate" inputmode="decimal" value="{rate_val}"><span class="unit">{e(t["rate_unit"])}</span></div>
    <input id="rate-range" type="range" min="0" max="20" step="0.1" value="{d["rate"]}" aria-label="{e(t["rate"])}">
  </div>
  <div class="field">
    <label for="years">{e(t["years"])}</label>
    <div class="box"><input id="years" inputmode="numeric" value="{d["years"]}"><span class="unit">{e(t["years_unit"])}</span></div>
    <input id="years-range" type="range" min="1" max="50" step="1" value="{d["years"]}" aria-label="{e(t["years"])}">
  </div>
  <details class="field adv" id="adv">
    <summary>{e(t["adv"])}</summary>
    <div class="field">
      <label for="kfreq">{e(t["kfreq"])}</label>
      <div class="box"><select id="kfreq" style="flex:1">{kfreq}</select></div>
    </div>
    <fieldset class="field" style="border:0;padding:0;margin:0">
      <legend class="label" style="font-size:14px;font-weight:600;margin:0 0 6px;padding:0">{e(t["timing"])}</legend>
      <div class="seg row">{timings}</div>
    </fieldset>
  </details>
</form>

<a class="mini off" id="mini" href="#results" aria-hidden="true" tabindex="-1"><span id="mini-label"></span><b id="mini-val"></b><i>↓</i></a>
<div class="results" id="results" aria-live="polite">
  <section class="card">
    <div class="err" id="res-err" hidden></div>
    <div class="headline">
      <div class="main"><div class="label" id="res-fv-label"></div><div class="big" id="res-fv">-</div><div class="sub" id="res-fv-sub"></div></div>
      <div class="stat"><div class="label">{e(t["put"])}</div><b id="res-put">-</b></div>
      <div class="stat"><div class="label">{e(t["interest"])}</div><b id="res-interest">-</b></div>
    </div>
    <div class="split">
      <div class="bar" role="img" aria-label="{e(t["l_initial"])} / {e(t["l_contrib"])} / {e(t["l_interest"])}"><span class="p" id="split-p"></span><span class="c" id="split-c"></span><span class="i" style="flex:1"></span></div>
      <div class="legend"><span id="lg-p"><i class="sw sw-p"></i>{e(t["l_initial"])} <b id="res-initial"></b> · <span id="pct-p"></span></span><span id="lg-c"><i class="sw sw-c"></i>{e(t["l_contrib"])} <b id="res-contrib"></b> · <span id="pct-c"></span></span><span><i class="sw sw-i"></i>{e(t["l_interest"])} <b id="res-int2"></b> · <span id="pct-i"></span></span></div>
    </div>
  </section>

  <section class="card">
    <h2>{e(t["chart_title"])}</h2>
    <p class="note">{e(t["chart_note"])}</p>
    <div class="legend" style="margin:0 0 8px"><span><i class="sw sw-p"></i>{e(t["l_initial"])}</span><span><i class="sw sw-c"></i>{e(t["l_contrib"])}</span><span><i class="sw sw-i"></i>{e(t["l_interest"])}</span></div>
    <div class="chartbox"><svg id="chart" role="img" aria-label="{e(t["chart_title"])}" viewBox="0 0 640 260"></svg><div class="tip" id="chart-tip" hidden></div></div>
  </section>

  <section class="card">
    <h2>{e(t["cmp_title"])}</h2>
    <p class="note">{e(t["cmp_note"])}</p>
    <div class="cmpwrap"><table class="cmp"><thead><tr>{"".join(f'<th scope="col">{e(x)}</th>' for x in t["cmp_cols"])}</tr></thead>
    <tbody>{cmp_rows}</tbody></table></div>
  </section>

  <section class="card promo">
    <img src="/fincal/ic_launcher-playstore.png" alt="Fincal" width="56" height="56" loading="lazy">
    <div>
      <h2>{e(t["promo_title"])}</h2>
      <p class="note" style="margin:0">{e(t["promo_lead"])}</p>
      <ul>{promo}</ul>
      {stores(t, c)}
    </div>
  </section>

  <details class="card fold">
    <summary><h2>{e(t["sched_title"])}</h2><span class="fold-hint" id="sched-count"></span></summary>
    <div class="tablewrap"><table class="sched"><thead><tr>{cols}</tr></thead><tbody id="sched-body"></tbody></table></div>
    <p class="more">{e(t["sched_more"])}</p>
  </details>
</div>
</div>

<article class="article">
{article}
<h2>{c["faq_h"]}</h2>
<div class="faq">{faq}</div>
<p class="calc-links"><a href="{LOAN_PATH[lang]}">{e(t["loan_link"])} →</a></p>
{related(lang, t["path"], "save")}
</article>
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(c["footer_privacy"])}</a><a href="/fincal/support/">{e(c["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
<script src="/fincal/calc/compound.js" defer></script>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, C[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(page(lang))
    print(p, numbers(lang)["fv"])
