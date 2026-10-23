"""Shared layout for TX Torque content pages. Run _build/build.py to regenerate the HTML.
Never use em/en dashes in copy (house rule)."""
import json, html, os, re

SITE = 'https://torquebaseball.us'
PHONE = '+1-915-474-0940'
PHONE_DISPLAY = '+1 915-474-0940'
WA = 'https://wa.me/19154740940'
IG = 'https://www.instagram.com/tx.torque/'
APP = 'https://app.torquebaseball.us/'
LOGO = 'https://res.cloudinary.com/dsprn0ew4/image/upload/f_auto,q_auto,w_120/v1790046313/ChatGPT_Image_Sep_21_2026_09_05_04_PM_yiuj48.png'
LOGO_512 = 'https://res.cloudinary.com/dsprn0ew4/image/upload/f_auto,q_auto,w_512/v1790046313/ChatGPT_Image_Sep_21_2026_09_05_04_PM_yiuj48.png'
ADDR = {'@type': 'PostalAddress', 'streetAddress': '2010 Bassett Ave', 'addressLocality': 'El Paso',
        'addressRegion': 'TX', 'postalCode': '79901', 'addressCountry': 'US'}
MAPS = 'https://maps.google.com/?q=2010+Bassett+Ave,+El+Paso,+TX+79901'
ORG_ID = SITE + '/#academy'
ANALYTICS = '<script defer src="https://roots-engine.vercel.app/t.js" data-site="ae516dc734ece130f75ee0e5cf561244"></script>\n  <script src="/assets/meta-pixel.js" async></script>'
WA_SVG = open(os.path.join(os.path.dirname(__file__), 'wa_path.txt')).read().strip()

def org_schema(lang='en'):
    return {
        '@type': ['SportsActivityLocation', 'LocalBusiness'], '@id': ORG_ID,
        'name': 'TX Torque Baseball Academy', 'alternateName': 'TX Torque',
        'description': ("Pro-led baseball and softball academy in El Paso, Texas. Coached by former MLB draft picks and pro players, "
                        "with TrackMan data on every rep. Ages 7 and up.") if lang == 'en' else
                       ("Academia de béisbol y softball en El Paso, Texas, dirigida por exjugadores profesionales y draft picks de MLB, "
                        "con datos de TrackMan en cada repetición. Desde 7 años."),
        'url': SITE + ('/' if lang == 'en' else '/es'), 'telephone': PHONE, 'image': SITE + '/assets/img/wide-coaches.jpg',
        'logo': LOGO_512, 'address': ADDR, 'priceRange': '$$', 'sameAs': [IG],
        'areaServed': {'@type': 'City', 'name': 'El Paso, Texas'},
        'sport': ['Baseball', 'Softball'],
    }

def esc(s): return html.escape(s, quote=True)

def crumb_schema(trail):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(trail)]}

