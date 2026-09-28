# Design token sınıflandırması

## A — Çalışan temadan alınan veya türetilen değerler

Koyu tema renkleri (`#0e1621`, `#151f2c`, `#1b2938`, `#c9d3df`, `#e3eaf2`, `#9daebe`, `#75cbbb`, `#2a3a4a`) XML'deki v011/v040 değerlerinden birebir alınmıştır. 8/12/16/24/32/48 px boşluklar ile 4/8/10 px radius ölçeği mevcut kurallarda tekrar eden değerlerin adlandırılmış karşılığıdır.

## B — Yeni frontend mimarisi için önerilen değerler

Negatif ve uyarı semantik renkleri, genel panel gölgesi, standartlaştırılmış font ağırlıkları, z-index adları, geçiş süreleri ve breakpoint referans tokenları yeni mimari önerisidir. Bunların varlığı çalışan Blogger temasında kullanıldıkları anlamına gelmez.

Tema XML'i bu token dosyasına bağlanmamıştır; mevcut görünüm değişmemiştir. Breakpoint tokenları CSS medya sorgularında doğrudan kullanılamadığı için yalnız dokümantasyon referansıdır.
