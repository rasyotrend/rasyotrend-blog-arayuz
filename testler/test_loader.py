import json
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]


class LoaderTesti(unittest.TestCase):
    def test_pilot_sozlesmesi(self):
        html = (KOK / 'sayfalar/pilot-loader/index.html').read_text()
        for ifade in ("sayfa: 'pilot-loader'", "surum: '1.0.0'", 'css:', 'js:', 'veri:', 'aria-live'):
            self.assertIn(ifade, html)

    def test_ornek_null_korur(self):
        self.assertIn(None, json.loads((KOK / 'sayfalar/pilot-loader/ornek.json').read_text())['maddeler'])
        for dosya in ('ortak/js/analiz-sayfasi.js', 'sayfalar/pilot-loader/pilot.js'):
            metin = (KOK / dosya).read_text()
            self.assertNotRegex(metin, r'(?i)null\s*\?\s*0|\|\|\s*0')

    def test_loader_coklu_css_ve_fallback(self):
        js = (KOK / 'ortak/js/sayfa-loader.js').read_text()
        for ifade in ('Array.isArray(css)', '.forEach(function (adres)', 'data-css-fallback', 'data-css-hatalari'):
            self.assertIn(ifade, js)

    def test_ortak_veri_istemcisi_kullanilir(self):
        for dosya in ('ortak/js/analiz-sayfasi.js', 'sayfalar/pilot-loader/pilot.js'):
            metin = (KOK / dosya).read_text()
            self.assertIn('istemci.jsonGetir', metin)
            self.assertNotIn('fetch(', metin)

    def test_url_politikasi_tek_yardimcida(self):
        yardimci = (KOK / 'ortak/js/yardimcilar.js').read_text()
        self.assertIn("url.protocol !== 'http:'", yardimci)
        self.assertIn("url.protocol !== 'https:'", yardimci)
        self.assertIn('izinliOriginler', yardimci)
        self.assertIn('surumluURL', (KOK / 'ortak/js/sayfa-loader.js').read_text())


if __name__ == '__main__':
    unittest.main()
