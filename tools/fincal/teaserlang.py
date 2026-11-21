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

T["en"] = dict(
    path="/fincal/intro-rate-vs-variable-rate/", ct="web-fincal-article-teaser",
    title="Intro rate ending: how much will your mortgage payment rise? | Fincal",
    h1="When the intro rate ends: how much more will you pay each month?",
    desc="A 300,000 mortgage over 25 years at 4.5% fixed for two years, then a variable rate: how much the payment jumps in month 25, which deal is really cheaper, and how to prepare. With chart, tables and a calculator.",
    crumb="Intro rate vs variable rate", byline="Nanoko Studio · Updated 21 Nov 2026", summary="Summary",
    B=300_000, n=300, method="annuity", P=4.5, k=24, F=6.5,
    floats=[5.5, 6.5, 7.5, 8.5], chart_floats=[5.5, 6.5, 8.5],
    packages=[(3.9, 12), (4.5, 24), (4.9, 60)], pkg_floats=[5.5, 6.5, 7.5],
    fmt=dict(dc=False, cur="", pre=False, dec=0, intl="en-US", scale=1), div=1, sfx="% a year",
    methods=dict(annuity="Equal monthly payments", equal="Equal principal"),
    ticks=["0", "1,250", "2,500"], tick_max=2_500, year0="Now", year_tick="Year {y}",
    month_tip="Month {m}", series="Variable {r}",
    tldr="Borrow <b>300,000</b> over 25 years with equal monthly payments, <b>4.5%</b> fixed for 24 months, then a variable rate of, say, <b>6.5%</b>:",
    tile_before="last intro month, at 4.5%", tile_after="first variable month, at 6.5%",
    hero="After the intro rate, you pay", hero_small="more a month, up {pct} overnight",
    fig=("Monthly payment by variable rate", "Tap the chart to see the payment each year.",
         "Monthly payment over 25 years with a variable rate of 5.5%, 6.5% and 8.5%"),
    ftbl=("Variable rate", "Payment in month 25", "Rise vs month 24", "Total interest, 25 years"),
    ptbl=("Intro deal", "Total interest over 25 years if the variable rate is", "{r}%"), pkg_name="{p}% for {k} months",
    calc=dict(title="Try your own loan", amount="Loan amount", term="Loan term", term_unit="months",
              method="Repayment", promo="Intro rate", promo_months="Intro period", floating="Expected variable rate",
              rate_unit="% a year",
              rows=["Payment, last intro month", "Payment, first variable month", "Extra each month", "Total interest", "Total repaid"]),
    body="""
<p>Most mortgages open with an attractive number: a fixed or discounted rate for the first two to five years. What fewer people work out in advance is the first month after that deal ends, when the loan moves to a variable rate and the monthly payment resets to a new level.</p>

<h2>How the variable rate is set</h2>
<p>After the intro period, the rate usually follows a <b>reference rate plus a margin</b>. The reference may be the central bank rate, a market rate or the lender's own standard variable rate, and the margin is fixed in your contract. When the reference moves, your rate and your payment move with it.</p>
<p>Nobody knows what the reference will be in two or five years. The safe way to plan is to try a few variable rates, as below, rather than look only at the intro rate.</p>

<h2>Example: 300,000 at 4.5% for 2 years</h2>
<p>The loan runs 25 years with equal monthly payments. For the first 24 months you pay {before} a month. In month 25 the rate goes to 6.5% and the payment is recalculated on the remaining balance and term: it becomes {after}, <b>{jump} more every month</b>, a rise of {pct}.</p>
{FIG}
<p>How big that jump is depends on the variable rate. The table keeps the 4.5% intro rate for 24 months and changes only the variable rate:</p>
{FTABLE}
<p>Each extra 1% on the variable rate adds about {step1} to the month 25 payment and about {step_total} to the total interest over 25 years. If the whole loan were at 6.5% with no intro deal, total interest would be {no_promo}, so the two intro years save only about {promo_saving}. Most of the interest is paid in the variable years.</p>

<h2>The lowest intro rate is not always the cheapest deal</h2>
<p>Lenders often offer a choice between a lower rate for a short time and a slightly higher rate for longer. Three deals on the same 300,000 over 25 years:</p>
{PTABLE}
<p>The 3.9% deal looks best, but it lasts only 12 months, so with a 6.5% variable rate it costs about {pkg_gap} more than 4.9% fixed for 5 years. When the variable rate is well above the intro rate, <b>how long the deal lasts usually matters more than the rate itself</b>. Compare total interest at a few variable rates before choosing, and check the early repayment charges of each deal: longer deals tend to lock you in for longer.</p>

{CALC}

<h2>What to do before the intro rate ends</h2>
<ul>
<li><b>Work out the payment at a variable rate 2-3% higher than you expect</b>, and only borrow what you could still pay in that case.</li>
<li><b>Set money aside to overpay</b> when the deal ends. Early repayment charges usually stop with the intro period, and every pound or dollar you pay off then saves interest at the full variable rate. <a href="/fincal/paying-off-a-loan-early/">Is paying off a loan early worth it? →</a></li>
<li><b>Ask exactly how the variable rate is set</b>: which reference rate, what margin, how often it changes, and where that is written in the contract.</li>
<li>A few months before the deal ends, <b>compare remortgage offers</b>, counting arrangement, valuation and legal fees as well as the rate.</li>
</ul>
""",
    faq=[
        ("How is a variable mortgage rate calculated?",
         "Usually as a reference rate plus a fixed margin. The reference may be the central bank rate, a market rate or the lender's standard variable rate. The exact formula and how often it changes are in your loan contract."),
        ("How much will my payment go up when the intro rate ends?",
         "It depends on the gap between the intro and variable rates. On 300,000 over 25 years, 4.5% for two years then 6.5%, the payment rises by about 335 a month, around a fifth. Use the calculator above for your own loan."),
        ("Should I choose a short low-rate deal or a longer higher-rate one?",
         "When the variable rate is well above the intro rate, the longer deal is usually cheaper over the whole loan. Compare total interest at a few variable rates and check how long the early repayment charges last."),
        ("Should I pay down the loan when the intro period ends?",
         "If you have spare cash and the early repayment charges have ended, paying down then lowers both the monthly payment and the total interest. Keep an emergency fund of a few months' spending first."),
    ],
    promo=("Tracking rate changes?", "The Fincal app recalculates your schedule whenever the rate changes, and works offline:",
           [("Several rate periods", "intro then variable, as many periods as you need"),
            ("Overpayments", "one-off or regular, with fees, and see what you save"),
            ("Save and compare", "put loan deals side by side and pick the cheapest")]),
)

