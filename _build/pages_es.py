from lib import *
from pages_en import COACHES, TIERS, money

L = 'es'
INICIO = ('Inicio', '/es')
PAGES = []
def add(path, **kw):
    PAGES.append((path, page(lang=L, path=path, **kw)))

def related(*links):
    return '<div class="grid g3" style="margin-top:18px">' + ''.join(
        f'<a class="card" href="{u}"><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p></a>' for tag, t, u, d in links) + '</div>'

def svc(name, desc, path):
    return {'@type': 'Service', 'name': name, 'serviceType': name, 'description': desc, 'url': SITE + path, 'inLanguage': 'es',
            'provider': {'@id': ORG_ID}, 'areaServed': {'@type': 'City', 'name': 'El Paso, Texas'}}

GRATIS = ('Siguiente paso', 'Agenda tu clase gratis', '/es/clase-gratis', 'Viernes y sábados. Sin depósito y sin compromiso.')
PROGS = ('Desde 7 años', 'Programas por edad', '/es/programas', 'Tres grupos de edad, cada uno a su hora.')
MEMB = ('Desde $260 al mes', 'Membresías y precios', '/es/membresias', 'A, AA, AAA o MLB ilimitado. Ahorra hasta 20%.')
COACH = ('El staff', 'Conoce a los coaches', '/es/coaches', 'Draft picks de MLB y profesionales de EE. UU., México y Latinoamérica.')

ROLES_ES = {
 'justin-maese': ('Director de operaciones · Pitcheo', '3a ronda, Draft MLB 2015',
   'Justin Maese fue seleccionado en la 3a ronda del Draft de MLB 2015 y jugó nueve años como profesional en las organizaciones de los Yankees de Nueva York, los Bravos de Atlanta y los Azulejos de Toronto. Está en el Salón de la Fama del Béisbol de El Paso desde 2015. En Torque dirige la operación de entrenamiento y el programa de pitcheo.'),
 'eudor-garcia': ('Director de fildeo y bateo', '4a ronda, Draft MLB 2014',
   'Eudor Garcia fue Jugador del Año NJCAA con El Paso Community College y elegido en la 4a ronda del Draft de MLB 2014. Jugó doce años como profesional, desde la organización de los Mets de Nueva York hasta la Liga Mexicana con Toros de Tijuana, Algodoneros e Indios de Juárez. Está en el Salón de la Fama del Béisbol de El Paso desde 2014. En Torque dirige el bateo y la defensa.'),
 'alex-reyes': ('Director de eventos y reclutamiento', 'Universitario two-way · 5 años pro',
   'Alex Reyes jugó cuatro años de béisbol universitario como two-way en New Mexico State y cinco temporadas profesionales en México, Venezuela y Colombia, con Bravos de León, Tigres de Aragua y Venados de Mazatlán. En Torque dirige eventos y reclutamiento, y guía a las familias en el proceso para llegar al béisbol universitario.'),
 'gabriel-aguilar': ('Operación de equipos · Pitcheo · Fuerza', '10 años de pitcheo pro',
   'Gabriel Aguilar lanzó cuatro años en la Universidad de Nuevo México y una década como profesional, con Sultanes de Monterrey, Leones de Yucatán y Rieleros. En Torque lleva la operación de equipos y entrena pitcheo, fuerza y acondicionamiento.'),
 'angel-vega': ('Especialista en catcher y bateo', 'ABCA/Rawlings All-Region First Team',
   "Angel Vega fue catcher universitario en St. Mary's y San Jacinto, nombrado ABCA/Rawlings All-Region First Team, y catcher en la Liga Mexicana con Algodoneros y Pericos de Puebla. En Torque da entrenamiento especializado de catcher una sesión por semana y también trabaja con bateadores."),
}

def coach_card_es(c):
    role, badge, _ = ROLES_ES[c['slug']]
    ph = f'<img src="{c["photo"]}" alt="{c["name"]}, {role} en TX Torque" width="600" height="600" loading="lazy" />' if c['photo'] else ''
    return f'<a class="card" href="/coaches/{c["slug"]}" hreflang="en">{ph}<span class="tag">{badge}</span><h3>{c["name"]}</h3><p>{role}</p></a>'

