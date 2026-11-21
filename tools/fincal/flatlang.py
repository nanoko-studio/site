"""Content for the flat vs reducing-balance article, one dict per language.
Body placeholders: {FIG1} {FIG2} {EXTABLE} {HBARS} {APRTABLE} {CONV} {flat_i} {last_bal} {last_bal_s}
{flat_i12_s} {eq_i12_s} {ex_link} {lo} {hi} {P}. FAQ answers may use {small}."""

A = {}

# ---------------------------------------------------------------- vi
A["vi"] = dict(
    path="/fincal/lai-phang-va-lai-giam-dan/", ct="web-fincal-article-flat-vi",
    title="Lãi phẳng và lãi giảm dần: cách tính, ví dụ và quy đổi lãi suất thực | Fincal",
    h1="Lãi phẳng và lãi giảm dần: khác nhau thế nào, loại nào đắt hơn?",
    desc="Lãi phẳng 1%/tháng thực ra đắt gần gấp đôi lãi giảm dần cùng mức. Xem cách tính từng loại, ví dụ vay 100 triệu có biểu đồ và bảng quy đổi lãi phẳng sang lãi suất thực.",
    crumb="Lãi phẳng và lãi giảm dần", byline="Nanoko Studio · Cập nhật 20/11/2026", summary="Tóm tắt",
    P=100_000_000, rate=12, small_rate=6, unit="m", conv=(1, 12), div=1,
    rates=[12, 18, 24], terms=[6, 12, 24, 36, 60],
    fmt=dict(sep=".", dc=True, cur="đ", pre=False, dec=0, intl="vi-VN"),
    names=dict(flat="Lãi phẳng", equal="Dư nợ giảm dần", annuity="Trả góp đều"),
    sfx="%/năm", row="{m}%/tháng<small>{y}%/năm</small>",
    tbl_group="Lãi suất thực theo thời hạn vay (tháng)",
    month_tick="T{m}", month_tick_rest="T{m}", month_tip="Tháng {m}",
    ticks1=["0", "500k", "1tr"], ticks2=["0", "50tr", "100tr"],
    tip_bal="Còn nợ thực tế", tip_base="Lãi phẳng tính trên",
    ex_rows=["Trả tháng 1", "Trả tháng 12", "Tổng tiền lãi"], hbars_aria="Tổng tiền lãi theo cách tính",
    tldr="Cùng ghi là <b>12%/năm</b>, vay 100 triệu trong 12 tháng:", tile_small="tiền lãi",
    hero="Lãi phẳng 12%/năm thực chất là", hero_small="tính theo dư nợ giảm dần",
    fig1=("Tiền lãi mỗi tháng", "Vay 100 triệu, 12%/năm, 12 tháng. Chạm vào cột để xem số tiền.",
          "Lãi phẳng giữ nguyên <b>{flat_i12_s}</b> đến tháng cuối. Lãi giảm dần chỉ còn <b>{eq_i12_s}</b> ở tháng 12.",
          "Tiền lãi mỗi tháng: lãi phẳng giữ nguyên, dư nợ giảm dần giảm dần theo tháng"),
    fig2=("Lãi được tính trên số tiền nào?", "Cột là số tiền còn nợ đầu mỗi tháng. Đường nét đứt là số tiền lãi phẳng dùng để tính lãi.",
          "Còn nợ thực tế", "Lãi phẳng tính trên 100 triệu",
          "Số tiền còn nợ giảm dần mỗi tháng, trong khi lãi phẳng luôn tính trên 100 triệu"),
    conv_t=dict(title="Quy đổi nhanh", rate="Lãi phẳng", rate_unit="%/tháng", term="Thời hạn", term_unit="tháng",
                apr="Lãi suất thực", flat="Vay 100 triệu, tiền lãi phẳng", equal="Nếu tính dư nợ giảm dần cùng mức",
                more="Tính với số tiền của bạn →"),
    body="""
<h2>Lãi phẳng là gì?</h2>
<p>Lãi phẳng, hay lãi tính trên dư nợ ban đầu, là cách tính lãi mỗi tháng trên <b>toàn bộ số tiền vay ban đầu</b>, dù bạn đã trả bớt gốc.</p>
<div class="formula">Tiền lãi mỗi tháng = Số tiền vay × Lãi suất năm ÷ 12</div>
<p>Vay 100 triệu với lãi phẳng 12%/năm thì tháng nào cũng trả {flat_i} tiền lãi, kể cả tháng cuối khi bạn chỉ còn nợ khoảng {last_bal_s}. Hình thức này hay gặp ở vay tiêu dùng và mua trả góp xe máy, điện thoại.</p>

<h2>Lãi giảm dần là gì?</h2>
<p>Lãi giảm dần, hay lãi tính trên dư nợ giảm dần, chỉ tính lãi trên <b>số tiền bạn còn nợ</b>. Trả bớt gốc thì tiền lãi giảm theo. Có hai cách trả phổ biến:</p>
<ul>
<li><b>Dư nợ giảm dần (gốc đều)</b>: mỗi tháng trả cùng một khoản gốc, nên tháng đầu trả nhiều nhất rồi giảm dần. Hay gặp ở vay mua nhà, mua xe tại ngân hàng.</li>
<li><b>Trả góp đều hằng tháng</b>: tháng nào cũng trả một số tiền như nhau. Những tháng đầu phần lãi chiếm nhiều, về sau phần gốc chiếm nhiều hơn.</li>
</ul>

{FIG1}

<h2>Ví dụ: vay 100 triệu, 12%/năm, 12 tháng</h2>
{EXTABLE}
{HBARS}
<p>Tháng đầu, lãi phẳng và dư nợ giảm dần trả bằng nhau. Khác biệt nằm ở các tháng sau: với lãi phẳng, tiền lãi không giảm dù dư nợ đã giảm. <a href="{ex_link}">Xem ví dụ này trong máy tính lãi vay →</a></p>

<h2>Vì sao lãi phẳng đắt gần gấp đôi?</h2>
<p>Trả góp đều trong 12 tháng thì tính trung bình bạn chỉ còn giữ khoảng một nửa số tiền vay. Lãi phẳng vẫn tính lãi trên đủ 100 triệu suốt cả năm.</p>
{FIG2}
<p>Vì vậy, muốn so sánh với lãi giảm dần, phải quy lãi phẳng ra <b>lãi suất thực tế</b>, hay lãi suất hiệu dụng. Đó là mức lãi giảm dần cho ra đúng số tiền bạn phải trả mỗi tháng.</p>

<h2>Bảng quy đổi lãi phẳng sang lãi suất thực</h2>
{APRTABLE}
<p>Quy tắc nhẩm nhanh: <b>lãi suất thực khoảng {lo}-{hi} lần lãi phẳng</b>. Không có công thức đơn giản để quy đổi chính xác, nên máy tính bên dưới giải phương trình để ra con số đúng.</p>

{CONV}

<h2>Cách nhận biết khi đọc hợp đồng</h2>
<ul>
<li>Lãi phẳng thường được ghi là "lãi suất tính trên số tiền vay ban đầu", "lãi suất cố định trên dư nợ gốc", hoặc chỉ ghi "x%/tháng" kèm một số tiền trả cố định.</li>
<li>Lãi giảm dần thường được ghi là "tính trên dư nợ thực tế" hoặc "tính trên dư nợ giảm dần".</li>
<li>Cách chắc chắn nhất là <b>xin lịch trả nợ và tổng số tiền lãi</b>, rồi nhập vào máy tính để xem lãi suất thực.</li>
</ul>
""",
    faq=[
        ("Lãi phẳng có lúc nào lợi hơn không?",
         "Có, nếu mức lãi phẳng thấp hơn khoảng một nửa mức lãi giảm dần bạn được chào. Ví dụ lãi phẳng 6%/năm trong 12 tháng tương đương lãi suất thực khoảng {small}, vẫn rẻ hơn khoản vay dư nợ giảm dần 12%/năm. Hãy so sánh theo lãi suất thực hoặc tổng tiền lãi, đừng so con số ghi trên quảng cáo."),
        ("Trả góp 0% có phải lãi phẳng không?",
         "Lãi bằng 0 thì cách tính lãi không còn quan trọng. Chi phí thật thường nằm ở phí hồ sơ, phí bảo hiểm hoặc giá bán cao hơn giá trả thẳng. Hãy cộng các khoản này lại để so sánh."),
        ("Trả nợ trước hạn với khoản vay lãi phẳng thì sao?",
         "Tuỳ hợp đồng. Có nơi chỉ thu lãi đến ngày tất toán cộng phí phạt, có nơi vẫn thu phần lãi còn lại. Hãy hỏi rõ trước khi ký."),
        ("Vay ngân hàng mua nhà thường tính lãi kiểu nào?",
         "Phần lớn là lãi giảm dần, theo kiểu gốc đều hoặc trả góp đều hằng tháng, thường kèm lãi suất ưu đãi cố định một thời gian rồi thả nổi."),
    ],
    promo=("Đang cân nhắc một khoản vay?", "App Fincal giúp bạn so sánh trước khi ký, dùng được cả khi không có mạng:",
           [("Quy đổi lãi phẳng", "xem lãi suất thực của mọi khoản vay trả góp"),
            ("Lưu và so sánh", "đặt các phương án cạnh nhau để chọn khoản rẻ nhất"),
            ("Trả nợ trước hạn", "tính cả phí phạt, xem tiết kiệm được bao nhiêu")]),
)