T["id"] = dict(
    path="/fincal/bunga-fix-vs-floating/", ct="web-fincal-article-teaser-id",
    title="Bunga fix dan floating KPR: setelah fix habis, cicilan naik berapa? | Fincal",
    h1="Bunga fix lalu floating: setelah masa fix habis, cicilan naik berapa?",
    desc="KPR Rp 500 juta selama 15 tahun, bunga fix 5,5% tiga tahun lalu floating: berapa kenaikan cicilan di bulan ke-37, paket mana yang benar-benar lebih murah, dan cara bersiap. Dengan grafik, tabel, dan kalkulator.",
    crumb="Bunga fix dan floating", byline="Nanoko Studio · Diperbarui 21/11/2026", summary="Ringkasan",
    B=500_000_000, n=180, method="annuity", P=5.5, k=36, F=11,
    floats=[9, 10, 11, 12, 13], chart_floats=[9, 11, 13],
    packages=[(3.5, 12), (5.5, 36), (7, 60)], pkg_floats=[10, 11, 12],
    fmt=dict(dc=True, cur="Rp", pre=True, dec=0, intl="id-ID", scale=1), div=1, sfx="% per tahun",
    methods=dict(annuity="Anuitas (cicilan tetap)", equal="Pokok tetap (bunga efektif)"),
    ticks=["0", "3 jt", "6 jt"], tick_max=6_000_000, year0="Kini", year_tick="Thn {y}",
    month_tip="Bulan {m}", series="Floating {r}",
    tldr="KPR <b>Rp 500 juta</b> selama 15 tahun, cicilan anuitas, bunga fix <b>5,5%</b> selama 36 bulan, lalu misalnya floating <b>11%</b> per tahun:",
    tile_before="bulan terakhir fix, bunga 5,5%", tile_after="bulan pertama floating, bunga 11%",
    hero="Setelah masa fix, cicilan naik", hero_small="per bulan, naik {pct} dalam sebulan",
    fig=("Cicilan per bulan menurut bunga floating", "Ketuk grafik untuk melihat cicilan setiap tahun.",
         "Cicilan per bulan selama 15 tahun dengan bunga floating 9%, 11% dan 13%"),
    ftbl=("Bunga floating", "Cicilan bulan 37", "Naik dari bulan 36", "Total bunga 15 tahun"),
    ptbl=("Paket bunga fix", "Total bunga 15 tahun jika floating", "{r}%"), pkg_name="{p}% selama {k} bulan",
    calc=dict(title="Hitung untuk pinjaman Anda", amount="Jumlah pinjaman", term="Tenor", term_unit="bulan",
              method="Cara cicilan", promo="Bunga fix", promo_months="Masa fix", floating="Perkiraan bunga floating",
              rate_unit="% per tahun",
              rows=["Cicilan bulan terakhir fix", "Cicilan bulan pertama floating", "Kenaikan per bulan", "Total bunga", "Total pembayaran"]),
    body="""
<p>Hampir semua KPR dibuka dengan angka yang menarik: bunga fix 3-7% per tahun selama 1-5 tahun pertama. Yang jarang dihitung sejak awal adalah bulan pertama setelah masa fix habis, ketika bunga berubah menjadi floating dan cicilan bulanan melonjak ke tingkat baru.</p>

<h2>Bagaimana bunga floating dihitung</h2>
<p>Setelah masa fix, bunga biasanya mengikuti <b>suku bunga acuan ditambah margin</b>. Acuannya bisa suku bunga dasar kredit (SBDK) bank, BI Rate, atau suku bunga deposito, dan margin biasanya beberapa persen. Bank menyesuaikannya secara berkala, dan di banyak KPR bunga floating berada di kisaran 10-13% per tahun.</p>
<p>Tidak ada yang tahu pasti berapa bunga floating beberapa tahun lagi. Cara yang aman adalah mencoba beberapa tingkat bunga, seperti contoh di bawah, bukan hanya melihat angka bunga fix.</p>

<h2>Contoh: KPR Rp 500 juta, fix 5,5% selama 3 tahun</h2>
<p>Tenor 15 tahun dengan cicilan anuitas. Selama 36 bulan pertama Anda membayar {before} per bulan. Di bulan ke-37 bunga naik ke 11% dan cicilan dihitung ulang dari sisa pokok dan sisa tenor: menjadi {after}, <b>naik {jump} setiap bulan</b>, atau {pct}.</p>
{FIG}
<p>Besar lonjakan itu tergantung bunga floating. Tabel di bawah tetap memakai fix 5,5% selama 36 bulan dan hanya mengubah bunga floating:</p>
{FTABLE}
<p>Setiap 1% bunga floating yang lebih tinggi menambah cicilan bulan ke-37 sekitar {step1} dan total bunga 15 tahun sekitar {step_total}. Jika seluruh pinjaman berbunga 11% tanpa masa fix, total bunganya {no_promo}, jadi tiga tahun bunga fix hanya menghemat sekitar {promo_saving}. Sebagian besar bunga dibayar di masa floating.</p>

<h2>Bunga fix terendah belum tentu paket termurah</h2>
<p>Bank sering menawarkan pilihan antara bunga fix rendah dalam waktu singkat dan bunga fix sedikit lebih tinggi untuk waktu lebih lama. Tiga paket untuk KPR yang sama, Rp 500 juta selama 15 tahun:</p>
{PTABLE}
<p>Paket 3,5% terlihat paling menarik, tetapi hanya berlaku 12 bulan, sehingga dengan floating 11% justru lebih mahal sekitar {pkg_gap} dibanding fix 7% selama 5 tahun. Jika bunga floating jauh di atas bunga fix, <b>lamanya masa fix biasanya lebih penting daripada besar bunganya</b>. Bandingkan total bunga pada beberapa tingkat floating sebelum memilih, dan baca penalti pelunasan dipercepat setiap paket.</p>

{CALC}

<h2>Persiapan sebelum masa fix habis</h2>
<ul>
<li><b>Hitung cicilan dengan bunga floating 2-3% lebih tinggi dari perkiraan</b>, dan pinjam hanya sejumlah yang tetap sanggup Anda bayar dalam kondisi itu.</li>
<li><b>Siapkan dana untuk pelunasan sebagian</b> saat masa fix habis. Banyak bank membebaskan atau menurunkan penalti setelah masa fix, dan setiap rupiah yang dilunasi saat itu menghemat bunga sebesar bunga floating. <a href="/fincal/pelunasan-dipercepat/">Apakah pelunasan dipercepat menguntungkan? →</a></li>
<li><b>Tanyakan rumus bunga floating</b>: acuannya apa, marginnya berapa, seberapa sering disesuaikan, dan apakah tertulis di perjanjian kredit.</li>
<li>Menjelang masa fix habis, <b>bandingkan tawaran take over KPR</b> dari bank lain, termasuk biaya provisi, appraisal, dan notaris.</li>
</ul>
""",
    faq=[
        ("Bagaimana bunga floating KPR dihitung?",
         "Biasanya suku bunga acuan ditambah margin. Acuannya bisa SBDK bank, BI Rate, atau bunga deposito, dan bank menyesuaikannya secara berkala. Rumus pastinya ada di perjanjian kredit Anda."),
        ("Setelah masa fix habis, cicilan naik berapa?",
         "Tergantung selisih bunga fix dan floating. Untuk KPR Rp 500 juta selama 15 tahun, fix 5,5% tiga tahun lalu floating 11%, cicilan naik sekitar Rp 1,3 juta per bulan, hampir sepertiga. Gunakan kalkulator di atas untuk pinjaman Anda."),
        ("Pilih bunga fix rendah yang singkat atau fix lebih tinggi yang lama?",
         "Jika bunga floating jauh di atas bunga fix, paket fix yang lebih lama biasanya lebih murah untuk keseluruhan pinjaman. Bandingkan total bunga pada beberapa tingkat floating, dan periksa penalti pelunasan setiap paket."),
        ("Sebaiknya melunasi sebagian saat masa fix habis?",
         "Jika ada dana menganggur dan penaltinya sudah turun, pelunasan sebagian saat itu menurunkan cicilan sekaligus total bunga. Tetap sisihkan dana darurat untuk beberapa bulan pengeluaran."),
    ],
    promo=("Memantau perubahan bunga?", "Aplikasi Fincal menghitung ulang jadwal cicilan setiap kali bunga berubah, dan bisa dipakai offline:",
           [("Beberapa periode bunga", "fix lalu floating, berapa pun periodenya"),
            ("Pelunasan dipercepat", "sekali atau berkala, dengan penalti, lihat penghematannya"),
            ("Simpan dan bandingkan", "letakkan paket KPR berdampingan dan pilih yang termurah")]),
)

