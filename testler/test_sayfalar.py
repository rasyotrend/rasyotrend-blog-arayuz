import json,unittest
from pathlib import Path
K=Path(__file__).resolve().parents[1]; ADLAR=('temel-analiz','teknik-analiz','temel-analiz-puan','teknik-analiz-puan','adil-deger','degerleme-puan','hisse-skor','hisse-karnesi')
class SayfaSozlesmesiTesti(unittest.TestCase):
 def test_sekiz_sozlesme(self):
  for ad in ADLAR:
   a=json.loads((K/'sayfalar'/ad/'yukleme.json').read_text())
   self.assertEqual(a['sayfa'],ad); self.assertEqual(a['surum'],'1.0.0'); self.assertEqual(a['nullDavranisi'],'veri-yok')
 def test_tek_ortak_giris(self):
  js=(K/'ortak/js/analiz-sayfasi.js').read_text()
  for ad in ADLAR:self.assertIn("'"+ad+"'",js)
  self.assertNotIn('hesapla(',js)
if __name__=='__main__':unittest.main()
