'use strict';
const assert = require('assert');
const fs = require('fs');
const vm = require('vm');

const context = {
  URL,
  window: { location: { href: 'https://www.rasyotrend.com/pilot/' } },
  document: {},
  Promise
};
context.window.URL = URL;
vm.createContext(context);
vm.runInContext(fs.readFileSync('ortak/js/yardimcilar.js', 'utf8'), context);
vm.runInContext(fs.readFileSync('ortak/js/sayfa-loader.js', 'utf8'), context);

const yardimci = context.window.RasyoTrend.yardimcilar;
assert.strictEqual(yardimci.guvenliURL('javascript:alert(1)'), null);
assert.strictEqual(yardimci.guvenliURL('data:text/css,bad'), null);
assert.strictEqual(yardimci.guvenliURL('pilot.css'), 'https://www.rasyotrend.com/pilot/pilot.css');
assert.strictEqual(yardimci.guvenliURL('https://evil.example/x.js', undefined, ['https://www.rasyotrend.com']), null);

const test = context.window.RasyoTrendLoader._test;
assert.deepStrictEqual(Array.from(test.cssListesi([])), []);
assert.deepStrictEqual(Array.from(test.cssListesi('tek.css')), ['tek.css']);
const ayar = test.ayarlariCoz({
  sayfa: 'pilot', surum: '1.0.0', kok: '#pilot', css: ['a.css', 'b.css'], js: 'pilot.js', veri: 'ornek.json'
});
assert.strictEqual(ayar.css.length, 2);
assert.ok(ayar.css.every((url) => url.includes('rt-surum=1.0.0')));
assert.ok(ayar.js.includes('rt-surum=1.0.0'));
assert.ok(ayar.veri.includes('rt-surum=1.0.0'));
assert.throws(() => test.ayarlariCoz({surum: '1.0.0', css: [], js: 'javascript:x', veri: 'x.json'}));
assert.throws(() => test.ayarlariCoz({surum: '1.0.0', css: [], js: 'x.js?rt-surum=2.0.0', veri: 'x.json'}));
console.log('loader URL ve çoklu CSS testleri başarılı');
