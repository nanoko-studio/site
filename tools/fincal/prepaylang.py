"""Content for the prepayment article, one dict per language.
Example: balance B, yearly rate R, n months left, method, prepay X with fee F%.
Body placeholders are filled from the computed example (see prepaypage.py)."""

A = {}

A["vi"] = dict(
    path="/fincal/tra-no-truoc-han/", ct="web-fincal-article-prepay-vi",
    title="Trả nợ trước hạn: có nên không, giảm kỳ hạn hay giảm tiền trả? | Fincal",
    h1="Trả nợ trước hạn: có nên không, và nên giảm kỳ hạn hay giảm tiền trả?",
    desc="Trả trước 200 triệu cho khoản vay 800 triệu tiết kiệm được bao nhiêu tiền lãi, phí phạt 2% có đáng không, và chọn giảm kỳ hạn hay giảm tiền trả hằng tháng. Có biểu đồ, bảng và máy tính.",
    crumb="Trả nợ trước hạn", byline="Nanoko Studio · Cập nhật 21/11/2026", summary="Tóm tắt",
    B=800_000_000, R=10, n=180, method="equal", X=200_000_000, F=2,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=True, cur="đ", pre=False, dec=0, intl="vi-VN", scale=1), div=1, sfx="%/năm",
    names=dict(base="Không trả trước", shorter="Giảm kỳ hạn", lower="Giảm tiền trả"),
    methods=dict(equal="Gốc đều (dư nợ giảm dần)", annuity="Trả góp đều hằng tháng"),
    m1="{n} tháng", mn="{n} tháng",
    ticks=["0", "400tr", "800tr"], year0="Nay", year_tick="{y} năm", year_tip="Sau {y} năm", year_tip0="Ngay sau khi trả trước",
    tldr="Còn nợ <b>800 triệu</b>, lãi 10%/năm, còn 15 năm. Trả trước <b>200 triệu</b>, phí 2%:",
    tile_shorter="tiền lãi tiết kiệm được, hết nợ sớm {cut}", tile_lower="tiền lãi tiết kiệm được, mỗi tháng trả ít hơn {drop}",
    hero="Sau phí, 200 triệu trả trước sinh lợi", hero_small="gần bằng lãi vay 10%/năm",
    ex_rows=["Trả tháng tới", "Hết nợ sau", "Tổng lãi còn phải trả", "Tiền lãi tiết kiệm được", "Sau khi trừ phí {fee}"],
    fig=("Dư nợ còn lại theo thời gian", "Chạm vào biểu đồ để xem số dư từng năm.",
         "Dư nợ còn lại của ba phương án: không trả trước, giảm kỳ hạn và giảm tiền trả"),
    tbl_head="Phí trả trước", tbl_group="Lợi suất sau phí (%/năm) theo thời gian vay còn lại", tbl_year="{y} năm",
    calc=dict(title="Tính cho khoản vay của bạn", bal="Dư nợ hiện tại", rate="Lãi suất", rate_unit="%/năm",
              term="Thời gian còn lại", term_unit="tháng", method="Cách trả", extra="Số tiền trả trước",
              fee="Phí trả trước", fee_unit="% số tiền trả", fee_line="Phí phạt phải trả:",
              rows=["Tiền lãi tiết kiệm được", "Sau khi trừ phí", "Kết quả", "Lợi suất sau phí"],
              cut="Hết nợ sớm {m}", newpay="Tháng tới trả {v}", paidoff="Tất toán ngay",
              more="Xem lịch trả nợ mới →"),
    body="""
<p>Có một khoản tiền thưởng, tiền bán đất hay tiền tiết kiệm đến hạn, nhiều người nghĩ ngay tới chuyện trả bớt nợ ngân hàng. Trước khi làm, có hai câu hỏi cần trả lời: <b>phí phạt có ăn hết phần lợi không</b>, và khi ngân hàng hỏi <b>giảm kỳ hạn hay giảm số tiền trả hằng tháng</b> thì chọn gì.</p>

<h2>Ví dụ: còn nợ 800 triệu, còn 15 năm</h2>
<p>Khoản vay mua nhà theo kiểu gốc đều, lãi 10%/năm, còn 180 tháng. Bạn trả trước 200 triệu và chịu phí 2%, tức {fee}. Sau đó ngân hàng cho chọn một trong hai cách:</p>
<ul>
<li><b>Giảm kỳ hạn</b>: giữ nguyên khoản gốc {keep} mỗi tháng như cũ, nên hết nợ sớm hơn.</li>
<li><b>Giảm tiền trả</b>: giữ nguyên 15 năm, chia lại 600 triệu còn lại cho 180 tháng, nên mỗi tháng trả ít hơn.</li>
</ul>
{EXTABLE}
{HBARS}
<p>Dù chọn cách nào, phí 2% vẫn nhỏ so với tiền lãi tiết kiệm được. <a href="{ex_link}">Xem lịch trả nợ khi chưa trả trước →</a></p>

{FIG}

<h2>Giảm kỳ hạn tiết kiệm nhiều hơn, nhưng chưa chắc lợi hơn</h2>
<p>Nhìn bảng trên, giảm kỳ hạn tiết kiệm được {s_saved}, gần gấp đôi con số {l_saved} của giảm tiền trả. Lý do không phải vì cách này khôn hơn. Khi giảm kỳ hạn, bạn tiếp tục trả gốc nhiều mỗi tháng như cũ, tức là <b>đưa thêm tiền vào trả nợ</b> trong suốt những năm sau. Tiền trả nợ nhiều hơn thì đương nhiên lãi ít hơn.</p>
<p>Thước đo công bằng hơn là <b>lợi suất</b>: mỗi đồng trả trước giúp bạn tránh được bao nhiêu phần trăm lãi một năm. Không có phí thì cả hai cách đều cho đúng bằng lãi suất khoản vay, 10%/năm. Có phí 2% thì giảm kỳ hạn cho {s_yield}, giảm tiền trả cho {l_yield}, gần như nhau.</p>
<p>Vì vậy hãy chọn theo dòng tiền của bạn:</p>
<ul>
<li>Thu nhập ổn định, muốn sớm hết nợ: <b>giảm kỳ hạn</b>.</li>
<li>Muốn mỗi tháng nhẹ gánh hơn, phòng khi thu nhập giảm: <b>giảm tiền trả</b>. Phần tiền dư mỗi tháng, nếu sau này bạn lại dùng để trả trước, thì kết quả gần giống giảm kỳ hạn.</li>
</ul>

<h2>Phí phạt bao nhiêu thì không còn đáng?</h2>
<p>Trả trước giống như gửi tiền vào một khoản tiết kiệm có lãi bằng lãi vay của bạn, không rủi ro. Phí phạt trả một lần ngay lúc đầu, nên thời gian vay còn càng dài thì phí chia ra mỗi năm càng nhỏ. Bảng dưới là lợi suất sau phí của khoản vay lãi 10%/năm, theo cách giảm tiền trả:</p>
{YTABLE}
<p>Còn từ 5 năm trở lên, phí 1-3% chỉ kéo lợi suất xuống còn {y5_lo}-{y5_hi}. Còn 1 năm thì khác hẳn: phí 3% làm lợi suất chỉ còn {y1_lo}, có khi thấp hơn lãi gửi tiết kiệm. Nếu sắp qua mốc phí giảm hoặc hết phí trong hợp đồng, chờ vài tháng có thể đáng hơn.</p>
<p>So lợi suất này với số tiền bạn có thể kiếm được nếu giữ lại khoản tiền đó, ví dụ lãi gửi tiết kiệm. Lợi suất trả trước cao hơn thì trả trước có lợi. Với khoản vay lãi thả nổi, lợi suất thực tế đi theo lãi suất những năm tới, nên lãi càng tăng thì trả trước càng có lợi.</p>

{CALC}

<h2>Hỏi ngân hàng những gì trước khi trả</h2>
<ul>
<li><b>Phí tính trên số tiền nào</b>: số tiền trả trước hay toàn bộ dư nợ, và mức phí theo từng năm vay.</li>
<li><b>Có được chọn</b> giảm kỳ hạn hay giảm tiền trả không, hay ngân hàng áp dụng sẵn một cách.</li>
<li><b>Số tiền trả trước tối thiểu</b> và có giới hạn số lần trả trước trong năm không.</li>
<li>Xin <b>lịch trả nợ mới</b> sau khi trả trước, rồi đối chiếu với máy tính ở trên.</li>
</ul>
<p>Đừng dùng hết tiền dự phòng để trả nợ. Tiền đã trả vào khoản vay rất khó lấy lại khi cần gấp, nên hãy giữ lại ít nhất vài tháng chi tiêu.</p>
""",
    faq=[
        ("Phí trả nợ trước hạn thường là bao nhiêu?",
         "Thường khoảng 1-3% số tiền trả trước, giảm dần theo số năm đã vay, và nhiều hợp đồng miễn phí sau vài năm. Mỗi ngân hàng và mỗi gói vay một khác, hãy đọc mục phí trả nợ trước hạn trong hợp đồng."),
        ("Nên trả nợ trước hạn hay gửi tiết kiệm?",
         "So lợi suất sau phí của việc trả trước với lãi gửi tiết kiệm bạn nhận được. Nếu trả trước cho lợi suất cao hơn thì trả nợ có lợi hơn, với điều kiện bạn vẫn giữ đủ tiền dự phòng."),
        ("Đang trong thời gian lãi ưu đãi có nên trả trước không?",
         "Trong thời gian ưu đãi, mỗi đồng trả trước chỉ tránh được mức lãi thấp, nhưng sau đó nó tránh được mức lãi thả nổi. Với khoản vay còn dài, phần lớn lợi ích nằm ở giai đoạn thả nổi. Nếu phí phạt sẽ giảm sau ưu đãi, nhiều người chọn chờ đến mốc đó rồi mới trả."),
        ("Giảm kỳ hạn hay giảm tiền trả, cách nào lợi hơn?",
         "Lợi suất của hai cách gần như bằng nhau. Giảm kỳ hạn tiết kiệm nhiều tiền lãi hơn vì bạn tiếp tục trả nhiều tiền hơn mỗi tháng. Chọn giảm tiền trả nếu bạn muốn dòng tiền hằng tháng dễ thở hơn."),
    ],
    promo=("Lên kế hoạch trả nợ sớm?", "App Fincal tính sẵn mọi phương án trả trước, dùng được cả khi không có mạng:",
           [("Trả trước nhiều lần", "một lần hoặc định kỳ, có phí phạt, xem tiết kiệm được bao nhiêu"),
            ("Lãi suất thay đổi", "lãi ưu đãi rồi thả nổi, thêm bao nhiêu giai đoạn cũng được"),
            ("Lưu và so sánh", "đặt các phương án cạnh nhau để chọn cách hợp nhất")]),
)

