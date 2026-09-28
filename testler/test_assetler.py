import hashlib
import json
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
YAYIN = KOK / 'docs' / 'assets' / 'v1.0.0'


class AssetTesti(unittest.TestCase):
    def test_manifest_butunlugu(self):
        manifest = json.loads((YAYIN / 'manifest.json').read_text())
        self.assertEqual(manifest['surum'], '1.0.0')
        for yol, ozet in manifest['dosyalar'].items():
            dosya = KOK / 'docs' / yol
            self.assertTrue(dosya.is_file(), yol)
            self.assertEqual(hashlib.sha256(dosya.read_bytes()).hexdigest(), ozet, yol)

    def test_kaynak_yayin_byte_esitligi(self):
        for kok_adi in ('ortak', 'ana-tema', 'sayfalar'):
            kaynaklar = {
                p.relative_to(KOK / kok_adi)
                for p in (KOK / kok_adi).rglob('*')
                if p.is_file() and p.suffix in ('.css', '.js')
            }
            kopyalar = {
                p.relative_to(YAYIN / kok_adi)
                for p in (YAYIN / kok_adi).rglob('*')
                if p.is_file() and p.suffix in ('.css', '.js')
            }
            self.assertEqual(kaynaklar, kopyalar, kok_adi)
            for goreli in kaynaklar:
                self.assertEqual(
                    (KOK / kok_adi / goreli).read_bytes(),
                    (YAYIN / kok_adi / goreli).read_bytes(),
                    str(goreli),
                )

    def test_pilot_html_bilincli_production_farki(self):
        kaynak = (KOK / 'sayfalar/pilot-loader/index.html').read_text()
        yayin = (YAYIN / 'sayfalar/pilot-loader/index.html').read_text()
        self.assertNotEqual(kaynak, yayin)
        self.assertIn("params.get('rt-mod') === 'production'", kaynak)
        self.assertNotIn("params.get('rt-mod')", yayin)
        self.assertIn("RasyoTrendOrtam.pilot('production')", yayin)

        production_root = 'https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/'
        for dosya in ('ortam-ayarlari.js', 'yardimcilar.js', 'veri-istemcisi.js', 'sayfa-loader.js'):
            self.assertIn(
                production_root + 'ortak/js/' + dosya + '?rt-surum=1.0.0',
                yayin,
            )
        for dosya in ('pilot.css', 'pilot.js', 'ornek.json'):
            self.assertTrue((YAYIN / 'sayfalar/pilot-loader' / dosya).is_file())

    def test_degisken_surum_yok(self):
        for dosya in (KOK / 'docs').rglob('*'):
            if dosya.is_file():
                self.assertNotIn('/latest/', dosya.read_text(errors='ignore'))


if __name__ == '__main__':
    unittest.main()