T["th"] = dict(
    path="/fincal/dokbia-khongthi-kap-loitua/", ct="web-fincal-article-teaser-th",
    title="ดอกเบี้ยคงที่กับลอยตัว: หมดโปรแล้วค่างวดขึ้นเท่าไร | Fincal",
    h1="ดอกเบี้ยคงที่แล้วลอยตัว: หมดช่วงโปรโมชัน ค่างวดเพิ่มขึ้นเท่าไร",
    desc="กู้บ้าน 2 ล้านบาท 30 ปี ดอกเบี้ยคงที่ 3% สามปีแรกแล้วลอยตัว: เดือนที่ 37 ค่างวดเพิ่มเท่าไร โปรไหนถูกกว่าจริง และควรเตรียมตัวอย่างไร พร้อมกราฟ ตาราง และเครื่องคำนวณ",
    crumb="ดอกเบี้ยคงที่กับลอยตัว", byline="Nanoko Studio · อัปเดต 21 พ.ย. 2026", summary="สรุป",
    B=2_000_000, n=360, method="annuity", P=3, k=36, F=6,
    floats=[4, 5, 6, 7, 8], chart_floats=[4, 6, 8],
    packages=[(2.5, 12), (3, 36), (3.5, 60)], pkg_floats=[5, 6, 7],
    fmt=dict(dc=False, cur="บาท", pre=False, dec=0, intl="th-TH", scale=1), div=1, sfx="% ต่อปี",
    methods=dict(annuity="ผ่อนงวดเท่ากัน", equal="เงินต้นเท่ากันทุกงวด"),
    ticks=["0", "7,500", "15,000"], tick_max=15_000, year0="วันนี้", year_tick="ปี {y}",
    month_tip="เดือนที่ {m}", series="ลอยตัว {r}",
    tldr="กู้บ้าน <b>2 ล้านบาท</b> 30 ปี ผ่อนงวดเท่ากัน ดอกเบี้ยคงที่ <b>3%</b> 36 เดือน จากนั้นสมมติลอยตัว <b>6%</b> ต่อปี:",
    tile_before="เดือนสุดท้ายของโปร ดอกเบี้ย 3%", tile_after="เดือนแรกที่ลอยตัว ดอกเบี้ย 6%",
    hero="หมดโปรแล้ว ค่างวดเพิ่ม", hero_small="ต่อเดือน เพิ่มขึ้น {pct} ในเดือนเดียว",
    fig=("ค่างวดต่อเดือนตามดอกเบี้ยลอยตัว", "แตะกราฟเพื่อดูค่างวดแต่ละปี",
         "ค่างวดต่อเดือนตลอด 30 ปี เมื่อดอกเบี้ยลอยตัว 4%, 6% และ 8%"),
    ftbl=("ดอกเบี้ยลอยตัว", "ค่างวดเดือนที่ 37", "เพิ่มจากเดือนที่ 36", "ดอกเบี้ยรวม 30 ปี"),
    ptbl=("โปรดอกเบี้ยคงที่", "ดอกเบี้ยรวม 30 ปี ถ้าลอยตัว", "{r}%"), pkg_name="{p}% นาน {k} เดือน",
    calc=dict(title="คำนวณสินเชื่อของคุณ", amount="ยอดกู้", term="ระยะเวลากู้", term_unit="เดือน",
              method="วิธีผ่อน", promo="ดอกเบี้ยช่วงโปร", promo_months="ระยะเวลาโปร", floating="ดอกเบี้ยลอยตัวที่คาด",
              rate_unit="% ต่อปี",
              rows=["ค่างวดเดือนสุดท้ายของโปร", "ค่างวดเดือนแรกที่ลอยตัว", "เพิ่มขึ้นต่อเดือน", "ดอกเบี้ยรวม", "ยอดชำระรวม"]),
    body="""
<p>สินเชื่อบ้านเกือบทุกแห่งเริ่มต้นด้วยตัวเลขที่น่าสนใจ: ดอกเบี้ยคงที่หรือดอกเบี้ยเฉลี่ย 3 ปีแรกประมาณ 2-4% ต่อปี สิ่งที่หลายคนไม่ได้คำนวณไว้ก่อนคือเดือนแรกหลังหมดโปร เมื่อดอกเบี้ยเปลี่ยนเป็นลอยตัวและค่างวดขยับขึ้นไปอีกระดับ</p>

<h2>ดอกเบี้ยลอยตัวคิดอย่างไร</h2>
<p>หลังหมดโปร ดอกเบี้ยมักอิงกับ <b>อัตราอ้างอิงของธนาคารบวกหรือลบส่วนต่าง</b> เช่น MRR ลบ 1-2% ซึ่ง MRR เปลี่ยนตามภาวะตลาดและนโยบายของธนาคาร ทำให้ดอกเบี้ยลอยตัวของสินเชื่อบ้านมักอยู่ราว 5-7% ต่อปี</p>
<p>ไม่มีใครรู้แน่ว่าอีกไม่กี่ปีดอกเบี้ยลอยตัวจะเป็นเท่าไร วิธีที่ปลอดภัยคือลองคำนวณหลายระดับ อย่างตัวอย่างด้านล่าง ไม่ใช่ดูแค่ดอกเบี้ยช่วงโปร</p>

<h2>ตัวอย่าง: กู้ 2 ล้านบาท ดอกเบี้ยคงที่ 3% นาน 3 ปี</h2>
<p>กู้ 30 ปี ผ่อนงวดเท่ากัน ช่วง 36 เดือนแรกผ่อนเดือนละ {before} พอถึงเดือนที่ 37 ดอกเบี้ยขึ้นเป็น 6% และธนาคารคำนวณค่างวดใหม่จากเงินต้นและระยะเวลาที่เหลือ: กลายเป็น {after} <b>เพิ่มขึ้นเดือนละ {jump}</b> หรือ {pct}</p>
{FIG}
<p>ค่างวดจะกระโดดมากหรือน้อยขึ้นกับดอกเบี้ยลอยตัว ตารางด้านล่างใช้โปร 3% นาน 36 เดือนเหมือนเดิม และเปลี่ยนแค่ดอกเบี้ยลอยตัว:</p>
{FTABLE}
<p>ดอกเบี้ยลอยตัวที่สูงขึ้นทุก 1% ทำให้ค่างวดเดือนที่ 37 เพิ่มราว {step1} และดอกเบี้ยรวม 30 ปีเพิ่มราว {step_total} ถ้าทั้งสัญญาเป็น 6% โดยไม่มีโปรเลย ดอกเบี้ยรวมคือ {no_promo} แปลว่าโปร 3 ปีช่วยประหยัดได้แค่ราว {promo_saving} ดอกเบี้ยส่วนใหญ่จ่ายในช่วงลอยตัว</p>

<h2>ดอกเบี้ยโปรต่ำสุดอาจไม่ใช่ข้อเสนอที่ถูกที่สุด</h2>
<p>ธนาคารมักให้เลือกระหว่างดอกเบี้ยต่ำในช่วงสั้น กับดอกเบี้ยสูงกว่าเล็กน้อยแต่นานกว่า ลองเทียบสามโปรสำหรับเงินกู้เดียวกัน 2 ล้านบาท 30 ปี:</p>
{PTABLE}
<p>โปร 2.5% ดูน่าสนใจที่สุด แต่มีแค่ 12 เดือน ถ้าลอยตัว 6% จะแพงกว่าโปร 3.5% นาน 5 ปีราว {pkg_gap} เมื่อดอกเบี้ยลอยตัวสูงกว่าดอกเบี้ยโปรมาก <b>ความยาวของโปรมักสำคัญกว่าตัวเลขดอกเบี้ย</b> ควรเทียบดอกเบี้ยรวมที่ดอกเบี้ยลอยตัวหลายระดับก่อนเลือก และอ่านค่าปรับไถ่ถอนก่อนกำหนดของแต่ละโปร</p>

{CALC}

<h2>เตรียมตัวก่อนหมดโปร</h2>
<ul>
<li><b>คำนวณค่างวดที่ดอกเบี้ยลอยตัวสูงกว่าที่คาด 2-3%</b> และกู้เท่าที่ยังผ่อนไหวในกรณีนั้น</li>
<li><b>เก็บเงินไว้โปะ</b> ตอนหมดโปร ค่าปรับไถ่ถอนมักหมดหลังผ่าน 3 ปี และทุกบาทที่โปะตอนนั้นช่วยประหยัดดอกเบี้ยเท่ากับดอกเบี้ยลอยตัว <a href="/fincal/poppit-ni-kon-kamnot/">โปะหนี้บ้านคุ้มไหม →</a></li>
<li><b>ถามสูตรดอกเบี้ยลอยตัวให้ชัด</b>: อิงอัตราไหน ส่วนต่างเท่าไร ปรับบ่อยแค่ไหน และเขียนไว้ในสัญญาหรือไม่</li>
<li>ใกล้หมดโปร <b>ลองขอรีไฟแนนซ์หรือรีเทนชั่น</b> และนับค่าจดจำนอง ค่าประเมิน และค่าธรรมเนียมอื่นด้วยเมื่อเปรียบเทียบ</li>
</ul>
""",
    faq=[
        ("ดอกเบี้ยลอยตัวของสินเชื่อบ้านคิดอย่างไร",
         "มักเป็นอัตราอ้างอิงของธนาคาร เช่น MRR บวกหรือลบส่วนต่าง ซึ่ง MRR ปรับตามภาวะตลาด สูตรที่แน่นอนอยู่ในสัญญาเงินกู้ของคุณ"),
        ("หมดโปรแล้วค่างวดเพิ่มขึ้นเท่าไร",
         "ขึ้นกับส่วนต่างระหว่างดอกเบี้ยโปรและดอกเบี้ยลอยตัว กู้ 2 ล้านบาท 30 ปี คงที่ 3% สามปีแล้วลอยตัว 6% ค่างวดเพิ่มราว 3,200 บาทต่อเดือน หรือเกือบ 40% ลองใช้เครื่องคำนวณด้านบนกับสินเชื่อของคุณ"),
        ("ควรเลือกโปรดอกเบี้ยต่ำช่วงสั้น หรือดอกเบี้ยสูงกว่าแต่นานกว่า",
         "ถ้าดอกเบี้ยลอยตัวสูงกว่าโปรมาก โปรที่นานกว่ามักถูกกว่าเมื่อนับทั้งสัญญา ควรเทียบดอกเบี้ยรวมที่ดอกเบี้ยลอยตัวหลายระดับ และดูช่วงเวลาที่มีค่าปรับไถ่ถอน"),
        ("ควรโปะหนี้ตอนหมดโปรไหม",
         "ถ้ามีเงินเหลือและพ้นช่วงค่าปรับแล้ว การโปะตอนนั้นช่วยลดทั้งค่างวดและดอกเบี้ยรวม แต่ควรเก็บเงินสำรองฉุกเฉินไว้หลายเดือนก่อน"),
    ],
    promo=("ติดตามดอกเบี้ยที่เปลี่ยน?", "แอป Fincal คำนวณตารางผ่อนใหม่ทุกครั้งที่ดอกเบี้ยเปลี่ยน ใช้งานได้แม้ไม่มีอินเทอร์เน็ต:",
           [("ดอกเบี้ยหลายช่วง", "โปรแล้วลอยตัว เพิ่มได้หลายช่วงตามต้องการ"),
            ("โปะหนี้", "ครั้งเดียวหรือเป็นประจำ มีค่าปรับ ดูว่าประหยัดได้เท่าไร"),
            ("บันทึกและเปรียบเทียบ", "วางข้อเสนอสินเชื่อเทียบกันแล้วเลือกที่ถูกที่สุด")]),
)

