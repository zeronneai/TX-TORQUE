from lib import *

L = 'en'
HOME = ('Home', '/')
CLOUD = 'https://res.cloudinary.com/dsprn0ew4/image/upload/f_auto,q_auto,w_600/'

COACHES = [
 dict(slug='justin-maese', name='Justin Maese', role='Director of Facility Operations · Pitching', badge='3rd round, 2015 MLB Draft',
      photo=CLOUD + 'v1777676822/Captura_de_pantalla_2026-05-01_163730_uudbo5.png',
      teams=['New York Yankees', 'Atlanta Braves', 'Toronto Blue Jays'], honors=['2015 El Paso Baseball Hall of Fame'],
      bio='Justin Maese was selected in the 3rd round of the 2015 MLB Draft and spent nine years in professional baseball with the New York Yankees, Atlanta Braves and Toronto Blue Jays organizations. He is a 2015 inductee of the El Paso Baseball Hall of Fame. At Torque he leads all training operations and runs the pitching program.',
      focus='Pitching', service='/pitching', job='Director of Facility Operations and Pitching Coach'),
 dict(slug='eudor-garcia', name='Eudor Garcia', role='Fielding & Hitting Director', badge='4th round, 2014 MLB Draft',
      photo=CLOUD + 'v1787776032/EDURO_qg39ly.jpg',
      teams=['EPCC', 'New York Mets', 'Toros de Tijuana', 'Algodoneros', 'Indios de Juárez'], honors=['NJCAA Player of the Year', '2014 El Paso Baseball Hall of Fame'],
      bio='Eudor Garcia was the NJCAA Player of the Year at El Paso Community College and a 4th round pick in the 2014 MLB Draft. He played twelve years of professional baseball, from the New York Mets organization to the Mexican League with Toros de Tijuana, Algodoneros and Indios de Juárez, and was inducted into the El Paso Baseball Hall of Fame in 2014. He directs hitting and defense at Torque with a detail-driven approach.',
      focus='Hitting and fielding', service='/hitting', job='Fielding and Hitting Director'),
 dict(slug='alex-reyes', name='Alex Reyes', role='Events & Recruitment Director', badge='College two-way · 5 years pro',
      photo=CLOUD + 'v1777587918/WhatsApp_Image_2026-04-30_at_4.19.51_PM_4_djunua.jpg',
      teams=['New Mexico State University', 'Bravos de León', 'Tigres de Aragua', 'Venados de Mazatlán'], honors=[],
      bio='Alex Reyes played four years of college baseball as a two-way player at New Mexico State University, then five professional seasons across Mexico, Venezuela and Colombia, including Bravos de León, Tigres de Aragua and Venados de Mazatlán. He runs events and recruitment at Torque and guides families through the recruiting process.',
      focus='Events and recruiting', service='/teams-tryouts', job='Events and Recruitment Director'),
 dict(slug='gabriel-aguilar', name='Gabriel Aguilar', role='Team Operations · Pitching · Strength & Conditioning', badge='10 years of pro pitching',
      photo=CLOUD + 'v1787776032/GABRIELBASE_mu5fkm.jpg',
      teams=['University of New Mexico', 'Sultanes de Monterrey', 'Leones de Yucatán', 'Rieleros'], honors=[],
      bio='Gabriel Aguilar pitched four years at the University of New Mexico and spent a decade pitching professionally, including Sultanes de Monterrey, Leones de Yucatán and Rieleros. At Torque he handles team operations and coaches pitching development plus strength and conditioning.',
      focus='Pitching and strength and conditioning', service='/strength-conditioning', job='Team Operations, Pitching and Strength and Conditioning Coach'),
 dict(slug='angel-vega', name='Angel Vega', role='Catching & Hitting Specialist', badge='ABCA/Rawlings All-Region First Team',
      photo=None,
      teams=["St. Mary's", 'San Jacinto', 'Algodoneros', 'Pericos de Puebla'], honors=['ABCA/Rawlings All-Region First Team'],
      bio="Angel Vega caught in college at St. Mary's and San Jacinto, earned ABCA/Rawlings All-Region First Team honors, and caught professionally in the Mexican League with Algodoneros and Pericos de Puebla. He leads Torque's specialized catching coaching, one session per week, and also works with hitters.",
      focus='Catching and hitting', service='/catching-fielding', job='Catching and Hitting Specialist'),
]

def coach_card(c, prefix=''):
    ph = f'<img src="{c["photo"]}" alt="{c["name"]}, {c["role"]} at TX Torque" width="600" height="600" loading="lazy" />' if c['photo'] else ''
    return (f'<a class="card" href="{prefix}/coaches/{c["slug"]}">{ph}<span class="tag">{c["badge"]}</span>'
            f'<h3>{c["name"]}</h3><p>{c["role"]}</p></a>')

def service_schema(name, desc, path):
    return {'@type': 'Service', 'name': name, 'serviceType': name, 'description': desc, 'url': SITE + path,
            'provider': {'@id': ORG_ID}, 'areaServed': {'@type': 'City', 'name': 'El Paso, Texas'}}

def related(*links):
    return '<div class="grid g3" style="margin-top:18px">' + ''.join(
        f'<a class="card" href="{u}"><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p></a>' for tag, t, u, d in links) + '</div>'

TRIAL_CARD = ('Next step', 'Book a free trial', '/free-trial', 'Fridays and Saturdays. No deposit, no commitment.')
COACHES_CARD = ('The staff', 'Meet the coaches', '/coaches', 'MLB draft picks and pros from the U.S., Mexico and Latin America.')
PROGRAMS_CARD = ('Ages 7+', 'Programs by age', '/programs', 'Three age groups, each at its own time.')
MEMBER_CARD = ('From $260/mo', 'Membership & prices', '/membership', 'A, AA, AAA or MLB unlimited. Save up to 20%.')
TRACK_CARD = ('Data', 'TrackMan training', '/trackman', 'Exit velocity, launch angle, velo and spin on every rep.')

PAGES = []
def add(path, **kw):
    PAGES.append((path, page(lang=L, path=path, **kw)))