# ---------------------------------------------------------------- en
A["en"] = dict(
    path="/fincal/paying-off-a-loan-early/", ct="web-fincal-article-prepay",
    title="Paying Off a Loan Early: Shorter Term or Lower Payment, and Is the Fee Worth It? | Fincal",
    h1="Paying off a loan early: shorter term or lower payment, and is the fee worth it?",
    desc="How much interest does a 20,000 overpayment on a 200,000 mortgage save, is a 2% early repayment charge worth paying, and should you shorten the term or lower the payment? With a chart, tables and a calculator.",
    crumb="Paying off a loan early", byline="Nanoko Studio · Updated 21 Nov 2026", summary="Summary",
    B=200_000, R=6, n=240, method="annuity", X=20_000, F=2,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=False, cur="", pre=False, dec=0, intl="en-US", scale=1), div=1, sfx="% a year",
    names=dict(base="No overpayment", shorter="Shorter term", lower="Lower payment"),
    methods=dict(annuity="Equal monthly payments", equal="Equal principal"),
    m1="{n} month", mn="{n} months",
    ticks=["0", "100K", "200K"], year0="Now", year_tick="Year {y}", year_tip="After {y} years", year_tip0="Right after the overpayment",
    tldr="You owe <b>200,000</b> at 6% a year with 20 years to go. You pay off <b>20,000</b> early with a 2% fee:",
    tile_shorter="interest saved, debt-free {cut} sooner", tile_lower="interest saved, {drop} less every month",
    hero="After the fee, the 20,000 earns", hero_small="close to the 6% loan rate",
    ex_rows=["Next payment", "Paid off in", "Interest still to pay", "Interest saved", "After the {fee} fee"],
    fig=("What you still owe over time", "Tap the chart to see the balance year by year.",
         "Balance owed under three options: no overpayment, shorter term and lower payment"),
    tbl_head="Early repayment fee", tbl_group="Return after the fee (% a year), by years left on the loan", tbl_year="{y} yrs",
    calc=dict(title="Try it with your loan", bal="Balance owed", rate="Interest rate", rate_unit="% a year",
              term="Time left", term_unit="months", method="Repayment type", extra="Amount to pay early",
              fee="Early repayment fee", fee_unit="% of amount", fee_line="Fee to pay:",
              rows=["Interest saved", "After the fee", "Result", "Return after the fee"],
              cut="Paid off {m} sooner", newpay="Next payment {v}", paidoff="Paid off in full",
              more="See the new repayment schedule →"),
    body="""
<p>A bonus, an inheritance or a savings account that has just matured: putting it towards the mortgage is a natural thought. Before you do, two questions are worth answering: <b>does the early repayment fee eat the benefit</b>, and when the lender asks whether you want a <b>shorter term or a lower monthly payment</b>, which should you pick?</p>

<h2>Example: 200,000 owed with 20 years left</h2>
<p>A mortgage with equal monthly payments of {basepay}, at 6% a year, with 240 months left. You pay 20,000 early and the lender charges 2% on it, which is {fee}. Then you choose one of two options:</p>
<ul>
<li><b>Shorter term</b>: keep paying {keep} a month as before, so the loan ends sooner.</li>
<li><b>Lower payment</b>: keep the 20 years and spread the remaining 180,000 over 240 months, so each payment drops to {newpay}.</li>
</ul>
{EXTABLE}
{HBARS}
<p>Either way, the 2% fee is small next to the interest you save. <a href="{ex_link}">See the repayment schedule without the overpayment →</a></p>

{FIG}

<h2>A shorter term saves more, but is not necessarily better</h2>
<p>The table shows the shorter term saving {s_saved}, well over twice the {l_saved} saved by lowering the payment. That is not because it is the smarter option. With a shorter term you keep paying the full amount every month, so you <b>put more money into the loan</b> over the following years. More money into the loan means less interest, of course.</p>
<p>A fairer measure is the <b>return</b>: the yearly percentage of interest that the money paid early lets you avoid. Without a fee, both options return exactly the loan rate, 6% a year. With a 2% fee, the shorter term returns {s_yield} and the lower payment {l_yield}, almost the same.</p>
<p>So choose based on your cash flow:</p>
<ul>
<li>Steady income and you want to be debt-free sooner: <b>shorter term</b>.</li>
<li>You want breathing room each month in case income drops: <b>lower payment</b>. If you later put the monthly difference towards the loan, you end up close to the shorter-term result anyway.</li>
</ul>

<h2>How big a fee is too big?</h2>
<p>Paying early is like putting money into a risk-free savings account that pays your loan rate. The fee is paid once, up front, so the longer the loan still has to run, the smaller the fee is per year. The table below shows the return after the fee on a 6% loan, using the lower-payment option:</p>
{YTABLE}
<p>With 5 years or more left, a 1-3% fee only pulls the return down to {y5_lo}-{y5_hi}. With 1 year left it is a different story: a 3% fee leaves just {y1_lo}, often less than a savings account pays. If the fee drops or ends soon under your contract, waiting a few months can pay off.</p>
<p>Compare this return with what the money could earn if you kept it, for example in savings. If paying early returns more, it is the better use. On a variable-rate loan the real return follows the rate in the years ahead, so the higher rates go, the more paying early is worth.</p>

{CALC}

<h2>What to ask your lender first</h2>
<ul>
<li><b>How the fee works</b>: a percentage of the amount paid early or of the whole balance, and how it changes over the years.</li>
<li><b>Free allowance</b>: many lenders let you pay a set amount each year, often around 10% of the balance, without any fee.</li>
<li><b>Whether you can choose</b> a shorter term or a lower payment, or the lender applies one by default.</li>
<li>Ask for the <b>new repayment schedule</b> afterwards and check it against the calculator above.</li>
</ul>
<p>Do not use your whole emergency fund. Money paid into a loan is hard to get back when you need it, so keep at least a few months of expenses aside.</p>
""",
    faq=[
        ("How much is a typical early repayment fee?",
         "Often around 1-3% of the amount paid early, falling as the loan gets older, and many loans charge nothing after a few years or below a yearly allowance. It differs by lender and product, so check the early repayment section of your contract."),
        ("Should I pay off my loan early or save the money?",
         "Compare the return after the fee with the interest your savings would earn. If paying early returns more, it is the better choice, as long as you still keep enough for emergencies."),
        ("Is it worth paying early during a fixed-rate deal?",
         "During the deal, money paid early avoids the fixed rate, and afterwards it avoids whatever rate follows. Fees are usually highest during the fixed period, so many people wait until it ends, or stay within the free allowance."),
        ("Shorter term or lower payment: which is better?",
         "The return is almost the same. A shorter term saves more interest because you keep paying more each month. Choose a lower payment if you want an easier monthly budget."),
    ],
    promo=("Planning to pay off early?", "The Fincal app works out every overpayment option for you, even offline:",
           [("Multiple overpayments", "one-off or regular, with fees, and see what you save"),
            ("Changing rates", "an intro rate and then a variable one, as many periods as you need"),
            ("Save and compare", "put your options side by side and pick the best")]),
)

