(function (global) {
  'use strict';

  function guvenliURL(deger, taban, izinliOriginler) {
    if (typeof deger !== 'string' || !deger.trim()) return null;
    try {
      var url = new URL(deger, taban || global.location.href);
      if (url.protocol !== 'http:' && url.protocol !== 'https:') return null;
      if (Array.isArray(izinliOriginler) && izinliOriginler.length && izinliOriginler.indexOf(url.origin) === -1) return null;
      return url.href;
    } catch (_) { return null; }
  }

  function surumluURL(deger, surum, taban, izinliOriginler) {
    if (typeof surum !== 'string' || !/^\d+\.\d+\.\d+$/.test(surum)) return null;
    var guvenli = guvenliURL(deger, taban, izinliOriginler);
    if (!guvenli) return null;
    var url = new URL(guvenli);
    var mevcut = url.searchParams.get('rt-surum');
    if (mevcut && mevcut !== surum) return null;
    url.searchParams.set('rt-surum', surum);
    return url.href;
  }

  function metinYaz(dugum, deger, eksik) {
    if (!dugum) return;
    dugum.textContent = deger === null || deger === undefined ? (eksik || 'Veri yok') : String(deger);
  }

  global.RasyoTrend = global.RasyoTrend || {};
  global.RasyoTrend.yardimcilar = { guvenliURL: guvenliURL, surumluURL: surumluURL, metinYaz: metinYaz };
}(window));