NAV = {
 'en': [('Programs', '/programs'), ('Coaches', '/coaches'), ('Facility', '/facility'), ('Membership', '/membership'), ('Guides', '/guides'), ('FAQ', '/faq')],
 'es': [('Programas', '/es/programas'), ('Coaches', '/es/coaches'), ('Instalaciones', '/es/instalaciones'), ('Membresías', '/es/membresias'), ('Preguntas', '/es/preguntas-frecuentes')],
}
T = {
 'en': dict(trial='Free Trial', trial_long='Book a Free Trial', login='Member Login', lang_label='ES', menu='Open menu',
            home='Home', visit='Visit', contact='Contact', training='Training', academy='Academy', help='Help',
            directions='Directions', rights='TX Torque Baseball Academy. All rights reserved.', wa='WhatsApp', trial_path='/free-trial'),
 'es': dict(trial='Clase gratis', trial_long='Agenda tu clase gratis', login='Miembros', lang_label='EN', menu='Abrir menú',
            home='Inicio', visit='Visítanos', contact='Contacto', training='Entrenamiento', academy='Academia', help='Ayuda',
            directions='Cómo llegar', rights='TX Torque Baseball Academy. Todos los derechos reservados.', wa='WhatsApp', trial_path='/es/clase-gratis'),
}
FOOT = {
 'en': {'training': [('Hitting lessons', '/hitting'), ('Pitching lessons', '/pitching'), ('Catching & fielding', '/catching-fielding'),
                     ('Strength & conditioning', '/strength-conditioning'), ('TrackMan training', '/trackman'), ('Softball', '/softball')],
        'academy': [('Programs by age', '/programs'), ('Coaches', '/coaches'), ('Teams & tryouts', '/teams-tryouts'), ('Camps & events', '/events'),
                    ('Facility', '/facility'), ('Membership & prices', '/membership')],
        'help': [('Free trial class', '/free-trial'), ('FAQ', '/faq'), ('Guides', '/guides'), ('Español', '/es'), ('Member login', APP)]},
 'es': {'training': [('Clases de bateo', '/es/clases-de-bateo'), ('Clases de pitcheo', '/es/clases-de-pitcheo'), ('Programas por edad', '/es/programas'),
                     ('Softball', '/softball'), ('TrackMan (inglés)', '/trackman')],
        'academy': [('Coaches', '/es/coaches'), ('Instalaciones', '/es/instalaciones'), ('Membresías y precios', '/es/membresias'),
                    ('Equipos y tryouts (inglés)', '/teams-tryouts')],
        'help': [('Clase gratis', '/es/clase-gratis'), ('Preguntas frecuentes', '/es/preguntas-frecuentes'), ('English', '/'), ('Acceso miembros', APP)]},
}

def page(*, lang, path, title, desc, h1_html, body, trail, schema=(), alt=None, image='/assets/img/wide-coaches.jpg',
         kicker='', answer='', hero_img=None, hero_alt='', ctas=True, og_type='website'):
    """path: '/hitting'. trail: [(name, path), ...] including the current page. alt: {'en': path, 'es': path} for hreflang."""
    t = T[lang]
    url = SITE + (path if path != '/' else '/')
    graph = [crumb_schema(trail)] + list(schema)
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=None)
    hreflang = ''
    if alt:
        for l, p in alt.items():
            hreflang += f'<link rel="alternate" hreflang="{l}" href="{SITE}{p if p != "/" else "/"}" />\n  '
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt.get("en", "/")}" />'
    img_abs = image if image.startswith('http') else SITE + image
    nav = ''.join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == path else ""}>{n}</a></li>' for n, u in NAV[lang])
    mnav = ''.join(f'<a class="big" href="{u}">{n}</a>' for n, u in NAV[lang])
    other = alt.get('es' if lang == 'en' else 'en') if alt else ('/es' if lang == 'en' else '/')
    crumbs = ''.join(f'<li><a href="{u}">{esc(n)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{esc(n)}</li>'
                     for i, (n, u) in enumerate(trail))
    hero_cta = (f'<div class="ctas"><a class="btn btn-primary" href="{t["trial_path"]}">{t["trial_long"]}</a>'
                f'<a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{t["wa"]} {PHONE_DISPLAY}</a></div>') if ctas else ''
    hero_inner = (f'<ol class="crumbs">{crumbs}</ol>' + (f'<p class="kicker">{kicker}</p>' if kicker else '') +
                  f'<h1 class="display">{h1_html}</h1>' + (f'<p class="answer">{answer}</p>' if answer else '') + hero_cta)
    if hero_img:
        hero = (f'<section class="hero"><div class="wrap hero-grid"><div>{hero_inner}</div>'
                f'<figure><img src="{hero_img}" alt="{esc(hero_alt)}" width="900" height="1125" fetchpriority="high" /></figure></div></section>')
    else:
        hero = f'<section class="hero"><div class="wrap">{hero_inner}</div></section>'
    foot = FOOT[lang]
    flist = lambda items: ''.join(f'<li><a href="{u}"{" target=\"_blank\" rel=\"noopener\"" if u.startswith("http") else ""}>{n}</a></li>' for n, u in items)
    out = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <link rel="canonical" href="{url}" />
  {hreflang}
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="TX Torque Baseball Academy" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{img_abs}" />
  <meta property="og:locale" content="{'en_US' if lang == 'en' else 'es_MX'}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(desc)}" />
  <meta name="twitter:image" content="{img_abs}" />
  <meta name="theme-color" content="#05080f" />
  <link rel="icon" href="{LOGO}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/site.css" />
  <script type="application/ld+json">{ld}</script>
  {ANALYTICS}