# ── Inicio ────────────────────────────────────────────────────────────────────
FAQ_HOME = [
 ('¿Dónde está TX Torque?', 'En 2010 Bassett Ave, El Paso, TX 79901, a partir del lunes 2 de noviembre de 2026.'),
 ('¿La primera clase es gratis?', 'Sí. La primera clase de prueba es gratis y sin depósito. Viernes y sábados, todo el año, para todos los niveles.'),
 ('¿Desde qué edad?', 'Desde 7 años, en tres grupos: 7 a 10, 11 a 14 y 14 en adelante.'),
 ('¿Cuánto cuesta?', 'Membresías mensuales de $260 (A, 4 clases), $360 (AA, 8 clases), $440 (AAA, 12 clases) y $600 (MLB, ilimitado).'),
]
add('/es',
  title='Academia de Béisbol en El Paso, TX | TX Torque, Built by Pros',
  desc='Clases de béisbol en El Paso con exjugadores profesionales y draft picks de MLB. Datos de TrackMan en cada repetición. Desde 7 años. Tu primera clase es gratis.',
  kicker='El Paso, TX · Academia de béisbol y softball', h1_html='Clases de béisbol en El Paso, <span class="blue">hechas por pros</span>',
  answer='TX Torque es una academia de béisbol en El Paso dirigida por exjugadores profesionales, con dos draft picks de MLB en el staff y TrackMan en cada repetición. Entrenamos desde los 7 años y la primera clase es gratis.',
  hero_img='/assets/img/staff18_coach.webp', hero_alt='Coach de TX Torque dando indicaciones a un jugador en el campo',
  trail=[INICIO], schema=[org_schema(L), faq_schema(FAQ_HOME)], alt={'en': '/', 'es': '/es'},
  body=f'''<section><div class="wrap prose">
<div class="grid g4" style="margin-top:32px">
<div class="card"><span class="stat">2</span><p>Draft picks de MLB en el staff</p></div>
<div class="card"><span class="stat">36+</span><p>Años de béisbol profesional</p></div>
<div class="card"><span class="stat">500+</span><p>Atletas entrenados</p></div>
<div class="card"><span class="stat">TrackMan</span><p>Cada repetición medida</p></div>
</div>
<h2>Lo jugamos al más alto nivel. Ahora lo traemos a casa.</h2>
<p>Torque lo fundaron jugadores de El Paso que vivieron el béisbol profesional: el día del draft, los viajes en autobús de ligas menores y el béisbol invernal en México y Venezuela. Regresamos para subir el nivel de los niños que vienen detrás de nosotros.</p>
<h2>El Método Torque</h2>
<div class="grid g4">
<div class="card"><span class="tag">01</span><h3>Fuerza</h3><p>Fuerza y acondicionamiento según la edad para un cuerpo atlético y resistente.</p></div>
<div class="card"><span class="tag">02</span><h3>Potencia</h3><p>Potencia rotacional y velocidad que se convierten en velocidad de bate y de lanzamiento.</p></div>
<div class="card"><span class="tag">03</span><h3>Swing</h3><p>Mecánica de bateo, pitcheo y fildeo enseñada por coaches que jugaron como profesionales.</p></div>
<div class="card"><span class="tag">04</span><h3>Datos</h3><p>Números de TrackMan en cada repetición: el progreso se mide, no se adivina.</p></div>
</div>
<h2>Entrenamiento</h2>
{related(('Bateo', 'Clases de bateo', '/es/clases-de-bateo', 'Velocidad de salida y ángulo en cada swing.'), ('Pitcheo', 'Clases de pitcheo', '/es/clases-de-pitcheo', 'Con un draft pick de MLB 2015.'), PROGS)}
<h2>Nueva casa: 2010 Bassett Ave</h2>
<p>Desde el lunes 2 de noviembre entrenamos en nuestra nueva instalación, con el doble de espacio y más cerca del lado Este y del lado Oeste. <a href="/es/instalaciones">Conoce las instalaciones</a>.</p>
<h2>Preguntas rápidas</h2>{faq_html(FAQ_HOME)}
<p><a class="link" href="/es/preguntas-frecuentes">Ver todas las preguntas</a></p>
{related(GRATIS, MEMB, COACH)}
</div></section>{band(L)}''')