# ---------------------------------------------------------------- en
A["en"] = dict(
    path="/fincal/flat-rate-vs-reducing-balance/", ct="web-fincal-article-flat",
    title="Flat Rate vs Reducing Balance: How Loan Interest Works, With a Converter | Fincal",
    h1="Flat rate vs reducing balance: which loan really costs more?",
    desc="A 12% flat rate costs almost twice as much as 12% on a reducing balance. See how each is worked out, a 10,000 loan example with charts, and a table that converts flat rates to the effective rate.",
    crumb="Flat rate vs reducing balance", byline="Nanoko Studio · Updated 20 Nov 2026", summary="Summary",
    P=10_000, rate=12, small_rate=6, unit="y", conv=(8, 36), div=1,
    rates=[5, 8, 12], terms=[12, 24, 36, 60, 84],
    fmt=dict(sep=",", dc=False, cur="", pre=False, dec=2, intl="en-US"),
    names=dict(flat="Flat rate", equal="Reducing balance", annuity="Equal payments"),
    sfx="% a year", row="{y}%",
    tbl_group="Effective rate a year, by term (months)",
    month_tick="Month {m}", month_tick_rest="{m}", month_tip="Month {m}",
    ticks1=["0", "50", "100"], ticks2=["0", "5K", "10K"],
    tip_bal="You still owe", tip_base="Flat rate charged on",
    ex_rows=["Payment, month 1", "Payment, month 12", "Total interest"], hbars_aria="Total interest by method",
    tldr="Both quoted at <b>12% a year</b>, borrowing 10,000 for 12 months:", tile_small="interest",
    hero="A 12% flat rate is really", hero_small="on a reducing balance",
    fig1=("Interest each month", "10,000 at 12% a year over 12 months. Tap a bar to see the amount.",
          "The flat rate stays at <b>{flat_i12_s}</b> right to the end. On a reducing balance it is down to <b>{eq_i12_s}</b> by month 12.",
          "Interest each month: the flat rate stays the same, the reducing balance falls every month"),
    fig2=("What is the interest charged on?", "Bars show what you still owe at the start of each month. The dashed line is the amount the flat rate charges interest on.",
          "You still owe", "Flat rate charged on 10,000",
          "The balance owed falls every month, while the flat rate is always charged on 10,000"),
    conv_t=dict(title="Quick converter", rate="Flat rate", rate_unit="% a year", term="Term", term_unit="months",
                apr="Effective rate", flat="Interest on 10,000 at the flat rate", equal="Same rate on a reducing balance",
                more="Try it with your own numbers →"),
    body="""
<h2>What is a flat interest rate?</h2>
<p>With a flat rate, the interest is worked out on the <b>full amount you originally borrowed</b>, and it stays that way however much you have already paid back.</p>
<div class="formula">Monthly interest = Loan amount × Annual rate ÷ 12</div>
<p>Borrow 10,000 at a 12% flat rate and you pay {flat_i} in interest every month - even in the final month, when you only owe about {last_bal_s}. Flat rates turn up mostly on personal loans, car finance and store instalment plans.</p>

<h2>What is a reducing balance rate?</h2>
<p>A reducing balance rate (also called a diminishing or effective rate) charges interest only on <b>what you still owe</b>. Each repayment shrinks the balance, so the interest shrinks with it. It usually comes in one of two forms:</p>
<ul>
<li><b>Equal principal</b>: you pay off the same slice of the loan every month, so the first payment is the largest and each one after is a little smaller.</li>
<li><b>Equal monthly payments</b>: the payment never changes. Early on it is mostly interest; towards the end it is mostly principal. Most mortgages and bank car loans work this way.</li>
</ul>

{FIG1}

<h2>Worked example: 10,000 at 12% for 12 months</h2>
{EXTABLE}
{HBARS}
<p>In month 1 the flat-rate loan and the reducing-balance loan cost exactly the same. The gap opens up after that: on a flat rate the interest never drops, even though your balance does. <a href="{ex_link}">Open this example in the loan calculator →</a></p>

<h2>Why does a flat rate cost almost twice as much?</h2>
<p>When you repay in monthly instalments over a year, you only have about half of the money for the year on average. A flat rate still charges interest on the full 10,000 the whole time.</p>
{FIG2}
<p>So before comparing a flat-rate offer with a reducing-balance one, convert it to the <b>effective rate</b>: the reducing-balance rate that gives you exactly the same monthly payment. It is close to the APR lenders quote, although an APR may also include fees.</p>

<h2>Flat rate to effective rate conversion table</h2>
{APRTABLE}
<p>Rule of thumb: <b>the effective rate is roughly {lo}-{hi} times the flat rate</b>. There is no simple formula for the exact figure, so the converter below solves it for you.</p>

{CONV}

<h2>How to spot a flat rate in a loan offer</h2>
<ul>
<li>Flat rates are often labelled "flat rate p.a.", "add-on interest", or shown as a bare percentage next to a fixed monthly payment.</li>
<li>Reducing balance loans usually mention "interest on the outstanding balance", "reducing balance" or an APR.</li>
<li>The surest way is to <b>ask for the repayment schedule and the total interest</b>, then put them into the calculator to see the real rate.</li>
</ul>
""",
    faq=[
        ("Is a flat rate ever the better deal?",
         "Yes, if the flat rate is less than about half of the reducing-balance rate you have been offered. A 6% flat rate over 12 months works out to an effective rate of about {small}, which still beats a 12% reducing-balance loan. Compare effective rates or total interest, not the headline number."),
        ("Is a flat rate the same as a fixed rate?",
         "No. A fixed rate means the rate does not change during the loan, and it is normally charged on a reducing balance. A flat rate is about what the interest is charged on: always the original amount."),
        ("Is 0% finance a flat rate?",
         "With no interest, the method makes no difference. The real cost tends to hide in arrangement fees, insurance, or a price that is higher than paying upfront. Add those up before you compare."),
        ("What happens if I pay off a flat-rate loan early?",
         "It depends on the contract. Some lenders only charge interest up to the settlement date plus a fee; others still charge part or all of the remaining interest. Check before you sign."),
    ],
    promo=("Weighing up a loan?", "The Fincal app helps you compare before you sign, even offline:",
           [("Flat rate converter", "see the effective rate of any instalment loan"),
            ("Save and compare", "put your options side by side and pick the cheapest"),
            ("Early repayment", "include fees and see how much you save")]),
)

