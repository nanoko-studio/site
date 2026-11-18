// Chuyển ngữ vi/en. Nạp trong <head>, KHÔNG defer: phải đặt data-lang trước lần
// vẽ đầu tiên, nếu không trang sẽ nháy hiện cả hai bản rồi mới ẩn bớt.
(function () {
  var STORE_KEY = 'punyo-lang';

  function pick() {
    try {
      var saved = localStorage.getItem(STORE_KEY);
      if (saved === 'vi' || saved === 'en') return saved;
    } catch (e) {
      // Safari private mode ném ở đây. Không có gì để cứu — rơi về đoán theo trình duyệt.
    }
    var nav = (navigator.language || 'en').toLowerCase();
    return nav.indexOf('vi') === 0 ? 'vi' : 'en';
  }

  function apply(lang) {
    var html = document.documentElement;
    html.setAttribute('data-lang', lang);
    // lang phải đổi theo: nó là thứ screen reader dùng để chọn giọng đọc.
    html.setAttribute('lang', lang);
    var buttons = document.querySelectorAll('.langswitch button');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute('aria-pressed', String(buttons[i].dataset.lang === lang));
    }
  }

  apply(pick());

  document.addEventListener('DOMContentLoaded', function () {
    apply(document.documentElement.getAttribute('data-lang'));
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('.langswitch button');
      if (!btn) return;
      var lang = btn.dataset.lang;
      try {
        localStorage.setItem(STORE_KEY, lang);
      } catch (e2) {
        // Không nhớ được thì thôi, trang vẫn đổi ngôn ngữ cho lượt xem này.
      }
      apply(lang);
    });
  });
})();