# ── Programas ─────────────────────────────────────────────────────────────────
add('/es/programas',
  title='Clases de Béisbol por Edad en El Paso: 7 a 10, 11 a 14 y 14+ | TX Torque',
  desc='Clases de béisbol para niños y jóvenes en El Paso por grupo de edad: 7 a 10, 11 a 14 y 14 en adelante. Coaches profesionales y TrackMan.',
  kicker='Programas', h1_html='Clases de béisbol <span class="blue">por edad</span>',
  answer='En TX Torque entrenamos desde los 7 años en tres grupos: 7 a 10 años (4:00 a 6:00 PM), 11 a 14 años (6:00 a 7:00 PM) y 14 en adelante (7:00 a 8:00 PM). Cada atleta entrena con jugadores de su nivel.',
  hero_img='/assets/img/kids56_grupo.webp', hero_alt='Grupo de jugadores jóvenes de TX Torque escuchando a un coach',
  trail=[INICIO, ('Programas', '/es/programas')],
  schema=[svc('Clases de béisbol por grupo de edad', 'Clases de béisbol para 7 a 10, 11 a 14 y 14+ años en El Paso, TX.', '/es/programas')],
  alt={'en': '/programs', 'es': '/es/programas'},
  body=f'''<section><div class="wrap prose">
<h2>Tres grupos, un solo sistema</h2>
<div class="grid g3">
<div class="card"><span class="tag">Grupo 01 · 4:00 a 6:00 PM</span><h3>7 a 10 años</h3><p>Bases bien hechas: lanzar, atrapar, fundamentos de bateo y movimiento atlético, en un ambiente divertido y con energía.</p></div>
<div class="card"><span class="tag">Grupo 02 · 6:00 a 7:00 PM</span><h3>11 a 14 años</h3><p>Mecánica más fina, más fuerza y sus primeras mediciones de TrackMan rumbo al béisbol de high school.</p></div>
<div class="card"><span class="tag">Grupo 03 · 7:00 a 8:00 PM</span><h3>14 años en adelante</h3><p>Desarrollo avanzado con entrenamiento de nivel profesional, datos y disciplina para quienes buscan el siguiente nivel.</p></div>
</div>
<h2>Qué incluye cada sesión</h2>
<ul><li><b>Fuerza</b> según la edad.</li><li><b>Potencia</b> rotacional y velocidad.</li><li><b>Mecánica</b> de <a href="/es/clases-de-bateo">bateo</a>, <a href="/es/clases-de-pitcheo">pitcheo</a> y fildeo.</li><li><b>Datos</b> de TrackMan en cada repetición.</li></ul>
<p>Los jugadores que quieren juegos pueden formar parte de Torque Youth, nuestro equipo de club. <a href="/teams-tryouts" hreflang="en">Equipos y tryouts (en inglés)</a>.</p>
{related(GRATIS, MEMB, COACH)}
</div></section>{band(L)}''')

# ── Bateo / Pitcheo ───────────────────────────────────────────────────────────
add('/es/clases-de-bateo',
  title='Clases de Bateo en El Paso, TX | TX Torque',
  desc='Clases de bateo de béisbol en El Paso con un exdraft pick de MLB. Mecánica, potencia y TrackMan: velocidad de salida y ángulo de lanzamiento en cada swing.',
  kicker='Entrenamiento', h1_html='Clases de bateo <span class="blue">en El Paso</span>',
  answer='En TX Torque el bateo lo dirige Eudor Garcia, elegido en la 4a ronda del Draft de MLB 2014, con doce años como profesional. Cada swing se mide con TrackMan: velocidad de salida y ángulo de lanzamiento.',
  hero_img='/assets/img/kids26_bateo.webp', hero_alt='Bateador joven haciendo swing en una jaula de bateo de TX Torque',
  trail=[INICIO, ('Programas', '/es/programas'), ('Bateo', '/es/clases-de-bateo')],
  schema=[svc('Clases de bateo de béisbol', 'Instrucción de bateo con medición de TrackMan en El Paso, TX.', '/es/clases-de-bateo')],
  alt={'en': '/hitting', 'es': '/es/clases-de-bateo'},
  body=f'''<section><div class="wrap prose">
<h2>Cómo entrenamos a los bateadores</h2>
<ul>
<li><b>Mecánica:</b> trabajo de swing con coaches que batearon como profesionales en EE. UU. y México.</li>
<li><b>Potencia:</b> potencia rotacional y velocidad que se convierten en velocidad de bate.</li>
<li><b>Datos:</b> TrackMan mide la velocidad de salida (qué tan fuerte sale la bola del bat) y el ángulo de lanzamiento en cada swing.</li>
<li><b>Repeticiones:</b> cinco jaulas de bateo con máquina en cada carril en nuestra <a href="/es/instalaciones">nueva instalación</a>.</li>
</ul>
<h2>Quién entrena bateo</h2>
<div class="grid g3">{''.join(coach_card_es(c) for c in COACHES if c['slug'] in ('eudor-garcia', 'angel-vega'))}</div>
{related(GRATIS, PROGS, MEMB)}
</div></section>{band(L)}''')

