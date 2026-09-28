# Public JSON entegrasyon sözleşmesi

> Pilot `ornek.json` yalnız test verisidir. Gerçek analiz sayfalarındaki `PUBLIC_JSON_URL_GEREKLI` değiştirilmemiştir.

- URL mutlaka `https:` olmalı ve production `izinliOriginler` listesinde açıkça tanımlanmış onaylı origin'den gelmelidir.
- İstemci `ortak/js/veri-istemcisi.js` olmalı; varsayılan timeout 8000 ms ve `AbortController` kullanılmalıdır.
- HTTP `2xx` dışı yanıtlar hata sayılmalı; teknik ayrıntı yerine okunabilir fallback gösterilmelidir.
- Minimum zarf `{ "kayitlar": [] }` biçimidir. Alan bazlı finansal şema veri sahibi tarafından ayrıca sağlanmadan uydurulmaz.
- `null` ve eksik değerler `0` yapılmaz, tahmin edilmez; “Veri yok” olarak sunulur.
- Frontend yalnız hazır veriyi doğrular, filtreler, sıralar, biçimlendirir ve gösterir; puan, oran, skor veya adil değer hesaplamaz.
- JSON response MIME türü ve Blogger origin'ine CORS izni production kontrol listesinde doğrulanmalıdır.
