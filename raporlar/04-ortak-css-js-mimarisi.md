# Aşama 4 — Ortak CSS ve JavaScript mimarisi
## 1. Aşamanın amacı
Sorumlulukları modüllere ayırmak ve bağımsız asset temelini davranış değişikliği olmadan hazırlamak.
## 2. Yapılan değişiklikler
Ortak temel/erişilebilirlik/bileşen/tablo/analiz CSS'i; URL, timeout, hata, tablo, filtre ve sıralama JS'i; ana tema sorumluluk dosyaları oluşturuldu. Null değerler `Veri yok` olarak korunur, hesaplanmaz.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/css/*`, `ortak/js/*`, `ana-tema/css/*`, `ana-tema/js/*`, bu rapor.
## 4. Değiştirilmeyen alanlar
XML harici modüllere bağlanmadı; inline çalışan uygulama, URL'ler ve Blogger yapıları değişmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; tüm yeni JS dosyalarında `node --check`.
## 6. Test sonuçları
Tema testleri ve JavaScript syntax kontrolleri başarılı.
## 7. Tespit edilen riskler
Ana tema modülleri henüz yalnızca kontrollü geçiş yüzeyidir; XML ile birlikte çalıştırılırsa iki kez başlatmayı önleyen bootstrap gerekir.
## 8. Geri dönüş yöntemi
Commit geri alınır; XML bağımsız olduğundan kullanıcı görünümü değişmez.
## 9. Bir sonraki aşamaya aktarılan yapı
Sürümlemeye hazır framework bağımsız asset kaynakları.
## 10. Açık kalan konular
Tarayıcı entegrasyonu ve Blogger CSP/CORS davranışı production öncesi önizlemede sınanmalıdır.