add('/es/clases-de-pitcheo',
  title='Clases de Pitcheo en El Paso, TX | TX Torque',
  desc='Clases de pitcheo en El Paso con un draft pick de MLB 2015. Mecánica, velocidad y cuidado del brazo, con TrackMan: velocidad y spin en cada lanzamiento.',
  kicker='Entrenamiento', h1_html='Clases de pitcheo <span class="blue">en El Paso</span>',
  answer='El programa de pitcheo de TX Torque lo dirige Justin Maese, elegido en la 3a ronda del Draft de MLB 2015, con nueve años como profesional. Los pitchers entrenan en un carril con montículo y TrackMan mide velocidad y spin en cada lanzamiento.',
  hero_img='/assets/img/kids2_pitcheo.webp', hero_alt='Pitcher joven de TX Torque lanzando en el campo',
  trail=[INICIO, ('Programas', '/es/programas'), ('Pitcheo', '/es/clases-de-pitcheo')],
  schema=[svc('Clases de pitcheo de béisbol', 'Instrucción de pitcheo con medición de TrackMan en El Paso, TX.', '/es/clases-de-pitcheo')],
  alt={'en': '/pitching', 'es': '/es/clases-de-pitcheo'},
  body=f'''<section><div class="wrap prose">
<h2>Cómo entrenamos a los pitchers</h2>
<ul>
<li><b>Mecánica:</b> trabajo de entrega con coaches que lanzaron en las organizaciones de Yankees, Bravos y Azulejos, y en la Liga Mexicana.</li>
<li><b>Fuerza y potencia:</b> fuerza según la edad y potencia rotacional que se convierte en velocidad.</li>
<li><b>Datos:</b> TrackMan mide la velocidad en millas por hora y el spin rate de cada lanzamiento.</li>
<li><b>Espacio:</b> carril de pitcheo con montículo en nuestra <a href="/es/instalaciones">nueva instalación</a>.</li>
</ul>
<h2>Quién entrena pitcheo</h2>
<div class="grid g3">{''.join(coach_card_es(c) for c in COACHES if c['slug'] in ('justin-maese', 'gabriel-aguilar'))}</div>
<p>¿Quieres saber más? Lee (en inglés) <a href="/guides/increase-pitching-velocity" hreflang="en">cómo subir la velocidad de pitcheo</a> y <a href="/guides/what-age-start-pitching-lessons" hreflang="en">a qué edad empezar clases de pitcheo</a>.</p>
{related(GRATIS, PROGS, MEMB)}
</div></section>{band(L)}''')

# ── Coaches ───────────────────────────────────────────────────────────────────
bios = ''.join(f'<h3>{c["name"]}</h3><p>{ROLES_ES[c["slug"]][2]}</p>' for c in COACHES)
add('/es/coaches',
  title='Coaches de Béisbol en El Paso: Draft Picks de MLB y Profesionales | TX Torque',
  desc='Conoce a los coaches de TX Torque en El Paso: dos draft picks de MLB, miembros del Salón de la Fama de El Paso y profesionales de México y Latinoamérica.',
  kicker='El staff', h1_html='Te entrena gente <span class="blue">que lo vivió</span>',
  answer='El staff de TX Torque incluye dos draft picks de MLB, miembros del Salón de la Fama del Béisbol de El Paso y profesionales de EE. UU., México y Latinoamérica, con más de 36 años de béisbol profesional en conjunto.',
  trail=[INICIO, ('Coaches', '/es/coaches')], alt={'en': '/coaches', 'es': '/es/coaches'},
  body=f'''<section><div class="wrap">
<div class="grid g3" style="margin-top:32px">{''.join(coach_card_es(c) for c in COACHES)}</div>
<div class="prose narrow" style="margin-top:20px"><h2>Trayectoria</h2>{bios}</div>
{related(GRATIS, PROGS, MEMB)}
</div></section>{band(L)}''')

