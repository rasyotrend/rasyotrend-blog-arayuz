# Rollback

1. **Blogger:** Özel sayfadaki pilot snippet'ini kaldırın veya yayın öncesi yedeğine dönün. Önizleyip kaydedin; tema XML'ine dokunmayın.
2. **Asset sürümü:** Sorun yeni bir sürümdeyse Blogger referansını doğrulanmış önceki immutable `/assets/vX.Y.Z/` dizinine döndürün. `v1.0.0` byte'larını yerinde değiştirmeyin.
3. **Git:** Merge edilmiş değişiklik için merge commit/PR'ı yeni bir revert PR ile geri alın; geçmişi force-push ile yeniden yazmayın. Merge edilmemiş PR kapatılabilir.
4. **Doğrulama:** Blogger fallback, ağ istekleri ve production matrisi tekrar kontrol edilir.

`tema/rasyotrend-tema.xml` bu pilotta değişmediğinden tema rollback'i gerekmemelidir; başlangıç SHA-256 değeri `94b777d41530571558abc42ec371932d06f4dc0253a2ee7e6955e591ba57e513` olarak doğrulanmalıdır.
