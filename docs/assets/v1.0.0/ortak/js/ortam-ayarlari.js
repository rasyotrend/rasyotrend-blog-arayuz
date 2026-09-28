(function (global) {
  'use strict';

  var SURUM = '1.0.0';
  var PRODUCTION_ORIGIN = 'https://rasyotrend.github.io';
  var PRODUCTION_ROOT = 'https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/';
  var LOCAL_ROOT = '../../';

  function birlestir(kok, yol) { return kok + yol; }

  function pilot(mod) {
    var production = mod === 'production';
    var kok = production ? PRODUCTION_ROOT : LOCAL_ROOT;
    return {
      mod: production ? 'production' : 'local',
      sayfa: 'pilot-loader',
      surum: SURUM,
      kok: '#rt-pilot',
      css: [
        birlestir(kok, 'ortak/css/degiskenler.css'),
        birlestir(kok, 'ortak/css/temel.css'),
        birlestir(kok, 'ortak/css/bilesenler.css'),
        birlestir(kok, 'sayfalar/pilot-loader/pilot.css')
      ],
      js: birlestir(kok, 'sayfalar/pilot-loader/pilot.js'),
      veri: birlestir(kok, 'sayfalar/pilot-loader/ornek.json'),
      timeout: 8000,
      izinliOriginler: production ? [PRODUCTION_ORIGIN] : []
    };
  }

  global.RasyoTrendOrtam = {
    surum: SURUM,
    productionOrigin: PRODUCTION_ORIGIN,
    productionAssetRoot: PRODUCTION_ROOT,
    pilot: pilot
  };
}(window));