# ── Clase gratis ──────────────────────────────────────────────────────────────
QA_GRATIS = [
 ('¿De verdad la primera clase es gratis?', 'Sí. La primera clase de prueba es gratis y sin depósito. Viernes y sábados, todo el año, para todos los niveles.'),
 ('¿Qué horarios hay?', 'Viernes a las 4:00, 5:00 o 6:00 PM y sábados a las 12:00, 1:00 o 2:00 PM. Te confirmamos la hora en menos de 24 horas.'),
 ('¿Qué debe traer mi hijo?', 'Ropa deportiva, tenis o zapatos de turf, guante, bat si tiene y una botella de agua. Nosotros ponemos lo demás.'),
 ('¿Desde qué edad?', 'Desde 7 años y para todos los niveles.'),
]
add('/es/clase-gratis',
  title='Clase de Béisbol Gratis en El Paso | TX Torque',
  desc='Agenda una clase de prueba de béisbol gratis en El Paso. Viernes y sábados, todo el año, desde 7 años y todos los niveles. Sin depósito y sin compromiso.',
  kicker='Prueba Torque', h1_html='Tu primera clase <span class="blue">es gratis</span>',
  answer='La primera clase en TX Torque es gratis, sin depósito y sin compromiso. Las clases de prueba son viernes y sábados, todo el año, desde 7 años y para todos los niveles.',
  trail=[INICIO, ('Clase gratis', '/es/clase-gratis')], ctas=False,
  schema=[{'@type': 'Offer', 'name': 'Clase de prueba de béisbol gratis', 'price': '0', 'priceCurrency': 'USD', 'url': SITE + '/es/clase-gratis', 'offeredBy': {'@id': ORG_ID}}, faq_schema(QA_GRATIS)],
  alt={'en': '/free-trial', 'es': '/es/clase-gratis'},
  body=f'''<section><div class="wrap"><div class="hero-grid" style="align-items:start;margin-top:28px">
<div class="prose">
<h2 style="margin-top:0">Tres pasos para empezar</h2>
<ol><li><b>Agenda tu clase gratis.</b> Elige un horario de viernes o sábado.</li><li><b>Entrena con el staff</b> en el <a href="/es/programas">grupo de su edad</a>.</li><li><b>Elige tu plan</b> con la <a href="/es/membresias">membresía</a> que te quede.</li></ol>
<p>¿Prefieres hablar primero? <a href="{WA}" target="_blank" rel="noopener">Escríbenos por WhatsApp al {PHONE_DISPLAY}</a>.</p>
<h2>Preguntas</h2>{faq_html(QA_GRATIS)}
</div>
<div>{lead_form(L, 'es-landing-trial', redirect='/thank-you')}</div>
</div></div></section>''')

# ── Membresías ────────────────────────────────────────────────────────────────
LES = {'4 lessons / month': '4 clases al mes', '8 lessons / month': '8 clases al mes', '12 lessons / month': '12 clases al mes', 'Unlimited': 'Ilimitado'}
rows = ''.join(f'<tr><td><b>{t}</b></td><td>{LES[les]}</td><td>{money(m)}</td><td>{money(m*.9)}</td><td>{money(m*.85)}</td><td>{money(m*12*.8)}</td></tr>' for t, les, m, _ in TIERS)
add('/es/membresias',
  title='Membresías y Precios de Clases de Béisbol en El Paso | TX Torque',
  desc='Precios de TX Torque en El Paso: A $260, AA $360, AAA $440 y MLB ilimitado $600 al mes. Ahorra 10%, 15% o 20% con planes de 6 meses, 12 meses o anual.',
  kicker='Membresías', h1_html='Membresías <span class="blue">y precios</span>',
  answer='Las membresías de TX Torque se eligen por clases al mes: A (4 clases) $260, AA (8) $360, AAA (12) $440 y MLB ilimitado $600 al mes. Los planes de 6 meses, 12 meses y anual ahorran 10%, 15% y 20%.',
  trail=[INICIO, ('Membresías', '/es/membresias')], alt={'en': '/membership', 'es': '/es/membresias'},
  body=f'''<section><div class="wrap prose">
<h2>Precio por plan</h2>
<table class="t"><thead><tr><th>Nivel</th><th>Clases</th><th>Mensual</th><th>6 meses (al mes, 10% menos)</th><th>12 meses (al mes, 15% menos)</th><th>Anual (pago único, 20% menos)</th></tr></thead><tbody>{rows}</tbody></table>
<p>Todo se maneja en la app de Torque: reservar clases, ver cuántas te quedan y tus pagos. <a href="{APP}" target="_blank" rel="noopener">Ir a la app</a>.</p>
<h2>Horarios por edad</h2>
<ul><li>7 a 10 años: 4:00 a 6:00 PM</li><li>11 a 14 años: 6:00 a 7:00 PM</li><li>14 en adelante: 7:00 a 8:00 PM</li></ul>
<p>¿No sabes cuál elegir? <a href="/es/clase-gratis">Empieza con una clase gratis</a> y un coach te ayuda.</p>
{related(GRATIS, PROGS, COACH)}
</div></section>{band(L)}''')

