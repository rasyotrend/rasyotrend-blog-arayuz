# GitHub Pages yayın sözleşmesi

`docs/`, `Settings → Pages` ekranında `Source: Deploy from a branch`, `Branch: main`, `Folder: /docs` seçimiyle kullanılacak statik yayın köküdür; aktivasyon repository yöneticisinin manuel işlemidir. URL'ler sabit `v1.0.0` segmentini taşır; loader ayrıca sözleşmedeki semver değerini `rt-surum` parametresi olarak uygular ve farklı sürüm taşıyan URL'yi reddeder. Yeni sürüm yeni dizine kopyalanır; mevcut yayın immutable kabul edilir. Cache busting sürümle, rollback Blogger referansını önceki sürüme döndürerek yapılır.

CSS, JavaScript ve JSON için yalnız `http:`, `https:` veya bunlara çözümlenen relative yollar kabul edilir; `javascript:`, `data:` ve diğer şemalar reddedilir. Production entegrasyonunda `izinliOriginler` listesi RasyoTrend ve onaylı Pages originleriyle sınırlandırılmalıdır. Harici asset hata verirse Blogger XML'deki first-render CSS, içerik ve inline davranış fallback olarak kalır.

Manifest SHA-256 değerleri dağıtım kopyasını, otomatik source→Pages testi ise `ortak/` ve `ana-tema/` altındaki yayımlanan CSS/JS dosyalarının byte eşitliğini doğrular. GitHub Actions yoktur; Pages etkinleştirilmemiştir.

## Pilot sayfası production farkı

`docs/assets/v1.0.0/sayfalar/pilot-loader/index.html`, kaynak `sayfalar/pilot-loader/index.html` dosyasının bilinçli bir production varyantıdır ve bu nedenle HTML için byte eşitliği beklenmez. Kaynak HTML local/production sorgu modu seçimini korurken yayın HTML'i ortak loader betiklerini sabit production asset root üzerinden `rt-surum=1.0.0` ile yükler ve pilotu doğrudan production modunda başlatır. CSS, JavaScript ve örnek JSON dosyaları loader tarafından aynı sürümlü asset root altından yüklenir. GitHub Pages public URL'si `/docs` segmenti içermez: `https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/sayfalar/pilot-loader/`.