# ---------------------------------------------------------------- id
A["id"] = dict(
    path="/fincal/pelunasan-dipercepat/", ct="web-fincal-article-prepay-id",
    title="Pelunasan Sebagian KPR: Kurangi Tenor atau Cicilan, dan Apakah Penaltinya Sepadan? | Fincal",
    h1="Pelunasan sebagian KPR: pilih kurangi tenor atau cicilan, dan apakah penaltinya sepadan?",
    desc="Berapa bunga yang dihemat jika melunasi Rp 100 juta dari KPR Rp 500 juta, apakah penalti 2% sepadan, dan lebih baik mengurangi tenor atau cicilan. Lengkap dengan grafik, tabel dan kalkulator.",
    crumb="Pelunasan dipercepat", byline="Nanoko Studio · Diperbarui 21/11/2026", summary="Ringkasan",
    B=500_000_000, R=11, n=180, method="annuity", X=100_000_000, F=2,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=True, cur="Rp", pre=True, dec=0, intl="id-ID", scale=1), div=1, sfx="% per tahun",
    names=dict(base="Tanpa pelunasan", shorter="Kurangi tenor", lower="Kurangi cicilan"),
    methods=dict(annuity="Anuitas (cicilan tetap)", equal="Pokok tetap (bunga efektif)"),
    m1="{n} bulan", mn="{n} bulan",
    ticks=["0", "250 jt", "500 jt"], year0="Kini", year_tick="Thn {y}", year_tip="Setelah {y} tahun", year_tip0="Tepat setelah pelunasan",
    tldr="Sisa KPR <b>Rp 500 juta</b>, bunga 11% per tahun, tenor tinggal 15 tahun. Anda melunasi <b>Rp 100 juta</b> dengan penalti 2%:",
    tile_shorter="bunga yang dihemat, lunas {cut} lebih cepat", tile_lower="bunga yang dihemat, cicilan turun {drop} per bulan",
    hero="Setelah penalti, Rp 100 juta itu menghasilkan", hero_small="hampir sama dengan bunga KPR 11%",
    ex_rows=["Cicilan bulan depan", "Lunas dalam", "Sisa bunga yang dibayar", "Bunga yang dihemat", "Setelah penalti {fee}"],
    fig=("Sisa pokok dari waktu ke waktu", "Ketuk grafik untuk melihat sisa pokok tiap tahun.",
         "Sisa pokok untuk tiga pilihan: tanpa pelunasan, kurangi tenor dan kurangi cicilan"),
    tbl_head="Penalti", tbl_group="Imbal hasil setelah penalti (% per tahun) menurut sisa tenor", tbl_year="{y} thn",
    calc=dict(title="Hitung untuk pinjaman Anda", bal="Sisa pokok", rate="Suku bunga", rate_unit="% per tahun",
              term="Sisa tenor", term_unit="bulan", method="Jenis cicilan", extra="Jumlah pelunasan",
              fee="Penalti", fee_unit="% dari jumlah", fee_line="Penalti yang dibayar:",
              rows=["Bunga yang dihemat", "Setelah penalti", "Hasil", "Imbal hasil setelah penalti"],
              cut="Lunas {m} lebih cepat", newpay="Cicilan berikutnya {v}", paidoff="Lunas seluruhnya",
              more="Lihat jadwal angsuran baru →"),
    body="""
<p>Dapat bonus, THR atau deposito yang jatuh tempo, banyak orang langsung terpikir untuk melunasi sebagian KPR. Sebelum ke bank, ada dua hal yang perlu dijawab: <b>apakah penaltinya menghabiskan keuntungan</b>, dan saat bank bertanya mau <b>kurangi tenor atau kurangi cicilan</b>, mana yang dipilih.</p>

<h2>Contoh: sisa KPR Rp 500 juta, tenor tinggal 15 tahun</h2>
<p>KPR anuitas dengan cicilan {basepay} per bulan, bunga 11% per tahun (sudah floating), sisa 180 bulan. Anda melunasi Rp 100 juta dan kena penalti 2%, yaitu {fee}. Setelah itu bank menawarkan dua pilihan:</p>
<ul>
<li><b>Kurangi tenor</b>: cicilan tetap {keep} per bulan seperti sebelumnya, jadi pinjaman lunas lebih cepat.</li>
<li><b>Kurangi cicilan</b>: tenor tetap 15 tahun, sisa Rp 400 juta dibagi ulang ke 180 bulan, jadi cicilan turun menjadi {newpay}.</li>
</ul>
{EXTABLE}
{HBARS}
<p>Pilihan mana pun, penalti 2% tetap kecil dibandingkan bunga yang dihemat. <a href="{ex_link}">Lihat jadwal angsuran tanpa pelunasan →</a></p>

{FIG}

<h2>Kurangi tenor menghemat lebih banyak, tapi belum tentu lebih untung</h2>
<p>Di tabel, kurangi tenor menghemat {s_saved}, lebih dari dua kali lipat {l_saved} dari kurangi cicilan. Alasannya bukan karena cara ini lebih pintar. Dengan kurangi tenor, Anda tetap membayar cicilan besar setiap bulan, artinya <b>menyetor lebih banyak uang ke pinjaman</b> selama tahun-tahun berikutnya. Makin banyak uang yang disetor, tentu makin sedikit bunganya.</p>
<p>Ukuran yang lebih adil adalah <b>imbal hasil</b>: setiap rupiah yang dilunasi lebih awal menghindarkan Anda dari bunga berapa persen per tahun. Tanpa penalti, kedua pilihan memberi tepat sebesar bunga pinjaman, 11% per tahun. Dengan penalti 2%, kurangi tenor memberi {s_yield} dan kurangi cicilan {l_yield}, hampir sama.</p>
<p>Jadi pilihlah sesuai arus kas Anda:</p>
<ul>
<li>Penghasilan stabil dan ingin cepat bebas utang: <b>kurangi tenor</b>.</li>
<li>Ingin cicilan bulanan lebih ringan, berjaga-jaga jika penghasilan turun: <b>kurangi cicilan</b>. Jika selisih cicilan itu nanti dipakai untuk melunasi lagi, hasilnya hampir sama dengan kurangi tenor.</li>
</ul>

<h2>Berapa penalti yang masih sepadan?</h2>
<p>Melunasi lebih awal mirip menaruh uang di tabungan bebas risiko dengan bunga sebesar bunga pinjaman Anda. Penalti dibayar sekali di awal, jadi makin panjang sisa tenor, makin kecil penalti itu jika dibagi per tahun. Tabel di bawah adalah imbal hasil setelah penalti untuk pinjaman berbunga 11% per tahun, dengan pilihan kurangi cicilan:</p>
{YTABLE}
<p>Jika sisa tenor 5 tahun atau lebih, penalti 1-3% hanya menurunkan imbal hasil menjadi {y5_lo}-{y5_hi}. Jika tinggal 1 tahun, ceritanya lain: penalti 3% membuat imbal hasil tinggal {y1_lo}, bisa lebih rendah dari bunga deposito. Jika sebentar lagi masa penalti berakhir sesuai perjanjian kredit, menunggu beberapa bulan bisa lebih menguntungkan.</p>
<p>Bandingkan imbal hasil ini dengan hasil yang bisa Anda dapat jika uangnya disimpan, misalnya bunga deposito setelah pajak. Jika melunasi memberi imbal hasil lebih tinggi, melunasi lebih untung. Pada bunga floating, imbal hasil sebenarnya mengikuti suku bunga tahun-tahun mendatang, jadi makin naik bunganya, makin untung melunasi lebih awal.</p>

{CALC}

<h2>Yang perlu ditanyakan ke bank sebelum melunasi</h2>
<ul>
<li><b>Dasar penalti</b>: dihitung dari jumlah yang dilunasi atau dari seluruh sisa pokok, dan besarnya pada masa fixed maupun floating.</li>
<li><b>Boleh memilih</b> kurangi tenor atau kurangi cicilan, atau bank sudah menetapkan salah satunya.</li>
<li><b>Jumlah minimal</b> pelunasan sebagian dan berapa kali boleh dilakukan dalam setahun.</li>
<li>Minta <b>jadwal angsuran baru</b> setelah pelunasan, lalu cocokkan dengan kalkulator di atas.</li>
</ul>
<p>Jangan pakai seluruh dana darurat untuk melunasi. Uang yang sudah masuk ke pinjaman sulit diambil kembali saat butuh mendadak, jadi sisakan setidaknya biaya hidup beberapa bulan.</p>
""",
    faq=[
        ("Berapa biasanya penalti pelunasan dipercepat KPR?",
         "Umumnya sekitar 1-3% dari jumlah yang dilunasi, sering lebih tinggi selama masa bunga fixed dan lebih rendah atau gratis setelahnya. Tiap bank dan produk berbeda, jadi baca bagian pelunasan dipercepat di perjanjian kredit Anda."),
        ("Lebih baik melunasi KPR atau menabung di deposito?",
         "Bandingkan imbal hasil setelah penalti dengan bunga deposito setelah pajak yang Anda terima. Jika melunasi memberi imbal hasil lebih tinggi, melunasi lebih untung, asalkan dana darurat tetap cukup."),
        ("Apakah sebaiknya melunasi saat masih masa bunga fixed?",
         "Selama masa fixed, setiap rupiah yang dilunasi hanya menghindari bunga promo yang rendah, tetapi setelah itu ia menghindari bunga floating. Karena penalti biasanya lebih besar di masa fixed, banyak orang menunggu sampai masa fixed berakhir."),
        ("Kurangi tenor atau kurangi cicilan, mana yang lebih untung?",
         "Imbal hasil keduanya hampir sama. Kurangi tenor menghemat lebih banyak bunga karena Anda tetap membayar lebih besar setiap bulan. Pilih kurangi cicilan jika ingin arus kas bulanan lebih longgar."),
    ],
    promo=("Merencanakan pelunasan lebih cepat?", "Aplikasi Fincal menghitung semua skenario pelunasan, bisa dipakai tanpa internet:",
           [("Pelunasan berkali-kali", "sekali atau rutin, dengan penalti, lihat berapa yang dihemat"),
            ("Bunga berubah", "bunga fixed lalu floating, berapa pun periodenya"),
            ("Simpan dan bandingkan", "jejerkan beberapa skenario untuk memilih yang paling pas")]),
)