</head>
<body>
  <header id="nav">
    <div class="wrap bar">
      <a href="{'/' if lang == 'en' else '/es'}" class="brand" aria-label="TX Torque {t['home']}"><img src="{LOGO}" alt="" width="42" height="42" /><span>TX TORQUE</span></a>
      <ul class="nav-links">{nav}</ul>
      <div class="nav-cta">
        <a class="lang" href="{other}" hreflang="{'es' if lang == 'en' else 'en'}">{t['lang_label']}</a>
        <a href="{APP}" class="btn btn-ghost btn-sm hide-m" target="_blank" rel="noopener">{t['login']}</a>
        <a href="{t['trial_path']}" class="btn btn-primary btn-sm">{t['trial']}</a>
        <button id="burger" aria-label="{t['menu']}" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 7h18M3 12h18M3 17h12"/></svg></button>
      </div>
    </div>
  </header>
  <nav id="mnav" aria-label="Menu">
    <button id="mnav-close" aria-label="Close"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
    <a class="big" href="{'/' if lang == 'en' else '/es'}">{t['home']}</a>{mnav}
    <a class="big" href="{t['trial_path']}">{t['trial']}</a>
    <a class="big" href="{other}">{'Español' if lang == 'en' else 'English'}</a>
  </nav>
  <main>
  {hero}
  {body}
  </main>
  <footer>
    <div class="wrap">
      <div class="fgrid">
        <div><p class="kicker">TX Torque Baseball Academy</p><p class="fbig">Built<br>by <span class="blue">Pros.</span></p></div>
        <div><h4>{t['visit']}</h4><ul><li>2010 Bassett Ave</li><li>El Paso, TX 79901</li><li><a href="{MAPS}" target="_blank" rel="noopener">{t['directions']}</a></li></ul>
             <h4 style="margin-top:22px">{t['contact']}</h4><ul><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram @tx.torque</a></li></ul></div>
        <div><h4>{t['training']}</h4><ul>{flist(foot['training'])}</ul></div>
        <div><h4>{t['academy']}</h4><ul>{flist(foot['academy'])}</ul></div>
        <div><h4>{t['help']}</h4><ul>{flist(foot['help'])}</ul></div>
      </div>
      <div class="fbottom"><span>&copy; <span id="footer-year">2026</span> {t['rights']}</span><span>El Paso, Texas</span></div>
    </div>
  </footer>
  <div class="trial-bar"><a class="btn btn-primary" href="{t['trial_path']}">{t['trial']}</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
  <a id="wa-btn" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp"><svg width="28" height="28" viewBox="0 0 24 24" fill="white"><path {WA_SVG}/></svg></a>
  <script src="/assets/site.js" defer></script>
