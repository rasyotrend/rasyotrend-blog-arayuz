# Loader pilotu

Bu pilot yalnız sahte `ornek.json` verisini gösterir; gerçek finansal veri değildir.

- **Local/test:** `index.html` varsayılan olarak relative `ortak/` ve pilot yollarını kullanır.
- **Production:** `index.html?mod=production`, asset ve test JSON yollarını immutable `https://rasyotrend.github.io/rasyotrend-blog-arayuz/assets/v1.0.0/` köküne çözer. URL ancak Pages kullanıcı tarafından etkinleştirilince çalışır.
- Tek sürüm kaynağı `ortak/js/asset-yapilandirmasi.js` içindeki `SURUM` sözleşmesidir; loader `rt-surum` parametresini uygular.

Production HTTP/CORS/MIME doğrulaması Pages etkin olmadığı için henüz yapılmamıştır.
