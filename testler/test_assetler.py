import hashlib,json,unittest
from pathlib import Path
KOK=Path(__file__).resolve().parents[1]
class AssetTesti(unittest.TestCase):
 def test_manifest_butunlugu(self):
  m=json.loads((KOK/'pages/assets/v1.0.0/manifest.json').read_text())
  self.assertEqual(m['surum'],'1.0.0')
  for yol,ozet in m['dosyalar'].items(): self.assertEqual(hashlib.sha256((KOK/'pages'/yol).read_bytes()).hexdigest(),ozet)
 def test_degisken_surum_yok(self):
  for p in (KOK/'pages').rglob('*'):
   if p.is_file(): self.assertNotIn('/latest/',p.read_text(errors='ignore'))
if __name__=='__main__': unittest.main()
