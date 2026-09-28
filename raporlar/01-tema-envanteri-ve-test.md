# Aşama 1 — Tema envanteri ve test altyapısı

## 1. Aşamanın amacı
Çalışan v040 temasını değiştirmeden CSS, JavaScript, erişilebilirlik ve responsive davranış envanterini çıkarmak; regresyon sınırlarını otomatikleştirmek.
## 2. Yapılan değişiklikler
Tema salt okunur incelendi; envanter dokümanı, XML/Blogger/slider/navigasyon/güvenlik testleri ve test çalıştırıcısı eklendi.
## 3. Değiştirilen / oluşturulan dosyalar
`tema/dokumantasyon/envanter.md`, `testler/test_tema.py`, `testler/calistir.sh`, bu rapor.
## 4. Değiştirilmeyen alanlar
`tema/rasyotrend-tema.xml`, menü URL'leri, Blogger render akışı ve canlı site değiştirilmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; XML parse, kritik ifadeler, 16:9/contain, erişilebilirlik, URL/fetch sınırı, finansal hesaplama yasağı ve Actions yokluğu.
## 6. Test sonuçları
8 statik test başarılı. Tarayıcı tabanlı test için render edilmiş Blogger fixture'ı ve tarayıcı bağımlılığı bulunmadığından çalıştırılmadı.
## 7. Tespit edilen riskler
CSS override sırası hassastır; statik test görsel eşdeğerlik kanıtı değildir. Skip link eksiktir. Koşullu Blogger DOM'u yerel XML parse ile bütünüyle modellenemez.
## 8. Geri dönüş yöntemi
Bu aşama commit'i geri alınır; tema dosyası değişmediği için production rollback gerekmez.
## 9. Bir sonraki aşamaya aktarılan yapı
Tek komutlu regresyon paketi ve ayrıntılı selector/script envanteri.
## 10. Açık kalan konular
Canlıya geçmeden önce Blogger önizlemesinde 320/360/375/390/430/768/1024 px görsel ve klavye testi gereklidir.
