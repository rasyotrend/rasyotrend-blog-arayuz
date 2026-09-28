# Aşama 7 — Loader mimarisini özel sayfalara yaygınlaştırma
## 1. Aşamanın amacı
Pilot API'yi sekiz planlanan analiz sayfası için tekrar etmeyen standart sözleşmeye dönüştürmek.
## 2. Yapılan değişiklikler
Sekiz README/yükleme JSON sözleşmesi ve tek ortak analiz giriş noktası eklendi. Hazır kayıtlar yalnızca doğrulanır/gösterilir; hesaplanmaz.
## 3. Değiştirilen / oluşturulan dosyalar
Sekiz `sayfalar/*/README.md`, sekiz `yukleme.json`, `ortak/js/analiz-sayfasi.js`, Pages kopyası/manifest, `testler/test_sayfalar.py`, bu rapor.
## 4. Değiştirilmeyen alanlar
Gerçek Blogger sayfaları, public veri URL'leri ve tema XML'i değiştirilmedi; placeholder URL bilinçli olarak publish edilmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; sekiz sözleşme, sabit sürüm, null ilkesi, ortak giriş ve finansal hesaplama sınırı.
## 6. Test sonuçları
15 statik test ve bütün JS syntax kontrolleri başarılı.
## 7. Tespit edilen riskler
Şemalar minimaldir; gerçek public JSON sözleşmeleri repository'de olmadığından alan bazlı doğrulama production öncesi tamamlanmalıdır.
## 8. Geri dönüş yöntemi
Commit geri alınır; canlı entegrasyon olmadığından kullanıcı etkisi yoktur.
## 9. Bir sonraki aşamaya aktarılan yapı
Sekiz sayfa için ortak loader/entry ve belgelenmiş null/hata davranışı.
## 10. Açık kalan konular
Onaylı public JSON URL'leri ve her sayfanın alan şeması veri sahibiyle netleştirilmelidir.
