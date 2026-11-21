"""Crawl a site from / and sitemap.xml, check every internal href/src/srcset/poster/data-* path returns 200.
usage: python3 -I linkcheck.py http://localhost:8765   (or https://nanoko.app)
"""
import re
import sys
import urllib.request
from urllib.error import HTTPError
from urllib.parse import urljoin, urlparse

BASE = sys.argv[1].rstrip("/")
host = urlparse(BASE).netloc
ATTR = re.compile(r'\s(?:href|src|poster|data-src-en|data-src-vi|data-en|data-vi|content)=["\']([^"\']+)["\']')
CSSURL = re.compile(r'url\(["\']?([^"\')]+)["\']?\)')
ASSET = re.compile(r"(\.(png|jpe?g|webp|svg|gif|mp4|css|js|ico|ttf|txt|xml)|/)(\?.*)?$", re.I)

status, seen, queue, refs = {}, set(), [], {}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "linkcheck"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except HTTPError as e:
        return e.code, "", b""


def add(url, frm):
    u = urlparse(url)
    if u.netloc not in (host, "nanoko.app") or u.scheme not in ("http", "https"):
        return
    url = BASE + u.path + (("?" + u.query) if u.query else "")
    refs.setdefault(url, frm)
    if url not in seen:
        seen.add(url)
        queue.append(url)


add(BASE + "/", "start")
code, _, body = fetch(BASE + "/sitemap.xml")
for loc in re.findall(r"<loc>([^<]+)</loc>", body.decode()):
    add(loc, "sitemap")
for extra in ("/app-ads.txt", "/robots.txt", "/sitemap.xml", "/CNAME"):
    add(BASE + extra, "root")

while queue:
    url = queue.pop()
    code, ctype, body = fetch(url)
    status[url] = code
    if code != 200:
        continue
    text = body.decode("utf-8", "replace")
    if "html" in ctype:
        for v in ATTR.findall(text):
            if v.startswith(("mailto:", "tel:", "#", "data:", "intent:", "javascript:")):
                continue
            if v.startswith(("http", "/", ".")) or ASSET.search(v):
                if " " in v:
                    continue
                add(urljoin(url, v), url)
    elif "css" in ctype:
        for v in CSSURL.findall(text):
            if not v.startswith("data:"):
                add(urljoin(url, v), url)

bad = {u: c for u, c in status.items() if c != 200}
print(f"checked {len(status)} urls, {len(bad)} bad")
for u, c in sorted(bad.items()):
    print(c, u, "<-", refs.get(u))
