# Ana tema kod envanteri (v040 baz)

## CSS selector grupları

- Temel: `:root`, reset, `body`, bağlantılar, `.wrap`, başlık ve metin stilleri.
- Yerleşim: `.site-header`, `.header-row`, `.layout`, `.main-column`, `.sidebar`, footer.
- Navigasyon: `.desktop-nav`, `.mobile-menu`, `.nav-list`, `.nav-dropdown`, `.nav-submenu`, `.nav-submenu-level2`.
- Slider: `.news-slider`, `.news-toolbar`, `.news-track`, `.news-slide`, `.news-media`, `.news-copy`, `.news-controls`, `.news-arrow`, `.news-dot`.
- İçerik: `.post-grid`, `.post-card`, `.full-post`, `.post-body`, `.post-meta`, `.pagination`.
- Yardımcı/erişilebilirlik: `[hidden]`, `:focus-visible`, `.slider-title-sr-only`, reduced-motion medya sorgusu.

## Override zinciri

İlk v011 kuralları temel görünümü kurar. v015 masaüstü hover menülerini, v017 ikinci seviye Fon menülerini, v035 slider alt-bant sunumunu, v038 erişilebilir slider başlığını, v040 ise 16:9 kesmesiz görsel alanını son katmanda kesinleştirir. `.news-media`, `.news-media img`, `.news-toolbar`, `.news-controls`, `.news-arrow` ve `.news-dot` tekrarlı selectorlardır; sıra bağımlıdır ve silme adayı değildir. `700px` mobil, `701px` masaüstü ve `960px` tablet zinciri birlikte korunmalıdır.

Kullanılmıyor olabilecek kurallar yalnızca adaydır: eski slider kopya değerleri ve `.hero-note`. DOM/koşullu Blogger çıktısı tarayıcıda doğrulanmadan kaldırılmamalıdır.

## JavaScript envanteri

- Blogger yorum scriptleri: Blogger yorum/form render akışına bağlıdır.
- Aktif navigasyon IIFE'si: geçerli yolu menü bağlantılarıyla eşler ve `aria-current` yazar.
- Slider IIFE'si: JSON feed, `safeURL`, DOM üretimi, 8 saniye `AbortController` timeout'u, fallback, ok/nokta/klavye ve scroll senkronu.
- Kategori sıralama IIFE'si: label feed'ini okur, mevcut bağlantıları sayıya göre sıralar; hatada DOM sırasını korur.
- Mobil menü IIFE'si: `details`, dış tıklama, Escape ve masaüstü dropdown odak davranışını yönetir.

## Erişilebilirlik ve viewport değerlendirmesi

`focus-visible`, `aria-current`, `aria-live`, `aria-label`, `aria-hidden`, ok tuşları, Escape ve reduced-motion vardır. Ayrı skip link yoktur; iyileştirme adayıdır. Dropdown davranışı masaüstünde hover/focus, mobilde yerel `details` üzerindedir. 320, 360, 375, 390, 430 ve 700 altı genişlikler aynı mobil zincire; 768 ve 960 tablet zincirine; 1024 masaüstü zincirine girer. Statik incelemede tek sütun, 16:9 slider ve 40–48px kontroller korunur; gerçek Blogger render'ı bulunmadığından piksel/görsel eşdeğerlik tarayıcıyla kanıtlanmamıştır.
