# Aşama 4 — Ortak CSS ve JavaScript mimarisi
## 1. Aşamanın amacı
Sorumlulukları modüllere ayırmak ve bağımsız asset temelini davranış değişikliği olmadan hazırlamak.
## 2. Yapılan değişiklikler
Ortak temel/erişilebilirlik/bileşen/tablo/analiz CSS’i; URL, timeout, hata, tablo, filtre ve sıralama JS’i; production replacement olmayan ana tema geçiş iskeletleri oluşturuldu. Null değerler `Veri yok` olarak korunur, hesaplanmaz.
## 3. Değiştirilen / oluşturulan dosyalar
`ortak/css/*`, `ortak/js/*`, `ana-tema/css/*`, `ana-tema/js/*`, bu rapor.
## 4. Değiştirilmeyen alanlar
XML harici modüllere bağlanmadı; inline çalışan uygulama, URL'ler ve Blogger yapıları değişmedi.
## 5. Yapılan testler
`./testler/calistir.sh`; tüm yeni JS dosyalarında `node --check`.
## 6. Test sonuçları
18 Python testi, Node loader davranış paketi ve tüm JavaScript syntax kontrolleri başarılı.
## 7. Tespit edilen riskler
Ana tema JavaScript modülleri yalnız geçiş iskeleti/sorumluluk sınırıdır ve XML davranışının tam eşdeğeri değildir. Production kaynağı inline XML’dir; Blogger Preview eşdeğerliği doğrulanmadan onun yerine kullanılamaz.
## 8. Geri dönüş yöntemi
PR merge edilmeden önce branch/PR bütünüyle terk edilebilir. Merge sonrasında PR’nin merge commit’i geri alınabilir. Bir asset entegrasyonu ayrıca yapılmışsa Blogger referansı önceki immutable sürüme döndürülür; çalışan tema başlangıç XML SHA-256 değeriyle doğrulanır.
## 9. Bir sonraki aşamaya aktarılan yapı
Sürümlemeye hazır framework bağımsız asset kaynakları.
## 10. Açık kalan konular
Tarayıcı entegrasyonu ve Blogger CSP/CORS davranışı production öncesi önizlemede sınanmalıdır.