T["pt-BR"] = dict(
    path="/fincal/taxa-promocional-x-pos-fixada/", ct="web-fincal-article-teaser-pt",
    title="Taxa promocional x pós-fixada: quanto a parcela sobe depois? | Fincal",
    h1="Taxa promocional e depois pós-fixada: quanto a parcela sobe quando a promoção acaba?",
    desc="Financiamento de R$ 300 mil em 25 anos pelo SAC, 9% nos dois primeiros anos e depois taxa pós-fixada: quanto a parcela sobe no mês 25, qual oferta sai mais barata e como se preparar. Com gráfico, tabelas e calculadora.",
    crumb="Taxa promocional x pós-fixada", byline="Nanoko Studio · Atualizado em 21/11/2026", summary="Resumo",
    B=300_000, n=300, method="equal", P=9, k=24, F=12,
    floats=[10, 11, 12, 13, 14], chart_floats=[10, 12, 14],
    packages=[(8, 12), (9, 24), (9.5, 36)], pkg_floats=[11, 12, 13],
    fmt=dict(dc=True, cur="R$", pre=True, dec=0, intl="pt-BR", scale=1), div=1, sfx="% ao ano",
    methods=dict(equal="SAC", annuity="Tabela Price"),
    ticks=["0", "2,5 mil", "5 mil"], tick_max=5_000, year0="Hoje", year_tick="Ano {y}",
    month_tip="Mês {m}", series="Pós-fixada {r}",
    tldr="Financiamento de <b>R$ 300 mil</b> em 25 anos pelo SAC, taxa promocional de <b>9%</b> por 24 meses e depois, por exemplo, <b>12%</b> ao ano:",
    tile_before="último mês da promoção, a 9%", tile_after="primeiro mês pós-fixado, a 12%",
    hero="Fim da promoção, a parcela sobe", hero_small="por mês, alta de {pct} de um mês para o outro",
    fig=("Parcela mensal conforme a taxa pós-fixada", "Toque no gráfico para ver a parcela de cada ano.",
         "Parcela mensal ao longo de 25 anos com taxa pós-fixada de 10%, 12% e 14%"),
    ftbl=("Taxa pós-fixada", "Parcela do mês 25", "Alta em relação ao mês 24", "Juros totais em 25 anos"),
    ptbl=("Oferta promocional", "Juros totais em 25 anos se a taxa pós-fixada for", "{r}%"), pkg_name="{p}% por {k} meses",
    calc=dict(title="Simule o seu financiamento", amount="Valor financiado", term="Prazo", term_unit="meses",
              method="Sistema de amortização", promo="Taxa promocional", promo_months="Duração da promoção", floating="Taxa pós-fixada esperada",
              rate_unit="% ao ano",
              rows=["Parcela no último mês da promoção", "Parcela no primeiro mês pós-fixado", "Aumento por mês", "Juros totais", "Total pago"]),
    body="""
<p>Algumas ofertas de crédito começam com uma taxa promocional ou fixa nos primeiros anos e depois passam a uma taxa pós-fixada, que acompanha um índice. O que pouca gente calcula antes de assinar é o primeiro mês depois da promoção, quando a taxa muda e a parcela salta para outro patamar.</p>

<h2>Como a taxa pós-fixada é calculada</h2>
<p>Depois da promoção, a taxa costuma ser <b>um índice mais um percentual fixo</b>. O índice pode ser a Selic, o CDI, a TR ou o IPCA, conforme o contrato, e o percentual fixo é definido na assinatura. Quando o índice sobe, a taxa e a parcela sobem junto.</p>
<p>Ninguém sabe ao certo onde o índice estará daqui a alguns anos. O jeito seguro de planejar é testar algumas taxas, como nos exemplos abaixo, e não olhar só para a taxa promocional.</p>

<h2>Exemplo: R$ 300 mil a 9% por 2 anos</h2>
<p>O prazo é de 25 anos pelo SAC: cada mês você paga {prin} de amortização mais os juros sobre o saldo devedor. Nos primeiros 24 meses a parcela cai de {first} para {before}. No mês 25 a taxa vai a 12% e a parcela sobe para {after}: <b>{jump} a mais por mês</b>, ou {pct}, mesmo com o saldo devedor caindo.</p>
{FIG}
<p>O tamanho do salto depende da taxa pós-fixada. A tabela mantém a promoção de 9% por 24 meses e muda só a taxa depois dela:</p>
{FTABLE}
<p>Cada 1% a mais na taxa pós-fixada acrescenta cerca de {step1} à parcela do mês 25 e cerca de {step_total} aos juros totais em 25 anos. Se o financiamento inteiro fosse a 12%, sem promoção, os juros totais seriam {no_promo}, então os dois anos promocionais economizam só cerca de {promo_saving}. A maior parte dos juros é paga depois da promoção.</p>

<h2>A menor taxa promocional nem sempre é a oferta mais barata</h2>
<p>Às vezes dá para escolher entre uma taxa menor por pouco tempo e uma taxa um pouco maior por mais tempo. Três ofertas para os mesmos R$ 300 mil em 25 anos:</p>
{PTABLE}
<p>A oferta de 8% parece a melhor, mas dura só 12 meses, e com taxa pós-fixada de 12% sai cerca de {pkg_gap} mais cara do que 9,5% por 3 anos. Quando a taxa pós-fixada fica bem acima da promocional, <b>a duração da promoção costuma pesar mais do que a própria taxa</b>. Compare os juros totais com algumas taxas antes de escolher e olhe o Custo Efetivo Total (CET) de cada proposta.</p>

{CALC}

<h2>O que fazer antes de a promoção acabar</h2>
<ul>
<li><b>Calcule a parcela com uma taxa pós-fixada 2 a 3 pontos acima do esperado</b> e só financie o que ainda conseguiria pagar nesse cenário.</li>
<li><b>Guarde dinheiro para amortizar</b> quando a promoção acabar. Pela regra do Banco Central, a amortização antecipada tem desconto proporcional dos juros, e cada real amortizado nessa hora deixa de render juros à taxa pós-fixada. <a href="/fincal/amortizacao-antecipada/">Vale a pena amortizar o financiamento? →</a></li>
<li><b>Pergunte exatamente como a taxa é calculada</b>: qual índice, qual percentual fixo, com que frequência muda e onde isso está no contrato.</li>
<li>Perto do fim da promoção, <b>simule a portabilidade de crédito</b> para outro banco, que é gratuita, comparando o CET das propostas.</li>
</ul>
""",
    faq=[
        ("Como é calculada a taxa pós-fixada de um financiamento?",
         "Normalmente como um índice, como Selic, CDI, TR ou IPCA, mais um percentual fixo definido no contrato. A fórmula exata e a frequência de reajuste estão no seu contrato."),
        ("Quanto a parcela sobe quando a taxa promocional acaba?",
         "Depende da diferença entre a taxa promocional e a pós-fixada. Em R$ 300 mil por 25 anos no SAC, 9% por dois anos e depois 12%, a parcela sobe cerca de R$ 680 por mês, mais de um quinto. Use a calculadora acima para o seu caso."),
        ("É melhor uma promoção curta com taxa baixa ou uma mais longa com taxa maior?",
         "Quando a taxa pós-fixada fica bem acima da promocional, a promoção mais longa costuma sair mais barata no total. Compare os juros totais com algumas taxas e o CET de cada proposta."),
        ("Vale a pena amortizar quando a promoção acaba?",
         "Se você tem dinheiro parado, amortizar nesse momento reduz a parcela ou o prazo e os juros totais. Mantenha antes uma reserva de emergência de alguns meses de gastos."),
    ],
    promo=("Acompanhando a mudança de taxa?", "O app Fincal recalcula o seu cronograma sempre que a taxa muda, e funciona offline:",
           [("Vários períodos de taxa", "promocional e depois pós-fixada, quantos períodos precisar"),
            ("Amortizações", "única ou periódica, com tarifa, e veja quanto economiza"),
            ("Salvar e comparar", "coloque as ofertas lado a lado e escolha a mais barata")]),
)

