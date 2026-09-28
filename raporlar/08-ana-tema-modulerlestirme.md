# Aşama 8 — Ana tema CSS ve JavaScript modülerleştirmesi
## 1. Aşamanın amacı
Production dışsallaştırması yapmadan tema sorumluluklarının geçiş sınırını, fallback haritasını ve doğrulama planını belirlemek.
## 2. Yapılan değişiklikler
Aşama başlangıcı SHA-256: `ef603be93c2fe039a262a4aa3b4737137ebfcb8f7f7839355b651bc35e1ef6c7`. XML’e davranışsız modül haritası açıklamaları eklendi; sorumluluk sınırları, fallback haritası, production geçiş planı ve statik güvenlik kontrolü belgelendi. Bu aşama tamamlanmış production modülerleştirmesi değildir.
## 3. Değiştirilen / oluşturulan dosyalar
`tema/rasyotrend-tema.xml`, `tema/dokumantasyon/modul-haritasi.md`, `raporlar/00-genel-sonuc.md`, bu rapor.
## 4. Değiştirilmeyen alanlar
Inline CSS kaldırılmadı, inline JS kaldırılmadı ve XML dış assetlere zorunlu bağlanmadı. `b:skin`, Blogger tag/ifadeleri, menü URL’leri, slider feed/16:9/contain, mobil details ve render/comment/pagination akışları içerik olarak korunmuştur.
## 5. Yapılan testler
`./testler/calistir.sh`; `node --check` tüm JS; XML parse; parent diff ve kritik davranış statik kontrolleri; yedi viewport için kaynak medya zinciri incelemesi.
## 6. Test sonuçları
18 Python testi, Node loader davranış paketi ve bütün JS syntax kontrolleri başarılı. XML diff'i yalnızca dört açıklama satırıdır. Render edilmiş Blogger ortamı bulunmadığından tarayıcı tabanlı görsel eşdeğerlik çalıştırılamadı; statik test bunun kanıtı değildir.
## 7. Tespit edilen riskler
Ana tema dosyaları production replacement değil, geçiş iskeletidir. Asıl risk canlı Blogger yorum/render koşulları ve CSS sıra bağımlılığıdır. Harici modüllere gerçek geçiş yapılmadan önce preview, klavye, CSP/CORS ve piksel karşılaştırması gerekir.
## 8. Geri dönüş yöntemi
PR merge edilmeden önce branch/PR bütünüyle terk edilebilir. Merge sonrasında PR’nin merge commit’i geri alınabilir. Bir asset entegrasyonu ayrıca yapılmışsa Blogger referansı önceki immutable sürüme döndürülür; çalışan tema başlangıç XML SHA-256 değeriyle doğrulanır.
## 9. Bir sonraki aşamaya aktarılan yapı
Production öncesi kontrollü, modül modül entegrasyon için kaynak sınırları, sürümlü assetler, fallback ve test paketi.
## 10. Açık kalan konular
320/360/375/390/430/768/1024 px gerçek Blogger preview, hover/Fon alt menü, klavye slider, static_page/item ve özel URL koşulları kullanıcı tarafından görsel olarak onaylanmalıdır.