# ---------------------------------------------------------------- th
A["th"] = dict(
    path="/fincal/poppit-ni-kon-kamnot/", ct="web-fincal-article-prepay-th",
    title="โปะบ้าน ลดงวดหรือลดค่างวด และค่าธรรมเนียมคุ้มไหม | Fincal",
    h1="โปะหนี้บ้าน: เลือกลดระยะเวลาหรือลดค่างวด และค่าธรรมเนียมคุ้มไหม",
    desc="โปะ 300,000 บาทจากหนี้บ้าน 2 ล้านบาทประหยัดดอกเบี้ยได้เท่าไร ค่าธรรมเนียม 3% คุ้มไหม และควรลดระยะเวลาหรือลดค่างวด พร้อมกราฟ ตาราง และเครื่องคำนวณ",
    crumb="โปะหนี้ก่อนกำหนด", byline="Nanoko Studio · อัปเดต 21 พ.ย. 2026", summary="สรุป",
    B=2_000_000, R=6, n=240, method="annuity", X=300_000, F=3,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=False, cur="บาท", pre=False, dec=0, intl="th-TH", scale=1), div=1, sfx="% ต่อปี",
    names=dict(base="ไม่โปะ", shorter="ลดระยะเวลา", lower="ลดค่างวด"),
    methods=dict(annuity="ผ่อนงวดเท่ากัน", equal="เงินต้นเท่ากันทุกงวด"),
    m1="{n} เดือน", mn="{n} เดือน",
    ticks=["0", "1 ล้าน", "2 ล้าน"], year0="วันนี้", year_tick="ปี {y}", year_tip="ผ่านไป {y} ปี", year_tip0="ทันทีหลังโปะ",
    tldr="หนี้บ้านคงเหลือ <b>2 ล้านบาท</b> ดอกเบี้ย 6% ต่อปี เหลือ 20 ปี โปะ <b>300,000 บาท</b> โดยเสียค่าธรรมเนียม 3%:",
    tile_shorter="ดอกเบี้ยที่ประหยัดได้ หมดหนี้เร็วขึ้น {cut}", tile_lower="ดอกเบี้ยที่ประหยัดได้ ค่างวดลดลงเดือนละ {drop}",
    hero="หลังหักค่าธรรมเนียม เงินที่โปะให้ผลตอบแทน", hero_small="ใกล้เคียงดอกเบี้ยเงินกู้ 6% ต่อปี",
    ex_rows=["ค่างวดเดือนหน้า", "หมดหนี้ใน", "ดอกเบี้ยที่ยังต้องจ่าย", "ดอกเบี้ยที่ประหยัดได้", "หลังหักค่าธรรมเนียม {fee}"],
    fig=("หนี้คงเหลือตามเวลา", "แตะกราฟเพื่อดูยอดหนี้แต่ละปี",
         "หนี้คงเหลือของสามทางเลือก: ไม่โปะ ลดระยะเวลา และลดค่างวด"),
    tbl_head="ค่าธรรมเนียม", tbl_group="ผลตอบแทนหลังหักค่าธรรมเนียม (% ต่อปี) ตามระยะเวลากู้ที่เหลือ", tbl_year="{y} ปี",
    calc=dict(title="คำนวณสำหรับเงินกู้ของคุณ", bal="หนี้คงเหลือ", rate="อัตราดอกเบี้ย", rate_unit="% ต่อปี",
              term="ระยะเวลาที่เหลือ", term_unit="เดือน", method="วิธีผ่อน", extra="จำนวนเงินที่โปะ",
              fee="ค่าธรรมเนียม", fee_unit="% ของเงินที่โปะ", fee_line="ค่าธรรมเนียมที่ต้องจ่าย:",
              rows=["ดอกเบี้ยที่ประหยัดได้", "หลังหักค่าธรรมเนียม", "ผลลัพธ์", "ผลตอบแทนหลังหักค่าธรรมเนียม"],
              cut="หมดหนี้เร็วขึ้น {m}", newpay="ค่างวดเดือนหน้า {v}", paidoff="ปิดหนี้ทันที",
              more="ดูตารางผ่อนชำระใหม่ →"),
    body="""
<p>ได้โบนัส ขายที่ดิน หรือเงินฝากครบกำหนด หลายคนคิดถึงการโปะหนี้บ้านเป็นอย่างแรก ก่อนตัดสินใจมีสองคำถามที่ควรตอบ: <b>ค่าธรรมเนียมจะกินกำไรไปหมดหรือเปล่า</b> และเมื่อธนาคารถามว่าจะ <b>ลดระยะเวลาหรือลดค่างวด</b> ควรเลือกแบบไหน</p>

<h2>ตัวอย่าง: หนี้บ้านเหลือ 2 ล้านบาท อีก 20 ปี</h2>
<p>สินเชื่อบ้านแบบผ่อนงวดเท่ากัน ค่างวด {basepay} ต่อเดือน ดอกเบี้ย 6% ต่อปี เหลือ 240 เดือน คุณโปะ 300,000 บาท และสมมติว่าสัญญาเก็บค่าธรรมเนียม 3% คือ {fee} จากนั้นเลือกได้สองแบบ:</p>
<ul>
<li><b>ลดระยะเวลา</b>: ผ่อนเท่าเดิม {keep} ต่อเดือน หนี้จึงหมดเร็วขึ้น</li>
<li><b>ลดค่างวด</b>: คงระยะเวลา 20 ปีไว้ แล้วกระจายหนี้ที่เหลือ 1.7 ล้านบาทใหม่ใน 240 เดือน ค่างวดจึงลดเหลือ {newpay}</li>
</ul>
{EXTABLE}
{HBARS}
<p>ไม่ว่าเลือกแบบไหน ค่าธรรมเนียม 3% ก็ยังน้อยกว่าดอกเบี้ยที่ประหยัดได้มาก <a href="{ex_link}">ดูตารางผ่อนชำระเมื่อไม่โปะ →</a></p>

{FIG}

<h2>ลดระยะเวลาประหยัดได้มากกว่า แต่ไม่ได้แปลว่าคุ้มกว่า</h2>
<p>จากตาราง ลดระยะเวลาประหยัดได้ {s_saved} มากกว่าสองเท่าของ {l_saved} ที่ได้จากการลดค่างวด เหตุผลไม่ใช่เพราะวิธีนี้ฉลาดกว่า เมื่อลดระยะเวลา คุณยังผ่อนเท่าเดิมทุกเดือน แปลว่า <b>ใส่เงินเข้าไปจ่ายหนี้มากขึ้น</b> ตลอดหลายปีต่อจากนั้น จ่ายหนี้มากขึ้น ดอกเบี้ยก็ย่อมน้อยลง</p>
<p>ตัวชี้วัดที่ยุติธรรมกว่าคือ <b>ผลตอบแทน</b>: เงินทุกบาทที่โปะช่วยเลี่ยงดอกเบี้ยได้กี่เปอร์เซ็นต์ต่อปี ถ้าไม่มีค่าธรรมเนียม ทั้งสองแบบให้ผลตอบแทนเท่ากับดอกเบี้ยเงินกู้พอดี คือ 6% ต่อปี เมื่อมีค่าธรรมเนียม 3% ลดระยะเวลาให้ {s_yield} ส่วนลดค่างวดให้ {l_yield} แทบไม่ต่างกัน</p>
<p>จึงควรเลือกตามกระแสเงินสดของคุณ:</p>
<ul>
<li>รายได้มั่นคง อยากหมดหนี้เร็ว: <b>ลดระยะเวลา</b></li>
<li>อยากให้แต่ละเดือนเบาลง เผื่อรายได้ลด: <b>ลดค่างวด</b> ถ้าภายหลังนำส่วนต่างค่างวดไปโปะต่อ ผลลัพธ์ก็จะใกล้เคียงการลดระยะเวลา</li>
</ul>

<h2>ค่าธรรมเนียมเท่าไรถึงไม่คุ้ม</h2>
<p>การโปะหนี้เหมือนการฝากเงินในบัญชีที่ไม่มีความเสี่ยงและได้ดอกเบี้ยเท่ากับดอกเบี้ยเงินกู้ ค่าธรรมเนียมจ่ายครั้งเดียวตอนต้น ยิ่งเหลือเวลากู้นาน ค่าธรรมเนียมเมื่อเฉลี่ยต่อปีก็ยิ่งน้อย ตารางด้านล่างคือผลตอบแทนหลังหักค่าธรรมเนียมของเงินกู้ดอกเบี้ย 6% ต่อปี แบบลดค่างวด:</p>
{YTABLE}
<p>ถ้าเหลือเวลากู้ตั้งแต่ 5 ปีขึ้นไป ค่าธรรมเนียม 1-3% ทำให้ผลตอบแทนลดลงเหลือ {y5_lo}-{y5_hi} เท่านั้น แต่ถ้าเหลือ 1 ปี ค่าธรรมเนียม 3% ทำให้ผลตอบแทนเหลือแค่ {y1_lo} อาจต่ำกว่าดอกเบี้ยเงินฝาก ถ้าอีกไม่นานจะพ้นช่วงที่เก็บค่าธรรมเนียมตามสัญญา รอสักไม่กี่เดือนอาจคุ้มกว่า</p>
<p>เทียบผลตอบแทนนี้กับสิ่งที่เงินก้อนนั้นจะทำได้ถ้าเก็บไว้ เช่น ดอกเบี้ยเงินฝาก ถ้าการโปะให้ผลตอบแทนสูงกว่า การโปะก็คุ้มกว่า สำหรับเงินกู้ดอกเบี้ยลอยตัว ผลตอบแทนจริงขึ้นกับดอกเบี้ยในปีต่อ ๆ ไป ดอกเบี้ยยิ่งขึ้น การโปะก็ยิ่งคุ้ม</p>

{CALC}

<h2>ควรถามธนาคารอะไรก่อนโปะ</h2>
<ul>
<li><b>ค่าธรรมเนียมคิดจากอะไร</b>: จากเงินที่โปะหรือจากยอดหนี้ทั้งหมด และเก็บเฉพาะตอนปิดหนี้ทั้งก้อนหรือการโปะบางส่วนด้วย</li>
<li><b>เลือกได้ไหม</b> ว่าจะลดระยะเวลาหรือลดค่างวด หรือธนาคารกำหนดไว้แล้ว</li>
<li><b>ยอดโปะขั้นต่ำ</b> และจำนวนครั้งที่โปะได้ต่อปี</li>
<li>ขอ <b>ตารางผ่อนชำระใหม่</b> หลังโปะ แล้วเทียบกับเครื่องคำนวณด้านบน</li>
</ul>
<p>อย่าใช้เงินสำรองฉุกเฉินจนหมด เงินที่โปะเข้าไปแล้วเอาคืนยากเมื่อต้องใช้ด่วน ควรเก็บไว้อย่างน้อยเท่าค่าใช้จ่ายสักสองสามเดือน</p>
""",
    faq=[
        ("ค่าธรรมเนียมโปะหรือปิดหนี้ก่อนกำหนดปกติเท่าไร",
         "สินเชื่อบ้านมักเก็บประมาณ 2-3% ในช่วง 3 ปีแรก โดยเฉพาะเมื่อปิดหนี้ทั้งก้อนหรือรีไฟแนนซ์ ส่วนการโปะบางส่วนหลายสัญญาไม่เก็บ แต่ละธนาคารและแต่ละสัญญาต่างกัน ควรอ่านเงื่อนไขในสัญญาเงินกู้"),
        ("ควรโปะหนี้บ้านหรือเก็บเงินไว้ลงทุน",
         "เทียบผลตอบแทนหลังหักค่าธรรมเนียมของการโปะกับดอกเบี้ยเงินฝากหรือผลตอบแทนที่คุณได้จริง ถ้าโปะได้มากกว่า การโปะก็คุ้มกว่า โดยยังต้องมีเงินสำรองฉุกเฉินพอ"),
        ("ช่วงดอกเบี้ยคงที่ปีแรก ๆ ควรโปะไหม",
         "ช่วงนั้นเงินที่โปะช่วยเลี่ยงดอกเบี้ยต่ำ แต่หลังจากนั้นจะช่วยเลี่ยงดอกเบี้ยลอยตัว สำหรับเงินกู้ที่ยังเหลือนาน ประโยชน์ส่วนใหญ่อยู่ในช่วงลอยตัว ถ้าค่าธรรมเนียมจะหมดหลัง 3 ปี หลายคนจึงรอถึงตอนนั้นค่อยโปะก้อนใหญ่"),
        ("ลดระยะเวลาหรือลดค่างวด แบบไหนคุ้มกว่า",
         "ผลตอบแทนของทั้งสองแบบแทบเท่ากัน ลดระยะเวลาประหยัดดอกเบี้ยได้มากกว่าเพราะคุณยังจ่ายมากขึ้นทุกเดือน เลือกลดค่างวดถ้าอยากให้แต่ละเดือนสบายขึ้น"),
    ],
    promo=("วางแผนโปะหนี้?", "แอป Fincal คำนวณทุกแผนการโปะให้ ใช้ได้แม้ไม่มีอินเทอร์เน็ต:",
           [("โปะหลายครั้ง", "ครั้งเดียวหรือเป็นประจำ มีค่าธรรมเนียม ดูว่าประหยัดได้เท่าไร"),
            ("ดอกเบี้ยเปลี่ยน", "ดอกเบี้ยคงที่แล้วลอยตัว กี่ช่วงก็ได้"),
            ("บันทึกและเปรียบเทียบ", "วางหลายแผนเทียบกันเพื่อเลือกแผนที่เหมาะที่สุด")]),
)

