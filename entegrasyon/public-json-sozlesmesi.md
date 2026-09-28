# Public JSON sözleşmesi

## Güvenlik sınırı

- Veri adresi yalnız **HTTPS** olmalıdır. `javascript:`, `data:` ve diğer şemalar reddedilir.
- Production'da kesin origin allowlist kullanılır; yönlendirme sonrası adresin de beklenen origin/CORS politikasına uygunluğu sunucuda sağlanır. Kullanıcı girdisi URL olarak birleştirilmez.
- JSON sunucusu yalnız gerekli Blogger ve GitHub Pages originlerine `Access-Control-Allow-Origin` vermeli; gizli anahtar, token, kişisel veri ve erişim bilgisi public JSON'a konmamalıdır.
- Gerçek analiz sayfalarındaki `PUBLIC_JSON_URL_GEREKLI` değeri, veri sahibi onayı ve endpoint doğrulaması tamamlanana kadar korunur. Pilotun `ornek.json` dosyası yalnız test verisidir.

## İstek davranışı

Ortak veri istemcisi güvenli URL kontrolünden sonra `fetch` çağırır. Varsayılan timeout 8 saniyedir; `AbortController` süresi dolan isteği iptal eder ve timer her sonuçta temizlenir. HTTP `2xx` dışındaki yanıtlar `HTTP <durum>` hatasına dönüşür. Ağ, parse, CORS, timeout ve HTTP hataları loader'ın kullanıcıya görünür fallback'ine gider.

## Minimum JSON sözleşmesi

```json
{"baslik":"Metin","maddeler":["Metin",null]}
```

- Kök değer nesne; `baslik` görüntülenecek metin; `maddeler` dizi olmalıdır.
- `null`, **0 değildir** ve “Veri yok” olarak gösterilir. Frontend eksik/null değeri sıfıra çeviremez.
- Boş `maddeler` geçerlidir ve boş liste üretir; “sonuç yok” sunumu sayfa bileşeninin sorumluluğudur.
- Frontend finansal hesaplama, oran üretme, yuvarlama veya veri türetme yapmaz; yalnız doğrulanmış sunucu çıktısını sunar.
