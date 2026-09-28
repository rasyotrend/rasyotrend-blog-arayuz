import json
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
ADLAR = ('temel-analiz', 'teknik-analiz', 'temel-analiz-puan', 'teknik-analiz-puan', 'adil-deger', 'degerleme-puan', 'hisse-skor', 'hisse-karnesi')


class SayfaSozlesmesiTesti(unittest.TestCase):
    def test_sekiz_sozlesme_loader_ile_uyumlu(self):
        for ad in ADLAR:
            ayar = json.loads((KOK / 'sayfalar' / ad / 'yukleme.json').read_text())
            self.assertEqual(ayar['sayfa'], ad)
            self.assertRegex(ayar['surum'], r'^\d+\.\d+\.\d+$')
            self.assertIsInstance(ayar['css'], list)
            self.assertTrue(all(isinstance(yol, str) for yol in ayar['css']))
            self.assertIsInstance(ayar['js'], str)
            self.assertEqual(ayar['veri'], 'PUBLIC_JSON_URL_GEREKLI')
            self.assertEqual(ayar['nullDavranisi'], 'veri-yok')

    def test_tek_ortak_giris_hesaplama_yapmaz(self):
        js = (KOK / 'ortak/js/analiz-sayfasi.js').read_text()
        for ad in ADLAR:
            self.assertIn("'" + ad + "'", js)
        self.assertNotIn('hesapla(', js)


if __name__ == '__main__':
    unittest.main()