# ── Programs by age ────────────────────────────────────────────────────────────
add('/programs',
  title='Baseball Training by Age in El Paso: 7 to 10, 11 to 14, 14+ | TX Torque',
  desc='Youth baseball classes in El Paso grouped by age: 7 to 10, 11 to 14 and 14+. Pro coaches, TrackMan data and a clear path to high school and college ball.',
  kicker='Programs', h1_html='Baseball training <span class="blue">by age</span> in El Paso',
  answer='TX Torque trains athletes ages 7 and up in three age groups: 7 to 10 (4:00 to 6:00 PM), 11 to 14 (6:00 to 7:00 PM) and 14+ (7:00 to 8:00 PM). Every athlete trains with peers at their level.',
  hero_img='/assets/img/kids56_grupo.webp', hero_alt='Group of young TX Torque players listening to a coach on the field',
  trail=[HOME, ('Programs', '/programs')],
  schema=[service_schema('Youth baseball training by age group', 'Baseball classes for ages 7 to 10, 11 to 14 and 14+ in El Paso, TX.', '/programs')],
  alt={'en': '/programs', 'es': '/es/programas'},
  body=f'''<section><div class="wrap prose">
<h2>Three groups, one system</h2>
<p>Register in the correct age group, then pick the membership that fits your schedule. Every group follows the same Torque Method: strength, power, swing and data.</p>
<div class="grid g3">
  <div class="card"><span class="tag">Group 01 · 4:00 to 6:00 PM</span><h3>Ages 7 to 10</h3><p>Foundations done right: throwing, catching, swing basics and athletic movement, in a fun, high-energy environment.</p></div>
  <div class="card"><span class="tag">Group 02 · 6:00 to 7:00 PM</span><h3>Ages 11 to 14</h3><p>Sharper mechanics, more strength and the first TrackMan baselines as players get ready for high school ball.</p></div>
  <div class="card"><span class="tag">Group 03 · 7:00 to 8:00 PM</span><h3>Ages 14+</h3><p>Advanced development with pro-level training, data and accountability for athletes chasing the next level.</p></div>
</div>
<h2>What every session includes</h2>
<ul>
<li><b>Strength:</b> age-appropriate strength and conditioning that builds a durable, athletic body. <a href="/strength-conditioning">More on strength and conditioning</a>.</li>
<li><b>Power:</b> rotational power and speed work that turns strength into bat speed and velocity.</li>
<li><b>Swing:</b> hitting, pitching and fielding mechanics taught by coaches who did it as pros. See <a href="/hitting">hitting</a>, <a href="/pitching">pitching</a> and <a href="/catching-fielding">catching and fielding</a>.</li>
<li><b>Data:</b> <a href="/trackman">TrackMan</a> numbers on every rep, so progress is measured, not guessed.</li>
</ul>
<h2>Beyond classes</h2>
<p>Players who want game reps can join the <a href="/teams-tryouts">Torque Youth Club Team</a>, our first club team, coached in real games by our staff. Older players get help with the recruiting process from coaches with real college and pro connections.</p>
{related(TRIAL_CARD, MEMBER_CARD, COACHES_CARD)}
</div></section>{band(L)}''')

# ── Service pages ──────────────────────────────────────────────────────────────
def coach_mini(slugs):
    return '<div class="grid g3" style="margin-top:12px">' + ''.join(coach_card(c) for c in COACHES if c['slug'] in slugs) + '</div>'

add('/hitting',
  title='Hitting Lessons in El Paso, TX | TX Torque Baseball Academy',
  desc='Baseball hitting lessons in El Paso taught by a former MLB draft pick. Swing mechanics, approach and TrackMan exit velocity and launch angle on every swing.',
  kicker='Training', h1_html='Hitting lessons <span class="blue">in El Paso</span>',
  answer='TX Torque teaches hitting in El Paso with coaches who played pro ball, led by Fielding and Hitting Director Eudor Garcia (4th round, 2014 MLB Draft). Every swing is measured with TrackMan for exit velocity and launch angle.',
  hero_img='/assets/img/kids26_bateo.webp', hero_alt='Young hitter in an orange jersey swinging in a TX Torque batting cage',
  trail=[HOME, ('Programs', '/programs'), ('Hitting', '/hitting')],
  schema=[service_schema('Baseball hitting lessons', 'Hitting instruction with TrackMan exit velocity and launch angle measurement in El Paso, TX.', '/hitting')],
  alt={'en': '/hitting', 'es': '/es/clases-de-bateo'},
  body=f'''<section><div class="wrap prose">
<h2>How we train hitters</h2>
<p>Hitting at Torque is part of one connected system. What we build in the weight room shows up in the cage, and the numbers prove it.</p>
<ul>
<li><b>Mechanics:</b> swing work taught by coaches who hit at the professional level in the U.S. and Mexico.</li>
<li><b>Power:</b> rotational power and speed work that turns strength into bat speed.</li>
<li><b>Data:</b> <a href="/trackman">TrackMan</a> tracks exit velocity (how hard the ball comes off the bat) and launch angle (the flight that turns contact into damage) on every swing.</li>
<li><b>Reps:</b> five batting cages with machines on every lane at our <a href="/facility">new facility</a>.</li>
</ul>
<h2>Who coaches hitting</h2>
{coach_mini(['eudor-garcia', 'angel-vega'])}
<h2>Ages and schedule</h2>
<p>Hitting is built into every age group: 7 to 10, 11 to 14 and 14+. See <a href="/programs">programs by age</a> for class times and <a href="/membership">membership and prices</a> for plans.</p>
{related(TRIAL_CARD, TRACK_CARD, MEMBER_CARD)}
</div></section>{band(L)}''')

