import json,unittest
from pathlib import Path
K=Path(__file__).resolve().parents[1]
class LoaderTesti(unittest.TestCase):
 def test_pilot_sozlesmesi(self):
  html=(K/'sayfalar/pilot-loader/index.html').read_text()
  for x in ("sayfa:'pilot-loader'","surum:'1.0.0'","css:","js:","veri:",'aria-live'): self.assertIn(x,html)
 def test_ornek_null_korur(self):
  self.assertIn(None,json.loads((K/'sayfalar/pilot-loader/ornek.json').read_text())['maddeler'])
 def test_loader_fallback(self):
  js=(K/'ortak/js/sayfa-loader.js').read_text()
  for x in ('onerror','İçerik yüklenemedi','aria-busy','data-css-fallback'): self.assertIn(x,js)
if __name__=='__main__': unittest.main()
