"""Generate the Fincal blog index pages (one per language) from articles.py."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import BLOG, CALCS, CSS_HREF, ORDER, TOPICS, UI, articles, e, nav, postlist  # noqa: E402

ROOT = sys.argv[1]
BASE = "https://nanoko.app"


def jsonld(lang, b):
    url = BASE + b["path"]
    items = articles(lang)
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": b["title"], "url": url, "inLanguage": lang, "description": b["desc"],
         "publisher": {"@type": "Organization", "name": "Nanoko Studio", "url": BASE + "/"},
         "mainEntity": {"@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": BASE + t["path"], "name": t["h1"]} for i, (_, t) in enumerate(items)]}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Nanoko Studio", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Fincal", "item": BASE + "/fincal/"},
            {"@type": "ListItem", "position": 3, "name": b["nav"], "item": url}]},
    ]}, ensure_ascii=False)


def build(lang):
    b, u = BLOG[lang], UI[lang]
    url = BASE + b["path"]
    hreflang = "\n".join(f'<link rel="alternate" hreflang="{k}" href="{BASE}{BLOG[k]["path"]}">' for k in ORDER)
    langmenu = "".join(
        f'<a href="{BLOG[k]["path"]}" hreflang="{k}" lang="{k}"' + (' aria-current="true"' if k == lang else "") + f'>{e(UI[k]["name"])}</a>'
        for k in ORDER)
    calcs = "".join(f'<a href="{CALCS[topic][lang][0]}">{e(CALCS[topic][lang][1])} →</a>' for topic in TOPICS)
    body = postlist(articles(lang)) + f'\n<p class="calc-links">{calcs}</p>'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(b["title"])}</title>
<meta name="description" content="{e(b["desc"])}">
<link rel="canonical" href="{url}">
{hreflang}
<link rel="alternate" hreflang="x-default" href="{BASE}{BLOG["en"]["path"]}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fincal">
<meta property="og:title" content="{e(b["title"])}">
<meta property="og:description" content="{e(b["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/fincal/ic_launcher-playstore.png">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f6f6f1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15171a" media="(prefers-color-scheme: dark)">
<link rel="icon" type="image/png" href="/fincal/ic_launcher-playstore.png">
<link rel="stylesheet" href="{CSS_HREF}">
<script type="application/ld+json">{jsonld(lang, b)}</script>
</head>
<body>
<header class="topbar"><div class="wrap">
<a class="brand" href="/fincal/"><img src="/fincal/ic_launcher-playstore.png" alt="" width="32" height="32">Fincal</a>
<span class="spacer"></span>
{nav(lang, current=True)}
<details class="langs"><summary aria-label="{e(u["name"])}">{u["short"]}</summary><nav class="langmenu">{langmenu}</nav></details>
</div></header>

<main class="wrap blog">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Nanoko Studio</a> › <a href="/fincal/">Fincal</a> › <span>{e(b["nav"])}</span></nav>
<h1>{e(b["nav"])}</h1>
<p class="intro">{e(b["intro"])}</p>
{body}
</main>

<footer class="site"><div class="wrap">
<a href="/fincal/">Fincal</a><a href="/fincal/privacy/">{e(u["footer_privacy"])}</a><a href="/fincal/support/">{e(u["footer_support"])}</a>
<div class="copy">© 2026 <a href="{"/vi/" if lang == "vi" else "/"}">Nanoko Studio</a> · Truong Phuong Nam</div>
</div></footer>
</body>
</html>
"""


for lang in ORDER:
    p = os.path.join(ROOT, BLOG[lang]["path"].strip("/"), "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(build(lang))
    print(p)