# ---------------------------------------------------------------- id
A["id"] = dict(
    path="/fincal/bunga-flat-vs-bunga-efektif/", ct="web-fincal-article-flat-id",
    title="Bunga Flat vs Bunga Efektif: Cara Hitung, Contoh dan Tabel Konversi | Fincal",
    h1="Bunga flat vs bunga efektif: apa bedanya, mana yang lebih mahal?",
    desc="Bunga flat 1% per bulan ternyata hampir dua kali lebih mahal dari bunga efektif dengan angka yang sama. Lihat cara hitungnya, contoh pinjaman Rp 100 juta lengkap dengan grafik, dan tabel konversi ke bunga efektif.",
    crumb="Bunga flat vs bunga efektif", byline="Nanoko Studio · Diperbarui 20/11/2026", summary="Ringkasan",
    P=100_000_000, rate=12, small_rate=6, unit="m", conv=(1, 12), div=1,
    rates=[6, 12, 18], terms=[6, 12, 24, 36, 60],
    fmt=dict(sep=".", dc=True, cur="Rp", pre=True, dec=0, intl="id-ID"),
    names=dict(flat="Bunga flat", equal="Bunga efektif", annuity="Anuitas"),
    sfx="% per tahun", row="{m}%/bulan<small>{y}%/tahun</small>",
    tbl_group="Bunga efektif per tahun menurut tenor (bulan)",
    month_tick="Bulan {m}", month_tick_rest="{m}", month_tip="Bulan ke-{m}",
    ticks1=["0", "500 rb", "1 jt"], ticks2=["0", "50 jt", "100 jt"],
    tip_bal="Sisa utang", tip_base="Bunga flat dihitung dari",
    ex_rows=["Cicilan bulan ke-1", "Cicilan bulan ke-12", "Total bunga"], hbars_aria="Total bunga menurut metode",
    tldr="Sama-sama tertulis <b>1% per bulan</b> (12% per tahun), pinjam Rp 100 juta selama 12 bulan:", tile_small="total bunga",
    hero="Bunga flat 1% per bulan sebenarnya setara", hero_small="bunga efektif",
    fig1=("Bunga setiap bulan", "Pinjaman Rp 100 juta, 12% per tahun, 12 bulan. Ketuk batang untuk melihat angkanya.",
          "Bunga flat tetap <b>{flat_i12_s}</b> sampai bulan terakhir. Bunga efektif tinggal <b>{eq_i12_s}</b> di bulan ke-12.",
          "Bunga setiap bulan: bunga flat tetap, bunga efektif turun setiap bulan"),
    fig2=("Bunga dihitung dari uang yang mana?", "Batang menunjukkan sisa utang di awal setiap bulan. Garis putus-putus adalah dasar perhitungan bunga flat.",
          "Sisa utang sebenarnya", "Bunga flat dihitung dari Rp 100 juta",
          "Sisa utang turun setiap bulan, sementara bunga flat selalu dihitung dari Rp 100 juta"),
    conv_t=dict(title="Konversi cepat", rate="Bunga flat", rate_unit="% per bulan", term="Tenor", term_unit="bulan",
                apr="Bunga efektif", flat="Pinjam Rp 100 juta, total bunga flat", equal="Jika memakai bunga efektif dengan angka sama",
                more="Hitung dengan jumlah pinjaman Anda →"),
    body="""
<h2>Apa itu bunga flat?</h2>
<p>Bunga flat dihitung dari <b>pokok pinjaman awal</b> setiap bulan, berapa pun pokok yang sudah Anda cicil.</p>
<div class="formula">Bunga per bulan = Pokok awal × Suku bunga per tahun ÷ 12</div>
<p>Pinjam Rp 100 juta dengan bunga flat 12% per tahun, bunga yang Anda bayar tetap {flat_i} setiap bulan, termasuk di bulan terakhir saat sisa utang tinggal sekitar {last_bal_s}. Bunga flat banyak dipakai untuk KTA, kredit motor, kredit mobil dan cicilan elektronik.</p>

<h2>Apa itu bunga efektif?</h2>
<p>Bunga efektif, sering juga disebut bunga menurun, hanya dihitung dari <b>sisa pokok yang belum dibayar</b>. Setiap kali pokok berkurang, bunganya ikut turun. Ada dua cara bayar yang umum:</p>
<ul>
<li><b>Pokok tetap</b>: pokok yang dicicil sama setiap bulan, jadi cicilan pertama paling besar lalu terus mengecil.</li>
<li><b>Anuitas</b>: cicilan sama besar setiap bulan. Di awal porsi bunganya besar, belakangan porsi pokok yang lebih besar. Hampir semua KPR memakai cara ini.</li>
</ul>

{FIG1}

<h2>Contoh: pinjaman Rp 100 juta, 12% per tahun, 12 bulan</h2>
{EXTABLE}
{HBARS}
<p>Di bulan pertama, cicilan bunga flat dan bunga efektif sama besar. Bedanya muncul di bulan-bulan berikutnya: dengan bunga flat, bunganya tidak turun walaupun utang Anda sudah berkurang. <a href="{ex_link}">Lihat contoh ini di simulasi kredit →</a></p>

<h2>Kenapa bunga flat hampir dua kali lebih mahal?</h2>
<p>Kalau dicicil rata selama setahun, rata-rata Anda hanya memegang sekitar separuh uang pinjaman. Tapi bunga flat tetap dihitung dari Rp 100 juta penuh sepanjang tahun.</p>
{FIG2}
<p>Karena itu, sebelum membandingkan dengan pinjaman bunga efektif, ubah dulu bunga flat menjadi <b>bunga efektif</b>: bunga menurun yang menghasilkan cicilan bulanan yang persis sama.</p>

<h2>Tabel konversi bunga flat ke bunga efektif</h2>
{APRTABLE}
<p>Cara cepat menaksir: <b>bunga efektif kira-kira {lo}-{hi} kali bunga flat</b>. Tidak ada rumus sederhana untuk angka pastinya, jadi kalkulator di bawah ini yang menghitungnya.</p>

{CONV}

<h2>Cara mengenali bunga flat di penawaran pinjaman</h2>
<ul>
<li>Bunga flat biasanya ditulis "bunga flat", "bunga tetap per bulan", atau hanya "mulai 0,99% per bulan" dengan cicilan yang sudah dipatok.</li>
<li>Bunga efektif biasanya ditulis "bunga efektif", "bunga menurun" atau "dihitung dari sisa pokok".</li>
<li>Cara paling pasti adalah <b>minta tabel angsuran dan total bunganya</b>, lalu masukkan ke simulasi kredit untuk melihat bunga efektifnya.</li>
</ul>
""",
    faq=[
        ("Apakah bunga flat bisa lebih murah?",
         "Bisa, kalau bunga flat-nya kurang dari sekitar separuh bunga efektif yang ditawarkan. Misalnya bunga flat 6% per tahun selama 12 bulan setara bunga efektif sekitar {small}, masih lebih murah dari pinjaman bunga efektif 12% per tahun. Bandingkan bunga efektif atau total bunganya, jangan angka di iklan."),
        ("Cicilan 0% itu pakai bunga flat?",
         "Kalau bunganya nol, metode perhitungannya tidak berpengaruh. Biaya sebenarnya biasanya ada di biaya admin, asuransi, atau harga barang yang lebih mahal dibanding bayar tunai. Jumlahkan semuanya sebelum membandingkan."),
        ("Bagaimana kalau pinjaman bunga flat dilunasi lebih cepat?",
         "Tergantung perjanjiannya. Ada yang hanya menagih bunga sampai tanggal pelunasan ditambah penalti, ada juga yang tetap menagih sebagian atau seluruh sisa bunga. Tanyakan dulu sebelum tanda tangan."),
        ("KPR pakai bunga flat atau bunga efektif?",
         "Hampir semua KPR bank memakai bunga efektif dengan cicilan anuitas, biasanya dengan bunga fixed beberapa tahun pertama lalu floating."),
    ],
    promo=("Sedang menimbang pinjaman?", "Aplikasi Fincal membantu Anda membandingkan sebelum tanda tangan, bisa dipakai tanpa internet:",
           [("Konversi bunga flat", "lihat bunga efektif dari setiap pinjaman cicilan"),
            ("Simpan dan bandingkan", "taruh beberapa pilihan berdampingan untuk memilih yang termurah"),
            ("Pelunasan dipercepat", "termasuk penalti, lihat berapa yang bisa dihemat")]),
)

