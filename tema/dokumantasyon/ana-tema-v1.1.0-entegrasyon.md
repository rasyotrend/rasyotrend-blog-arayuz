# Ana tema v1.1.0 canlı entegrasyon kaydı

## Mimari ve kapsam

`tema/rasyotrend-tema.xml` production kaynak alınmıştır. `b:skin` içindeki çalışan görünüm `ana-tema/css/ana-tema.css` dosyasına eşdeğer olarak taşınmıştır. Ortak first-render sözleşmesi `ortak/css/tema-cekirdegi.css`, tek-sefer çalışma kaydı `ortak/js/tema-runtime.js` ve navigasyon, slider ile kategori sıralama davranışlarının tamamı `ana-tema/js/ana-tema.js` içindedir.

Blogger render yapıları, widget/section/loop/if ifadeleri, menü bağlantıları, özel sayfa içerikleri, yayınlar, yorumlar ve pagination şablonları değiştirilmemiştir. Yeni menü veya sayfa eklenmemiştir. Masaüstü hover ve iki seviyeli Fon menüsü CSS ile; mobil `details`, Escape ve dış tıklama davranışı JavaScript ile korunur. Slider 16:9 medya, ok, nokta, klavye, kaydırma ve erişilebilir durum metnini korur.

## Güvenli yükleme ve fallback

XML, sürümlü ve sabit HTTPS origininden önce ortak runtime'ı, sonra ana tema runtime'ını yükler. Sekiz saniyelik zaman aşımı, ağ hatası, eksik giriş noktası veya senkron başlatma hatasında XML içinde korunan production davranışı devreye girer. `__RASYOTREND_V11__.baslatilan['ana-tema']` sahiplik kaydı external ve fallback kodunun aynı davranışı iki kez başlatmasını engeller. `b:skin` tamamen korunduğundan harici CSS yüklenemese de kritik first-render kaybolmaz ve sayfa boş kalmaz.

## Bütünlük

- Entegrasyon öncesi XML SHA-256: `94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513`
- Entegrasyon sonrası XML SHA-256: `d2de23ef55263ec5d4bbfd7307f63bda35b3abeff7be9d949b91ea13c2b9fff7`
- Asset kökü: `https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.1.0/`
- Manifest: `https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.1.0/manifest.json`

Manifest her yayın dosyasının SHA-256 özetini içerir. `docs/assets/v1.0.0/` immutable bırakılmıştır.

## Manuel yükleme ve rollback

Blogger'a manuel yüklenecek dosya: `tema/rasyotrend-tema.xml`.

Sorunda Blogger'a son çalışan XML tekrar yüklenmelidir. Repository'den birebir geri alma:

```bash
git show 33b160d:tema/rasyotrend-tema.xml > /tmp/rasyotrend-tema-rollback.xml
sha256sum /tmp/rasyotrend-tema-rollback.xml
# Beklenen: 94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513
```

Yüklemeden önce Blogger tema yedeği ayrıca indirilmelidir. Preview'da masaüstü/mobil menüler, Fon ikinci seviye menüsü, ana sayfa slider'ı, etiket sıralaması, yazı detayı, yorumlar ve pagination kontrol edilmelidir. GitHub Pages URL'lerinin 200 ve doğru MIME tipi döndürdüğü doğrulanmalıdır. Bu repository çalışması Blogger'a deploy veya `main` branch'ine merge yapmaz.
