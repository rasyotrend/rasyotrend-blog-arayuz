(function (global) {
  'use strict';
  function calistir() {
  (function () {
    var current = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('.nav-list a').forEach(function (link) {
      if ((new URL(link.href).pathname.replace(/\/$/, '') || '/') === current) link.setAttribute('aria-current', 'page');
    });
  }());

  (function () {
    'use strict';
    var panel = document.getElementById('news-slider');
    if (!panel) return;
    var track = panel.querySelector('.news-track');
    var dots = panel.querySelector('.news-dots');
    var controls = panel.querySelector('.news-controls');
    var status = panel.querySelector('.news-status');
    var message = panel.querySelector('.news-empty');
    function showMessage(title, detail) {
      message.querySelector('h3').textContent = title;
      message.querySelector('p').textContent = detail;
      message.hidden = false; track.hidden = true; controls.hidden = true;
    }
    showMessage('Öne çıkan içerikler yükleniyor…', 'İçerikler hazırlanıyor.');
    var slides = [], index = 0, scrollTimer;
    function safeURL(value) {
      if (typeof value !== 'string' || !value.trim()) return '';
      try { var url = new URL(value, window.location.href); return /^https?:$/.test(url.protocol) ? url.href : ''; } catch (error) { return ''; }
    }
    function element(tag, className, text) {
      var node = document.createElement(tag); node.className = className;
      if (text !== undefined) node.textContent = text; return node;
    }
    function sync() {
      slides.forEach(function (slide, i) {
        var active = i === index;
        slide.setAttribute('aria-hidden', String(!active));
        slide.querySelectorAll('a').forEach(function (link) { link.tabIndex = active ? 0 : -1; });
        dots.children[i].setAttribute('aria-current', String(active));
      });
      status.textContent = (index + 1) + ' / ' + slides.length + ' — ' + slides[index].querySelector('.news-title').textContent;
    }
    function go(next) {
      index = (next + slides.length) % slides.length;
      track.scrollTo({ left: index * track.clientWidth, behavior: 'auto' });
      sync();
    }
    var controller = new AbortController();
    var timeout = window.setTimeout(function () { controller.abort(); }, 8000);
    fetch(panel.getAttribute('data-feed-url'), { signal: controller.signal, credentials: 'same-origin' })
      .then(function (response) { if (!response.ok) throw new Error('Feed unavailable'); return response.json(); })
      .then(function (data) {
        var entries = data && data.feed && data.feed.entry;
        if (!Array.isArray(entries)) entries = [];
        entries.slice(0, 5).forEach(function (entry) {
          if (!entry || !Array.isArray(entry.link)) return;
          var alternate = entry.link.find(function (link) { return link.rel === 'alternate'; });
          var href = safeURL(alternate && alternate.href);
          if (!href) return;
          var title = entry.title && entry.title.$t || 'Öne çıkan içerik';
          var slide = element('article', 'news-slide');
          slide.setAttribute('role', 'group'); slide.setAttribute('aria-roledescription', 'slayt');
          var media = element('div', 'news-media'); media.setAttribute('aria-hidden', 'true');
          var imageURL = safeURL(entry.media$thumbnail && entry.media$thumbnail.url);
          if (imageURL) {
            imageURL = imageURL
              .replace(/\/s\d+(?:-c)?\//, '/s1200/')
              .replace(/=s\d+(?:-c)?(?:$|&)/, '=s1200$1');
          }
          if (imageURL) {
            var img = element('img', ''); img.alt = ''; img.decoding = 'async';
            img.loading = slides.length === 0 ? 'eager' : 'lazy';
            img.addEventListener('error', function () { img.remove(); }); img.src = imageURL; media.appendChild(img);
          }
          var copy = element('div', 'news-copy'); copy.appendChild(element('div', 'eyebrow', 'RASYOTREND'));
          var heading = element('h3', 'news-title slider-title-sr-only', title); copy.appendChild(heading);
          var date = new Date(entry.published && entry.published.$t);
          if (!isNaN(date.getTime())) { var time = element('time', 'news-date', date.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' })); time.dateTime = date.toISOString(); time.style.display = 'block'; copy.appendChild(time); }
          var read = element('a', 'news-read', 'Yazıyı oku ↗'); read.href = href; copy.appendChild(read);
          slide.appendChild(media); slide.appendChild(copy); track.appendChild(slide); slides.push(slide);
          var position = slides.length - 1;
          var dot = element('button', 'news-dot'); dot.type = 'button'; dot.setAttribute('aria-label', (position + 1) + '. içeriği göster'); dot.setAttribute('aria-controls', 'news-track'); dot.addEventListener('click', function () { go(position); }); dots.appendChild(dot);
        });
        if (!slides.length) {
          showMessage('Henüz öne çıkan içerik yok', 'Öne çıkan içerikler yayımlandığında burada gösterilecek.');
          return;
        }
        slides.forEach(function (slide, i) { slide.setAttribute('aria-label', (i + 1) + ' / ' + slides.length); });
        message.hidden = true; track.hidden = false; controls.hidden = slides.length < 2; sync();
        panel.querySelector('.news-prev').addEventListener('click', function () { go(index - 1); });
        panel.querySelector('.news-next').addEventListener('click', function () { go(index + 1); });
        track.addEventListener('keydown', function (event) {
          if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') { event.preventDefault(); go(index + (event.key === 'ArrowRight' ? 1 : -1)); }
        });
        track.addEventListener('scroll', function () {
          window.clearTimeout(scrollTimer); scrollTimer = window.setTimeout(function () {
            index = Math.max(0, Math.min(slides.length - 1, Math.round(track.scrollLeft / track.clientWidth))); sync();
          }, 100);
        }, { passive: true });
        window.addEventListener('resize', function () { go(index); });
      })
      .catch(function () { showMessage('Öne çıkan içerikler şu anda yüklenemiyor', 'Lütfen daha sonra tekrar deneyin.'); })
      .finally(function () { window.clearTimeout(timeout); });
  }());

  (function () {
    'use strict';
    var list = document.getElementById('rt-topic-list');
    if (!list) return;

    var items = Array.prototype.slice.call(list.querySelectorAll('li[data-topic]'));
    var fixedLast = items.find(function (item) { return item.getAttribute('data-fixed') === 'last'; });
    var dynamicItems = items.filter(function (item) { return item !== fixedLast; });

    if (!dynamicItems.length) return;

    var feedUrl = document.querySelector('link[rel="alternate"][type="application/atom+xml"]');
    var baseFeed = feedUrl && feedUrl.href ? feedUrl.href : (window.location.origin + '/feeds/posts/default');
    var separator = baseFeed.indexOf('?') === -1 ? '?' : '&';
    var url = baseFeed + separator + 'alt=json&max-results=50&orderby=published';

    fetch(url, { credentials: 'same-origin' })
      .then(function (response) {
        if (!response.ok) throw new Error('Feed unavailable');
        return response.json();
      })
      .then(function (data) {
        var entries = data && data.feed && data.feed.entry;
        if (!Array.isArray(entries)) entries = [];

        var latest = Object.create(null);

        entries.forEach(function (entry) {
          var published = entry && entry.published && entry.published.$t;
          var time = published ? Date.parse(published) : NaN;
          if (!isFinite(time)) return;

          var categories = Array.isArray(entry.category) ? entry.category : [];
          categories.forEach(function (category) {
            var term = category && category.term;
            if (!term) return;
            if (latest[term] === undefined || time > latest[term]) latest[term] = time;
          });
        });

        dynamicItems.sort(function (a, b) {
          var aTopic = a.getAttribute('data-topic');
          var bTopic = b.getAttribute('data-topic');
          var aTime = latest[aTopic] || 0;
          var bTime = latest[bTopic] || 0;

          if (aTime !== bTime) return bTime - aTime;
          return items.indexOf(a) - items.indexOf(b);
        });

        dynamicItems.forEach(function (item) { list.appendChild(item); });
        if (fixedLast) list.appendChild(fixedLast);
      })
      .catch(function () {
        /* Feed alınamazsa mevcut sabit sıra korunur. */
      });
  }());

  (function () {
    /* v015: Masaüstü dropdownlar yalnızca CSS :hover ile çalışır.
       JavaScript sadece mobil <details> menülerini yönetir. */
    var mobileMenus = document.querySelectorAll('.mobile-menu .nav-dropdown');

    mobileMenus.forEach(function (menu) {
      var summary = menu.querySelector('summary');

      if (menu.querySelector('[aria-current="page"]') || window.location.pathname.replace(/\/$/, '') === '/search/label/' + encodeURIComponent(menu.getAttribute('data-category'))) {
        menu.classList.add('is-current');
      }

      menu.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && menu.open) {
          menu.open = false;
          summary.focus();
          event.stopPropagation();
        }
      });
    });

    document.addEventListener('click', function (event) {
      mobileMenus.forEach(function (menu) {
        if (!menu.contains(event.target)) menu.open = false;
      });
    });

    /* Masaüstünde yalnızca aktif kategori vurgusu için sınıf eklenir;
       açma/kapatma davranışı JavaScript kullanmaz. */
    document.querySelectorAll('.desktop-dropdown').forEach(function (menu) {
      if (menu.querySelector('[aria-current="page"]') || window.location.pathname.replace(/\/$/, '') === '/search/label/' + encodeURIComponent(menu.getAttribute('data-category'))) {
        menu.classList.add('is-current');
      }
    });
  }());

  }
  function baslat() {
    var state = global.__RASYOTREND_V11__;
    if (!state || !state.claim || !state.claim('ana-tema')) return false;
    try { calistir(); return true; }
    catch (error) { delete state.baslatilan['ana-tema']; throw error; }
  }
  global.RasyoTrendAnaTema = { surum: '1.1.0', baslat: baslat };
}(window));
