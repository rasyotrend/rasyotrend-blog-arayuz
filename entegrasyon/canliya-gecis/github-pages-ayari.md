# GitHub Pages ayarı — kullanıcı işlemi

GitHub Pages branch kaynağı arayüzü yalnız branch kökü (`/`) veya `/docs` seçeneğini destekler; repository içindeki `/pages` doğrudan seçilemeyebilir. Beklenen URL'de fazladan `/pages/` oluşmaması için önerilen Actions'sız yöntem ayrı bir yayın branch'idir.

1. Bu PR kullanıcı incelemesiyle main'e merge edildikten sonra, `pages/` **içeriğini** (klasörün kendisini değil) kökünde taşıyan `gh-pages` yayın branch'ini manuel ve doğrulanabilir biçimde hazırlayın.
2. GitHub repository **Settings → Pages** bölümünü açın.
3. **Build and deployment / Source** için **Deploy from a branch** seçin; GitHub Actions seçmeyin.
4. Branch olarak `gh-pages`, klasör olarak `/(root)` seçip kaydedin.
5. `https://rasyotrend.github.io/rasyotrend-blog-arayuz/` adresinin hazır olmasını bekleyin.
6. Manifest/source eşitliği, pilot, MIME, CORS ve cache kontrollerini tamamlamadan Blogger kodunu yayınlamayın.

Bu çalışma branch/Pages ayarı oluşturmaz, push/deploy yapmaz. Yayın branch'inin hazırlanması ve Pages aktivasyonu repository yöneticisinin manuel işlemidir.
