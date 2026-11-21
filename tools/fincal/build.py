"""Rebuild every generated Fincal page and keep sitemap.xml in step.

Run from anywhere:  python3 -I tools/fincal/build.py
Pages whose HTML changed get today's lastmod; pages missing from sitemap.xml are added.
"""
import datetime
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from articles import site_urls  # noqa: E402

BASE = "https://nanoko.app"
# Each article generator also re-runs loanpage on import; that is harmless.
GENERATORS = ["loanpage", "comppage", "teaserpage", "flatpage", "prepaypage", "depositpage", "blogpage"]


def digest(path):
    p = os.path.join(ROOT, path.strip("/"), "index.html")
    return hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


urls = site_urls()
before = {u: digest(u) for u in urls}
for g in GENERATORS:
    subprocess.run([sys.executable, "-I", os.path.join(HERE, g + ".py"), ROOT], check=True, stdout=subprocess.DEVNULL)
changed = [u for u in urls if digest(u) != before[u]]

today = datetime.date.today().isoformat()
sm_path = os.path.join(ROOT, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()
added = []
for u in urls:
    loc = f"<loc>{BASE}{u}</loc>"
    if loc in sm:
        if u in changed:
            sm = re.sub(re.escape(loc) + r"<lastmod>[^<]*</lastmod>", f"{loc}<lastmod>{today}</lastmod>", sm)
        continue
    # New page: insert after the last Fincal entry.
    last = list(re.finditer(r"  <url><loc>" + re.escape(BASE) + r"/fincal/[^\n]*\n", sm))[-1]
    sm = sm[:last.end()] + f"  <url>{loc}<lastmod>{today}</lastmod></url>\n" + sm[last.end():]
    added.append(u)
open(sm_path, "w", encoding="utf-8").write(sm)

print(f"{len(urls)} pages, {len(changed)} changed, {len(added)} added to sitemap")
for u in added:
    print("  +", u)
