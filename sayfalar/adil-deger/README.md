# adil-deger yükleme sözleşmesi

- **Sayfa kimliği:** `adil-deger`; **asset sürümü:** sabit `1.0.0`. Loader bu değeri CSS, JS ve veri URL'lerine `rt-surum` olarak uygular; URL'de farklı bir sürüm varsa yüklemeyi reddeder.
- **Giriş noktası:** ortak `ortak/js/analiz-sayfasi.js`; loader `RasyoTrendSayfalar["adil-deger"]` kaydını çağırır.
- **Beklenen JSON:** gerçek alan şeması henüz sağlanmamıştır. Kökte yalnız `kayitlar` dizisi beklenir; değerler backend tarafından hazır sağlanır.
- **Null davranışı:** null/eksik alan sıfıra çevrilmez, türetilmez; sunumda “Veri yok” kullanılır.
- **Hata davranışı:** geçersiz JSON/HTTP/asset hatası ortak loader'ın okunabilir hata fallback'ine gider.
- **Şu anda kullanılan ortak modüller:** URL güvenlik yardımcısı, timeout/AbortController veri istemcisi, loader; token, temel, bileşen ve analiz CSS'i.
- **İleriki entegrasyon için hazır fakat kullanılmayanlar:** filtre, sıralama, tablo JS'i ve tablo CSS'i.
- `PUBLIC_JSON_URL_GEREKLI` gerçek onaylı public URL gelene kadar korunur. Bu iskelet canlı Blogger HTML'i değildir ve finansal puan/oran/değer hesaplamaz.