# ── Instalaciones ─────────────────────────────────────────────────────────────
add('/es/instalaciones',
  title='Instalaciones de Béisbol en El Paso | 2010 Bassett Ave | TX Torque',
  desc='La nueva instalación de TX Torque en 2010 Bassett Ave, El Paso, TX 79901: 5 jaulas de bateo, carril de pitcheo con montículo, campo de turf, área de fuerza y lobby.',
  kicker='Apertura 2 de noviembre', h1_html='Nueva casa: <span class="blue">2010 Bassett Ave</span>',
  answer='TX Torque entrena en 2010 Bassett Ave, El Paso, TX 79901, a partir del lunes 2 de noviembre de 2026. Tiene 5 jaulas de bateo con máquina en cada carril, carril de pitcheo con montículo, campo de turf, área de fuerza y lobby para papás.',
  hero_img='/assets/img/facility-plan.webp', hero_alt='Plano de la nueva instalación de TX Torque con jaulas de bateo y campo de turf',
  trail=[INICIO, ('Instalaciones', '/es/instalaciones')], schema=[org_schema(L)], alt={'en': '/facility', 'es': '/es/instalaciones'},
  body=f'''<section><div class="wrap prose">
<p class="small" style="margin-top:28px"><b>Semana de mudanza:</b> cerramos del 23 de octubre al 1 de noviembre. Gran apertura el lunes 2 de noviembre en 2010 Bassett Ave.</p>
<h2>El doble de espacio, en el corazón de la ciudad</h2>
<p>La nueva instalación queda más cerca del lado Este y del lado Oeste, y se construyó desde cero para la forma en que entrenamos.</p>
<div class="grid g3">
<div class="card"><span class="stat">5</span><h3>Jaulas de bateo</h3><p>Máquina en cada carril.</p></div>
<div class="card"><span class="stat">1</span><h3>Carril de pitcheo</h3><p>Con montículo.</p></div>
<div class="card"><span class="stat">Turf</span><h3>Campo abierto</h3><p>Defensa y fildeo.</p></div>
<div class="card"><span class="stat">Pesas</span><h3>Área de fuerza</h3><p>Área completa de rendimiento.</p></div>
<div class="card"><span class="stat">Datos</span><h3>TrackMan</h3><p>Cada repetición medida.</p></div>
<div class="card"><span class="stat">Lobby</span><h3>Lobby para papás</h3><p>Ver, esperar y convivir.</p></div>
</div>
<h2>Dirección</h2>
<p><b>TX Torque Baseball Academy</b><br>2010 Bassett Ave<br>El Paso, TX 79901<br><a href="{MAPS}" target="_blank" rel="noopener">Abrir en Google Maps</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></p>
<p class="small muted">Antes del 2 de noviembre de 2026 entrenábamos en N Zaragoza Rd. Ahora todo el entrenamiento es en Bassett Ave.</p>
<div style="border:1px solid var(--line);border-radius:4px;overflow:hidden;margin:18px 0"><iframe title="Mapa a TX Torque en 2010 Bassett Ave, El Paso" src="https://www.google.com/maps?q=2010+Bassett+Ave,+El+Paso,+TX+79901&output=embed" width="100%" height="340" style="border:0;display:block" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<h2>Horarios</h2>
<p>Clases por edad: 7 a 10 de 4:00 a 6:00 PM, 11 a 14 de 6:00 a 7:00 PM, 14 en adelante de 7:00 a 8:00 PM. Clases de prueba gratis viernes y sábados.</p>
<p class="small muted">Horario completo de la instalación: <span class="pending">[PENDIENTE: horario completo y días que abre]</span></p>
{related(GRATIS, PROGS, MEMB)}
</div></section>{band(L)}''')

