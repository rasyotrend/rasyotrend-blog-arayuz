# Rollback

1. Blogger pilot özel sayfasındaki entegrasyon snippet'ini kaldırın veya önceki içerikle değiştirin.
2. Daha önce doğrulanmış immutable asset sürümü varsa snippet URL'lerini o sürüme geri döndürün; `latest` kullanmayın.
3. Repository değişikliği sorunluysa ilgili PR merge commit'ini revert edin; geçmişi yeniden yazmayın.
4. `tema/rasyotrend-tema.xml` pilot tarafından değiştirilmediğinden ana tema rollback'i gerekmez; SHA-256 ile bütünlüğü doğrulayın.
5. Pages'i kapatmak gerekiyorsa yalnız repository yöneticisi Settings → Pages üzerinden işlem yapmalıdır.
