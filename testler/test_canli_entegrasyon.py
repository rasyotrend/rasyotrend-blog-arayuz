import hashlib
import json
import subprocess
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
SHA = '5d45f51140dd5a9b8363808b05d78fab3e1b4fa3'
PRODUCTION = 'https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/'
XML_SHA = '94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513'


class CanliEntegrasyonTesti(unittest.TestCase):
    def test_docs_public_yayin_agaci(self):
        self.assertTrue((KOK / 'docs/.nojekyll').is_file())
        self.assertTrue((KOK / 'docs/index.html').is_file())
        self.assertTrue((KOK / 'docs/assets/v1.0.0').is_dir())
        self.assertFalse((KOK / 'pages').exists())
        self.assertTrue((KOK / 'docs/assets/v1.0.0/sayfalar/pilot-loader/index.html').is_file())

    def test_merkezi_ortam_ayari(self):
        metin = (KOK / 'ortak/js/ortam-ayarlari.js').read_text()
        self.assertIn(PRODUCTION, metin)
        self.assertIn("var LOCAL_ROOT = '../../'", metin)
        self.assertIn("mod === 'production'", metin)
        self.assertIn("surum: SURUM", metin)
        self.assertIn("izinliOriginler", metin)

    def test_pilot_local_ve_production_modu(self):
        html = (KOK / 'sayfalar/pilot-loader/index.html').read_text()
        self.assertIn("params.get('rt-mod') === 'production'", html)
        self.assertIn("RasyoTrendOrtam.pilot(mod)", html)
        self.assertIn('../../ortak/js/ortam-ayarlari.js', html)

    def test_blogger_production_bootstrap(self):
        asil = (KOK / 'entegrasyon/blogger-pilot-loader.html').read_bytes()
        self.assertEqual(asil, (KOK / 'entegrasyon/canliya-gecis/blogger-pilot-loader.html').read_bytes())
        metin = asil.decode()
        for ifade in (PRODUCTION, '__RASYOTREND_PILOT_BOOTSTRAP__', "pilot('production')",
                       'aria-live="polite"', 'aria-busy', 'Yükleniyor', 'yüklenemiyor'):
            self.assertIn(ifade, metin)

    def test_veri_istemcisi_timeout_abort_ve_null(self):
        istemci = (KOK / 'ortak/js/veri-istemcisi.js').read_text()
        self.assertIn('new AbortController()', istemci)
        self.assertIn('controller.abort()', istemci)
        self.assertIn('secenek.timeout || 8000', istemci)
        pilot = (KOK / 'sayfalar/pilot-loader/pilot.js').read_text()
        self.assertIn("madde === null ? 'Veri yok'", pilot)
        self.assertNotIn('|| 0', pilot)

    def test_public_json_placeholder_korunur(self):
        analizler = list((KOK / 'sayfalar').glob('*/yukleme.json'))
        self.assertTrue(any('PUBLIC_JSON_URL_GEREKLI' in p.read_text() for p in analizler))

    def test_github_actions_yok(self):
        actions = KOK / '.github/workflows'
        self.assertFalse(actions.exists() and any(actions.iterdir()))

    def test_xml_parse_ve_baslangic_kaydi(self):
        xml = KOK / 'tema/rasyotrend-tema.xml'
        ET.parse(xml)
        baslangic = subprocess.check_output(['git', 'show', '33b160d:tema/rasyotrend-tema.xml'], cwd=KOK)
        self.assertEqual(hashlib.sha256(baslangic).hexdigest(), XML_SHA)
        self.assertNotEqual(xml.read_bytes(), baslangic)

    def test_immutable_manifest_tum_dosyalari_kapsar(self):
        yayin = KOK / 'docs/assets/v1.0.0'
        manifest = json.loads((yayin / 'manifest.json').read_text())
        beklenen = {str(p.relative_to(KOK / 'docs')) for p in yayin.rglob('*') if p.is_file() and p.name != 'manifest.json'}
        self.assertEqual(set(manifest['dosyalar']), beklenen)
        self.assertEqual(manifest['surum'], '1.0.0')


if __name__ == '__main__':
    unittest.main()
