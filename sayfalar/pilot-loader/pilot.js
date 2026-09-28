(function (global) {
  'use strict';
  global.RasyoTrendSayfalar = global.RasyoTrendSayfalar || {};
  global.RasyoTrendSayfalar['pilot-loader'] = function (kok, ayar) {
    var istemci = global.RasyoTrend && global.RasyoTrend.veri;
    if (!istemci) return Promise.reject(new Error('Veri istemcisi bulunamadı'));
    return istemci.jsonGetir(ayar.veri, { izinliOriginler: ayar.izinliOriginler }).then(function (veri) {
      kok.textContent = '';
      var baslik = document.createElement('h1');
      baslik.textContent = veri.baslik;
      kok.appendChild(baslik);
      var liste = document.createElement('ul');
      liste.className = 'pilot-liste';
      (veri.maddeler || []).forEach(function (madde) {
        var satir = document.createElement('li');
        satir.textContent = madde === null ? 'Veri yok' : String(madde);
        liste.appendChild(satir);
      });
      kok.appendChild(liste);
    });
  };
}(window));