add('/pitching',
  title='Pitching Lessons in El Paso, TX | TX Torque Baseball Academy',
  desc='Pitching lessons in El Paso led by a former MLB draft pick. Mechanics, velocity and arm strength, with TrackMan pitch velocity and spin rate on every throw.',
  kicker='Training', h1_html='Pitching lessons <span class="blue">in El Paso</span>',
  answer='The TX Torque pitching program is led by Justin Maese, a 3rd round pick in the 2015 MLB Draft with nine years of pro experience. Pitchers train on a dedicated pitching lane with a mound, and TrackMan measures velocity and spin rate on every pitch.',
  hero_img='/assets/img/kids2_pitcheo.webp', hero_alt='Young TX Torque pitcher delivering a pitch on the field',
  trail=[HOME, ('Programs', '/programs'), ('Pitching', '/pitching')],
  schema=[service_schema('Baseball pitching lessons', 'Pitching instruction with TrackMan velocity and spin rate measurement in El Paso, TX.', '/pitching')],
  alt={'en': '/pitching', 'es': '/es/clases-de-pitcheo'},
  body=f'''<section><div class="wrap prose">
<h2>How we train pitchers</h2>
<ul>
<li><b>Mechanics:</b> delivery work from coaches who pitched in the Yankees, Braves and Blue Jays organizations and in the Mexican League.</li>
<li><b>Strength and power:</b> age-appropriate strength and conditioning plus rotational power work that turns into velocity. <a href="/strength-conditioning">See strength and conditioning</a>.</li>
<li><b>Data:</b> <a href="/trackman">TrackMan</a> measures pitch velocity in MPH and spin rate, the movement and quality of every pitch.</li>
<li><b>Space:</b> a dedicated pitching lane with a mound at our <a href="/facility">new facility</a>.</li>
</ul>
<p>Want to understand the process first? Read our guides on <a href="/guides/increase-pitching-velocity">how to increase pitching velocity</a> and <a href="/guides/what-age-start-pitching-lessons">what age to start pitching lessons</a>.</p>
<h2>Who coaches pitching</h2>
{coach_mini(['justin-maese', 'gabriel-aguilar'])}
{related(TRIAL_CARD, PROGRAMS_CARD, MEMBER_CARD)}
</div></section>{band(L)}''')

add('/catching-fielding',
  title='Catching & Fielding Training in El Paso, TX | TX Torque',
  desc='Catching lessons and defensive training in El Paso. Specialized weekly catching coaching from a former Mexican League catcher, plus fielding with a former MLB draft pick.',
  kicker='Training', h1_html='Catching &amp; fielding <span class="blue">training</span>',
  answer='TX Torque offers specialized catching coaching once a week with Angel Vega, a former college and Mexican League catcher, and defensive training led by Fielding and Hitting Director Eudor Garcia.',
  hero_img='/assets/img/kids10_fildeo.webp', hero_alt='Young TX Torque infielder in a ready fielding position',
  trail=[HOME, ('Programs', '/programs'), ('Catching & fielding', '/catching-fielding')],
  schema=[service_schema('Baseball catching and fielding training', 'Specialized catching coaching and defensive training in El Paso, TX.', '/catching-fielding')],
  body=f'''<section><div class="wrap prose">
<h2>Catching</h2>
<p>Catching is its own position with its own skills. Angel Vega caught at St. Mary's and San Jacinto, earned ABCA/Rawlings All-Region First Team honors and caught in the Mexican League with Algodoneros and Pericos de Puebla. He runs specialized catching coaching one session per week.</p>
<h2>Fielding and defense</h2>
<p>Eudor Garcia, a 4th round pick in the 2014 MLB Draft with twelve years of pro baseball, leads detail-driven defensive work. Fielding is trained on the open turf field at our <a href="/facility">new facility</a>.</p>
<h2>Coaches</h2>
{coach_mini(['angel-vega', 'eudor-garcia'])}
{related(TRIAL_CARD, PROGRAMS_CARD, MEMBER_CARD)}
</div></section>{band(L)}''')

add('/strength-conditioning',
  title='Baseball Strength & Conditioning in El Paso, TX | TX Torque',
  desc='Age-appropriate strength, power and speed training for baseball players in El Paso. Built to turn strength into bat speed and pitching velocity.',
  kicker='Training', h1_html='Strength &amp; <span class="blue">conditioning</span> for baseball',
  answer='Strength and conditioning at TX Torque is age-appropriate training that builds a durable, athletic body, plus rotational power and speed work that turns that strength into bat speed and velocity.',
  hero_img='/assets/img/train-strength.webp', hero_alt='TX Torque athlete lifting in the strength area',
  trail=[HOME, ('Programs', '/programs'), ('Strength & conditioning', '/strength-conditioning')],
  schema=[service_schema('Baseball strength and conditioning', 'Age-appropriate strength, power and speed training for baseball players in El Paso, TX.', '/strength-conditioning')],
  body=f'''<section><div class="wrap prose">
<h2>Why it matters for baseball</h2>
<p>Strength is the first step of the Torque Method. It connects to everything else: what we build in the weight room shows up in the cage and on the mound, and <a href="/trackman">TrackMan</a> numbers show whether it is working.</p>
<ul>
<li><b>Strength:</b> age-appropriate training for a durable, athletic body.</li>
<li><b>Power:</b> rotational power that transfers to bat speed and throwing velocity.</li>
<li><b>Speed:</b> speed work as part of every athlete's plan.</li>
</ul>
<p>Training happens in the full weight and strength area at our <a href="/facility">new facility</a>. Strength and conditioning is coached by Gabriel Aguilar, who pitched four years at UNM and ten years professionally.</p>
{coach_mini(['gabriel-aguilar'])}
{related(TRIAL_CARD, ('Pitching', 'Pitching lessons', '/pitching', 'Turn strength into velocity on the mound.'), ('Hitting', 'Hitting lessons', '/hitting', 'Turn strength into bat speed in the cage.'))}
</div></section>{band(L)}''')

