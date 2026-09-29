#!/usr/bin/env python3
import hashlib
import json
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
YAYIN = KOK / 'docs/assets/v1.1.0'
ROOT = 'https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.1.0/'
KAYNAKLAR = {
    'ana-tema/css/ana-tema.css', 'ana-tema/js/ana-tema.js',
    'ortak/css/tema-cekirdegi.css', 'ortak/js/tema-runtime.js',
}

class AnaTemaV11Testi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml_path = KOK / 'tema/rasyotrend-tema.xml'
        cls.xml = cls.xml_path.read_text()

    def test_xml_parse_ve_blogger_yapilari(self):
        ET.parse(self.xml_path)
        for value in ('<b:skin', '<b:section', '<b:widget', '<b:if', '<b:loop', 'data:', 'expr:'):
            self.assertIn(value, self.xml)

    def test_production_url_sozlesmesi(self):
        self.assertNotIn('http://rasyotrend.github.io', self.xml)
        for path in ('ortak/css/tema-cekirdegi.css', 'ana-tema/css/ana-tema.css'):
            self.assertIn(ROOT + path, self.xml)
        for path in ('ortak/js/tema-runtime.js', 'ana-tema/js/ana-tema.js'):
            self.assertIn("load('" + path + "'", self.xml)
        self.assertNotIn('/latest/', self.xml)

    def test_fallback_ve_duplicate_bootstrap_koruması(self):
        for value in ('__RASYOTREND_V11__', "claim('ana-tema')", 'function fallback()',
                      'script.onerror = fallback', 'setTimeout(fallback, 8000)', 'if (finished) return'):
            self.assertIn(value, self.xml)
        # Kritik CSS ve gerçek davranış fallback içinde kalır.
        for value in ('aspect-ratio:16/9', 'AbortController', "event.key === 'Escape'",
                      "event.key === 'ArrowRight'", 'dynamicItems.sort', '.desktop-dropdown'):
            self.assertIn(value, self.xml)

    def test_manifest_sha256_ve_kapsam(self):
        manifest = json.loads((YAYIN / 'manifest.json').read_text())
        self.assertEqual(manifest['surum'], '1.1.0')
        self.assertEqual(set(manifest['dosyalar']), {'assets/v1.1.0/' + p for p in KAYNAKLAR})
        for path, digest in manifest['dosyalar'].items():
            self.assertEqual(hashlib.sha256((KOK/'docs'/path).read_bytes()).hexdigest(), digest)

    def test_kaynak_docs_byte_esitligi(self):
        for path in KAYNAKLAR:
            self.assertEqual((KOK/path).read_bytes(), (YAYIN/path).read_bytes(), path)

    def test_responsive_ve_davranis_esdegerligi(self):
        css = (KOK/'ana-tema/css/ana-tema.css').read_text()
        js = (KOK/'ana-tema/js/ana-tema.js').read_text()
        for value in ('@media(max-width:700px)', '@media(max-width:960px)', 'aspect-ratio:16/9',
                      '.nav-submenu-level2', '.post-grid', '.post-body', '.sidebar'):
            self.assertIn(value, css)
        for value in ('news-prev', 'news-next', 'ArrowRight', 'ArrowLeft', 'Escape',
                      'dynamicItems.sort', "credentials: 'same-origin'", 'safeURL'):
            self.assertIn(value, js)

    def test_v100_agaci_degismedi(self):
        changed = subprocess.check_output(['git', 'diff', '--name-only', '33b160d', '--', 'docs/assets/v1.0.0'], cwd=KOK, text=True)
        self.assertEqual(changed, '')

if __name__ == '__main__': unittest.main(verbosity=2)
