# teknik-analiz yükleme sözleşmesi

- **Sayfa kimliği:** `teknik-analiz`; **asset sürümü:** sabit `1.0.0`.
- **Giriş noktası:** ortak `ortak/js/analiz-sayfasi.js`; loader `RasyoTrendSayfalar["teknik-analiz"]` kaydını çağırır.
- **Beklenen JSON:** kökte `kayitlar` dizisi ve isteğe bağlı `guncellenme`; değerler backend tarafından hazır sağlanır.
- **Null davranışı:** null/eksik alan sıfıra çevrilmez, türetilmez; sunumda “Veri yok” kullanılır.
- **Hata davranışı:** geçersiz JSON/HTTP/asset hatası ortak loader'ın okunabilir hata fallback'ine gider.
- **Ortak bileşenler:** token, temel, erişilebilirlik, bileşen, tablo ve analiz CSS'i; veri istemcisi, filtre ve sıralama JS'i.
- Bu iskelet canlı Blogger HTML'i değildir ve hiçbir finansal puan/oran/değer hesaplamaz.