add('/trackman',
  title='TrackMan Baseball Training in El Paso, TX | TX Torque',
  desc='Train with TrackMan in El Paso. Exit velocity, launch angle, pitch velocity and spin rate measured on every rep, the same technology used by MLB organizations.',
  kicker='Technology', h1_html='TrackMan training <span class="blue">in El Paso</span>',
  answer='TX Torque uses TrackMan, the same technology used by MLB organizations, to measure exit velocity, launch angle, pitch velocity and spin rate on every rep. Players and parents see real progress, and college coaches get the numbers they ask for.',
  hero_img='/assets/img/train-data.webp', hero_alt='TrackMan readout showing pitch and hit metrics',
  trail=[HOME, ('Programs', '/programs'), ('TrackMan', '/trackman')],
  schema=[service_schema('TrackMan baseball training', 'Baseball training with TrackMan measurement of exit velocity, launch angle, pitch velocity and spin rate in El Paso, TX.', '/trackman')],
  body=f'''<section><div class="wrap prose">
<h2>What we measure</h2>
<table class="t"><thead><tr><th>Metric</th><th>What it tells you</th></tr></thead><tbody>
<tr><td>Exit velocity</td><td>How hard the ball comes off the bat.</td></tr>
<tr><td>Launch angle</td><td>The flight that turns contact into damage.</td></tr>
<tr><td>Pitch velocity</td><td>Bullpen and position throws, in MPH.</td></tr>
<tr><td>Spin rate</td><td>The movement and quality of every pitch.</td></tr>
</tbody></table>
<h2>Why it matters</h2>
<p>We don't guess, we measure. Data turns training into measurable goals, shows parents real progress over time, and gives players recruiting-ready numbers for college coaches. Players in the 11 to 14 group get their first TrackMan baselines as they get ready for high school ball.</p>
<p>New to the technology? Read <a href="/guides/what-is-trackman">what TrackMan is and what it is for</a>.</p>
{related(TRIAL_CARD, ('Hitting', 'Hitting lessons', '/hitting', 'Exit velocity and launch angle on every swing.'), ('Pitching', 'Pitching lessons', '/pitching', 'Velocity and spin rate on every pitch.'))}
</div></section>{band(L)}''')

add('/softball',
  title='Softball Training in El Paso, TX: Coming Soon | TX Torque',
  desc='TX Torque is building a softball program in El Paso: clinics, coaching and development for players of every age. Join the interest list to be first in.',
  kicker='Coming soon', h1_html='Torque <span class="blue">Softball</span> is coming',
  answer='TX Torque is building a softball program in El Paso: clinics, coaching and development for players of every age, with everything we built for baseball. Join the interest list and be part of it from day one.',
  hero_img='/assets/img/train-focus.webp', hero_alt='Focused athlete at TX Torque',
  trail=[HOME, ('Programs', '/programs'), ('Softball', '/softball')], ctas=False,
  schema=[service_schema('Softball training', 'Softball clinics, coaching and development for players of every age in El Paso, TX (launching soon).', '/softball')],
  body=f'''<section><div class="wrap">
<div class="hero-grid" style="align-items:start">
<div class="prose">
<h2 style="margin-top:32px">Be part of it from the start</h2>
<p>We are working on Torque Softball right now. The same pro-led coaching, structure and data that our baseball athletes get, built for softball players.</p>
<p>This is the chance to be one of the first families in. Leave your info and we will reach out with launch dates, clinics and how to join.</p>
<p>We already ran our first softball clinic in September 2026. See <a href="/events">camps and events</a>.</p>
<p class="small muted">Launch date and schedule: <span class="pending">[PENDIENTE: fecha de lanzamiento y horarios de softball]</span></p>
</div>
<div>{lead_form(L, 'softball-interest', interest='Softball interest list', btn='Join the softball list', note='No cost. By submitting you agree to be contacted about Torque Softball.')}</div>
</div>
</div></section>''')

# ── Coaches ────────────────────────────────────────────────────────────────────
add('/coaches',
  title='Baseball Coaches in El Paso: MLB Draft Picks & Pros | TX Torque',
  desc='Meet the TX Torque coaching staff in El Paso: two MLB draft picks, El Paso Hall of Famers and pros from the U.S., Mexico and Latin America. 36+ years of pro baseball.',
  kicker='The staff', h1_html='Coached by <span class="blue">people who did it</span>',
  answer='The TX Torque staff includes two MLB draft picks, El Paso Baseball Hall of Famers and pros from the U.S., Mexico and Latin America, with more than 36 years of professional baseball combined.',
  trail=[HOME, ('Coaches', '/coaches')],
  schema=[{'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE}/coaches/{c["slug"]}', 'name': c['name']} for i, c in enumerate(COACHES)]}],
  alt={'en': '/coaches', 'es': '/es/coaches'},
  body=f'''<section><div class="wrap">
<div class="grid g3" style="margin-top:32px">{''.join(coach_card(c) for c in COACHES)}</div>
<div class="prose" style="margin-top:32px">
<p>Our coaches wore the jerseys of the New York Yankees, Atlanta Braves, Toronto Blue Jays and New York Mets organizations, the Mexican League (Toros de Tijuana, Sultanes de Monterrey, Leones de Yucatán, Algodoneros, Pericos de Puebla, Bravos de León, Indios de Juárez), Venezuelan winter ball with Tigres de Aragua, and NMSU, UNM and EPCC in college.</p>
</div>
{related(TRIAL_CARD, PROGRAMS_CARD, ('Teams', 'Teams & tryouts', '/teams-tryouts', 'Our coaches are in the dugout with players in real games.'))}
</div></section>{band(L)}''')

