# 16 — Entegrasyon testleri
## Amaç
Production/local URL, pilot, Blogger şablonu, Pages bütünlüğü ve değişmez güvenlik sınırlarını otomatik doğrulamak.
## Yapılan değişiklikler
8 yeni Python entegrasyon testi ve Node yapılandırma kontrolleri eklendi; eski pilot sözleşme testi merkezi ayara uyarlandı.
## Oluşturulan/değiştirilen dosyalar
`testler/test_entegrasyon.py`, `testler/test_loader.py`, `testler/test_loader_url.js` ve bu rapor.
## Değiştirilmeyen alanlar
Mevcut testler kaldırılmadı; Actions eklenmedi.
## Yapılan testler
`./testler/calistir.sh`: 26 Python test metodu, 21 Node assertion, tüm JS için `node --check`.
## Test sonucu
Final koşuda tüm kontroller başarılıdır. Geliştirme sırasında eski pilot assertion'ı merkezi config'e geçişi ve iki hatalı relative URL base kullanımı yakaladı; testler kaldırılmadan kod/test sözleşmesi düzeltilip yeniden çalıştırıldı.
## Tespit edilen riskler
Gerçek Pages HTTP, Blogger Preview ve görsel test ortamı bulunmadığından otomasyon bunları kanıtlamaz.
## Rollback yöntemi
PR revert edilir; XML ve dış sistemler etkilenmemiştir.
## Açık kalan konular
Production matrisindeki bekleyen ağ/tarayıcı maddeleri.
## Bir sonraki aşamaya aktarılan yapı
47 otomatik assertion/test ve syntax kontrolüyle doğrulanmış paket.
