# Aşama 12 — Pilot production modu

`RasyoTrendOrtam.pilot(mod)` local modda relative, production modda HTTPS ve sürümlü yollar üretir. Pilot `?rt-mod=production` ile production seçer; varsayılan local/test modudur. Ortak loader, yardımcılar ve veri istemcisi kullanılır. Pilot JSON test verisidir, finansal hesaplama yoktur ve null “Veri yok” olarak korunur.
