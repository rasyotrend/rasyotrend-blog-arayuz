(function (global) {
  'use strict';
  function yukle(ayar) {
    var kok = document.querySelector(ayar.kok); if (!kok) return Promise.reject(new Error('Loader kökü bulunamadı'));
    kok.setAttribute('aria-busy', 'true'); kok.setAttribute('data-sayfa', ayar.sayfa); kok.textContent = 'Yükleniyor…';
    var css = document.createElement('link'); css.rel = 'stylesheet'; css.href = ayar.css; css.onerror = function(){ kok.setAttribute('data-css-fallback','true'); }; document.head.appendChild(css);
    return new Promise(function(resolve,reject){
      var js=document.createElement('script'); js.src=ayar.js; js.defer=true;
      js.onload=function(){
        var baslat=global.RasyoTrendSayfalar&&global.RasyoTrendSayfalar[ayar.sayfa];
        if(typeof baslat!=='function'){reject(new Error('Sayfa giriş noktası bulunamadı'));return;}
        Promise.resolve(baslat(kok,ayar)).then(resolve,reject);
      };
      js.onerror=function(){reject(new Error('Sayfa asseti yüklenemedi'));}; document.head.appendChild(js);
    }).catch(function(hata){kok.setAttribute('data-durum','hata');kok.textContent='İçerik yüklenemedi.';throw hata;})
      .finally(function(){kok.removeAttribute('aria-busy');});
  }
  global.RasyoTrendLoader={yukle:yukle};
}(window));
