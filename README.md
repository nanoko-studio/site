# nanoko.app

Website tĩnh của Nanoko Studio, deploy bằng GitHub Pages (branch `main`, root), custom domain `nanoko.app` (file `CNAME`).
HTML/CSS/JS thuần, không có bước build khi deploy (trang Fincal sinh sẵn bằng `tools/fincal/`, xem bên dưới).

## Cấu trúc

| Đường dẫn | Nội dung |
|---|---|
| `/`, `/vi/` | Trang studio EN và VI, nối nhau bằng `hreflang`; `/` tự chuyển sang `/vi/` theo ngôn ngữ trình duyệt hoặc lựa chọn đã lưu (`localStorage` `nanoko-lang`) |
| `/assets/` | CSS và favicon của trang studio |
| `/<app>/` | Landing của từng app |
| `/<app>/privacy/`, `/<app>/support/` | Trang pháp lý và hỗ trợ. **URL cố định, đang khai trên App Store / Google Play: không đổi, không xoá.** |
| `/limno/terms/`, `/limno/license/` | Điều khoản và giấy phép dữ liệu của Limno |
| `/lotingo/vi/...`, `/purrchup/vi/...` | Bản tiếng Việt theo path riêng |
| `/app-ads.txt` | AdMob, phải luôn trả 200 |
| `/sitemap.xml`, `/robots.txt`, `/404.html` | SEO và trang lỗi chung |

App: `lendnote`, `purrchup`, `lotingo`, `fincal`, `limno`, `punyo`.

## Ngôn ngữ

- Studio, Lotingo, Purrch Up: mỗi ngôn ngữ một URL (`/vi/...`), có `hreflang`.
- Lendnote, Fincal, Limno, Punyo: hai ngôn ngữ trong cùng một trang, chọn bằng JS (Limno nhận `?lang=vi|en`). Sẽ chuẩn hoá sang path riêng sau.

## Quy ước

- Đường dẫn nội bộ luôn tuyệt đối từ gốc: `/<app>/...`.
- Mỗi trang có `<title>` và `description` bắt đầu bằng tên app, `canonical` trỏ chính nó, Open Graph; landing có JSON-LD `SoftwareApplication`.
- Thêm/xoá trang thì sửa `sitemap.xml`.
- Văn bản dùng `-`, không dùng dấu gạch dài.

## Fincal: công cụ tính và bài viết

Các trang công cụ tính, bài viết và trang Blog của Fincal được sinh ra bằng script trong `tools/fincal/`. Không sửa tay các file HTML này, sửa script rồi chạy lại:

```bash
python3 -I tools/fincal/build.py
```

- `tools/fincal/articles.py`: danh sách bài viết (chủ đề, ngày), dùng để dựng trang Blog, mục "Bài liên quan", link Blog trên header và cập nhật `sitemap.xml`.
- `<x>lang.py`: nội dung từng ngôn ngữ. `<x>page.py`: khung trang.
- Thêm bài: viết `<x>lang.py` + `<x>page.py`, thêm một dòng vào `ARTICLES` và tên script vào `GENERATORS` trong `build.py`, rồi chạy lại build.
- Kiểm tra link: `python3 -m http.server 8765` ở gốc repo, rồi `python3 -I tools/linkcheck.py http://localhost:8765`.

## Những thứ KHÔNG nằm ở đây

Vẫn ở repo site cũ vì gắn với domain cũ hoặc app đọc lúc chạy:

- `namnoit/limno-app` `data/`: mirror dữ liệu loài cho app Limno, do CI của `limno-data` đẩy lên.
- `Purrch-Up/purrch-up.github.io` `.well-known/`, `c/`: universal link thách đấu.
- `lotingo-app/lotingo-app.github.io` `.well-known/`, `404.html`: App Links `/l/`.
- `namnoit/namnoit.github.io` `app-ads.txt`.

## Xem thử trên máy

```bash
python3 -m http.server 8000
```

Mở http://localhost:8000.
