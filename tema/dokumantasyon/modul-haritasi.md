# Tema modül haritası v1.0.0

| Sorumluluk | Geçiş iskeleti | Production kaynağı |
|---|---|---|
| Token/temel/erişilebilirlik | `ortak/css/*` | `b:skin` içinde korunur |
| Yerleşim/navigasyon/slider/içerik/sidebar | `ana-tema/css/*` | `b:skin` ve responsive override zinciri |
| URL/fetch/hata | `ortak/js/*` | slider inline IIFE içindeki çalışan uygulama |
| Navigasyon/slider/kategori | `ana-tema/js/*` | ana inline script |
| Blogger render/yorum/pagination | Yok | yalnız XML |

Bu sürümde production CSS/JS dışsallaştırması yapılmamıştır: inline CSS/JS kaldırılmamış ve XML dış assetlere zorunlu bağlanmamıştır. `ana-tema/js/navigasyon.js`, `slider.js` ve `kategori-siralama.js` tam işlevsel eşdeğer değil, modülerleşme için geçiş iskeleti/sorumluluk sınırıdır. Blogger Preview üzerinde davranış eşdeğerliği kanıtlanmadan XML kodunun yerine kullanılamaz.
