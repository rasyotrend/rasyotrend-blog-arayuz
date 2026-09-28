# Aşama 2 — Ortak design token sistemi
## 1. Aşamanın amacı
Ana tema ve gelecekteki analiz sayfaları için mevcut koyu tema değerlerinden ortak, ASCII Türkçe adlandırılmış token sistemi üretmek.
## 2. Yapılan değişiklikler
Renk, spacing, radius, shadow, tipografi, font weight, line height, z-index, transition ve breakpoint referansları tanımlandı; Python artefact'ları ignore edildi.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/css/degiskenler.css`, `.gitignore`, bu rapor; yanlışlıkla izlenen `testler/__pycache__` kaldırıldı.
## 4. Değiştirilmeyen alanlar
Tema XML'i ve görsel değerleri değiştirilmedi; tema harici CSS'e bağımlı kılınmadı.
## 5. Yapılan testler
`./testler/calistir.sh`; token kategori ve adlarının elle karşılaştırılması.
## 6. Test sonuçları
Statik tema testleri başarılı; token dosyası henüz runtime'a bağlanmadığından görsel değişiklik yok.
## 7. Tespit edilen riskler
Custom property breakpoint değerleri medya sorgularında doğrudan kullanılamaz; referans niteliğindedir. Pozitif/negatif/uyarı renkleri özel sayfalarda kontrast kontrolü gerektirir.
## 8. Geri dönüş yöntemi
Commit geri alınır; tema bağımlı olmadığı için çalışma görünümü etkilenmez.
## 9. Bir sonraki aşamaya aktarılan yapı
`ortak/css` altında sürümlenebilir tasarım sözlüğü.
## 10. Açık kalan konular
Tokenların gerçek Blogger önizlemesinde kademeli eşlenmesi Aşama 8/production öncesi incelemeye bırakıldı.