# ---------------------------------------------------------------- th
A["th"] = dict(
    path="/fincal/flat-rate-kap-lot-ton-lot-dok/", ct="web-fincal-article-flat-th",
    title="ดอกเบี้ย Flat Rate กับลดต้นลดดอก ต่างกันอย่างไร พร้อมตารางแปลงเป็น Effective Rate | Fincal",
    h1="ดอกเบี้ย flat rate กับลดต้นลดดอก ต่างกันอย่างไร แบบไหนแพงกว่า",
    desc="ดอกเบี้ย flat rate 12% ต่อปี ที่จริงแพงเกือบเท่าตัวของดอกเบี้ยลดต้นลดดอกในอัตราเดียวกัน ดูวิธีคิด ตัวอย่างกู้ 100,000 บาทพร้อมกราฟ และตารางแปลง flat rate เป็นดอกเบี้ยที่แท้จริง",
    crumb="Flat rate กับลดต้นลดดอก", byline="Nanoko Studio · อัปเดต 20 พ.ย. 2569", summary="สรุป",
    P=100_000, rate=12, small_rate=6, unit="y", conv=(3, 60), div=1,
    rates=[3, 6, 12], terms=[12, 36, 48, 60, 84],
    fmt=dict(sep=",", dc=False, cur="บาท", pre=False, dec=0, intl="th-TH"),
    names=dict(flat="Flat rate", equal="ลดต้นลดดอก", annuity="ผ่อนงวดเท่ากัน"),
    sfx="% ต่อปี", row="{y}%",
    tbl_group="ดอกเบี้ยที่แท้จริงต่อปี ตามระยะเวลาผ่อน (เดือน)",
    month_tick="เดือน {m}", month_tick_rest="{m}", month_tip="เดือนที่ {m}",
    ticks1=["0", "500", "1,000"], ticks2=["0", "5 หมื่น", "1 แสน"],
    tip_bal="หนี้คงเหลือ", tip_base="Flat rate คิดจาก",
    ex_rows=["ค่างวดเดือนที่ 1", "ค่างวดเดือนที่ 12", "ดอกเบี้ยรวม"], hbars_aria="ดอกเบี้ยรวมตามวิธีคิด",
    tldr="อัตราเท่ากันที่ <b>12% ต่อปี</b> กู้ 100,000 บาท ผ่อน 12 เดือน:", tile_small="ดอกเบี้ยรวม",
    hero="Flat rate 12% ต่อปี ที่จริงคือ", hero_small="เมื่อคิดแบบลดต้นลดดอก",
    fig1=("ดอกเบี้ยแต่ละเดือน", "กู้ 100,000 บาท ดอกเบี้ย 12% ต่อปี ผ่อน 12 เดือน แตะที่แท่งเพื่อดูตัวเลข",
          "Flat rate ยังคิดดอกเบี้ย <b>{flat_i12_s}</b> ไปจนถึงเดือนสุดท้าย ส่วนลดต้นลดดอกเหลือแค่ <b>{eq_i12_s}</b> ในเดือนที่ 12",
          "ดอกเบี้ยแต่ละเดือน: flat rate เท่าเดิมทุกเดือน ลดต้นลดดอกลดลงทุกเดือน"),
    fig2=("ดอกเบี้ยคิดจากเงินก้อนไหน", "แท่งคือหนี้คงเหลือต้นเดือน เส้นประคือยอดที่ flat rate ใช้คิดดอกเบี้ย",
          "หนี้คงเหลือจริง", "Flat rate คิดจาก 100,000 บาท",
          "หนี้คงเหลือลดลงทุกเดือน แต่ flat rate คิดดอกเบี้ยจาก 100,000 บาทเสมอ"),
    conv_t=dict(title="แปลงอัตราดอกเบี้ย", rate="Flat rate", rate_unit="% ต่อปี", term="ระยะเวลาผ่อน", term_unit="เดือน",
                apr="ดอกเบี้ยที่แท้จริง", flat="กู้ 100,000 บาท ดอกเบี้ยรวมแบบ flat rate", equal="ถ้าคิดแบบลดต้นลดดอกที่อัตราเดียวกัน",
                more="คำนวณด้วยยอดกู้ของคุณ →"),
    body="""
<h2>ดอกเบี้ย flat rate คืออะไร</h2>
<p>ดอกเบี้ยแบบ flat rate คิดจาก<b>เงินต้นตั้งต้นทั้งก้อน</b>ทุกเดือน ไม่ว่าคุณจะผ่อนเงินต้นไปแล้วเท่าไร</p>
<div class="formula">ดอกเบี้ยต่อเดือน = เงินต้นตั้งต้น × ดอกเบี้ยต่อปี ÷ 12</div>
<p>กู้ 100,000 บาท flat rate 12% ต่อปี จะเสียดอกเบี้ยเดือนละ {flat_i} เท่ากันทุกเดือน แม้แต่เดือนสุดท้ายที่เหลือหนี้อยู่ราว {last_bal_s} แบบนี้พบบ่อยในสินเชื่อเช่าซื้อรถยนต์ รถจักรยานยนต์ และสินเชื่อส่วนบุคคลบางประเภท</p>

<h2>ดอกเบี้ยลดต้นลดดอกคืออะไร</h2>
<p>ดอกเบี้ยแบบลดต้นลดดอก (effective rate) คิดจาก<b>เงินต้นที่ยังค้างอยู่</b>เท่านั้น ผ่อนเงินต้นไปเท่าไร ดอกเบี้ยก็ลดลงตาม วิธีผ่อนที่เจอบ่อยมี 2 แบบ</p>
<ul>
<li><b>เงินต้นเท่ากัน</b>: ตัดเงินต้นเท่ากันทุกงวด งวดแรกจึงจ่ายมากที่สุด แล้วค่อย ๆ ลดลง</li>
<li><b>ผ่อนงวดเท่ากัน</b>: จ่ายเท่ากันทุกเดือน ช่วงแรกส่วนใหญ่เป็นดอกเบี้ย ช่วงหลังส่วนใหญ่เป็นเงินต้น สินเชื่อบ้านเกือบทั้งหมดใช้แบบนี้</li>
</ul>

{FIG1}

<h2>ตัวอย่าง: กู้ 100,000 บาท ดอกเบี้ย 12% ต่อปี 12 เดือน</h2>
{EXTABLE}
{HBARS}
<p>เดือนแรก flat rate กับลดต้นลดดอกจ่ายเท่ากัน ความต่างเกิดในเดือนถัด ๆ ไป เพราะ flat rate ไม่ลดดอกเบี้ยลงเลยแม้หนี้จะลดลงแล้ว <a href="{ex_link}">ดูตัวอย่างนี้ในเครื่องคำนวณสินเชื่อ →</a></p>

<h2>ทำไม flat rate ถึงแพงเกือบเท่าตัว</h2>
<p>เมื่อผ่อนเท่า ๆ กันตลอดปี โดยเฉลี่ยคุณถือเงินกู้อยู่แค่ราวครึ่งเดียว แต่ flat rate ยังคิดดอกเบี้ยจากเต็ม 100,000 บาทตลอดทั้งปี</p>
{FIG2}
<p>ดังนั้นถ้าจะเทียบกับเงินกู้แบบลดต้นลดดอก ต้องแปลง flat rate เป็น<b>ดอกเบี้ยที่แท้จริง (effective rate)</b> ก่อน ซึ่งก็คืออัตราแบบลดต้นลดดอกที่ทำให้ค่างวดออกมาเท่ากันพอดี</p>

<h2>ตารางแปลง flat rate เป็นดอกเบี้ยที่แท้จริง</h2>
{APRTABLE}
<p>จำง่าย ๆ: <b>ดอกเบี้ยที่แท้จริงประมาณ {lo}-{hi} เท่าของ flat rate</b> ตัวเลขที่แม่นยำไม่มีสูตรง่าย ๆ เครื่องมือด้านล่างจึงคำนวณให้</p>

{CONV}

<h2>ดูอย่างไรว่าสัญญาเป็นแบบ flat rate</h2>
<ul>
<li>Flat rate มักเขียนว่า "อัตราดอกเบี้ยคงที่ต่อปี" "ดอกเบี้ยแบบ flat" หรือบอกแค่อัตราดอกเบี้ยคู่กับค่างวดที่ตายตัว</li>
<li>ลดต้นลดดอกมักเขียนว่า "คิดจากเงินต้นคงเหลือ" หรือ "อัตราดอกเบี้ยที่แท้จริง (effective rate)"</li>
<li>วิธีที่ชัวร์ที่สุดคือ<b>ขอตารางผ่อนชำระและยอดดอกเบี้ยรวม</b> แล้วกรอกลงเครื่องคำนวณเพื่อดูอัตราที่แท้จริง</li>
</ul>
""",
    faq=[
        ("Flat rate ถูกกว่าในกรณีไหน",
         "เมื่อ flat rate ต่ำกว่าราวครึ่งหนึ่งของอัตราลดต้นลดดอกที่ได้รับข้อเสนอ เช่น flat rate 6% ต่อปี ผ่อน 12 เดือน เท่ากับดอกเบี้ยที่แท้จริงราว {small} ซึ่งยังถูกกว่าเงินกู้ลดต้นลดดอก 12% ต่อปี ให้เทียบด้วยดอกเบี้ยที่แท้จริงหรือยอดดอกเบี้ยรวม อย่าเทียบตัวเลขในโฆษณา"),
        ("ดอกเบี้ยคงที่ (fixed rate) กับ flat rate เหมือนกันไหม",
         "ไม่เหมือนกัน fixed rate หมายถึงอัตราดอกเบี้ยไม่เปลี่ยนในช่วงที่กำหนด และมักคิดแบบลดต้นลดดอก ส่วน flat rate หมายถึงคิดดอกเบี้ยจากเงินต้นตั้งต้นเสมอ ทั้งสองแบบมักถูกเรียกว่า \"ดอกเบี้ยคงที่\" จึงต้องถามให้ชัด"),
        ("ผ่อน 0% คิดแบบ flat rate หรือเปล่า",
         "ถ้าดอกเบี้ยเป็นศูนย์ วิธีคิดดอกเบี้ยก็ไม่มีผล ต้นทุนจริงมักอยู่ที่ค่าธรรมเนียม ประกัน หรือราคาสินค้าที่สูงกว่าซื้อเงินสด ลองรวมค่าใช้จ่ายเหล่านี้ก่อนเปรียบเทียบ"),
        ("ปิดสินเชื่อ flat rate ก่อนกำหนดได้ลดดอกเบี้ยไหม",
         "ขึ้นอยู่กับสัญญา บางแห่งคิดดอกเบี้ยถึงวันปิดบัญชีบวกค่าธรรมเนียม บางแห่งลดดอกเบี้ยที่เหลือให้เพียงบางส่วน ควรถามให้ชัดก่อนเซ็นสัญญา"),
    ],
    promo=("กำลังตัดสินใจเรื่องเงินกู้อยู่ใช่ไหม", "แอป Fincal ช่วยเปรียบเทียบก่อนเซ็นสัญญา ใช้ได้แม้ไม่มีอินเทอร์เน็ต:",
           [("แปลง flat rate", "ดูดอกเบี้ยที่แท้จริงของสินเชื่อผ่อนทุกแบบ"),
            ("บันทึกและเปรียบเทียบ", "วางหลายทางเลือกไว้ข้างกัน แล้วเลือกที่ถูกที่สุด"),
            ("โปะหนี้ก่อนกำหนด", "รวมค่าธรรมเนียม ดูว่าประหยัดได้เท่าไร")]),
)

