# 09 — Canlı entegrasyon başlangıç doğrulaması

## Amaç
Main'e merge edilmiş frontend v1 yapısının pilot entegrasyon öncesi güvenli başlangıç durumunu doğrulamak.
## Yapılan değişiklikler
Dizinler, v1.0.0 asset ağacı, manifest, loader, veri istemcisi, URL yardımcısı, pilot ve test dosyaları kontrol edildi; başlangıç XML SHA-256 kaydedildi.
## Oluşturulan/değiştirilen dosyalar
Bu rapor oluşturuldu.
## Değiştirilmeyen alanlar
Tema XML'i, Blogger, Pages ayarları ve public JSON bağlantıları değiştirilmedi.
## Yapılan testler
`./testler/calistir.sh`, dosya/dizin varlığı ve `sha256sum tema/rasyotrend-tema.xml`.
## Test sonucu
18 Python testi ve Node loader paketi başarılıdır. Başlangıç XML SHA-256: `94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513`.
## Tespit edilen riskler
GitHub Pages etkin değildir; public origin üzerinden HTTP/CORS/MIME testi yapılamaz.
## Rollback yöntemi
PR merge edilmeden branch terk edilir; merge sonrasında PR merge commit'i geri alınır. XML başlangıç SHA ile doğrulanır.
## Açık kalan konular
Production origin kullanıcı tarafından etkinleştirilmelidir.
## Bir sonraki aşamaya aktarılan yapı
Testleri geçen v1.0.0 kaynak ve dağıtım tabanı.