# ── Preguntas frecuentes ──────────────────────────────────────────────────────
FAQ = [
 ('¿Dónde está TX Torque?', 'En 2010 Bassett Ave, El Paso, TX 79901, a partir del lunes 2 de noviembre de 2026.'),
 ('¿La primera clase es gratis?', 'Sí. La primera clase de prueba es gratis y sin depósito. Viernes y sábados, todo el año, para todos los niveles.'),
 ('¿Desde qué edad entrenan?', 'Desde 7 años, en tres grupos: 7 a 10, 11 a 14 y 14 en adelante. Cada grupo entrena a su hora para estar con jugadores de su nivel.'),
 ('¿Qué horarios tienen?', '7 a 10 años de 4:00 a 6:00 PM, 11 a 14 de 6:00 a 7:00 PM y 14 en adelante de 7:00 a 8:00 PM.'),
 ('¿Cuánto cuestan las clases?', 'Membresías mensuales de $260 (A, 4 clases), $360 (AA, 8 clases), $440 (AAA, 12 clases) y $600 (MLB, ilimitado). Los planes de 6 meses, 12 meses y anual ahorran 10%, 15% y 20%.'),
 ('¿Cómo funcionan las membresías?', 'Eliges un nivel por clases al mes y pagas mensual, o ahorras con un plan de 6 meses, 12 meses o anual. Todo se maneja en la app de Torque.'),
 ('¿Quiénes son los coaches?', 'El staff incluye dos draft picks de MLB, Justin Maese (3a ronda, 2015) y Eudor Garcia (4a ronda, 2014), y los exprofesionales Alex Reyes, Gabriel Aguilar y Angel Vega.'),
 ('¿Usan TrackMan?', 'Sí. TrackMan mide velocidad de salida, ángulo de lanzamiento, velocidad de pitcheo y spin rate en cada repetición.'),
 ('¿Tienen clases de catcher?', 'Sí. Angel Vega, excatcher universitario y de Liga Mexicana, da entrenamiento especializado de catcher una vez por semana.'),
 ('¿Tienen softball?', 'Torque Softball viene pronto, con clínicas, coaching y desarrollo para todas las edades. Puedes apuntarte en la página de softball.'),
 ('¿Tienen equipo?', 'Sí. Torque Youth es nuestro equipo de club. Los jugadores entrenan en la instalación y nuestros coaches los dirigen en juegos reales.'),
 ('¿Ayudan con becas y reclutamiento universitario?', 'Sí. Nuestro staff tiene conexiones reales con universidades y béisbol profesional, organiza eventos de exposición y guía a las familias en el proceso. Los números de TrackMan dan a los coaches universitarios los datos que piden.'),
 ('¿Qué debe traer mi hijo?', 'Ropa deportiva, tenis o zapatos de turf, guante, bat si tiene y una botella de agua.'),
 ('¿Cómo los contacto?', 'Por WhatsApp al +1 915-474-0940 o en Instagram @tx.torque.'),
]
add('/es/preguntas-frecuentes',
  title='Preguntas Frecuentes: Precios, Edades y Ubicación | TX Torque El Paso',
  desc='Respuestas sobre TX Torque en El Paso: ubicación, clase gratis, edades, horarios, precios, coaches, TrackMan, softball, equipo y reclutamiento.',
  kicker='Para papás', h1_html='Preguntas <span class="blue">frecuentes</span>',
  answer='TX Torque es una academia de béisbol dirigida por profesionales en 2010 Bassett Ave, El Paso, desde 7 años. La primera clase es gratis y las membresías empiezan en $260 al mes.',
  trail=[INICIO, ('Preguntas frecuentes', '/es/preguntas-frecuentes')], schema=[faq_schema(FAQ)], alt={'en': '/faq', 'es': '/es/preguntas-frecuentes'},
  body=f'''<section><div class="wrap narrow" style="margin-top:20px">{faq_html(FAQ)}
<p class="muted" style="margin-top:24px">¿Tienes otra pregunta? <a class="link" href="{WA}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a> y un coach te contesta.</p></div></section>{band(L)}''')