# ---------------------------------------------------------------- pt-BR
A["pt-BR"] = dict(
    path="/fincal/amortizacao-antecipada/", ct="web-fincal-article-prepay-pt",
    title="Amortização Antecipada: Reduzir Prazo ou Parcela? Exemplo e Calculadora | Fincal",
    h1="Amortização antecipada: reduzir o prazo ou a parcela?",
    desc="Quanto se economiza amortizando R$ 50.000 de um financiamento de R$ 300.000, por que reduzir o prazo economiza mais juros e como comparar com deixar o dinheiro investido. Com gráfico, tabela e calculadora.",
    crumb="Amortização antecipada", byline="Nanoko Studio · Atualizado em 21/11/2026", summary="Resumo",
    B=300_000, R=11.5, n=300, method="equal", X=50_000, F=0,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=True, cur="R$", pre=True, dec=0, intl="pt-BR", scale=1), div=1, sfx="% ao ano",
    names=dict(base="Sem amortizar", shorter="Reduzir prazo", lower="Reduzir parcela"),
    methods=dict(equal="SAC", annuity="Tabela Price"),
    m1="{n} mês", mn="{n} meses",
    ticks=["0", "150 mil", "300 mil"], year0="Hoje", year_tick="Ano {y}", year_tip="Após {y} anos", year_tip0="Logo após amortizar",
    tldr="Saldo devedor de <b>R$ 300.000</b> no SAC, 11,5% ao ano, faltando 25 anos. Você amortiza <b>R$ 50.000</b>:",
    tile_shorter="de juros economizados, quitado {cut} antes", tile_lower="de juros economizados, parcela {drop} menor",
    hero="Cada real amortizado rende", hero_small="a mesma taxa do financiamento, sem risco",
    ex_rows=["Próxima parcela", "Quitado em", "Juros que ainda faltam", "Juros economizados", ""],
    fig=("Saldo devedor ao longo do tempo", "Toque no gráfico para ver o saldo de cada ano.",
         "Saldo devedor nas três opções: sem amortizar, reduzir prazo e reduzir parcela"),
    tbl_head="Tarifa", tbl_group="Retorno após a tarifa (% ao ano) pelo prazo restante", tbl_year="{y} anos",
    calc=dict(title="Calcule para o seu financiamento", bal="Saldo devedor", rate="Taxa de juros", rate_unit="% ao ano",
              term="Prazo restante", term_unit="meses", method="Sistema", extra="Valor a amortizar",
              fee="Tarifa (se houver)", fee_unit="% do valor", fee_line="Tarifa a pagar:",
              rows=["Juros economizados", "Após a tarifa", "Resultado", "Retorno ao ano"],
              cut="Quitado {m} antes", newpay="Próxima parcela {v}", paidoff="Quitado agora",
              more="Ver o novo cronograma →"),
    body="""
<p>Recebeu 13º, PLR ou resgatou uma aplicação? Muita gente pensa logo em amortizar o financiamento. Antes de pedir ao banco, vale responder duas perguntas: <b>reduzir o prazo ou reduzir a parcela</b>, e <b>compensa mais amortizar ou deixar o dinheiro investido</b>.</p>

<h2>Exemplo: saldo de R$ 300.000 e 25 anos pela frente</h2>
<p>Financiamento imobiliário no SAC, taxa de 11,5% ao ano, faltando 300 meses, próxima parcela de {basepay}. Você amortiza R$ 50.000. Em empréstimos para pessoa física, o banco não pode cobrar tarifa pela amortização antecipada e precisa abater os juros proporcionalmente. Depois disso, há duas escolhas:</p>
<ul>
<li><b>Reduzir o prazo</b>: a amortização mensal continua {keep}, então o financiamento termina antes.</li>
<li><b>Reduzir a parcela</b>: o prazo de 25 anos continua, os R$ 250.000 restantes são divididos de novo pelos 300 meses e a próxima parcela cai para {newpay}.</li>
</ul>
{EXTABLE}
{HBARS}
<p><a href="{ex_link}">Ver o cronograma sem amortizar →</a></p>

{FIG}

<h2>Reduzir o prazo economiza mais, mas não é necessariamente melhor</h2>
<p>Na tabela, reduzir o prazo economiza {s_saved}, quase o dobro dos {l_saved} de reduzir a parcela. Não é porque essa opção é mais esperta. Reduzindo o prazo, você continua amortizando o mesmo valor alto todo mês, ou seja, <b>coloca mais dinheiro no financiamento</b> nos anos seguintes. Mais dinheiro pagando a dívida significa, claro, menos juros.</p>
<p>A medida justa é o <b>retorno</b>: quantos por cento ao ano de juros cada real amortizado evita. Sem tarifa, as duas opções rendem exatamente a taxa do financiamento, {s_yield}. A escolha, então, depende do seu orçamento:</p>
<ul>
<li>Renda estável e vontade de quitar logo: <b>reduzir o prazo</b>.</li>
<li>Quer folga no orçamento caso a renda caia: <b>reduzir a parcela</b>. Se depois usar a diferença para amortizar de novo, o resultado fica perto de reduzir o prazo.</li>
</ul>

<h2>Amortizar ou deixar investido?</h2>
<p>Amortizar é como aplicar o dinheiro sem risco, rendendo a taxa do financiamento e sem imposto de renda. Para valer mais a pena investir, a aplicação precisa render mais que isso <b>depois do IR</b>, o que nem sempre acontece. Lembre também que o custo efetivo total inclui seguros obrigatórios e, no financiamento com TR, a correção do saldo, então o juro que você evita pode ser um pouco maior que a taxa nominal.</p>
<p>Se o contrato tiver alguma tarifa (por exemplo, em empréstimo para empresa), ela é paga uma vez só, e quanto mais tempo falta, menor o peso dela por ano. A calculadora abaixo tem um campo para isso.</p>

{CALC}

<h2>Antes de pedir a amortização</h2>
<ul>
<li>Confirme no app ou na agência se dá para <b>escolher entre prazo e parcela</b>, e o valor mínimo aceito.</li>
<li>No financiamento imobiliário, veja se você pode <b>usar o FGTS</b> para amortizar e quais são as regras do banco e do fundo.</li>
<li>Peça o <b>novo cronograma</b> depois da amortização e confira com a calculadora acima.</li>
</ul>
<p>Não use toda a reserva de emergência. Dinheiro colocado no financiamento é difícil de recuperar quando surge um imprevisto, então guarde pelo menos alguns meses de despesas.</p>
""",
    faq=[
        ("O banco pode cobrar multa por amortização antecipada?",
         "Para pessoa física, não: o Código de Defesa do Consumidor garante a redução proporcional dos juros, e as regras do Banco Central não permitem tarifa pela liquidação ou amortização antecipada nesses contratos. Contratos de empresas podem ter outras condições."),
        ("Vale mais a pena amortizar ou investir?",
         "Compare a taxa do financiamento com o rendimento líquido de IR que você teria. Se a aplicação render menos que a taxa do financiamento, amortizar é melhor, desde que você mantenha uma reserva de emergência."),
        ("Posso usar o FGTS para amortizar?",
         "No financiamento habitacional, em geral sim, para imóvel residencial e respeitando as regras do FGTS, como intervalos mínimos entre usos. Confirme as condições com o seu banco."),
        ("Reduzir prazo ou parcela, o que é melhor?",
         "O retorno das duas opções é o mesmo, a taxa do financiamento. Reduzir o prazo economiza mais juros porque você continua pagando mais por mês. Escolha reduzir a parcela se quiser um orçamento mensal mais folgado."),
    ],
    promo=("Planejando quitar antes?", "O app Fincal calcula todos os cenários de amortização, mesmo sem internet:",
           [("Várias amortizações", "uma vez ou todo mês, e veja quanto economiza"),
            ("Taxa que muda", "uma taxa inicial e depois outra, quantos períodos quiser"),
            ("Salve e compare", "coloque os cenários lado a lado e escolha o melhor")]),
)