for c in COACHES:
    person = {'@type': 'Person', 'name': c['name'], 'jobTitle': c['job'], 'worksFor': {'@id': ORG_ID},
              'description': c['bio'], 'url': f'{SITE}/coaches/{c["slug"]}', 'knowsAbout': [c['focus'], 'Baseball']}
    if c['photo']: person['image'] = c['photo']
    if c['honors']: person['award'] = c['honors']
    if c['teams']: person['affiliation'] = [{'@type': 'SportsOrganization', 'name': t} for t in c['teams']]
    svc_name = {'/pitching': 'Pitching lessons', '/hitting': 'Hitting lessons', '/teams-tryouts': 'Teams & tryouts',
                '/strength-conditioning': 'Strength & conditioning', '/catching-fielding': 'Catching & fielding'}[c['service']]
    photo = (f'<figure><img src="{c["photo"]}" alt="{c["name"]}, {c["role"]} at TX Torque" width="600" height="750" style="aspect-ratio:4/5;object-fit:cover" fetchpriority="high" /></figure>'
             if c['photo'] else '')
    teams = ''.join(f'<li>{t}</li>' for t in c['teams'])
    honors = ''.join(f'<li>{h}</li>' for h in c['honors'])
    add(f'/coaches/{c["slug"]}',
      title=f'{c["name"]}, {c["focus"]} Coach in El Paso | TX Torque',
      desc=f'{c["name"]}: {c["badge"]}. {c["role"]} at TX Torque Baseball Academy in El Paso, TX.',
      kicker=c['badge'], h1_html=c['name'], answer=c['bio'], og_type='profile',
      image=c['photo'] or '/assets/img/wide-coaches.jpg',
      trail=[HOME, ('Coaches', '/coaches'), (c['name'], f'/coaches/{c["slug"]}')],
      schema=[person],
      body=f'''<section><div class="wrap"><div class="hero-grid" style="align-items:start">
<div class="prose">
<h2>Role at Torque</h2><p>{c["role"]}</p>
<h2>Where he played</h2><ul>{teams}</ul>
{f"<h2>Honors</h2><ul>{honors}</ul>" if honors else ""}
<h2>Train with {c["name"].split()[0]}</h2>
<p>See <a href="{c["service"]}">{svc_name.lower()}</a>, or <a href="/free-trial">book a free trial class</a> and meet the staff.</p>
</div>{photo}</div>
{related(TRIAL_CARD, ('Training', svc_name, c['service'], 'How we train it at Torque.'), COACHES_CARD)}
</div></section>{band(L)}''')

# ── Free trial ─────────────────────────────────────────────────────────────────
TRIAL_QA = [
 ('Is the first class really free?', 'Yes. Your athlete\'s first trial class is free with no deposit. Trials run Fridays and Saturdays, year-round, for all skill levels.'),
 ('When are trial classes?', 'Fridays at 4:00, 5:00 or 6:00 PM and Saturdays at 12:00, 1:00 or 2:00 PM. We confirm your exact time within 24 hours.'),
 ('What should my athlete bring?', 'Athletic clothes, turf shoes or sneakers, a glove, a bat if they have one and a water bottle. We take care of the rest.'),
 ('What ages can try it?', 'Ages 7 and up, all skill levels.'),
]
add('/free-trial',
  title='Free Baseball Trial Class in El Paso | TX Torque',
  desc='Book a free baseball trial class in El Paso. Fridays and Saturdays, year-round, ages 7+, all skill levels. No deposit, no commitment.',
  kicker='Try Torque', h1_html='Your first class <span class="blue">is free</span>',
  answer='Your athlete\'s first class at TX Torque is free, with no deposit and no commitment. Trial classes run Fridays and Saturdays, year-round, for ages 7 and up and all skill levels.',
  trail=[HOME, ('Free trial', '/free-trial')], ctas=False,
  schema=[{'@type': 'Offer', 'name': 'Free baseball trial class', 'price': '0', 'priceCurrency': 'USD', 'url': SITE + '/free-trial', 'offeredBy': {'@id': ORG_ID}}, faq_schema(TRIAL_QA)],
  alt={'en': '/free-trial', 'es': '/es/clase-gratis'},
  body=f'''<section><div class="wrap"><div class="hero-grid" style="align-items:start;margin-top:28px">
<div class="prose">
<h2 style="margin-top:0">Three steps to day one</h2>
<ol>
<li><b>Book a free trial.</b> Pick a Friday or Saturday slot. Your first class is free, no deposit.</li>
<li><b>Train with the staff.</b> Your athlete trains with our coaches in the right <a href="/programs">age group</a>.</li>
<li><b>Choose your plan.</b> Join with the <a href="/membership">membership</a> that fits your schedule and goals.</li>
</ol>
<p>Prefer to talk first? <a href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp at {PHONE_DISPLAY}</a> and a coach will get back to you.</p>
<h2>Questions</h2>{faq_html(TRIAL_QA)}
</div>
<div>{lead_form(L, 'main-landing-trial', redirect='/thank-you')}</div>
</div></div></section>''')

# ── Membership ─────────────────────────────────────────────────────────────────
TIERS = [('A', '4 lessons / month', 260, 'About 1 session a week'), ('AA', '8 lessons / month', 360, 'About 2 sessions a week'),
         ('AAA', '12 lessons / month', 440, 'About 3 sessions a week'), ('MLB', 'Unlimited', 600, 'Train as often as you want')]
money = lambda v: '${:,.0f}'.format(v)
rows = ''.join(f'<tr><td><b>{t}</b></td><td>{les}</td><td>{money(m)}</td><td>{money(m*.9)}</td><td>{money(m*.85)}</td><td>{money(m*12*.8)}</td></tr>' for t, les, m, _ in TIERS)
offers = [{'@type': 'Offer', 'name': f'Package {t} ({les})', 'price': str(m), 'priceCurrency': 'USD',
           'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': str(m), 'priceCurrency': 'USD', 'unitText': 'MONTH'}} for t, les, m, _ in TIERS]
