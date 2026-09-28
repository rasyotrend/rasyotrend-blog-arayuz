# Aşama 6 — Özel sayfa loader pilotu
## 1. Aşamanın amacı
Gerçek Blogger sayfasına dokunmadan küçük loader ile sürümlü CSS/JS/veri/fallback yaklaşımını kanıtlamak.
## 2. Yapılan değişiklikler
Ortak loader, bağımsız pilot HTML/CSS/JS ve null içeren sahte JSON eklendi. Loading, CSS fallback, JS/data hata ve `aria-live` durumları tanımlandı.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/js/sayfa-loader.js`, `sayfalar/pilot-loader/*`, sürümlü Pages kopyası/manifest, `testler/test_loader.py`, bu rapor.
## 4. Değiştirilmeyen alanlar
Gerçek özel Blogger kaynağı olmadığı kabul edildi; canlı sayfa ve tema XML'i değiştirilmedi, gerçek finansal veri üretilmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; loader sözleşmesi, null koruma, fallback ve JS syntax kontrolleri.
## 6. Test sonuçları
13 statik test başarılı. Pilot dosyaları tarayıcıda sunucu üzerinden çalışmaya hazırdır.
## 7. Tespit edilen riskler
`file://` altında fetch tarayıcı güvenliği nedeniyle çalışmayabilir; HTTP sunucusu gerekir. Gerçek Pages/Blogger CORS ve CSP henüz doğrulanmadı.
## 8. Geri dönüş yöntemi
Pilot ve loader commit'i geri alınır; canlı entegrasyon bulunmadığından production etkisi yoktur.
## 9. Bir sonraki aşamaya aktarılan yapı
Tek ortak loader API'si ve durum sözleşmesi.
## 10. Açık kalan konular
Gerçek origin adresleri ancak Pages etkinleştirme ve kullanıcı onayı sonrası konfigüre edilmelidir.
