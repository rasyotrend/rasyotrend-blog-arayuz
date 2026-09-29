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

    def test_v100_manifestindeki_kaynak_yayin_byte_esitligi(self):
        # v1.0.0 immutable bir snapshot'tır; daha yeni kaynak dosyaları bu kümeye eklenmez.
        manifest = json.loads((YAYIN / 'manifest.json').read_text())
        for yayin_yolu in manifest['dosyalar']:
            goreli = Path(yayin_yolu).relative_to('assets/v1.0.0')
            if goreli.parts[0] not in ('ortak', 'ana-tema', 'sayfalar') or goreli.suffix not in ('.css', '.js'):
                continue
            self.assertEqual((KOK / goreli).read_bytes(), (YAYIN / goreli).read_bytes(), str(goreli))

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