add('/membership',
  title='Baseball Academy Membership & Prices in El Paso | TX Torque',
  desc='TX Torque membership prices in El Paso: A $260, AA $360, AAA $440 and MLB unlimited $600 per month. Save 10%, 15% or 20% with 6-month, 12-month or annual plans.',
  kicker='Membership', h1_html='Membership <span class="blue">&amp; prices</span>',
  answer='TX Torque memberships are chosen by lessons per month: A (4 lessons) $260, AA (8) $360, AAA (12) $440 and MLB unlimited $600 per month. 6-month, 12-month and annual plans save 10%, 15% and 20%.',
  trail=[HOME, ('Membership', '/membership')],
  schema=[{'@type': 'OfferCatalog', 'name': 'TX Torque memberships', 'itemListElement': offers, 'url': SITE + '/membership'}],
  alt={'en': '/membership', 'es': '/es/membresias'},
  body=f'''<section><div class="wrap prose">
<h2>Pick your level</h2>
<div class="grid g4">{''.join(f'<div class="card"><span class="tag">{les}</span><h3>Package {t}</h3><p class="price"><b>{money(m)}</b> / month</p><p>{perk}. Pro-led coaching. Train in your age group.</p></div>' for t, les, m, perk in TIERS)}</div>
<h2>Price per plan</h2>
<table class="t"><thead><tr><th>Level</th><th>Lessons</th><th>Monthly</th><th>6 months (per month, 10% off)</th><th>12 months (per month, 15% off)</th><th>Annual (paid once, 20% off)</th></tr></thead><tbody>{rows}</tbody></table>
<p>Everything is managed in the Torque app: book sessions, check your remaining classes and manage billing. <a href="{APP}" target="_blank" rel="noopener">Go to the member app</a>.</p>
<h2>Class times by age</h2>
<ul><li>Ages 7 to 10: 4:00 to 6:00 PM</li><li>Ages 11 to 14: 6:00 to 7:00 PM</li><li>Ages 14+: 7:00 to 8:00 PM</li></ul>
<p>Not sure which level fits? <a href="/free-trial">Start with a free trial</a> and a coach will help you pick.</p>
{related(TRIAL_CARD, PROGRAMS_CARD, COACHES_CARD)}
</div></section>{band(L)}''')

# ── Teams & tryouts ────────────────────────────────────────────────────────────
TRYOUT_EVENT = {'@type': 'Event', 'name': 'Torque Youth Club Team Tryouts', 'startDate': '2026-10-10T09:00:00-06:00', 'endDate': '2026-10-10T15:00:00-06:00',
    'eventStatus': 'https://schema.org/EventScheduled', 'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
    'location': {'@type': 'Place', 'name': 'Del Valle High School', 'address': {'@type': 'PostalAddress', 'addressLocality': 'El Paso', 'addressRegion': 'TX', 'addressCountry': 'US'}},
    'organizer': {'@id': ORG_ID}, 'isAccessibleForFree': True, 'description': 'Free open tryouts for the Torque Youth club teams, ages 13 and under: 9U at 9:00 AM, 11U at 11:00 AM, 12U and 13U at 1:00 PM.',
    'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD', 'url': SITE + '/teams-tryouts', 'availability': 'https://schema.org/SoldOut'}}
add('/teams-tryouts',
  title='Club Baseball Team & Tryouts in El Paso | Torque Youth',
  desc='Torque Youth is TX Torque\'s club baseball team in El Paso. See how the October 10 tryouts went and join the list to hear about the next tryouts first.',
  kicker='Torque Youth', h1_html='Club team &amp; <span class="blue">tryouts</span>',
  answer='Torque Youth is the first club team from TX Torque: players train at the facility and are coached by our staff in real games. Our first tryouts were held Saturday, October 10, 2026 at Del Valle High School. Join the list to hear about the next ones first.',
  hero_img='/assets/img/kids14_pitcheo.webp', hero_alt='TX Torque coach watching a young pitcher throw during an evaluation',
  trail=[HOME, ('Teams & tryouts', '/teams-tryouts')], ctas=False,
  schema=[TRYOUT_EVENT, {'@type': 'SportsTeam', 'name': 'Torque Youth', 'sport': 'Baseball', 'parentOrganization': {'@id': ORG_ID}}],
  body=f'''<section><div class="wrap">
<div class="prose">
<h2>Tryouts 2026: what we lived</h2>
<p>On Saturday, October 10 we held our first open tryouts for the Torque Youth club teams at Del Valle High School. It was free for every player, ages 13 and under, in three groups:</p>
<table class="t"><thead><tr><th>Group</th><th>Ages</th><th>Time</th></tr></thead><tbody>
<tr><td>9U</td><td>9 and under</td><td>9:00 AM</td></tr><tr><td>11U</td><td>10 and 11</td><td>11:00 AM</td></tr><tr><td>12U / 13U</td><td>12 and 13</td><td>1:00 PM</td></tr></tbody></table>
<p>More than 120 players registered. Thank you to every family that came out.</p>
</div>
<div class="grid g2" style="margin:20px 0">
<video controls preload="none" playsinline poster="https://res.cloudinary.com/dsprn0ew4/video/upload/so_2,w_720,q_auto,f_auto/v1790046353/Try_Outs_Torque_Recap_2_1_eldfwv.jpg" style="width:100%;border-radius:4px;background:#000" aria-label="TX Torque tryouts recap video"><source src="https://res.cloudinary.com/dsprn0ew4/video/upload/q_auto,w_720/v1790046353/Try_Outs_Torque_Recap_2_1_eldfwv.mp4" type="video/mp4" /></video>
<video controls preload="none" playsinline poster="https://res.cloudinary.com/dsprn0ew4/video/upload/so_1,w_720,q_auto,f_auto/v1790259284/Never_Train_at_Torque_fzxe62.jpg" style="width:100%;border-radius:4px;background:#000" aria-label="Never Train at Torque video"><source src="https://res.cloudinary.com/dsprn0ew4/video/upload/f_auto,q_auto,w_720/v1790259284/Never_Train_at_Torque_fzxe62.mp4" type="video/mp4" /></video>
</div>
<div class="hero-grid" style="align-items:start">
<div class="prose">
<h2 style="margin-top:12px">Why Torque Youth</h2>
<p>Most programs train kids in a cage and hope it shows up on game day. We don't. Our coaches are with your player at the facility <em>and</em> in the dugout during games.</p>
<ul>
<li><b>Coached on the field:</b> development does not stop when practice ends.</li>
<li><b>Baseball IQ:</b> because we see every rep in practice and in games, we teach the reads and decisions that separate good players from great ones.</li>
<li><b>Real feedback:</b> built on what your player actually did, not what we guess.</li>
<li><b>A real path:</b> as players get older they move into the recruiting process, the same way Torque guides our high school athletes. Tryouts are the first step.</li>
</ul>
<h2>Next tryouts</h2>
<p>New tryout dates will be announced here and on <a href="{IG}" target="_blank" rel="noopener">Instagram @tx.torque</a>. Join the list and we will let you know first.</p>
</div>
<div>{lead_form(L, 'tryout-interest', interest='Next tryouts list', btn='Tell me about the next tryouts', note='No cost. We will only contact you about Torque Youth tryouts.')}</div>
</div>
</div></section>''')