# ---------------------------------------------------------------- pt-BR
A["pt-BR"] = dict(
    path="/fincal/taxa-flat-x-saldo-devedor/", ct="web-fincal-article-flat-pt",
    title="Taxa Flat x Juros sobre o Saldo Devedor (SAC e Price): Como Comparar | Fincal",
    h1="Taxa flat ou juros sobre o saldo devedor: qual sai mais caro?",
    desc="Uma taxa flat de 2% ao mês custa quase o dobro de 2% ao mês sobre o saldo devedor. Veja como cada uma é calculada, um exemplo de R$ 10.000 com gráficos e uma tabela que converte a taxa flat em taxa efetiva.",
    crumb="Taxa flat x saldo devedor", byline="Nanoko Studio · Atualizado em 20/11/2026", summary="Resumo",
    P=10_000, rate=24, small_rate=12, unit="m", conv=(2, 12), div=12,
    rates=[12, 24, 36], terms=[6, 12, 24, 36, 48],
    fmt=dict(sep=".", dc=True, cur="R$", pre=True, dec=2, intl="pt-BR"),
    names=dict(flat="Taxa flat", equal="SAC", annuity="Price"),
    sfx="% ao mês", row="{m}% a.m.",
    tbl_group="Taxa efetiva ao mês, por prazo (meses)",
    month_tick="Mês {m}", month_tick_rest="{m}", month_tip="Mês {m}",
    ticks1=["0", "100", "200"], ticks2=["0", "5 mil", "10 mil"],
    tip_bal="Saldo devedor", tip_base="Taxa flat cobrada sobre",
    ex_rows=["1ª parcela", "12ª parcela", "Total de juros"], hbars_aria="Total de juros por sistema",
    tldr="Com a mesma taxa de <b>2% ao mês</b>, um empréstimo de R$ 10.000 em 12 meses:", tile_small="de juros",
    hero="2% ao mês flat equivalem a", hero_small="sobre o saldo devedor",
    fig1=("Juros de cada mês", "R$ 10.000 a 2% ao mês em 12 meses. Toque numa barra para ver o valor.",
          "Na taxa flat, os juros continuam em <b>{flat_i12_s}</b> até o último mês. No SAC, caem para <b>{eq_i12_s}</b> no mês 12.",
          "Juros de cada mês: na taxa flat ficam iguais, no SAC caem todo mês"),
    fig2=("Sobre quanto os juros são cobrados?", "As barras mostram o saldo devedor no início de cada mês. A linha tracejada é a base de cálculo da taxa flat.",
          "Saldo devedor real", "Taxa flat cobrada sobre R$ 10.000",
          "O saldo devedor cai todo mês, enquanto a taxa flat é sempre cobrada sobre R$ 10.000"),
    conv_t=dict(title="Conversor rápido", rate="Taxa flat", rate_unit="% a.m.", term="Prazo", term_unit="meses",
                apr="Taxa efetiva", flat="R$ 10.000 na taxa flat, total de juros", equal="Mesma taxa sobre o saldo (SAC)",
                more="Calcular com o seu valor →"),
    body="""
<h2>O que é taxa flat?</h2>
<p>Na taxa flat, os juros de todo mês são calculados sobre o <b>valor total emprestado</b>, não importa quanto você já pagou.</p>
<div class="formula">Juros do mês = Valor emprestado × Taxa ao mês</div>
<p>Num empréstimo de R$ 10.000 com taxa flat de 2% ao mês, você paga {flat_i} de juros todo mês, inclusive na última parcela, quando deve só uns {last_bal_s}. Esse cálculo aparece em algumas ofertas de crédito pessoal, parcelamentos de loja e empréstimos informais, às vezes com o nome de "juros simples sobre o total".</p>

<h2>O que são juros sobre o saldo devedor?</h2>
<p>Aqui os juros incidem só sobre o <b>que você ainda deve</b>. A cada parcela paga o saldo cai, e os juros caem junto. No Brasil, os dois sistemas mais comuns são:</p>
<ul>
<li><b>SAC (Sistema de Amortização Constante)</b>: a amortização é a mesma todo mês, então a primeira parcela é a maior e as seguintes vão diminuindo. Muito usado no financiamento imobiliário.</li>
<li><b>Tabela Price</b>: parcelas iguais do começo ao fim. No início a maior parte é juros; no final, quase tudo é amortização. É o padrão em financiamento de veículos e crédito pessoal.</li>
</ul>

{FIG1}

<h2>Exemplo: R$ 10.000 a 2% ao mês em 12 meses</h2>
{EXTABLE}
{HBARS}
<p>Na primeira parcela, taxa flat e SAC cobram os mesmos juros. A diferença vem depois: na taxa flat os juros não baixam, mesmo com a dívida diminuindo. <a href="{ex_link}">Abrir este exemplo na calculadora de empréstimo →</a></p>

<h2>Por que a taxa flat sai quase pelo dobro?</h2>
<p>Pagando em parcelas ao longo do ano, em média você fica com só metade do dinheiro emprestado. A taxa flat continua cobrando juros sobre os R$ 10.000 inteiros o ano todo.</p>
{FIG2}
<p>Por isso, para comparar com uma oferta sobre o saldo devedor, converta a taxa flat em <b>taxa efetiva</b>: a taxa sobre o saldo que gera exatamente a mesma parcela. E na hora de fechar, olhe o <b>CET (Custo Efetivo Total)</b>, que a instituição é obrigada a informar e que inclui também tarifas, impostos e seguros.</p>

<h2>Tabela de conversão: taxa flat para taxa efetiva</h2>
{APRTABLE}
<p>Regra prática: <b>a taxa efetiva fica entre {lo} e {hi} vezes a taxa flat</b>. Não existe fórmula simples para o valor exato, então o conversor abaixo faz a conta por você.</p>

{CONV}

<h2>Como identificar a taxa flat numa proposta</h2>
<ul>
<li>A taxa flat costuma aparecer como "juros de x% ao mês sobre o valor total", "juros simples" ou só uma taxa ao lado de uma parcela fixa.</li>
<li>Juros sobre o saldo devedor aparecem como "Tabela Price", "SAC" ou "juros sobre o saldo devedor".</li>
<li>O jeito mais seguro é <b>pedir a planilha de pagamento e o CET</b> e conferir na calculadora.</li>
</ul>
""",
    faq=[
        ("A taxa flat pode sair mais barata?",
         "Pode, se ela for menor que cerca da metade da taxa sobre o saldo devedor que te ofereceram. Uma taxa flat de 1% ao mês em 12 meses equivale a cerca de {small} sobre o saldo, mais barata que um empréstimo a 2% ao mês na Tabela Price. Compare a taxa efetiva ou o total de juros, nunca só a taxa do anúncio."),
        ("Parcelado sem juros é taxa flat?",
         "Sem juros, o sistema de cálculo não importa. O custo real costuma estar no desconto à vista que você deixa de ganhar, ou em tarifas e seguros. Pergunte o preço à vista antes de decidir."),
        ("E se eu quitar o empréstimo antes do prazo?",
         "Pelo Código de Defesa do Consumidor (art. 52), quem antecipa o pagamento tem direito à redução proporcional dos juros. Mesmo assim, peça o valor de quitação por escrito e confira se os juros futuros foram mesmo descontados."),
        ("Financiamento imobiliário usa taxa flat?",
         "Não. O financiamento de imóveis no Brasil usa SAC ou Tabela Price, com juros sobre o saldo devedor, geralmente com correção pela TR ou pelo IPCA."),
    ],
    promo=("Pensando em pegar um empréstimo?", "O app Fincal ajuda você a comparar antes de assinar, mesmo sem internet:",
           [("Conversor de taxa flat", "veja a taxa efetiva de qualquer empréstimo parcelado"),
            ("Salvar e comparar", "coloque as opções lado a lado e escolha a mais barata"),
            ("Quitação antecipada", "com tarifas, veja quanto você economiza")]),
)

