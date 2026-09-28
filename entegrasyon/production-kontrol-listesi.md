# Production doğrulama matrisi

Pages ve Blogger değişiklikleri uygulanmadığı için ağ/tarayıcı maddeleri **bekliyor** durumundadır; başarılı kabul edilmemiştir.

| Kontrol | Beklenen | Durum |
|---|---|---|
| CSS MIME | `text/css` | ⏳ Pages sonrası |
| JavaScript MIME | JavaScript uyumlu MIME | ⏳ Pages sonrası |
| JSON MIME | `application/json` | ⏳ Pages sonrası |
| HTTPS | Sertifika geçerli, mixed content yok | ⏳ Pages sonrası |
| CORS | Blogger origin JSON okuyabilir | ⏳ Pages sonrası |
| Cache headers | v1.0.0 uzun ömürlü; HTML kontrollü | ⏳ Pages sonrası |
| Immutable URL | `/assets/v1.0.0/` | ✅ Statik |
| 404 | Okunabilir fallback | ⏳ Pages sonrası |
| Timeout | 8000 ms ardından abort/fallback | ✅ Birim / ⏳ ağ |
| CSS fallback | `data-css-fallback` ve hatalı URL kaydı | ✅ Statik / ⏳ tarayıcı |
| JS hata fallback | Kullanıcı mesajı | ✅ Şablon / ⏳ tarayıcı |
| JSON hata fallback | Kullanıcı mesajı | ✅ Kod / ⏳ ağ |
| Null kayıt | Sıfıra dönüşmez | ✅ Otomatik |
| Boş kayıt | “Gösterilecek veri yok” | ✅ Kod / ⏳ tarayıcı |
| Çoklu CSS | Her URL ayrı `link` | ✅ Otomatik |
| Duplicate bootstrap | İkinci başlangıç engellenir | ✅ Şablon / ⏳ Blogger |
| Mobile viewport | 320–430 px okunabilir | ⏳ Blogger Preview |
| Desktop viewport | 768/1024+ px okunabilir | ⏳ Blogger Preview |
| Klavye | Odak sırası kullanılabilir | ⏳ Blogger Preview |
| Escape | Tema navigasyonu korunur | ⏳ Blogger Preview |
| `aria-live` | Loading/hata duyurulur | ✅ Şablon / ⏳ AT |
