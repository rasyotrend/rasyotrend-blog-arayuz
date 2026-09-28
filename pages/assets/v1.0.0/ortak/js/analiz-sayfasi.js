(function(global){
  'use strict';
  var SAYFALAR=['temel-analiz','teknik-analiz','temel-analiz-puan','teknik-analiz-puan','adil-deger','degerleme-puan','hisse-skor','hisse-karnesi'];
  function baslat(kok,ayar){return fetch(ayar.veri).then(function(r){if(!r.ok)throw new Error('Veri alınamadı');return r.json();}).then(function(veri){if(!veri||!Array.isArray(veri.kayitlar))throw new Error('Geçersiz veri sözleşmesi');kok.textContent='';var durum=document.createElement('p');durum.className='rt-durum';durum.textContent=veri.kayitlar.length?veri.kayitlar.length+' hazır kayıt gösteriliyor.':'Gösterilecek veri yok.';kok.appendChild(durum);return veri;});}
  global.RasyoTrendSayfalar=global.RasyoTrendSayfalar||{};SAYFALAR.forEach(function(ad){global.RasyoTrendSayfalar[ad]=baslat;});
}(window));
