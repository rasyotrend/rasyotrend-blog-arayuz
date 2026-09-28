(function (global) {
  'use strict';

  var SURUM = '1.0.0';
  var PRODUCTION_ORIGIN = 'https://rasyotrend.github.io';
  var PRODUCTION_KOKU = PRODUCTION_ORIGIN + '/rasyotrend-blog-arayuz/assets/v' + SURUM + '/';

  function birlestir(kok, yol) { return new URL(yol, kok).href; }
  function pilotAyari(mod) {
    var production = mod === 'production';
    var kok = production ? PRODUCTION_KOKU : new URL('../../', global.location.href).href;
    var pilotKoku = production ? birlestir(kok, 'sayfalar/pilot-loader/') : new URL('./', global.location.href).href;
    var yol = function (deger) { return birlestir(kok, deger); };
    return {
      mod: production ? 'production' : 'local',
      sayfa: 'pilot-loader',
      surum: SURUM,
      kok: '#rt-pilot',
      css: [
        yol('ortak/css/degiskenler.css'),
        yol('ortak/css/temel.css'),
        yol('ortak/css/bilesenler.css'),
        birlestir(pilotKoku, 'pilot.css')
      ],
      js: birlestir(pilotKoku, 'pilot.js'),
      veri: birlestir(pilotKoku, 'ornek.json'),
      izinliOriginler: production ? [PRODUCTION_ORIGIN] : undefined
    };
  }

  global.RasyoTrendAsset = Object.freeze({
    surum: SURUM,
    productionOrigin: PRODUCTION_ORIGIN,
    productionKoku: PRODUCTION_KOKU,
    pilotAyari: pilotAyari
  });
}(window));
