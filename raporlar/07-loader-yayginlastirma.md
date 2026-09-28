# Aşama 7 — Loader mimarisini özel sayfalara yaygınlaştırma
## 1. Aşamanın amacı
Pilot API'yi sekiz planlanan analiz sayfası için tekrar etmeyen standart sözleşmeye dönüştürmek.
## 2. Yapılan değişiklikler
Sekiz README/yükleme JSON sözleşmesi loader’ın çoklu CSS ve sürüm modeline uyumludur. Tek ortak analiz giriş noktası veriyi ortak timeout/AbortController istemcisiyle okur; hazır kayıtlar yalnızca doğrulanır/gösterilir, hesaplanmaz.
## 3. Değiştirilen / oluşturulan dosyalar
Sekiz `sayfalar/*/README.md`, sekiz `yukleme.json`, `ortak/js/analiz-sayfasi.js`, Pages kopyası/manifest, `testler/test_sayfalar.py`, bu rapor.
## 4. Değiştirilmeyen alanlar
Gerçek Blogger sayfaları, public veri URL'leri ve tema XML'i değiştirilmedi; placeholder URL bilinçli olarak publish edilmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; sekiz sözleşme, sabit sürüm, null ilkesi, ortak giriş ve finansal hesaplama sınırı.
## 6. Test sonuçları
18 Python testi, sekiz loader sözleşmesi, Node davranış paketi ve bütün JS syntax kontrolleri başarılı.
## 7. Tespit edilen riskler
Şemalar minimaldir; gerçek public JSON sözleşmeleri repository'de olmadığından alan bazlı doğrulama production öncesi tamamlanmalıdır.
## 8. Geri dönüş yöntemi
PR merge edilmeden önce branch/PR bütünüyle terk edilebilir. Merge sonrasında PR’nin merge commit’i geri alınabilir. Bir asset entegrasyonu ayrıca yapılmışsa Blogger referansı önceki immutable sürüme döndürülür; çalışan tema başlangıç XML SHA-256 değeriyle doğrulanır.
## 9. Bir sonraki aşamaya aktarılan yapı
Sekiz sayfa için ortak loader/entry ve belgelenmiş null/hata davranışı.
## 10. Açık kalan konular
Onaylı public JSON URL'leri ve her sayfanın alan şeması veri sahibiyle netleştirilmelidir.
