"""Regenerate all TX Torque content pages + sitemap/robots/llms.txt.
Usage (from repo root):  python3 _build/build.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import pages_en, pages_es, guides

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LASTMOD = '2026-10-22'
guides.build()
ALL = pages_en.PAGES + guides.PAGES + pages_es.PAGES
for path, html_ in ALL:
    write(path, html_)
open(os.path.join(ROOT, '404.html'), 'w').write(pages_en.NOT_FOUND)
print(f'wrote {len(ALL)} pages + 404')

# hreflang pairs (en path -> es path)
PAIRS = {'/': '/es', '/programs': '/es/programas', '/hitting': '/es/clases-de-bateo', '/pitching': '/es/clases-de-pitcheo',
         '/coaches': '/es/coaches', '/free-trial': '/es/clase-gratis', '/membership': '/es/membresias',
         '/facility': '/es/instalaciones', '/faq': '/es/preguntas-frecuentes'}
REV = {v: k for k, v in PAIRS.items()}
paths = ['/', '/tournament'] + [p for p, _ in ALL]
def entry(p):
    pri = '1.0' if p in ('/', '/es') else '0.8' if p.count('/') == 1 else '0.6'
    alts = ''
    if p in PAIRS or p in REV:
        en = p if p in PAIRS else REV[p]; es = PAIRS[en]
        alts = (f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>'
                f'<xhtml:link rel="alternate" hreflang="es" href="{SITE}{es}"/>'
                f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/>')
    return f'  <url><loc>{SITE}{p}</loc><lastmod>{LASTMOD}</lastmod><priority>{pri}</priority>{alts}</url>'
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(entry(p) for p in paths) + '\n</urlset>\n')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sitemap)

open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'''# TX Torque Baseball Academy
User-agent: *
Allow: /
Disallow: /thank-you

# AI crawlers are welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
''')

coaches = '\n'.join(f'- [{c["name"]}]({SITE}/coaches/{c["slug"]}): {c["role"]}. {c["badge"]}.' for c in pages_en.COACHES)
gl = '\n'.join(f'- [{g["h1"]}]({SITE}/guides/{g["slug"]})' for g in guides.GUIDES)
open(os.path.join(ROOT, 'llms.txt'), 'w').write(f'''# TX Torque Baseball Academy

> Pro-led baseball (and soon softball) academy in El Paso, Texas, for ages 7 and up. Coached by former MLB draft picks and professional players, with TrackMan data on every rep. The first trial class is free.

## Key facts
- Address: 2010 Bassett Ave, El Paso, TX 79901 (new facility, open from Monday, November 2, 2026; closed October 23 to November 1 for the move)
- Phone / WhatsApp: +1 915-474-0940
- Instagram: @tx.torque ({IG})
- Ages: 7 and up, in three groups: 7 to 10 (4:00 to 6:00 PM), 11 to 14 (6:00 to 7:00 PM), 14+ (7:00 to 8:00 PM)
- Free trial class: Fridays (4, 5 or 6 PM) and Saturdays (12, 1 or 2 PM), year-round, no deposit
- Monthly memberships: A $260 (4 lessons), AA $360 (8 lessons), AAA $440 (12 lessons), MLB $600 (unlimited). 6-month, 12-month and annual plans save 10%, 15% and 20%.
- Facility: 5 batting cages with machines, pitching lane with mound, open turf field, strength area, parent lobby
- Technology: TrackMan (exit velocity, launch angle, pitch velocity, spin rate)
- Club team: Torque Youth. First tryouts held October 10, 2026 at Del Valle High School.
- Softball: Torque Softball program coming soon (interest list open).
- Languages: English and Spanish site

## Coaches
{coaches}

## Main pages
- [Home]({SITE}/)
- [Programs by age]({SITE}/programs)
- [Hitting lessons]({SITE}/hitting)
- [Pitching lessons]({SITE}/pitching)
- [Catching & fielding]({SITE}/catching-fielding)
- [Strength & conditioning]({SITE}/strength-conditioning)
- [TrackMan training]({SITE}/trackman)
- [Softball (coming soon)]({SITE}/softball)
- [Coaches]({SITE}/coaches)
- [Free trial class]({SITE}/free-trial)
- [Membership & prices]({SITE}/membership)
- [Teams & tryouts]({SITE}/teams-tryouts)
- [Camps & events]({SITE}/events)
- [Facility & location]({SITE}/facility)
- [FAQ]({SITE}/faq)

## Guides
{gl}

## Español
- [Inicio]({SITE}/es)
- [Clase gratis]({SITE}/es/clase-gratis)
- [Membresías y precios]({SITE}/es/membresias)
- [Preguntas frecuentes]({SITE}/es/preguntas-frecuentes)
''')

json.dump({
  'cleanUrls': True,
  'trailingSlash': False,
  'redirects': [
    {'source': '/tryout', 'destination': '/teams-tryouts', 'permanent': True},
    {'source': '/tryouts', 'destination': '/teams-tryouts', 'permanent': True},
    {'source': '/torneo', 'destination': '/tournament', 'permanent': True},
    {'source': '/precios', 'destination': '/es/membresias', 'permanent': True},
    {'source': '/softbol', 'destination': '/softball', 'permanent': True},
  ],
  'headers': [
    {'source': '/assets/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=2592000'}]},
    {'source': '/thank-you', 'headers': [{'key': 'X-Robots-Tag', 'value': 'noindex'}]},
  ],
}, open(os.path.join(ROOT, 'vercel.json'), 'w'), indent=2)
open(os.path.join(ROOT, '.vercelignore'), 'w').write('_build\n')
print('sitemap, robots, llms.txt, vercel.json written')
