# Production kontrol matrisi

Bu liste canlı HTTP, GitHub Pages ve Blogger ortamında kullanıcı tarafından yürütülmelidir. Repository testleri bu maddeleri geçmiş sayılmaz.

| Alan | Kabul ölçütü | Durum |
|---|---|---|
| CSS MIME | `text/css`; stil uygulanıyor | Bekliyor |
| JavaScript MIME | JavaScript uyumlu MIME; çalışıyor | Bekliyor |
| JSON MIME | `application/json`; parse ediliyor | Bekliyor |
| HTTPS | Tüm istekler HTTPS, mixed content yok | Bekliyor |
| CORS | Yalnız onaylı origin yanıt alıyor | Bekliyor |
| cache | Sürümlü asset uzun süre cache edilebilir; HTML/config politikası doğrulanır | Bekliyor |
| immutable version | URL `/assets/v1.0.0/`; mevcut byte'lar değişmez | Hazır/statik |
| 404 | CSS, JS ve JSON 404'lerinde anlaşılır fallback | Bekliyor |
| timeout | 8 saniye sonunda abort ve fallback | Bekliyor |
| CSS fallback | İçerik okunabilir, `data-css-fallback` işaretli | Bekliyor |
| JS fallback | Kullanıcı mesajı görünür | Bekliyor |
| JSON fallback | Kullanıcı mesajı görünür | Bekliyor |
| null kayıt | “Veri yok”; sıfır değil | Hazır/statik |
| boş kayıt | Hatasız boş durum | Bekliyor |
| çoklu CSS | Dört stylesheet sıralı yükleniyor | Hazır/statik |
| duplicate loader | İkinci bootstrap ağacı başlatmıyor | Hazır/statik |
| mobile | 320–430 px taşma/okunabilirlik | Bekliyor |
| desktop | 768/1024+ px düzen | Bekliyor |
| klavye | Odak sırası ve tetikler kullanılabilir | Bekliyor |
| Escape | Açılır bileşen varsa kapatır; pilotta uygulanamaz | Kapsam dışı |
| aria-live | Loading, başarı/hata değişimi yardımcı teknolojiye iletiliyor | Bekliyor |