# ── Events ─────────────────────────────────────────────────────────────────────
EVENTS = [
 dict(name='Torque Youth Club Team Tryouts', date='2026-10-10', when='Saturday, October 10, 2026', where='Del Valle High School, El Paso', what='Free open tryouts, ages 13 and under, in 9U, 11U and 12U/13U groups.', link='/teams-tryouts'),
 dict(name='Softball Clinic', date='2026-09-26', when='Saturday, September 26, 2026, 3:00 to 5:00 PM', where='TX Torque, El Paso', what='Our first softball clinic, open to all ages. $50 per player.', link='/softball'),
 dict(name='Labor Day Baseball Camp', date='2026-09-07', when='Monday, September 7, 2026', where='TX Torque, El Paso', what='Holiday baseball camp for ages 4 to 7. $50 per player.', link=None),
 dict(name='Sportplex Tournament: TX Torque x Next Level Baseball', date='2026-07-24', when='July 24, 2026', where='Sportplex, El Paso, TX 79922', what='Skill competitions: Hardest Thrower (velocity ranked live) and Hardest Hit (exit velocity on every swing).', link='/tournament'),
]
ev_name = lambda e: f'<a href="{e["link"]}">{e["name"]}</a>' if e['link'] else e['name']
ev_schema = [{'@type': 'Event', 'name': e['name'], 'startDate': e['date'], 'eventStatus': 'https://schema.org/EventScheduled',
              'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode', 'description': e['what'],
              'location': {'@type': 'Place', 'name': e['where'], 'address': {'@type': 'PostalAddress', 'addressLocality': 'El Paso', 'addressRegion': 'TX', 'addressCountry': 'US'}},
              'organizer': {'@id': ORG_ID}} for e in EVENTS]
add('/events',
  title='Baseball Camps, Tournaments & Clinics in El Paso | TX Torque',
  desc='TX Torque baseball and softball events in El Paso: camps, clinics, tryouts and tournaments. See past events and how to hear about the next ones.',
  kicker='Events', h1_html='Camps, clinics &amp; <span class="blue">tournaments</span>',
  answer='TX Torque runs baseball camps, softball clinics, tryouts and tournaments in El Paso throughout the year. New events are announced on Instagram @tx.torque and in the Torque app.',
  trail=[HOME, ('Events', '/events')],
  schema=ev_schema,
  body=f'''<section><div class="wrap prose">
<h2>Recent events</h2>
<table class="t"><thead><tr><th>Event</th><th>Date</th><th>Where</th><th>What it was</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{ev_name(e)}</b></td><td>{e["when"]}</td><td>{e["where"]}</td><td>{e["what"]}</td></tr>' for e in EVENTS)}
</tbody></table>
<h2>Upcoming</h2>
<p>New camps, clinics and tryouts are announced on <a href="{IG}" target="_blank" rel="noopener">Instagram @tx.torque</a>. Members also see them in the Torque app. Want a heads up? <a href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp</a>.</p>
{related(TRIAL_CARD, ('Torque Youth', 'Teams & tryouts', '/teams-tryouts', 'Join the list for the next tryouts.'), ('Coming soon', 'Torque Softball', '/softball', 'Join the softball interest list.'))}
</div></section>{band(L)}''')

# ── Facility ───────────────────────────────────────────────────────────────────
add('/facility',
  title='Indoor Baseball Training Facility in El Paso | 2010 Bassett Ave | TX Torque',
  desc='TX Torque\'s new baseball training facility at 2010 Bassett Ave, El Paso, TX 79901: 5 batting cages, a pitching lane with mound, turf field, strength area and parent lobby.',
  kicker='Opening November 2', h1_html='Our new home: <span class="blue">2010 Bassett Ave</span>',
  answer='TX Torque trains at 2010 Bassett Ave, El Paso, TX 79901, starting Monday, November 2, 2026. The facility has 5 batting cages with machines on every lane, a pitching lane with a mound, an open turf field, a full strength area and a parent lobby.',
  hero_img='/assets/img/facility-plan.webp', hero_alt='Floor plan render of the new TX Torque facility with batting cages and turf field',
  trail=[HOME, ('Facility', '/facility')],
  schema=[org_schema(L)],
  alt={'en': '/facility', 'es': '/es/instalaciones'},
  body=f'''<section><div class="wrap prose">
<p class="small" style="margin-top:28px"><b>Moving week:</b> we are closed October 23 to November 1 while we move. Grand opening is Monday, November 2 at 2010 Bassett Ave.</p>
<h2>Twice the space, right in the heart of the city</h2>
<p>The new facility sits closer to both the East and West side, and it was built from the ground up for how we train.</p>
<div class="grid g3">
<div class="card"><span class="stat">5</span><h3>Batting cages</h3><p>Machines on every lane. <a class="link" href="/hitting">Hitting lessons</a>.</p></div>
<div class="card"><span class="stat">1</span><h3>Pitching lane</h3><p>With a pitching mound. <a class="link" href="/pitching">Pitching lessons</a>.</p></div>
<div class="card"><span class="stat">Turf</span><h3>Open field</h3><p>Defense and fielding. <a class="link" href="/catching-fielding">Catching and fielding</a>.</p></div>
<div class="card"><span class="stat">Weights</span><h3>Strength area</h3><p>Full performance area. <a class="link" href="/strength-conditioning">Strength and conditioning</a>.</p></div>
<div class="card"><span class="stat">Data</span><h3>TrackMan</h3><p>Every rep measured. <a class="link" href="/trackman">TrackMan training</a>.</p></div>
<div class="card"><span class="stat">Lobby</span><h3>Parent lobby</h3><p>Watch, wait, connect.</p></div>
</div>
<h2>Address and directions</h2>
<p><b>TX Torque Baseball Academy</b><br>2010 Bassett Ave<br>El Paso, TX 79901<br><a href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></p>
<p class="small muted">Before November 2, 2026 we trained at our previous location on N Zaragoza Rd. All training now happens at Bassett Ave.</p>
<div style="border:1px solid var(--line);border-radius:4px;overflow:hidden;margin:18px 0"><iframe title="Map to TX Torque at 2010 Bassett Ave, El Paso" src="https://www.google.com/maps?q=2010+Bassett+Ave,+El+Paso,+TX+79901&output=embed" width="100%" height="340" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<h2>Hours</h2>
<p>Class times by age: 7 to 10 from 4:00 to 6:00 PM, 11 to 14 from 6:00 to 7:00 PM, 14+ from 7:00 to 8:00 PM. Free trials on Fridays and Saturdays.</p>
<p class="small muted">Full facility hours: <span class="pending">[PENDIENTE: horario completo de la instalación y días que abre]</span></p>
{related(TRIAL_CARD, PROGRAMS_CARD, MEMBER_CARD)}
</div></section>{band(L)}''')