</body>
</html>
'''
    return out

def write(path, content):
    """path '/hitting' -> hitting.html ; '/coaches/x' -> coaches/x.html ; '/es' -> es/index.html"""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if path in ('/es',):
        f = os.path.join(root, 'es', 'index.html')
    else:
        f = os.path.join(root, path.strip('/') + '.html')
    os.makedirs(os.path.dirname(f), exist_ok=True)
    for bad in ('—', '–'):
        if bad in content:
            i = content.index(bad); raise SystemExit(f'Long dash in {path}: ...{content[max(0,i-60):i+20]}...')
    open(f, 'w').write(content)
    return f

def img(src, alt, w=900, h=1125, cls='figure', cap=''):
    return (f'<figure class="{cls}"><img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async" />'
            + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>')

def faq_schema(qas):
    strip = lambda s: re.sub(r'<[^>]+>', '', s)
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': strip(q),
            'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in qas]}

def faq_html(qas):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qas) + '</div>'

def lead_form(lang, source, *, preferred=True, redirect='', btn='', note='', interest=None):
    es = lang == 'es'
    L = (lambda en, sp: sp if es else en)
    days = ['Friday 4:00 PM', 'Friday 5:00 PM', 'Friday 6:00 PM', 'Saturday 12:00 PM', 'Saturday 1:00 PM', 'Saturday 2:00 PM']
    days_es = ['Viernes 4:00 PM', 'Viernes 5:00 PM', 'Viernes 6:00 PM', 'Sábado 12:00 PM', 'Sábado 1:00 PM', 'Sábado 2:00 PM']
    if interest is not None:
        pref = f'<input type="hidden" name="preferredDay" value="{esc(interest)}" />'
    elif preferred:
        opts = ''.join(f'<option value="{d}">{dd}</option>' for d, dd in zip(days, days_es if es else days))
        pref = (f'<div class="full"><label for="f-day-{source}">{L("Preferred day & time", "Día y hora")}</label>'
                f'<select id="f-day-{source}" name="preferredDay" required><option value="">{L("Select a day & time", "Elige día y hora")}</option>{opts}</select></div>')
    else:
        pref = ''
    return f'''<form class="form" data-lead data-source="{source}" data-status="{'booked' if redirect else 'new'}" {f'data-redirect="{redirect}"' if redirect else ''} novalidate>
  <input class="hp" type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true" />
  <div class="form-grid">
    <div><label for="f-pn-{source}">{L("Parent name", "Nombre del papá o mamá")}</label><input id="f-pn-{source}" name="parentName" autocomplete="name" required /></div>
    <div><label for="f-ph-{source}">{L("Phone", "Teléfono")}</label><input id="f-ph-{source}" name="phone" type="tel" autocomplete="tel" required /></div>
    <div class="full"><label for="f-em-{source}">{L("Email", "Correo")}</label><input id="f-em-{source}" name="email" type="email" autocomplete="email" required /></div>
    <div><label for="f-pl-{source}">{L("Player name", "Nombre del jugador")}</label><input id="f-pl-{source}" name="playerName" required /></div>
    <div><label for="f-ag-{source}">{L("Player age", "Edad del jugador")}</label><input id="f-ag-{source}" name="playerAge" type="number" min="4" max="25" inputmode="numeric" required /></div>
    {pref}
  </div>
  <div class="ctas" style="margin-top:20px"><button type="submit" class="btn btn-primary" style="flex:1 1 100%">{btn or L("Book my free trial", "Agendar mi clase gratis")}</button></div>
  <p class="err" role="alert"></p>
  <p class="ok" role="status">{L("Got it. A coach will reach out within 24 hours.", "Listo. Un coach te contacta en menos de 24 horas.")}</p>
  <p class="small muted" style="margin:12px 0 0">{note or L("No deposit, no cost. By submitting you agree to be contacted about your request.", "Sin depósito y sin costo. Al enviar aceptas que te contactemos.")}</p>
</form>'''

def band(lang, title=None, text=None):
    es = lang == 'es'
    title = title or ('Tu primera clase es <span class="blue">gratis.</span>' if es else 'Your first class is <span class="blue">free.</span>')
    text = text or ('Viernes y sábados, todo el año. Sin depósito y sin compromiso.' if es else 'Fridays and Saturdays, year-round. No deposit, no commitment.')
    t = T[lang]
    return (f'<section class="band"><div class="wrap"><h2>{title}</h2><p class="lead">{text}</p>'
            f'<div class="ctas"><a class="btn btn-primary" href="{t["trial_path"]}">{t["trial_long"]}</a>'
            f'<a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></div></div></section>')
