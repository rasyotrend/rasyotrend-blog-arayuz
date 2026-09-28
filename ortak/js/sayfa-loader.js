(function (global) {
  'use strict';

  function cssListesi(css) {
    if (css === undefined || css === null) return [];
    return Array.isArray(css) ? css.slice() : [css];
  }

  function ayarlariCoz(ayar) {
    var yardimcilar = global.RasyoTrend && global.RasyoTrend.yardimcilar;
    if (!yardimcilar || !yardimcilar.surumluURL) throw new Error('URL güvenlik yardımcısı bulunamadı');
    var cozumle = function (url) {
      var sonuc = yardimcilar.surumluURL(url, ayar.surum, ayar.taban, ayar.izinliOriginler);
      if (!sonuc) throw new Error('Güvenli olmayan veya sürümü uyuşmayan asset adresi');
      return sonuc;
    };
    return {
      sayfa: ayar.sayfa,
      surum: ayar.surum,
      kok: ayar.kok,
      css: cssListesi(ayar.css).map(cozumle),
      js: cozumle(ayar.js),
      veri: cozumle(ayar.veri),
      izinliOriginler: ayar.izinliOriginler,
      timeout: ayar.timeout
    };
  }

  function yukle(ayar) {
    var kok = document.querySelector(ayar.kok);
    if (!kok) return Promise.reject(new Error('Loader kökü bulunamadı'));
    var cozulmus;
    try { cozulmus = ayarlariCoz(ayar); }
    catch (_) {
      kok.setAttribute('data-durum', 'hata');
      kok.textContent = 'İçerik yüklenemedi.';
      return Promise.reject(new Error('Loader yapılandırması geçersiz'));
    }

    kok.setAttribute('aria-busy', 'true');
    kok.setAttribute('data-sayfa', cozulmus.sayfa);
    kok.textContent = 'Yükleniyor…';
    cozulmus.css.forEach(function (adres) {
      var link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = adres;
      link.onerror = function () {
        kok.setAttribute('data-css-fallback', 'true');
        var hatalar = kok.getAttribute('data-css-hatalari');
        kok.setAttribute('data-css-hatalari', hatalar ? hatalar + '|' + adres : adres);
      };
      document.head.appendChild(link);
    });

    return new Promise(function (resolve, reject) {
      var script = document.createElement('script');
      script.src = cozulmus.js;
      script.defer = true;
      script.onload = function () {
        var baslat = global.RasyoTrendSayfalar && global.RasyoTrendSayfalar[cozulmus.sayfa];
        if (typeof baslat !== 'function') { reject(new Error('Sayfa giriş noktası bulunamadı')); return; }
        Promise.resolve(baslat(kok, cozulmus)).then(resolve, reject);
      };
      script.onerror = function () { reject(new Error('Sayfa asseti yüklenemedi')); };
      document.head.appendChild(script);
    }).catch(function (hata) {
      kok.setAttribute('data-durum', 'hata');
      kok.textContent = 'İçerik yüklenemedi.';
      throw hata;
    }).finally(function () { kok.removeAttribute('aria-busy'); });
  }

  global.RasyoTrendLoader = { yukle: yukle, _test: { cssListesi: cssListesi, ayarlariCoz: ayarlariCoz } };
}(window));
