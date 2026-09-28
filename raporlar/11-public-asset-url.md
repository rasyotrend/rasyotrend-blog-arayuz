# 11 — Public asset URL çözümleme
## Amaç
Local relative yolları production immutable URL'lerinden tek sözleşmeyle ayırmak.
## Yapılan değişiklikler
`asset-yapilandirmasi.js`, `1.0.0` sürümü ve production kökünü tek yerde tanımlar; pilot ayarını moda göre üretir. `rt-surum` korunur.
## Oluşturulan/değiştirilen dosyalar
`ortak/js/asset-yapilandirmasi.js`, Pages kopyası/manifest ve bu rapor.
## Değiştirilmeyen alanlar
URL güvenlik yardımcısı ve tehlikeli scheme reddi korunmuştur.
## Yapılan testler
Local/production mod, HTTPS kök, semver, relative URL ve scheme reddi testleri.
## Test sonucu
Statik ve Node davranış testleri başarılıdır.
## Tespit edilen riskler
Production origin etkinleştirilmeden ağ erişimi kanıtlanamaz.
## Rollback yöntemi
PR revert edilir; gerçek entegrasyonda önceki immutable URL'ye dönülür.
## Açık kalan konular
Pages aktivasyonu sonrası gerçek origin smoke testi gerekir.
## Bir sonraki aşamaya aktarılan yapı
Tek merkezli pilot ayar üreticisi.
