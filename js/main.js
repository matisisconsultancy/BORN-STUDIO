/* ==========================================================================
   BORN STUDIO — interacciones
   Ligero, sin dependencias. Movimiento discreto, editorial, con propósito.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- Año dinámico ----------------------------------------------------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---- Hero: master claim ---------------------------------------------- */
  var claim = document.querySelector('.claim');
  if (claim) {
    // Rueda en el siguiente frame para garantizar la transición de entrada.
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { claim.classList.add('is-in'); });
    });
  }

  /* ---- Reveal on scroll ------------------------------------------------- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));

  // Índice para escalonar los chips de tono.
  document.querySelectorAll('.voice__tags .reveal').forEach(function (el, i) {
    el.style.setProperty('--i', i);
  });

  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Progress thread -------------------------------------------------- */
  var fill = document.querySelector('.thread-progress__fill');
  if (fill) {
    var ticking = false;
    var updateProgress = function () {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - doc.clientHeight;
      var pct = scrollable > 0 ? (doc.scrollTop || document.body.scrollTop) / scrollable : 0;
      fill.style.width = Math.min(100, Math.max(0, pct * 100)) + '%';
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(updateProgress); ticking = true; }
    }, { passive: true });
    updateProgress();
  }
})();