# ---------------------------------------------------------------- ms
A["ms"] = dict(
    path="/fincal/kadar-rata-vs-baki-berkurangan/", ct="web-fincal-article-flat-ms",
    title="Kadar Rata vs Baki Berkurangan: Cara Kira, Contoh dan Jadual EIR | Fincal",
    h1="Kadar rata vs baki berkurangan: apa bezanya, yang mana lebih mahal?",
    desc="Kadar rata 6% setahun sebenarnya hampir dua kali ganda kos 6% atas baki berkurangan. Lihat cara kiraannya, contoh pinjaman RM 10,000 dengan carta, dan jadual tukar kadar rata kepada kadar efektif (EIR).",
    crumb="Kadar rata vs baki berkurangan", byline="Nanoko Studio · Dikemas kini 20/11/2026", summary="Ringkasan",
    P=10_000, rate=6, small_rate=3, unit="y", conv=(4, 60), div=1,
    rates=[3, 5, 8], terms=[12, 36, 60, 84, 108],
    fmt=dict(sep=",", dc=False, cur="RM", pre=True, dec=2, intl="ms-MY"),
    names=dict(flat="Kadar rata", equal="Baki berkurangan", annuity="Ansuran sama"),
    sfx="% setahun", row="{y}%",
    tbl_group="Kadar efektif (EIR) setahun mengikut tempoh (bulan)",
    month_tick="Bulan {m}", month_tick_rest="{m}", month_tip="Bulan ke-{m}",
    ticks1=["0", "25", "50"], ticks2=["0", "5k", "10k"],
    tip_bal="Baki hutang", tip_base="Kadar rata dikira atas",
    ex_rows=["Ansuran bulan 1", "Ansuran bulan 12", "Jumlah faedah"], hbars_aria="Jumlah faedah mengikut kaedah",
    tldr="Sama-sama <b>6% setahun</b>, pinjam RM 10,000 selama 12 bulan:", tile_small="faedah",
    hero="Kadar rata 6% setahun sebenarnya", hero_small="jika dikira atas baki berkurangan",
    fig1=("Faedah setiap bulan", "Pinjaman RM 10,000, 6% setahun, 12 bulan. Sentuh bar untuk melihat jumlahnya.",
          "Kadar rata kekal <b>{flat_i12_s}</b> hingga bulan terakhir. Baki berkurangan tinggal <b>{eq_i12_s}</b> pada bulan ke-12.",
          "Faedah setiap bulan: kadar rata kekal sama, baki berkurangan turun setiap bulan"),
    fig2=("Faedah dikira atas jumlah mana?", "Bar menunjukkan baki hutang pada awal setiap bulan. Garis putus-putus ialah jumlah yang digunakan untuk mengira kadar rata.",
          "Baki hutang sebenar", "Kadar rata dikira atas RM 10,000",
          "Baki hutang turun setiap bulan, manakala kadar rata sentiasa dikira atas RM 10,000"),
    conv_t=dict(title="Penukar pantas", rate="Kadar rata", rate_unit="% setahun", term="Tempoh", term_unit="bulan",
                apr="Kadar efektif (EIR)", flat="Pinjam RM 10,000, faedah kadar rata", equal="Jika dikira atas baki berkurangan",
                more="Kira dengan jumlah anda →"),
    body="""
<h2>Apa itu kadar rata (flat rate)?</h2>
<p>Dengan kadar rata, faedah setiap bulan dikira atas <b>jumlah pinjaman asal</b>, walaupun anda sudah membayar sebahagian pokok.</p>
<div class="formula">Faedah sebulan = Jumlah pinjaman × Kadar setahun ÷ 12</div>
<p>Pinjam RM 10,000 pada kadar rata 6% setahun, faedahnya {flat_i} setiap bulan, termasuk bulan terakhir ketika baki hutang anda cuma sekitar {last_bal_s}. Kaedah ini biasa digunakan untuk pinjaman peribadi dan sewa beli kereta.</p>

<h2>Apa itu kadar baki berkurangan?</h2>
<p>Kadar baki berkurangan (reducing balance) hanya mengenakan faedah atas <b>baki yang masih terhutang</b>. Setiap kali pokok dibayar, faedah turut berkurang. Dua cara bayaran yang biasa ialah:</p>
<ul>
<li><b>Pokok sama</b>: pokok yang dibayar sama setiap bulan, jadi ansuran pertama paling tinggi lalu terus menurun.</li>
<li><b>Ansuran sama</b>: bayaran yang sama setiap bulan. Pada awalnya kebanyakannya faedah, kemudian kebanyakannya pokok. Inilah kaedah yang digunakan pinjaman perumahan.</li>
</ul>

{FIG1}

<h2>Contoh: RM 10,000 pada 6% setahun selama 12 bulan</h2>
{EXTABLE}
{HBARS}
<p>Pada bulan pertama, kadar rata dan baki berkurangan mengenakan faedah yang sama. Bezanya muncul selepas itu: dengan kadar rata, faedah tidak turun walaupun hutang sudah berkurang. <a href="{ex_link}">Buka contoh ini dalam kalkulator pinjaman →</a></p>

<h2>Kenapa kadar rata hampir dua kali ganda lebih mahal?</h2>
<p>Apabila anda membayar ansuran sepanjang tahun, secara purata anda hanya memegang kira-kira separuh daripada wang pinjaman. Kadar rata pula tetap mengenakan faedah atas RM 10,000 penuh sepanjang tahun.</p>
{FIG2}
<p>Oleh itu, sebelum membandingkan dengan pinjaman baki berkurangan, tukar dahulu kadar rata kepada <b>kadar faedah efektif (EIR)</b>: kadar baki berkurangan yang memberi ansuran bulanan yang sama. Bank di Malaysia biasanya menyatakan EIR bersebelahan kadar rata dalam iklan dan Helaian Pendedahan Produk.</p>

<h2>Jadual tukar kadar rata kepada kadar efektif</h2>
{APRTABLE}
<p>Cara anggar cepat: <b>kadar efektif lebih kurang {lo}-{hi} kali kadar rata</b>. Tiada formula mudah untuk angka tepat, jadi penukar di bawah yang mengiranya untuk anda.</p>

{CONV}

<h2>Cara kenal kadar rata dalam tawaran pinjaman</h2>
<ul>
<li>Kadar rata biasanya ditulis "flat rate", "kadar tetap setahun" atau hanya satu peratusan di sebelah ansuran bulanan yang tetap.</li>
<li>Baki berkurangan biasanya ditulis "reducing balance", "baki bulanan" atau "kadar efektif (EIR)".</li>
<li>Cara paling selamat ialah <b>minta jadual bayaran balik dan jumlah faedah</b>, atau EIR, kemudian masukkan ke dalam kalkulator.</li>
</ul>
""",
    faq=[
        ("Bilakah kadar rata lebih murah?",
         "Jika kadar rata kurang daripada kira-kira separuh kadar baki berkurangan yang ditawarkan. Contohnya kadar rata 3% setahun selama 12 bulan bersamaan kadar efektif sekitar {small}, masih lebih murah daripada pinjaman baki berkurangan 6% setahun. Bandingkan EIR atau jumlah faedah, bukan angka dalam iklan."),
        ("Adakah sewa beli kereta guna kadar rata?",
         "Ya, sewa beli kereta di Malaysia lazimnya dikira dengan kadar rata. Sebab itu kadar sekitar 3% setahun untuk tempoh panjang sebenarnya bersamaan kadar efektif yang hampir dua kali ganda. Masukkan kadar dan tempoh anda dalam penukar di atas."),
        ("Bagaimana jika saya selesaikan pinjaman lebih awal?",
         "Bergantung pada perjanjian. Ada yang hanya mengenakan faedah sehingga tarikh penyelesaian serta caj, ada yang memberi rebat faedah mengikut Rule 78 yang biasanya kurang menguntungkan peminjam. Tanya dahulu sebelum menandatangani."),
        ("Ansuran mudah 0% guna kadar rata?",
         "Jika faedahnya sifar, kaedah kiraan tidak penting. Kos sebenar biasanya pada yuran pemprosesan, insurans atau harga yang lebih tinggi daripada bayar tunai."),
    ],
    promo=("Sedang menimbang pinjaman?", "Aplikasi Fincal membantu anda membanding sebelum menandatangani, boleh guna tanpa internet:",
           [("Penukar kadar rata", "lihat kadar efektif bagi sebarang pinjaman ansuran"),
            ("Simpan dan banding", "letak beberapa pilihan bersebelahan dan pilih yang paling murah"),
            ("Bayar balik awal", "termasuk caj, lihat berapa yang dapat dijimatkan")]),
)
