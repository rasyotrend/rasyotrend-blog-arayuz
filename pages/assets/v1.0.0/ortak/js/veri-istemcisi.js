(function (global) {
  'use strict';

  function jsonGetir(url, secenek) {
    secenek = secenek || {};
    var yardimcilar = global.RasyoTrend && global.RasyoTrend.yardimcilar;
    var guvenli = yardimcilar && yardimcilar.guvenliURL(url, secenek.taban, secenek.izinliOriginler);
    if (!guvenli) return Promise.reject(new Error('Geçersiz veri adresi'));

    var controller = new AbortController();
    var sure = secenek.timeout || 8000;
    var timer = global.setTimeout(function () { controller.abort(); }, sure);
    return global.fetch(guvenli, { signal: controller.signal, credentials: secenek.credentials || 'omit' })
      .then(function (yanit) {
        if (!yanit.ok) throw new Error('HTTP ' + yanit.status);
        return yanit.json();
      })
      .finally(function () { global.clearTimeout(timer); });
  }

  global.RasyoTrend = global.RasyoTrend || {};
  global.RasyoTrend.veri = { jsonGetir: jsonGetir };
}(window));
