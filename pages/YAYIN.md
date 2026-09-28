# GitHub Pages yayın sözleşmesi

`pages/`, ayrı bir yayın branch'inin köküne kopyalanacak statik yayın ağacıdır. GitHub Pages branch arayüzü repository içindeki keyfi `/pages` klasörünü doğrudan kaynak olarak sunmadığından, Actions'sız öneri `pages/` **içeriğini** `gh-pages` branch kökünde yayımlamak ve Pages kaynağında `gh-pages` + `/(root)` seçmektir. Aktivasyon ve yayın branch'i kullanıcı/repository yöneticisinin manuel işlemidir.

URL'ler sabit `v1.0.0` segmentini taşır; loader sözleşmedeki semver değerini `rt-surum` parametresi olarak uygular ve farklı sürüm taşıyan URL'yi reddeder. Yeni sürüm yeni dizine kopyalanır; mevcut yayın immutable kabul edilir. Beklenen origin, aktivasyon sonrası `https://rasyotrend.github.io/rasyotrend-blog-arayuz/` olur.

CSS, JavaScript ve JSON için yalnız `http:`, `https:` veya bunlara çözümlenen relative yollar kabul edilir; `javascript:`, `data:` ve diğer şemalar reddedilir. Production entegrasyonunda `izinliOriginler` listesi RasyoTrend ve onaylı Pages originleriyle sınırlandırılmalıdır. Harici asset hata verirse Blogger XML'deki first-render CSS, içerik ve inline davranış fallback olarak kalır.

Manifest SHA-256 değerleri dağıtım kopyasını, otomatik source→Pages testi ise `ortak/` ve `ana-tema/` altındaki yayımlanan CSS/JS dosyalarının byte eşitliğini doğrular. GitHub Actions yoktur; Pages etkinleştirilmemiştir.
