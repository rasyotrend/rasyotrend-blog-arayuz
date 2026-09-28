# GitHub Pages yayın sözleşmesi

`pages/` branch/dizin tabanlı statik yayın köküdür; aktivasyon repository yöneticisinin manuel işlemidir. URL'ler mutlaka sabit `v1.0.0` segmentini taşır. Yeni sürüm yeni dizine kopyalanır; mevcut sürüm immutable kabul edilir. Cache busting sürüm segmentiyle, rollback Blogger referansını bir önceki sürüme döndürerek yapılır. Harici asset hata verirse Blogger XML'deki first-render CSS, içerik ve inline davranış fallback olarak kalır. Manifest SHA-256 değerleri kopya bütünlüğünü doğrular. GitHub Actions yoktur.
