(function (global) {
  'use strict';
  function guvenliURL(deger, taban) {
    if (typeof deger !== 'string' || !deger.trim()) return null;
    try { var url = new URL(deger, taban || global.location.href); return /^(https?:)$/.test(url.protocol) ? url.href : null; } catch (_) { return null; }
  }
  function metinYaz(dugum, deger, eksik) { if (!dugum) return; dugum.textContent = deger === null || deger === undefined ? (eksik || 'Veri yok') : String(deger); }
  global.RasyoTrend = global.RasyoTrend || {}; global.RasyoTrend.yardimcilar = { guvenliURL: guvenliURL, metinYaz: metinYaz };
}(window));
