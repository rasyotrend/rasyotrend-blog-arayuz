# 12 — Pilot production modu
## Amaç
Aynı pilotun local/test ve production URL modlarında kod tekrarı olmadan çalışmasını sağlamak.
## Yapılan değişiklikler
Local sayfa query-parametreyle mod seçer; public Pages pilotu production ayarını kullanır. Pilot JSON'un sahte/test verisi olduğu belgelendi.
## Oluşturulan/değiştirilen dosyalar
`sayfalar/pilot-loader/index.html`, `README.md`, `pages/pilot/index.html`, versioned pilot assetleri ve bu rapor.
## Değiştirilmeyen alanlar
Analiz sayfalarının `PUBLIC_JSON_URL_GEREKLI` değerleri ve finansal hesaplama sınırı korunmuştur.
## Yapılan testler
İki mod, çoklu CSS, JS/data yolları, null ve fallback kontrolleri.
## Test sonucu
Yerel otomatik testler başarılı; production HTTP testi henüz çalıştırılmadı.
## Tespit edilen riskler
Blogger CSP ve Pages CORS davranışı gerçek ortamda doğrulanmalıdır.
## Rollback yöntemi
Pilot kodu kaldırılır veya PR revert edilir; XML etkilenmez.
## Açık kalan konular
Pages etkinleştirme sonrası mobil/desktop tarayıcı testi.
## Bir sonraki aşamaya aktarılan yapı
Blogger şablonunun kullanacağı immutable URL sözleşmesi.
