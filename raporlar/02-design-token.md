# Aşama 2 — Ortak design token sistemi
## 1. Aşamanın amacı
Çalışan temadan alınan değerlerle yeni mimari önerilerini birbirine karıştırmadan, ASCII Türkçe adlandırılmış token sistemi üretmek.
## 2. Yapılan değişiklikler
Tokenlar iki sınıfa ayrıldı: A) çalışan XML’den birebir alınan/türetilen renk, spacing ve radius değerleri; B) yeni mimari için önerilen semantik renk, gölge, tipografi, z-index, transition ve breakpoint referansları. Python artefact’ları ignore edildi.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/css/degiskenler.css`, `tema/dokumantasyon/design-token-siniflandirmasi.md`, `.gitignore`, bu rapor; yanlışlıkla izlenen `testler/__pycache__` kaldırıldı.
## 4. Değiştirilmeyen alanlar
Tema XML'i ve görsel değerleri değiştirilmedi; tema harici CSS'e bağımlı kılınmadı.
## 5. Yapılan testler
`./testler/calistir.sh`; token kategori ve adlarının elle karşılaştırılması.
## 6. Test sonuçları
18 Python testi ve Node loader davranış paketi başarılı; token dosyası henüz runtime'a bağlanmadığından görsel değişiklik yok.
## 7. Tespit edilen riskler
Custom property breakpoint değerleri medya sorgularında doğrudan kullanılamaz; referans niteliğindedir. Pozitif/negatif/uyarı renkleri özel sayfalarda kontrast kontrolü gerektirir.
## 8. Geri dönüş yöntemi
PR merge edilmeden önce branch/PR bütünüyle terk edilebilir. Merge sonrasında PR’nin merge commit’i geri alınabilir. Bir asset entegrasyonu ayrıca yapılmışsa Blogger referansı önceki immutable sürüme döndürülür; çalışan tema başlangıç XML SHA-256 değeriyle doğrulanır.
## 9. Bir sonraki aşamaya aktarılan yapı
`ortak/css` altında sürümlenebilir tasarım sözlüğü.
## 10. Açık kalan konular
Tokenların gerçek Blogger önizlemesinde kademeli eşlenmesi Aşama 8/production öncesi incelemeye bırakıldı.
