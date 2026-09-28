import hashlib
import json
import re
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
PRODUCTION = 'https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/'
XML_SHA = '94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513'
SAYFALAR = ('temel-analiz', 'teknik-analiz', 'temel-analiz-puan', 'teknik-analiz-puan', 'adil-deger', 'degerleme-puan', 'hisse-skor', 'hisse-karnesi')


class EntegrasyonTesti(unittest.TestCase):
    def test_production_asset_sozlesmesi(self):
        js = (KOK / 'ortak/js/asset-yapilandirmasi.js').read_text()
        self.assertIn("var SURUM = '1.0.0'", js)
        self.assertIn("var PRODUCTION_ORIGIN = 'https://rasyotrend.github.io'", js)
        self.assertIn("'/rasyotrend-blog-arayuz/assets/v' + SURUM + '/'", js)
        self.assertNotIn('/latest/', js)

    def test_local_ve_production_modlari(self):
        js = (KOK / 'ortak/js/asset-yapilandirmasi.js').read_text()
        self.assertIn("mod === 'production'", js)
        self.assertIn("production ? PRODUCTION_KOKU : new URL('../../', global.location.href).href", js)
        pilot = (KOK / 'sayfalar/pilot-loader/index.html').read_text()
        self.assertIn("? 'production' : 'local'", pilot)

    def test_blogger_sablonu_production_url_ve_fallback(self):
        html = (KOK / 'entegrasyon/blogger-pilot-loader.html').read_text()
        for ad in ('asset-yapilandirmasi.js', 'yardimcilar.js', 'veri-istemcisi.js', 'sayfa-loader.js'):
            self.assertIn(PRODUCTION + 'ortak/js/' + ad, html)
        for ifade in ('aria-live="polite"', 'aria-busy="true"', 'data-bootstrap', 'rtPilotHata', "pilotAyari('production')"):
            self.assertIn(ifade, html)
        self.assertNotRegex(html, r'(?i)(hesapla|\|\|\s*0)')

    def test_public_json_placeholderlari_korunur(self):
        for ad in SAYFALAR:
            ayar = json.loads((KOK / 'sayfalar' / ad / 'yukleme.json').read_text())
            self.assertEqual(ayar['veri'], 'PUBLIC_JSON_URL_GEREKLI')

    def test_pilot_yayin_kopyalari_esit(self):
        for ad in ('pilot.css', 'pilot.js', 'ornek.json'):
            self.assertEqual(
                (KOK / 'sayfalar/pilot-loader' / ad).read_bytes(),
                (KOK / 'pages/assets/v1.0.0/sayfalar/pilot-loader' / ad).read_bytes(),
            )

    def test_xml_sha_degisime_karsi_sabit(self):
        sonuc = hashlib.sha256((KOK / 'tema/rasyotrend-tema.xml').read_bytes()).hexdigest()
        self.assertEqual(sonuc, XML_SHA)

    def test_actions_yok(self):
        self.assertFalse((KOK / '.github/workflows').exists())

    def test_canliya_gecis_paketi_tam(self):
        paket = KOK / 'entegrasyon/canliya-gecis'
        for ad in ('README.md', 'blogger-pilot-loader.html', 'github-pages-ayari.md', 'test-kontrol-listesi.md', 'rollback.md'):
            self.assertTrue((paket / ad).is_file(), ad)


if __name__ == '__main__':
    unittest.main()
