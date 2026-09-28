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

    def test_degisken_surum_yok(self):
        for dosya in (KOK / 'docs').rglob('*'):
            if dosya.is_file():
                self.assertNotIn('/latest/', dosya.read_text(errors='ignore'))


if __name__ == '__main__':
    unittest.main()