T["ms"] = dict(
    path="/fincal/kadar-promosi-vs-terapung/", ct="web-fincal-article-teaser-ms",
    title="Kadar promosi vs kadar terapung: selepas promosi, ansuran naik berapa? | Fincal",
    h1="Kadar promosi kemudian terapung: selepas promosi tamat, ansuran naik berapa?",
    desc="Pinjaman rumah RM 400K selama 30 tahun, kadar promosi 3.5% dua tahun pertama kemudian terapung: berapa ansuran naik pada bulan ke-25, pakej mana lebih murah, dan cara bersedia. Dengan carta, jadual dan kalkulator.",
    crumb="Kadar promosi vs terapung", byline="Nanoko Studio · Dikemas kini 21/11/2026", summary="Ringkasan",
    B=400_000, n=360, method="annuity", P=3.5, k=24, F=4.5,
    floats=[4, 4.5, 5, 5.5, 6], chart_floats=[4, 5, 6],
    packages=[(2.9, 12), (3.5, 24), (3.8, 36)], pkg_floats=[3.5, 4.5, 5.5],
    fmt=dict(dc=False, cur="RM", pre=True, dec=0, intl="ms-MY", scale=1), div=1, sfx="% setahun",
    methods=dict(annuity="Ansuran sama setiap bulan", equal="Pokok sama setiap bulan"),
    ticks=["0", "1,500", "3,000"], tick_max=3_000, year0="Kini", year_tick="Thn {y}",
    month_tip="Bulan {m}", series="Terapung {r}",
    tldr="Pinjaman rumah <b>RM 400K</b> selama 30 tahun, ansuran sama, kadar promosi <b>3.5%</b> selama 24 bulan, kemudian misalnya terapung <b>4.5%</b> setahun:",
    tile_before="bulan terakhir promosi, kadar 3.5%", tile_after="bulan pertama terapung, kadar 4.5%",
    hero="Selepas promosi, ansuran naik", hero_small="sebulan, naik {pct} dalam sebulan",
    fig=("Ansuran bulanan mengikut kadar terapung", "Sentuh carta untuk melihat ansuran setiap tahun.",
         "Ansuran bulanan selama 30 tahun dengan kadar terapung 4%, 5% dan 6%"),
    ftbl=("Kadar terapung", "Ansuran bulan 25", "Naik berbanding bulan 24", "Jumlah faedah 30 tahun"),
    ptbl=("Pakej promosi", "Jumlah faedah 30 tahun jika kadar terapung", "{r}%"), pkg_name="{p}% selama {k} bulan",
    calc=dict(title="Kira untuk pinjaman anda", amount="Jumlah pinjaman", term="Tempoh pinjaman", term_unit="bulan",
              method="Kaedah bayaran", promo="Kadar promosi", promo_months="Tempoh promosi", floating="Jangkaan kadar terapung",
              rate_unit="% setahun",
              rows=["Ansuran bulan terakhir promosi", "Ansuran bulan pertama terapung", "Kenaikan sebulan", "Jumlah faedah", "Jumlah bayaran"]),
    body="""
<p>Banyak pinjaman rumah bermula dengan kadar yang menarik pada tahun-tahun awal, sama ada kadar promosi atau kadar bertingkat. Yang jarang dikira awal-awal ialah bulan pertama selepas promosi tamat, apabila kadar bertukar kepada kadar terapung penuh dan ansuran bulanan naik ke paras baru.</p>

<h2>Bagaimana kadar terapung dikira</h2>
<p>Selepas promosi, kadar biasanya mengikut <b>kadar rujukan ditambah margin</b>. Di Malaysia rujukannya ialah Standardised Base Rate (SBR) yang berubah mengikut OPR Bank Negara, dan margin ditetapkan dalam perjanjian. Apabila OPR naik, kadar dan ansuran anda turut naik.</p>
<p>Tiada siapa tahu pasti berapa kadar terapung beberapa tahun lagi. Cara yang selamat ialah mencuba beberapa kadar, seperti contoh di bawah, bukan sekadar melihat kadar promosi.</p>

<h2>Contoh: RM 400K, 3.5% selama 2 tahun</h2>
<p>Tempoh 30 tahun dengan ansuran sama setiap bulan. Dalam 24 bulan pertama anda membayar {before} sebulan. Pada bulan ke-25 kadar naik ke 4.5% dan ansuran dikira semula berdasarkan baki pokok dan baki tempoh: menjadi {after}, <b>{jump} lebih setiap bulan</b>, atau {pct}.</p>
{FIG}
<p>Besar kenaikan itu bergantung pada kadar terapung. Jadual di bawah mengekalkan promosi 3.5% selama 24 bulan dan hanya menukar kadar terapung:</p>
{FTABLE}
<p>Setiap 0.5% kadar terapung yang lebih tinggi menambah ansuran bulan ke-25 kira-kira {step1} dan jumlah faedah 30 tahun kira-kira {step_total}. Jika seluruh pinjaman pada 4.5% tanpa promosi, jumlah faedahnya {no_promo}, jadi dua tahun promosi hanya menjimatkan kira-kira {promo_saving}. Kebanyakan faedah dibayar dalam tempoh terapung.</p>

<h2>Kadar promosi terendah tidak semestinya pakej termurah</h2>
<p>Bank kadangkala menawarkan pilihan antara kadar rendah untuk tempoh pendek dan kadar sedikit lebih tinggi untuk tempoh lebih panjang. Tiga pakej untuk pinjaman yang sama, RM 400K selama 30 tahun:</p>
{PTABLE}
<p>Pakej 2.9% nampak paling menarik, tetapi hanya 12 bulan. Jika kadar terapung kekal rendah pada 3.5%, pakej itu memang paling murah. Pada 4.5% ke atas, ia lebih mahal kira-kira {pkg_gap} berbanding 3.8% selama 3 tahun. Semakin tinggi kadar terapung berbanding kadar promosi, <b>semakin penting tempoh promosi berbanding kadarnya</b>. Bandingkan jumlah faedah pada beberapa kadar terapung sebelum memilih, dan semak tempoh lock-in serta penalti bayaran awal setiap pakej.</p>

{CALC}

<h2>Persediaan sebelum promosi tamat</h2>
<ul>
<li><b>Kira ansuran pada kadar terapung 1-2% lebih tinggi daripada jangkaan</b>, dan pinjam hanya jumlah yang masih mampu dibayar dalam keadaan itu.</li>
<li><b>Simpan wang untuk bayaran awal</b> selepas tempoh lock-in tamat. Setiap ringgit yang dibayar ketika itu menjimatkan faedah pada kadar terapung penuh. <a href="/fincal/bayar-pinjaman-awal/">Berbaloikah bayar pinjaman lebih awal? →</a></li>
<li><b>Tanya formula kadar terapung</b>: kadar rujukan apa, margin berapa, bila ia berubah, dan di mana ia ditulis dalam perjanjian.</li>
<li>Menjelang tamat promosi, <b>bandingkan tawaran refinance</b> daripada bank lain, termasuk duti setem, yuran guaman dan yuran penilaian.</li>
</ul>
""",
    faq=[
        ("Bagaimana kadar terapung pinjaman rumah dikira?",
         "Biasanya kadar rujukan ditambah margin. Di Malaysia rujukannya ialah Standardised Base Rate (SBR) yang mengikut OPR. Formula tepat ada dalam perjanjian pinjaman anda."),
        ("Selepas promosi tamat, ansuran naik berapa?",
         "Bergantung pada beza kadar promosi dan kadar terapung. Untuk RM 400K selama 30 tahun, 3.5% dua tahun kemudian 4.5%, ansuran naik kira-kira RM 218 sebulan, lebih kurang 12%. Gunakan kalkulator di atas untuk pinjaman anda."),
        ("Pilih promosi pendek berkadar rendah atau promosi panjang berkadar lebih tinggi?",
         "Jika kadar terapung jauh di atas kadar promosi, promosi yang lebih panjang biasanya lebih murah untuk keseluruhan pinjaman. Jika kadar terapung kekal rendah, promosi pendek boleh menang. Bandingkan jumlah faedah pada beberapa kadar."),
        ("Patutkah saya bayar sebahagian pinjaman apabila promosi tamat?",
         "Jika ada wang lebihan dan tempoh lock-in sudah tamat, bayaran awal ketika itu mengurangkan ansuran atau tempoh dan jumlah faedah. Simpan dahulu dana kecemasan untuk beberapa bulan perbelanjaan."),
    ],
    promo=("Memantau perubahan kadar?", "Aplikasi Fincal mengira semula jadual bayaran setiap kali kadar berubah, dan boleh digunakan luar talian:",
           [("Beberapa tempoh kadar", "promosi kemudian terapung, seberapa banyak tempoh yang perlu"),
            ("Bayaran awal", "sekali atau berkala, dengan penalti, lihat berapa yang dijimatkan"),
            ("Simpan dan bandingkan", "letakkan pakej pinjaman sebelah-menyebelah dan pilih yang termurah")]),
)
