"""Content for the promo-then-floating rate article, one dict per language.
Example: amount B over n months, promo rate P for k months, then floating F. Placeholders filled in teaserpage.py."""

T = {}

T["vi"] = dict(
    path="/fincal/lai-uu-dai-va-tha-noi/", ct="web-fincal-article-teaser-vi",
    title="Lãi suất ưu đãi và thả nổi: hết ưu đãi trả thêm bao nhiêu? | Fincal",
    h1="Lãi suất ưu đãi và thả nổi: hết ưu đãi, mỗi tháng phải trả thêm bao nhiêu?",
    desc="Vay 1 tỷ trong 20 năm, ưu đãi 7,5% hai năm đầu rồi thả nổi: tháng thứ 25 tiền trả tăng bao nhiêu, gói ưu đãi nào thật sự rẻ hơn, và cách chuẩn bị. Có biểu đồ, bảng và máy tính.",
    crumb="Lãi ưu đãi và thả nổi", byline="Nanoko Studio · Cập nhật 21/11/2026", summary="Tóm tắt",
    B=1_000_000_000, n=240, method="equal", P=7.5, k=24, F=11,
    floats=[9, 10, 11, 12, 13], chart_floats=[9, 11, 13],
    packages=[(6.5, 12), (7.5, 24), (8, 36)], pkg_floats=[10, 11, 12],
    fmt=dict(dc=True, cur="đ", pre=False, dec=0, intl="vi-VN", scale=1), div=1, sfx="%/năm",
    methods=dict(equal="Gốc đều (dư nợ giảm dần)", annuity="Trả góp đều hằng tháng"),
    ticks=["0", "7,5tr", "15tr"], tick_max=15_000_000, year0="Nay", year_tick="{y} năm",
    month_tip="Tháng {m}", series="Thả nổi {r}",
    tldr="Vay <b>1 tỷ</b> trong 20 năm, gốc đều, ưu đãi <b>7,5%</b> trong 24 tháng, sau đó giả sử thả nổi <b>11%</b>/năm:",
    tile_before="tháng cuối ưu đãi, lãi 7,5%", tile_after="tháng đầu thả nổi, lãi 11%",
    hero="Hết ưu đãi, mỗi tháng trả thêm", hero_small="tăng {pct} chỉ sau một tháng",
    fig=("Tiền trả mỗi tháng theo mức lãi thả nổi", "Chạm vào biểu đồ để xem số tiền từng năm.",
         "Tiền trả mỗi tháng trong 20 năm với lãi thả nổi 9%, 11% và 13%"),
    ftbl=("Lãi thả nổi", "Trả tháng 25", "Tăng so với tháng 24", "Tổng lãi 20 năm"),
    ptbl=("Gói ưu đãi", "Tổng lãi 20 năm nếu thả nổi", "{r}%"), pkg_name="{p}% trong {k} tháng",
    calc=dict(title="Tính cho khoản vay của bạn", amount="Số tiền vay", term="Thời hạn vay", term_unit="tháng",
              method="Cách trả", promo="Lãi ưu đãi", promo_months="Thời gian ưu đãi", floating="Lãi thả nổi dự kiến",
              rate_unit="%/năm",
              rows=["Trả tháng cuối ưu đãi", "Trả tháng đầu thả nổi", "Tăng thêm mỗi tháng", "Tổng tiền lãi", "Tổng phải trả"]),
    body="""
<p>Gần như mọi khoản vay mua nhà đều mở đầu bằng một con số rất đẹp: 6-8%/năm, cố định 1-3 năm. Điều ít người tính trước là chuyện gì xảy ra vào tháng đầu tiên sau ưu đãi, khi lãi chuyển sang thả nổi và tiền trả hằng tháng nhảy lên một mức mới.</p>

<h2>Lãi thả nổi được tính thế nào</h2>
<p>Hết thời gian ưu đãi, lãi suất thường được tính bằng <b>lãi suất tham chiếu cộng biên độ</b>. Lãi tham chiếu hay là lãi tiết kiệm kỳ hạn 12 hoặc 13 tháng của chính ngân hàng hoặc bình quân vài ngân hàng lớn, biên độ thường khoảng 3-4%. Ngân hàng điều chỉnh định kỳ, thường 3 hoặc 6 tháng một lần.</p>
<p>Vì lãi tiết kiệm lên xuống theo thị trường, không ai biết chắc lãi thả nổi sẽ là bao nhiêu. Cách an toàn là tính thử vài mức, như các ví dụ dưới đây, chứ không chỉ nhìn con số ưu đãi.</p>

<h2>Ví dụ: vay 1 tỷ, ưu đãi 7,5% trong 2 năm</h2>
<p>Khoản vay 20 năm theo kiểu gốc đều, mỗi tháng trả {prin} tiền gốc cộng tiền lãi trên dư nợ còn lại. Trong 24 tháng đầu, tiền trả giảm dần từ {first} xuống {before}. Đến tháng 25, lãi lên 11%, tiền trả nhảy lên {after}: <b>thêm {jump} mỗi tháng</b>, tức {pct}, dù dư nợ vẫn đang giảm.</p>
{FIG}
<p>Cú tăng ở tháng 25 lớn hay nhỏ tùy vào mức thả nổi. Bảng dưới giữ nguyên ưu đãi 7,5% trong 24 tháng và thay đổi lãi thả nổi:</p>
{FTABLE}
<p>Mỗi 1% lãi thả nổi cao hơn làm tiền trả tháng 25 tăng thêm khoảng {step1} và tổng lãi 20 năm tăng khoảng {step_total}. Nếu cứ giả định lãi 11% suốt 20 năm mà không có ưu đãi, tổng lãi là {no_promo}, nên 2 năm ưu đãi chỉ giúp bớt khoảng {promo_saving}. Phần lớn tiền lãi nằm ở giai đoạn thả nổi.</p>

<h2>Lãi ưu đãi thấp nhất chưa chắc là gói rẻ nhất</h2>
<p>Ngân hàng thường cho chọn giữa ưu đãi thấp trong thời gian ngắn và ưu đãi cao hơn trong thời gian dài. So ba gói cho cùng khoản vay 1 tỷ, 20 năm:</p>
{PTABLE}
<p>Gói 6,5% nghe hấp dẫn nhất nhưng chỉ kéo dài 12 tháng, nên với lãi thả nổi 11% nó lại tốn hơn gói 8% trong 36 tháng khoảng {pkg_gap}. Khi lãi thả nổi cao hơn ưu đãi khá nhiều, <b>thời gian ưu đãi thường quan trọng hơn mức lãi ưu đãi</b>. Hãy so tổng lãi với vài mức thả nổi trước khi chọn, và đọc kỹ phí trả nợ trước hạn của từng gói, vì gói ưu đãi dài hay đi kèm thời gian tính phí dài.</p>

{CALC}

<h2>Chuẩn bị gì trước khi hết ưu đãi</h2>
<ul>
<li><b>Tính tiền trả với lãi thả nổi cao hơn dự kiến 2-3%</b>, và chỉ vay mức mà bạn vẫn trả được trong trường hợp đó.</li>
<li><b>Dành sẵn một khoản để trả trước</b> khi hết ưu đãi. Nhiều hợp đồng giảm hoặc bỏ phí phạt sau vài năm, và mỗi đồng trả trước lúc đó tránh được đúng mức lãi thả nổi. <a href="/fincal/tra-no-truoc-han/">Xem trả nợ trước hạn có lợi không →</a></li>
<li><b>Hỏi rõ công thức thả nổi</b>: lãi tham chiếu là gì, biên độ bao nhiêu, bao lâu điều chỉnh một lần, và có ghi trong hợp đồng không.</li>
<li>Gần hết ưu đãi, <b>hỏi ngân hàng khác</b> về gói chuyển nợ. Nhớ cộng cả phí trả trước, phí thẩm định và phí công chứng khi so.</li>
</ul>
""",
    faq=[
        ("Lãi suất thả nổi thường được tính như thế nào?",
         "Thường bằng lãi suất tham chiếu cộng biên độ. Lãi tham chiếu hay là lãi tiết kiệm 12 hoặc 13 tháng của ngân hàng, biên độ thường khoảng 3-4%, điều chỉnh mỗi 3 hoặc 6 tháng. Công thức cụ thể nằm trong hợp đồng tín dụng của bạn."),
        ("Hết ưu đãi tiền trả mỗi tháng tăng bao nhiêu?",
         "Tùy chênh lệch giữa lãi ưu đãi và lãi thả nổi. Với khoản vay 1 tỷ, 20 năm, ưu đãi 7,5% hai năm rồi thả nổi 11%, tiền trả tháng 25 tăng khoảng 2,6 triệu, hơn một phần tư. Dùng máy tính ở trên để thử với khoản vay của bạn."),
        ("Nên chọn gói ưu đãi ngắn lãi thấp hay gói dài lãi cao hơn?",
         "Khi lãi thả nổi cao hơn ưu đãi nhiều, gói dài thường rẻ hơn tính trên cả khoản vay. Hãy so tổng lãi với vài mức thả nổi, và xem thời gian tính phí trả nợ trước hạn của từng gói."),
        ("Có nên trả bớt nợ ngay khi hết ưu đãi không?",
         "Nếu có tiền nhàn rỗi và phí trả trước đã giảm, trả bớt lúc hết ưu đãi giúp giảm cả tiền trả mỗi tháng lẫn tổng lãi. Vẫn nên giữ lại tiền dự phòng vài tháng chi tiêu."),
    ],
    promo=("Theo dõi lãi suất thay đổi?", "App Fincal tính lại lịch trả nợ mỗi khi lãi đổi, dùng được cả khi không có mạng:",
           [("Nhiều giai đoạn lãi", "ưu đãi rồi thả nổi, thêm bao nhiêu giai đoạn cũng được"),
            ("Trả trước", "một lần hoặc định kỳ, có phí phạt, xem tiết kiệm được bao nhiêu"),
            ("Lưu và so sánh", "đặt các gói vay cạnh nhau để chọn gói rẻ nhất")]),
)
