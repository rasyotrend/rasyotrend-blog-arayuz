# GitHub Pages yayın sözleşmesi

`pages/` branch/dizin tabanlı statik yayın köküdür; aktivasyon repository yöneticisinin manuel işlemidir. URL'ler sabit `v1.0.0` segmentini taşır; loader ayrıca sözleşmedeki semver değerini `rt-surum` parametresi olarak uygular ve farklı sürüm taşıyan URL'yi reddeder. Yeni sürüm yeni dizine kopyalanır; mevcut yayın immutable kabul edilir. Cache busting sürümle, rollback Blogger referansını önceki sürüme döndürerek yapılır.

CSS, JavaScript ve JSON için yalnız `http:`, `https:` veya bunlara çözümlenen relative yollar kabul edilir; `javascript:`, `data:` ve diğer şemalar reddedilir. Production entegrasyonunda `izinliOriginler` listesi RasyoTrend ve onaylı Pages originleriyle sınırlandırılmalıdır. Harici asset hata verirse Blogger XML'deki first-render CSS, içerik ve inline davranış fallback olarak kalır.

Manifest SHA-256 değerleri dağıtım kopyasını, otomatik source→Pages testi ise `ortak/` ve `ana-tema/` altındaki yayımlanan CSS/JS dosyalarının byte eşitliğini doğrular. GitHub Actions yoktur; Pages etkinleştirilmemiştir.
