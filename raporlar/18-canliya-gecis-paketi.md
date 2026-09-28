# 18 — Canlıya geçiş paketi
## Amaç
Kullanıcı incelemesi ve manuel aktivasyon için gerekli dosyaları tek dizinde toplamak.
## Yapılan değişiklikler
Paket README, Blogger snippet, Pages ayarı, test matrisi ve rollback talimatı hazırlandı.
## Oluşturulan/değiştirilen dosyalar
`entegrasyon/canliya-gecis/{README.md,blogger-pilot-loader.html,github-pages-ayari.md,test-kontrol-listesi.md,rollback.md}` ve bu rapor.
## Değiştirilmeyen alanlar
Pages ayarı, Blogger ve main değiştirilmedi.
## Yapılan testler
Beş zorunlu dosyanın varlığı ve Blogger snippet içerik testi.
## Test sonucu
Paket bütünlük testi başarılıdır.
## Tespit edilen riskler
GitHub arayüzünün `/pages` yayın seçeneği repository politikasına göre farklı olabilir; kullanıcı doğrulamalıdır.
## Rollback yöntemi
Snippet kaldırılır, önceki immutable asset seçilir ve gerekirse PR merge commit'i revert edilir; XML etkilenmez.
## Açık kalan konular
Kullanıcı onayı, Pages aktivasyonu ve Preview kabulü.
## Bir sonraki aşamaya aktarılan yapı
Manuel canlıya geçiş için kopyalanabilir paket.