# ── FAQ ────────────────────────────────────────────────────────────────────────
FAQ = [
 ('Where is TX Torque located?', 'TX Torque trains at 2010 Bassett Ave, El Paso, TX 79901, starting Monday, November 2, 2026.'),
 ('Is the first class really free?', 'Yes. The first trial class is free with no deposit. Trials run Fridays and Saturdays, year-round, for all skill levels.'),
 ('What ages do you train?', 'Ages 7 and up, in three groups: 7 to 10, 11 to 14 and 14+. Each group trains at its own time so athletes work with peers at their level.'),
 ('What are the class times?', 'Ages 7 to 10 train from 4:00 to 6:00 PM, ages 11 to 14 from 6:00 to 7:00 PM, and ages 14+ from 7:00 to 8:00 PM.'),
 ('How much does TX Torque cost?', 'Monthly memberships are $260 (A, 4 lessons), $360 (AA, 8 lessons), $440 (AAA, 12 lessons) and $600 (MLB, unlimited). 6-month, 12-month and annual plans save 10%, 15% and 20%.'),
 ('How do memberships work?', 'Choose a level by lessons per month (A, AA, AAA or MLB unlimited) and pay monthly, or save with a 6-month, 12-month or annual plan. Everything is managed in the Torque app.'),
 ('Who are the coaches?', 'The staff includes two MLB draft picks, Justin Maese (3rd round, 2015) and Eudor Garcia (4th round, 2014), plus former pros Alex Reyes, Gabriel Aguilar and Angel Vega.'),
 ('Do you use TrackMan?', 'Yes. TrackMan measures exit velocity, launch angle, pitch velocity and spin rate on every rep.'),
 ('Do you offer pitching lessons?', 'Yes. Pitching is led by Justin Maese, a 3rd round pick in the 2015 MLB Draft who pitched in the Yankees, Braves and Blue Jays organizations. Pitchers train on a dedicated lane with a mound.'),
 ('Do you offer catching lessons?', 'Yes. Angel Vega, a former college and Mexican League catcher, runs specialized catching coaching once a week.'),
 ('Do you have softball?', 'Torque Softball is coming soon, with clinics, coaching and development for players of every age. Join the interest list on the softball page.'),
 ('Do you have a club team?', 'Yes. Torque Youth is our club team. Players train at the facility and are coached by our staff in real games.'),
 ('Do you help with college recruiting?', 'Yes. Our staff has real college and pro connections, runs exposure events and guides families through the recruiting process. TrackMan numbers give college coaches the data they ask for.'),
 ('What should my athlete bring?', 'Athletic clothes, turf shoes or sneakers, a glove, a bat if they have one and a water bottle.'),
 ('How do I contact TX Torque?', 'Message us on WhatsApp at +1 915-474-0940 or on Instagram @tx.torque.'),
]
add('/faq',
  title='Baseball Academy FAQ: Prices, Ages, Location | TX Torque El Paso',
  desc='Answers about TX Torque in El Paso: location, free trial, ages, class times, prices, coaches, TrackMan, softball, club team and recruiting.',
  kicker='For parents', h1_html='Questions, <span class="blue">answered</span>',
  answer='TX Torque is a pro-led baseball academy at 2010 Bassett Ave in El Paso for ages 7 and up. The first class is free, and memberships start at $260 a month.',
  trail=[HOME, ('FAQ', '/faq')],
  schema=[faq_schema(FAQ)],
  alt={'en': '/faq', 'es': '/es/preguntas-frecuentes'},
  body=f'''<section><div class="wrap narrow" style="margin-top:20px">{faq_html(FAQ)}
<p class="muted" style="margin-top:24px">Still have a question? <a class="link" href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp</a> and a coach will get back to you.</p></div></section>{band(L)}''')

# ── 404 ────────────────────────────────────────────────────────────────────────
NOT_FOUND = page(lang=L, path='/404', title='Page not found | TX Torque Baseball Academy', desc='This page does not exist. Find programs, coaches, prices and the free trial class at TX Torque in El Paso.',
  kicker='404', h1_html='This page is <span class="blue">out</span>', answer='That page does not exist or moved. Here is where to go instead.',
  trail=[HOME, ('Not found', '/404')], ctas=False,
  body=f'''<section><div class="wrap">{related(TRIAL_CARD, PROGRAMS_CARD, COACHES_CARD)}{related(MEMBER_CARD, ('Location', 'Facility', '/facility', '2010 Bassett Ave, El Paso, TX 79901.'), ('Help', 'FAQ', '/faq', 'Answers for parents.'))}
<p style="margin-top:24px"><a class="btn btn-ghost" href="/">Back to home</a> <a class="btn btn-ghost" href="/es">Inicio en español</a></p></div></section>''')
NOT_FOUND = NOT_FOUND.replace('<link rel="canonical" href="https://torquebaseball.us/404" />', '<meta name="robots" content="noindex" />')