# ---------------------------------------------------------------- ms
A["ms"] = dict(
    path="/fincal/bayar-pinjaman-awal/", ct="web-fincal-article-prepay-ms",
    title="Bayar Pinjaman Rumah Lebih Awal: Pendekkan Tempoh atau Kurangkan Ansuran? | Fincal",
    h1="Bayar pinjaman lebih awal: pendekkan tempoh atau kurangkan ansuran, dan berbaloikah penaltinya?",
    desc="Berapa faedah dijimatkan jika membayar RM 50,000 lebih awal untuk pinjaman RM 400,000, berbaloikah penalti 2%, dan patutkah anda pendekkan tempoh atau kurangkan ansuran. Dengan carta, jadual dan kalkulator.",
    crumb="Bayar pinjaman lebih awal", byline="Nanoko Studio · Dikemas kini 21/11/2026", summary="Ringkasan",
    B=400_000, R=4.2, n=360, method="annuity", X=50_000, F=2,
    fees=[1, 2, 3], years=[1, 3, 5, 10, 15],
    fmt=dict(dc=False, cur="RM", pre=True, dec=0, intl="ms-MY", scale=1), div=1, sfx="% setahun",
    names=dict(base="Tanpa bayaran awal", shorter="Pendekkan tempoh", lower="Kurangkan ansuran"),
    methods=dict(annuity="Ansuran sama setiap bulan", equal="Pokok sama setiap bulan"),
    m1="{n} bulan", mn="{n} bulan",
    ticks=["0", "200K", "400K"], year0="Kini", year_tick="Thn {y}", year_tip="Selepas {y} tahun", year_tip0="Sejurus selepas bayaran awal",
    tldr="Baki pinjaman <b>RM 400,000</b>, kadar 4.2% setahun, tinggal 30 tahun. Anda membayar <b>RM 50,000</b> lebih awal dengan penalti 2%:",
    tile_shorter="faedah dijimatkan, selesai {cut} lebih awal", tile_lower="faedah dijimatkan, ansuran turun {drop} sebulan",
    hero="Selepas penalti, RM 50,000 itu memberi pulangan", hero_small="hampir sama dengan kadar pinjaman 4.2%",
    ex_rows=["Ansuran bulan depan", "Selesai dalam", "Baki faedah perlu dibayar", "Faedah dijimatkan", "Selepas penalti {fee}"],
    fig=("Baki pinjaman mengikut masa", "Sentuh carta untuk melihat baki setiap tahun.",
         "Baki pinjaman bagi tiga pilihan: tanpa bayaran awal, pendekkan tempoh dan kurangkan ansuran"),
    tbl_head="Penalti", tbl_group="Pulangan selepas penalti (% setahun) mengikut baki tempoh", tbl_year="{y} thn",
    calc=dict(title="Kira untuk pinjaman anda", bal="Baki pinjaman", rate="Kadar faedah", rate_unit="% setahun",
              term="Baki tempoh", term_unit="bulan", method="Cara bayaran", extra="Jumlah bayaran awal",
              fee="Penalti", fee_unit="% daripada jumlah", fee_line="Penalti perlu dibayar:",
              rows=["Faedah dijimatkan", "Selepas penalti", "Hasil", "Pulangan selepas penalti"],
              cut="Selesai {m} lebih awal", newpay="Ansuran seterusnya {v}", paidoff="Selesai sepenuhnya",
              more="Lihat jadual bayaran baharu →"),
    body="""
<p>Dapat bonus, dividen KWSP atau simpanan tetap yang matang, ramai terfikir untuk membayar sebahagian pinjaman rumah. Sebelum ke bank, ada dua soalan yang perlu dijawab: <b>adakah penalti menghabiskan manfaatnya</b>, dan apabila bank bertanya sama ada mahu <b>pendekkan tempoh atau kurangkan ansuran</b>, yang mana patut dipilih.</p>

<h2>Contoh: baki RM 400,000, tinggal 30 tahun</h2>
<p>Pinjaman rumah dengan ansuran sama {basepay} sebulan, kadar 4.2% setahun, baki 360 bulan. Anda membayar RM 50,000 lebih awal, masih dalam tempoh lock-in, dan dikenakan penalti 2%, iaitu {fee}. Selepas itu ada dua pilihan:</p>
<ul>
<li><b>Pendekkan tempoh</b>: terus bayar {keep} sebulan seperti biasa, jadi pinjaman selesai lebih awal.</li>
<li><b>Kurangkan ansuran</b>: kekalkan 30 tahun, baki RM 350,000 dibahagi semula kepada 360 bulan, jadi ansuran turun kepada {newpay}.</li>
</ul>
{EXTABLE}
{HBARS}
<p>Mana-mana pilihan pun, penalti 2% tetap kecil berbanding faedah yang dijimatkan. <a href="{ex_link}">Lihat jadual bayaran tanpa bayaran awal →</a></p>

{FIG}

<h2>Pendekkan tempoh menjimatkan lebih banyak, tetapi belum tentu lebih untung</h2>
<p>Dalam jadual, pendekkan tempoh menjimatkan {s_saved}, lebih dua kali ganda {l_saved} daripada kurangkan ansuran. Sebabnya bukan kerana cara ini lebih bijak. Apabila memendekkan tempoh, anda terus membayar jumlah penuh setiap bulan, bermakna <b>lebih banyak wang dimasukkan ke dalam pinjaman</b> pada tahun-tahun seterusnya. Lebih banyak wang membayar hutang, tentulah faedahnya kurang.</p>
<p>Ukuran yang lebih adil ialah <b>pulangan</b>: setiap ringgit yang dibayar awal mengelakkan faedah berapa peratus setahun. Tanpa penalti, kedua-dua pilihan memberi tepat kadar pinjaman, 4.2% setahun. Dengan penalti 2%, pendekkan tempoh memberi {s_yield} dan kurangkan ansuran {l_yield}, hampir sama.</p>
<p>Jadi pilihlah mengikut aliran tunai anda:</p>
<ul>
<li>Pendapatan stabil dan mahu cepat bebas hutang: <b>pendekkan tempoh</b>.</li>
<li>Mahu ansuran bulanan lebih ringan, berjaga-jaga jika pendapatan turun: <b>kurangkan ansuran</b>. Jika beza ansuran itu nanti digunakan untuk bayar awal lagi, hasilnya hampir sama dengan pendekkan tempoh.</li>
</ul>

<h2>Berapa penalti yang masih berbaloi?</h2>
<p>Membayar lebih awal sama seperti menyimpan wang dalam akaun tanpa risiko yang memberi kadar sama dengan kadar pinjaman anda. Penalti dibayar sekali sahaja di awal, jadi semakin panjang baki tempoh, semakin kecil penalti itu jika dibahagi setiap tahun. Jadual di bawah ialah pulangan selepas penalti bagi pinjaman 4.2% setahun, dengan pilihan kurangkan ansuran:</p>
{YTABLE}
<p>Jika baki tempoh 5 tahun atau lebih, penalti 1-3% hanya menurunkan pulangan kepada {y5_lo}-{y5_hi}. Jika tinggal 1 tahun, lain ceritanya: penalti 3% menjadikan pulangan {y1_lo}, iaitu anda rugi berbanding tidak membayar langsung. Jika tempoh lock-in akan tamat tidak lama lagi, menunggu beberapa bulan mungkin lebih berbaloi.</p>
<p>Bandingkan pulangan ini dengan apa yang boleh diperoleh jika wang itu disimpan, contohnya kadar simpanan tetap. Jika membayar awal memberi pulangan lebih tinggi, ia lebih berbaloi. Bagi pinjaman kadar terapung, pulangan sebenar mengikut kadar pada tahun-tahun akan datang, jadi semakin naik kadar, semakin berbaloi membayar awal.</p>

{CALC}

<h2>Perkara yang perlu ditanya kepada bank</h2>
<ul>
<li><b>Cara penalti dikira</b>: daripada jumlah yang dibayar awal atau daripada jumlah pinjaman asal, dan bila tempoh lock-in tamat. Jika dikira daripada jumlah asal, tukarkan kepada peratus jumlah yang anda bayar sebelum memasukkannya ke kalkulator.</li>
<li><b>Boleh memilih</b> pendekkan tempoh atau kurangkan ansuran, atau bank menetapkan salah satu.</li>
<li>Bagi pinjaman flexi atau semi-flexi, wang lebihan mungkin boleh dikeluarkan semula. Tanya syaratnya.</li>
<li>Minta <b>jadual bayaran baharu</b> selepas itu dan semak dengan kalkulator di atas.</li>
</ul>
<p>Jangan gunakan semua dana kecemasan. Wang yang sudah dimasukkan ke dalam pinjaman sukar diambil semula apabila diperlukan, jadi simpan sekurang-kurangnya perbelanjaan beberapa bulan.</p>
""",
    faq=[
        ("Berapakah penalti bayaran awal yang biasa?",
         "Ramai bank mengenakan sekitar 2-3% semasa tempoh lock-in, biasanya 3 hingga 5 tahun pertama, dan selalunya apabila pinjaman diselesaikan sepenuhnya. Ada yang mengira daripada jumlah pinjaman asal. Setiap bank dan produk berbeza, jadi baca surat tawaran anda."),
        ("Lebih baik bayar pinjaman awal atau simpan wang?",
         "Bandingkan pulangan selepas penalti dengan kadar simpanan atau pelaburan yang anda dapat. Jika membayar awal memberi pulangan lebih tinggi, ia pilihan yang lebih baik, asalkan dana kecemasan masih mencukupi."),
        ("Patutkah membayar awal semasa tempoh lock-in?",
         "Penalti biasanya hanya dikenakan dalam tempoh lock-in. Jika tempoh itu hampir tamat, menunggu selalunya lebih berbaloi. Jika masih lama dan baki tempoh pinjaman panjang, penalti kecil berbanding faedah yang dijimatkan."),
        ("Pendekkan tempoh atau kurangkan ansuran, mana lebih untung?",
         "Pulangan kedua-duanya hampir sama. Pendekkan tempoh menjimatkan lebih banyak faedah kerana anda terus membayar lebih setiap bulan. Pilih kurangkan ansuran jika mahu bajet bulanan lebih longgar."),
    ],
    promo=("Merancang bayar lebih awal?", "Aplikasi Fincal mengira semua senario bayaran awal, boleh digunakan tanpa internet:",
           [("Bayaran awal berkali-kali", "sekali atau berkala, dengan penalti, lihat berapa dijimatkan"),
            ("Kadar berubah", "kadar awal kemudian terapung, berapa banyak tempoh pun"),
            ("Simpan dan bandingkan", "letak senario bersebelahan dan pilih yang terbaik")]),
)
