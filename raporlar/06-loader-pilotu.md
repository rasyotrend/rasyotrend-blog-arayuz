# Aşama 6 — Özel sayfa loader pilotu
## 1. Aşamanın amacı
Gerçek Blogger sayfasına dokunmadan küçük loader ile sürümlü CSS/JS/veri/fallback yaklaşımını kanıtlamak.
## 2. Yapılan değişiklikler
Ortak loader; çoklu CSS, tek-string geriye uyumluluğu, sürümün `rt-surum` URL parametresine bağlanması, merkezi URL güvenliği ve ayrıntılı CSS fallback bilgisiyle güncellendi. Pilot veri okumada timeout/AbortController sağlayan ortak istemciyi kullanır.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/js/sayfa-loader.js`, `sayfalar/pilot-loader/*`, sürümlü Pages kopyası/manifest, `testler/test_loader.py`, bu rapor.
## 4. Değiştirilmeyen alanlar
Gerçek özel Blogger kaynağı olmadığı kabul edildi; canlı sayfa ve tema XML'i değiştirilmedi, gerçek finansal veri üretilmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; loader çoklu CSS, sürüm, relative URL, tehlikeli scheme reddi, ortak veri istemcisi, null koruma, fallback ve JS syntax kontrolleri.
## 6. Test sonuçları
18 Python testi ile Node URL/çoklu CSS davranış paketi başarılı. Pilot dosyaları tarayıcıda sunucu üzerinden çalışmaya hazırdır.
## 7. Tespit edilen riskler
`file://` altında fetch tarayıcı güvenliği nedeniyle çalışmayabilir; HTTP sunucusu gerekir. Gerçek Pages/Blogger CORS ve CSP henüz doğrulanmadı.
## 8. Geri dönüş yöntemi
PR merge edilmeden önce branch/PR bütünüyle terk edilebilir. Merge sonrasında PR’nin merge commit’i geri alınabilir. Bir asset entegrasyonu ayrıca yapılmışsa Blogger referansı önceki immutable sürüme döndürülür; çalışan tema başlangıç XML SHA-256 değeriyle doğrulanır.
## 9. Bir sonraki aşamaya aktarılan yapı
Tek ortak loader API'si ve durum sözleşmesi.
## 10. Açık kalan konular
Gerçek origin adresleri ancak Pages etkinleştirme ve kullanıcı onayı sonrası konfigüre edilmelidir.
