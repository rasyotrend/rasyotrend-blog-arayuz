#!/usr/bin/env python3
"""Blogger temasının değişmez güvenlik sınırları için bağımsız statik testler."""
import hashlib
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree

KOK = Path(__file__).resolve().parents[1]
TEMA = KOK / "tema" / "rasyotrend-tema.xml"

class TemaGuvenlikTesti(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metin = TEMA.read_text(encoding="utf-8")

    def test_kritik_dosyalar(self):
        self.assertTrue(TEMA.is_file())
        self.assertTrue((KOK / "README.md").is_file())

    def test_xml_parse(self):
        ElementTree.parse(TEMA)

    def test_blogger_yapilari(self):
        for ifade in ("<b:skin", "<b:section", "<b:widget", "<b:if", "<b:loop", "data:blog.", "data:view.", "data:post.", "expr:"):
            with self.subTest(ifade=ifade): self.assertIn(ifade, self.metin)

    def test_slider_gorsel_guvenceleri(self):
        self.assertRegex(self.metin, r"aspect-ratio\s*:\s*16\s*/\s*9")
        self.assertRegex(self.metin, r"object-fit\s*:\s*contain")
        for selector in ("news-slider", "news-track", "news-prev", "news-next"):
            self.assertIn(selector, self.metin)

    def test_navigasyon_ve_erisilebilirlik(self):
        for ifade in ("desktop-nav", "mobile-menu", "aria-current", "aria-live", "aria-label", "focus-visible", "prefers-reduced-motion", "Escape"):
            with self.subTest(ifade=ifade): self.assertIn(ifade, self.metin)

    def test_url_ve_fetch_guvenligi(self):
        for ifade in ("safeURL", "AbortController", "controller.abort()", "response.ok", "textContent"):
            with self.subTest(ifade=ifade): self.assertIn(ifade, self.metin)

    def test_finansal_hesaplama_siniri(self):
        yasak = (r"function\s+(?:temel|teknik|degerleme|adilDeger|hisseSkor)\w*\s*\(", r"(?:temel|teknik|degerleme)Puan\s*=")
        for desen in yasak:
            with self.subTest(desen=desen): self.assertIsNone(re.search(desen, self.metin, re.I))

    def test_github_actions_yok(self):
        self.assertFalse((KOK / ".github" / "workflows").exists())

if __name__ == "__main__": unittest.main(verbosity=2)
