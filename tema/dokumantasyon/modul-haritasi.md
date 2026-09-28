# Tema modül haritası v1.0.0

| Sorumluluk | Kaynak modül | Blogger fallback |
|---|---|---|
| Token/temel/erişilebilirlik | `ortak/css/*` | `b:skin` içinde korunur |
| Yerleşim/navigasyon/slider/içerik/sidebar | `ana-tema/css/*` | `b:skin` ve responsive override zinciri korunur |
| URL/fetch/hata | `ortak/js/*` | slider inline IIFE içinde korunur |
| Navigasyon/slider/kategori | `ana-tema/js/*` | ana inline script içinde korunur |
| Blogger render/yorum/pagination | XML | yalnızca XML içinde kalır |

Bu sürümde dış modüller tema tarafından çağrılmaz. Böylece CDN/Pages başarısızlığı yeni bir production bağımlılığı oluşturmaz. Modüler dosyalar kontrollü geliştirme ve ileride Blogger önizlemesinde tek tek geçiş için sınırları tanımlar; çalışan inline uygulama davranış eşdeğerliği fallback'idir.
