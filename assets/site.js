// TX Torque shared behavior for content pages: mobile menu + lead forms.
(function () {
  var burger = document.getElementById('burger'), mnav = document.getElementById('mnav'), close = document.getElementById('mnav-close');
  if (burger && mnav) {
    burger.addEventListener('click', function () { mnav.classList.add('open'); burger.setAttribute('aria-expanded', 'true'); });
    close && close.addEventListener('click', function () { mnav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); });
  }
  var y = document.getElementById('footer-year'); if (y) y.textContent = new Date().getFullYear();

  // Lead forms post to the same places as the home trial form: the Google Apps Script
  // (sheet + email) and the Torque app's lead endpoint. data-source picks the lead source.
  var LEAD_ENDPOINT = 'https://script.google.com/macros/s/AKfycbzetU-RRWEOlavyO3ufeAAFCOCt_NXnHuwQ_chzs8_imkZGD8yld6IK1IhAL87Z78ip/exec';
  document.querySelectorAll('form[data-lead]').forEach(function (form) {
    var es = document.documentElement.lang === 'es';
    var btn = form.querySelector('button[type=submit]'), err = form.querySelector('.err'), ok = form.querySelector('.ok');
    var label = btn ? btn.textContent : '';
    form.addEventListener('submit', async function (e) {
      e.preventDefault(); err.style.display = 'none';
      var f = form.elements;
      var payload = {
        parentName: f.parentName.value.trim(), phone: f.phone.value.trim(), email: f.email.value.trim(),
        playerName: f.playerName.value.trim(), playerAge: f.playerAge.value.trim(),
        preferredDay: f.preferredDay ? f.preferredDay.value : '',
        timestamp: new Date().toISOString(), source: form.dataset.source, status: form.dataset.status || 'new'
      };
      if (!payload.parentName || !payload.phone || !payload.email || !payload.playerName || !payload.playerAge || (f.preferredDay && !payload.preferredDay)) {
        err.textContent = es ? 'Llena todos los campos, por favor.' : 'Please fill out all fields before submitting.'; err.style.display = 'block'; return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)) {
        err.textContent = es ? 'Escribe un correo válido.' : 'Please enter a valid email address.'; err.style.display = 'block'; return;
      }
      btn.disabled = true; btn.textContent = es ? 'Enviando...' : 'Sending...';
      try {
        await fetch(LEAD_ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(payload) });
        fetch('https://app.torquebaseball.us/api/create-lead', { method: 'POST', headers: { 'Content-Type': 'application/json' }, keepalive: true,
          body: JSON.stringify(Object.assign({}, payload, { company: f.company ? f.company.value : '' })) }).catch(function () {});
        if (window.fbq) fbq('track', 'Lead');
        if (form.dataset.redirect) { window.location.href = form.dataset.redirect; return; }
        form.reset(); btn.textContent = label; btn.disabled = false; ok.style.display = 'block';
      } catch (x) {
        err.textContent = es ? 'Algo falló. Intenta otra vez o escríbenos por WhatsApp.' : 'Something went wrong. Please try again or message us on WhatsApp.';
        err.style.display = 'block'; btn.disabled = false; btn.textContent = label;
      }
    });
  });
})();
