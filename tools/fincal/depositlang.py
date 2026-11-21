"""Content for the 'interest paid monthly vs at maturity' article, one dict per language.
Example: amount A for t months, rate E at maturity, M paid monthly, monthly interest re-deposited at R.
Rates are stated as assumptions in the text, never as a bank's current offer."""

D = {}

D["vi"] = dict(
    path="/fincal/lai-hang-thang-hay-cuoi-ky/", ct="web-fincal-article-deposit-vi",
    title="Gửi tiết kiệm nhận lãi hằng tháng hay cuối kỳ: cách nào lời hơn? | Fincal",
    h1="Gửi tiết kiệm nhận lãi hằng tháng hay cuối kỳ: cách nào lời hơn?",
    desc="Gửi 500 triệu 12 tháng: nhận lãi cuối kỳ được bao nhiêu, nhận hằng tháng rồi gửi tiếp được bao nhiêu, và lãi hằng tháng phải bằng bao nhiêu mới hòa. Có biểu đồ, bảng và máy tính.",
    crumb="Lãi hằng tháng hay cuối kỳ", byline="Nanoko Studio · Cập nhật 21/11/2026", summary="Tóm tắt",
    A=500_000_000, t=12, E=5.5, M=5.35, R=3,
    res=[0.1, 3, 4, 5.5], terms=[6, 12, 24, 36],
    fmt=dict(dc=True, cur="đ", pre=False, dec=0, intl="vi-VN", scale=1), sfx="%/năm",
    m1="{n} tháng", mn="{n} tháng",
    ticks=["0", "15tr", "30tr"], tick_max=30_000_000, month_tick="T{m}",
    month_tip="Tháng {m}", series=("Nhận hằng tháng, gửi tiếp 3%", "Nhận cuối kỳ"),
    tldr="Gửi <b>500 triệu</b> kỳ hạn 12 tháng, giả sử lãi <b>5,5%</b>/năm nếu nhận cuối kỳ và <b>5,35%</b>/năm nếu nhận hằng tháng:",
    tile_end="lãi cuối kỳ, nhận một lần", tile_mon="nhận hằng tháng, gửi tiếp lãi 3%",
    hero="Nhận cuối kỳ lời hơn", hero_small="nếu để lãi trong tài khoản thanh toán thì chênh {idle}",
    fig=("Tiền lãi tích lũy qua 12 tháng", "Chạm vào biểu đồ để xem số tiền từng tháng.",
         "Tiền lãi tích lũy khi nhận cuối kỳ và khi nhận hằng tháng rồi gửi tiếp"),
    rtbl=("Tiền lãi hằng tháng để ở đâu", "Tổng sau 12 tháng", "Kém nhận cuối kỳ"),
    re_name={0.1: "Tài khoản thanh toán, 0,1%", 3: "Gửi kỳ hạn 1 tháng, 3%", 4: "Gửi kỳ hạn 1 tháng, 4%", 5.5: "Sinh lãi 5,5%, bằng lãi cuối kỳ"},
    ttbl=("Kỳ hạn", "Lãi cuối kỳ 5,5%", "Lãi hằng tháng tối thiểu"),
    calc=dict(title="Tính cho khoản gửi của bạn", amount="Số tiền gửi", term="Kỳ hạn", term_unit="tháng",
              end="Lãi nhận cuối kỳ", mon="Lãi nhận hằng tháng", re="Lãi khi gửi tiếp tiền lãi", rate_unit="%/năm",
              rows=["Lãi nhận cuối kỳ", "Mỗi tháng nhận", "Tổng khi nhận hằng tháng và gửi tiếp", "Chênh lệch", "Lãi hằng tháng để hòa"],
              endwins="Cuối kỳ hơn {v}", monwins="Hằng tháng hơn {v}", same="Bằng nhau"),
    body="""
<p>Khi gửi tiết kiệm, ngân hàng thường hỏi bạn muốn nhận lãi cuối kỳ, hằng tháng hay đầu kỳ. Lãi nhận hằng tháng luôn được niêm yết thấp hơn một chút. Câu hỏi là: nhận tiền sớm có bù lại được phần lãi thấp hơn đó không?</p>

<h2>Vì sao lãi nhận hằng tháng thấp hơn</h2>
<p>Nhận lãi cuối kỳ nghĩa là ngân hàng giữ toàn bộ tiền lãi đến ngày đáo hạn. Nhận hằng tháng thì bạn có tiền lãi sớm hơn và có thể đem đi gửi tiếp, nên ngân hàng trừ bớt đúng phần lợi đó vào lãi suất. Nếu ngân hàng tính chuẩn, hai cách cho kết quả gần như nhau, và chênh lệch chỉ đến từ việc bạn dùng tiền lãi hằng tháng vào đâu.</p>

<h2>Ví dụ: gửi 500 triệu trong 12 tháng</h2>
<p>Các mức lãi trong ví dụ là giả định để so sánh, không phải lãi của ngân hàng nào. Nhận cuối kỳ với lãi 5,5%/năm, sau 12 tháng bạn nhận <b>{end}</b> một lần. Nhận hằng tháng với lãi 5,35%/năm, mỗi tháng bạn nhận {each}, cộng lại 12 tháng là {paid}.</p>
<p>Nếu mỗi tháng đem tiền lãi gửi tiếp kỳ hạn 1 tháng với lãi 3%/năm, phần lãi đó sinh thêm {extra}, tổng cộng {pot}. Nhận cuối kỳ vẫn hơn <b>{gap}</b>.</p>
{FIG}
<p>Đường nhận hằng tháng đi lên đều, đường cuối kỳ nằm ở 0 cho đến tháng 12 rồi nhảy lên. Đến cuối kỳ, đường cuối kỳ vẫn cao hơn một chút.</p>

<h2>Tiền lãi hằng tháng để ở đâu quyết định kết quả</h2>
<p>Cùng ví dụ trên, chỉ thay đổi nơi bạn để tiền lãi nhận hằng tháng:</p>
{RTABLE}
<p>Để tiền lãi nằm yên trong tài khoản thanh toán là cách thiệt nhất, kém nhận cuối kỳ {idle}. Trong ví dụ này, ngay cả khi gửi tiếp được với lãi bằng lãi cuối kỳ, nhận hằng tháng vẫn kém một chút, vì mức lãi hằng tháng đã bị trừ nhiều hơn phần lợi từ việc nhận sớm. Với số tiền 500 triệu, chênh lệch chỉ vài trăm nghìn mỗi năm, nhỏ hơn nhiều so với chênh lệch lãi suất giữa các ngân hàng.</p>

<h2>Lãi hằng tháng phải bằng bao nhiêu mới hòa</h2>
<p>Muốn biết ngân hàng có trừ hợp lý không, hãy tính mức lãi hằng tháng hòa vốn: mức mà nếu bạn gửi tiếp tiền lãi với lãi 3%/năm thì cuối kỳ được đúng bằng nhận cuối kỳ. Nếu ngân hàng niêm yết cao hơn mức này, nhận hằng tháng lời hơn.</p>
{TTABLE}
<p>Kỳ hạn càng dài, mức hòa vốn càng thấp, vì lãi cuối kỳ không được gộp vào gốc trong suốt kỳ hạn còn tiền lãi hằng tháng thì có thời gian sinh lãi lâu hơn. Với kỳ hạn 2-3 năm, nhận hằng tháng rồi gửi tiếp đều đặn có thể lời hơn nếu ngân hàng trừ ít.</p>

{CALC}

<h2>Khi nào nên chọn nhận lãi hằng tháng</h2>
<ul>
<li><b>Bạn cần dòng tiền đều</b>, chẳng hạn người đã nghỉ hưu dùng tiền lãi để chi tiêu. Lúc đó khoản chênh vài trăm nghìn là cái giá hợp lý cho sự chủ động.</li>
<li><b>Kỳ hạn dài và bạn chắc chắn sẽ gửi tiếp tiền lãi</b>, nếu lãi niêm yết cao hơn mức hòa vốn ở bảng trên.</li>
<li>Nếu không cần tiền, <b>nhận cuối kỳ</b> thường đơn giản và lời hơn một chút. Khi đáo hạn, gửi lại cả gốc lẫn lãi là bạn đã có lãi kép. <a href="/fincal/tinh-lai-kep/">Tính lãi kép khi gửi nhiều năm →</a></li>
</ul>
<p>Một lưu ý: nếu rút trước hạn, phần lớn ngân hàng chỉ trả lãi không kỳ hạn cho thời gian đã gửi. Với khoản nhận lãi hằng tháng, tiền lãi đã nhận vượt mức đó sẽ bị trừ lại vào tiền gốc, nên nhận hằng tháng không giúp bạn tránh thiệt khi rút sớm.</p>
""",
    faq=[
        ("Nhận lãi hằng tháng hay cuối kỳ lời hơn?",
         "Thường nhận cuối kỳ lời hơn một chút, vì lãi nhận hằng tháng được niêm yết thấp hơn. Với 500 triệu gửi 12 tháng, lãi cuối kỳ 5,5% và lãi hằng tháng 5,35%, nhận cuối kỳ hơn khoảng 380 nghìn nếu bạn gửi tiếp tiền lãi với lãi 3%, và hơn khoảng 740 nghìn nếu để tiền lãi trong tài khoản thanh toán."),
        ("Vì sao lãi suất nhận hằng tháng thấp hơn lãi nhận cuối kỳ?",
         "Vì bạn nhận tiền lãi sớm và có thể dùng hoặc gửi tiếp số tiền đó. Ngân hàng trừ bớt lãi suất để bù lại phần lợi này."),
        ("Ai nên chọn nhận lãi hằng tháng?",
         "Người cần dòng tiền đều để chi tiêu, chẳng hạn người đã nghỉ hưu. Nếu không cần tiền, nhận cuối kỳ rồi gửi lại cả gốc lẫn lãi thường lời hơn."),
        ("Rút trước hạn khi đang nhận lãi hằng tháng thì sao?",
         "Phần lớn ngân hàng chỉ trả lãi không kỳ hạn cho thời gian đã gửi. Tiền lãi hằng tháng đã nhận vượt mức đó sẽ bị trừ lại vào tiền gốc khi bạn rút."),
    ],
    promo_title="Theo dõi nhiều khoản tiết kiệm?",
)

D["en"] = dict(
    path="/fincal/monthly-interest-vs-at-maturity/", ct="web-fincal-article-deposit",
    title="Fixed deposit interest: monthly payout or at maturity? | Fincal",
    h1="Fixed deposit interest: take it monthly or at maturity?",
    desc="Put 50,000 in a 12-month fixed deposit: what you get at maturity, what monthly interest adds up to if you save it again, and the monthly rate you need to break even. With chart, tables and calculator.",
    crumb="Monthly vs at maturity", byline="Nanoko Studio · Updated 21 Nov 2026", summary="Summary",
    A=50_000, t=12, E=4.5, M=4.4, R=3,
    res=[0, 3, 4, 4.5], terms=[6, 12, 24, 36],
    fmt=dict(dc=False, cur="", pre=False, dec=0, intl="en-US", scale=100), sfx="% a year",
    m1="{n} month", mn="{n} months",
    ticks=["0", "1,250", "2,500"], tick_max=2_500, month_tick="M{m}",
    month_tip="Month {m}", series=("Monthly, saved again at 3%", "At maturity"),
    tldr="Put <b>50,000</b> in a 12-month fixed deposit, assuming <b>4.5%</b> a year paid at maturity or <b>4.4%</b> a year paid monthly:",
    tile_end="paid once at maturity", tile_mon="monthly, each payment saved at 3%",
    hero="At maturity comes out ahead by", hero_small="{idle} if the monthly interest just sits in a current account",
    fig=("Interest built up over 12 months", "Tap the chart to see the amount for each month.",
         "Interest built up when paid at maturity and when paid monthly and saved again"),
    rtbl=("Where the monthly interest goes", "Total after 12 months", "Behind at maturity by"),
    re_name={0: "Current account, 0%", 3: "Savings account, 3%", 4: "Savings account, 4%", 4.5: "Earning 4.5%, same as the deposit"},
    rwin="monthly ahead by {v}",
    ttbl=("Term", "Interest at 4.5%", "Lowest monthly rate to break even"),
    calc=dict(title="Try your own deposit", amount="Amount", term="Term", term_unit="months",
              end="Rate paid at maturity", mon="Rate paid monthly", re="Rate on the monthly interest", rate_unit="% a year",
              rows=["Interest at maturity", "Paid each month", "Total if paid monthly and saved", "Difference", "Monthly rate to break even"],
              endwins="At maturity ahead by {v}", monwins="Monthly ahead by {v}", same="The same"),
    body="""
<p>When you open a fixed deposit or term deposit, the bank may ask whether you want the interest paid at maturity or every month. The monthly option usually comes with a slightly lower rate. So does getting the money sooner make up for the lower rate?</p>

<h2>Why the monthly rate is lower</h2>
<p>With interest at maturity, the bank keeps all the interest until the end of the term. With monthly interest you get the money earlier and can save or spend it, so the bank trims the rate to account for that. If the bank prices it fairly, both options end up close, and the difference comes down to what you do with the monthly payments.</p>

<h2>Example: 50,000 for 12 months</h2>
<p>The rates here are assumptions for comparison, not any bank's offer. At 4.5% a year paid at maturity, you get <b>{end}</b> in one go after 12 months. At 4.4% a year paid monthly, you get {each} a month, or {paid} over the year.</p>
<p>If you move each monthly payment into a savings account paying 3% a year, it earns another {extra}, for a total of {pot}. Interest at maturity is still ahead by <b>{gap}</b>.</p>
{FIG}
<p>The monthly line climbs steadily while the maturity line stays at zero until month 12 and then jumps. At the end of the term the maturity line is still slightly higher.</p>

<h2>Where the monthly interest goes decides the result</h2>
<p>Same example, changing only where the monthly interest goes:</p>
{RTABLE}
<p>Leaving the interest in a current account that pays nothing is the worst choice, {idle} behind. In this example, even earning the same 4.5% on the monthly payments still leaves you slightly behind, because the monthly rate was cut by more than the benefit of getting paid early. On 50,000 the gap is small, much smaller than the difference between rates at different banks.</p>

<h2>What monthly rate breaks even</h2>
<p>To check whether the bank's monthly rate is fair, work out the break-even rate: the monthly rate at which saving each payment at 3% a year ends up exactly equal to interest at maturity. If the bank offers more than this, monthly interest wins.</p>
{TTABLE}
<p>The longer the term, the lower the break-even rate, because interest at maturity is not compounded during the term while monthly payments have longer to earn. On 2-3 year deposits, monthly interest that you save regularly can come out ahead if the bank's discount is small. If the bank offers the same rate for both options, monthly interest that you save again always comes out slightly ahead.</p>

{CALC}

<h2>When monthly interest makes sense</h2>
<ul>
<li><b>You need a regular income</b>, for example in retirement. Giving up a little interest for a steady monthly payment is a fair trade.</li>
<li><b>Long terms where you will reliably save the interest</b>, if the offered monthly rate is above the break-even rate in the table.</li>
<li>If you don't need the money, <b>interest at maturity</b> is usually simpler and slightly better. Roll over the principal and interest together and you get compound interest. <a href="/fincal/compound-interest-calculator/">See how savings grow over many years →</a></li>
</ul>
<p>One caution: breaking a fixed deposit early usually costs you interest. With monthly payouts, interest already paid above what you are entitled to may be taken back from your principal, so monthly interest does not protect you if you withdraw early.</p>
""",
    faq=[
        ("Is it better to get fixed deposit interest monthly or at maturity?",
         "Interest at maturity usually comes out slightly ahead, because the monthly rate is set a little lower. With 50,000 for 12 months at 4.5% at maturity or 4.4% monthly, maturity wins by about 20 if you save the monthly interest at 3%, and by about 50 if it sits in a current account."),
        ("Why is the monthly interest rate lower?",
         "Because you receive the interest earlier and can use or save it. The bank lowers the rate to balance that benefit."),
        ("Who should choose monthly interest?",
         "People who need a regular income, such as retirees. If you don't need the money, interest at maturity rolled over with the principal is usually better."),
        ("What if the bank offers the same rate for both?",
         "Then monthly interest wins, as long as you save each payment somewhere that pays interest. The earlier money earns a little extra."),
    ],
    promo_title="Planning your savings?",
)

D["id"] = dict(
    path="/fincal/bunga-deposito-bulanan-atau-jatuh-tempo/", ct="web-fincal-article-deposit-id",
    title="Bunga deposito dibayar bulanan atau saat jatuh tempo? | Fincal",
    h1="Bunga deposito dibayar bulanan atau saat jatuh tempo: mana yang lebih untung?",
    desc="Deposito Rp 100 juta 12 bulan: berapa bunga saat jatuh tempo, berapa jika bunga bulanan ditempatkan lagi, dan bunga bulanan minimal agar impas. Dengan grafik, tabel dan kalkulator.",
    crumb="Bunga bulanan atau jatuh tempo", byline="Nanoko Studio · Diperbarui 21/11/2026", summary="Ringkasan",
    A=100_000_000, t=12, E=4.5, M=4.4, R=3,
    res=[0.5, 3, 4, 4.5], terms=[6, 12, 24, 36],
    fmt=dict(dc=True, cur="Rp", pre=True, dec=0, intl="id-ID", scale=1), sfx="% per tahun",
    m1="{n} bulan", mn="{n} bulan",
    ticks=["0", "2,5 jt", "5 jt"], tick_max=5_000_000, month_tick="B{m}",
    month_tip="Bulan {m}", series=("Bulanan, ditempatkan lagi 3%", "Saat jatuh tempo"),
    tldr="Deposito <b>Rp 100 juta</b> tenor 12 bulan, misalkan bunga <b>4,5%</b> per tahun jika dibayar saat jatuh tempo dan <b>4,4%</b> per tahun jika dibayar bulanan:",
    tile_end="dibayar sekali saat jatuh tempo", tile_mon="bulanan, ditempatkan lagi 3%",
    hero="Jatuh tempo lebih untung", hero_small="selisihnya {idle} jika bunga bulanan dibiarkan di tabungan",
    fig=("Bunga terkumpul selama 12 bulan", "Ketuk grafik untuk melihat jumlah tiap bulan.",
         "Bunga terkumpul jika dibayar saat jatuh tempo dan jika dibayar bulanan lalu ditempatkan lagi"),
    rtbl=("Bunga bulanan ditaruh di mana", "Total setelah 12 bulan", "Kalah dari jatuh tempo"),
    re_name={0.5: "Tabungan biasa, 0,5%", 3: "Deposito 1 bulan, 3%", 4: "Deposito 1 bulan, 4%", 4.5: "Berbunga 4,5%, sama dengan deposito"},
    rwin="bulanan unggul {v}",
    ttbl=("Tenor", "Bunga jatuh tempo 4,5%", "Bunga bulanan minimal"),
    calc=dict(title="Hitung deposito Anda", amount="Jumlah deposito", term="Tenor", term_unit="bulan",
              end="Bunga saat jatuh tempo", mon="Bunga dibayar bulanan", re="Bunga saat menempatkan lagi bunga bulanan", rate_unit="% per tahun",
              rows=["Bunga saat jatuh tempo", "Diterima tiap bulan", "Total jika bulanan dan ditempatkan lagi", "Selisih", "Bunga bulanan agar impas"],
              endwins="Jatuh tempo unggul {v}", monwins="Bulanan unggul {v}", same="Sama"),
    body="""
<p>Saat membuka deposito, Anda bisa ditanya apakah bunga ingin dibayar setiap bulan atau sekaligus saat jatuh tempo. Jika bank memasang bunga bulanan sedikit lebih rendah, apakah menerima uang lebih awal bisa menutup selisih itu?</p>

<h2>Mengapa bunga bulanan bisa lebih rendah</h2>
<p>Jika bunga dibayar saat jatuh tempo, bank menahan seluruh bunga sampai akhir tenor. Jika dibayar bulanan, Anda menerima uang lebih awal dan bisa memakainya atau menempatkannya lagi, sehingga bank bisa memotong suku bunga untuk mengimbangi keuntungan itu. Jika potongannya wajar, hasil kedua cara hampir sama, dan selisihnya ditentukan oleh ke mana bunga bulanan Anda pergi.</p>

<h2>Contoh: deposito Rp 100 juta selama 12 bulan</h2>
<p>Suku bunga dalam contoh ini adalah asumsi untuk perbandingan, bukan penawaran bank mana pun, dan belum dipotong pajak. Dengan bunga 4,5% per tahun dibayar saat jatuh tempo, setelah 12 bulan Anda menerima <b>{end}</b> sekaligus. Dengan bunga 4,4% per tahun dibayar bulanan, Anda menerima {each} per bulan, atau {paid} dalam setahun.</p>
<p>Jika setiap bulan bunga itu ditempatkan lagi di deposito 1 bulan berbunga 3% per tahun, bunga tersebut menghasilkan tambahan {extra}, totalnya {pot}. Bunga saat jatuh tempo masih unggul <b>{gap}</b>.</p>
{FIG}
<p>Garis bulanan naik perlahan, sedangkan garis jatuh tempo tetap di nol sampai bulan ke-12 lalu melonjak. Di akhir tenor, garis jatuh tempo masih sedikit lebih tinggi.</p>

<h2>Ke mana bunga bulanan ditaruh menentukan hasilnya</h2>
<p>Contoh yang sama, hanya mengubah tempat bunga bulanan disimpan:</p>
{RTABLE}
<p>Membiarkan bunga di tabungan biasa adalah pilihan paling rugi, kalah {idle}. Dalam contoh ini, meski bunga bulanan bisa ditempatkan lagi dengan bunga yang sama 4,5%, cara bulanan tetap sedikit kalah, karena potongan suku bunganya lebih besar daripada manfaat menerima uang lebih awal. Untuk Rp 100 juta, selisihnya kecil, jauh lebih kecil daripada perbedaan suku bunga antarbank.</p>

<h2>Berapa bunga bulanan agar impas</h2>
<p>Untuk menilai apakah potongan bank wajar, hitung bunga bulanan impas: tingkat bunga bulanan yang, jika setiap pembayaran ditempatkan lagi dengan bunga 3% per tahun, menghasilkan total yang sama dengan bunga saat jatuh tempo. Jika bank menawarkan lebih tinggi dari angka ini, bunga bulanan lebih untung.</p>
{TTABLE}
<p>Makin panjang tenor, makin rendah angka impasnya, karena bunga saat jatuh tempo tidak digabung ke pokok selama tenor, sementara bunga bulanan punya waktu lebih lama untuk berbunga. Sebagian bank memberi suku bunga yang sama untuk kedua cara. Jika begitu, bunga bulanan yang ditempatkan lagi selalu sedikit lebih untung.</p>

{CALC}

<h2>Kapan sebaiknya memilih bunga bulanan</h2>
<ul>
<li><b>Anda butuh pemasukan rutin</b>, misalnya setelah pensiun. Mengorbankan sedikit bunga demi uang bulanan yang pasti adalah pertukaran yang wajar.</li>
<li><b>Suku bunganya sama dengan bunga jatuh tempo</b>, atau di atas angka impas pada tabel, dan Anda rajin menempatkan lagi bunga tersebut.</li>
<li>Jika tidak butuh uangnya, <b>bunga saat jatuh tempo</b> biasanya lebih sederhana. Perpanjang pokok bersama bunganya (ARO pokok plus bunga) dan Anda mendapat bunga majemuk. <a href="/fincal/kalkulator-bunga-majemuk/">Hitung pertumbuhan tabungan beberapa tahun →</a></li>
</ul>
<p>Satu catatan: mencairkan deposito sebelum jatuh tempo biasanya dikenai penalti. Bunga bulanan yang sudah diterima tidak membuat Anda terhindar dari penalti itu, jadi pilih tenor sesuai kapan uang benar-benar dibutuhkan.</p>
""",
    faq=[
        ("Bunga deposito lebih untung dibayar bulanan atau saat jatuh tempo?",
         "Jika suku bunga bulanan lebih rendah, jatuh tempo biasanya sedikit lebih untung. Untuk Rp 100 juta selama 12 bulan dengan bunga 4,5% saat jatuh tempo atau 4,4% bulanan, jatuh tempo unggul sekitar Rp 39 ribu jika bunga bulanan ditempatkan lagi dengan bunga 3%. Jika suku bunganya sama, bunga bulanan yang ditempatkan lagi yang lebih untung."),
        ("Mengapa bunga bulanan bisa lebih rendah?",
         "Karena Anda menerima bunga lebih awal dan bisa memakainya atau menempatkannya lagi. Bank menurunkan suku bunga untuk mengimbangi manfaat itu."),
        ("Siapa yang cocok memilih bunga bulanan?",
         "Orang yang butuh pemasukan rutin, misalnya pensiunan. Jika tidak butuh uangnya, bunga saat jatuh tempo yang diperpanjang bersama pokok biasanya lebih baik."),
        ("Apakah pajak bunga deposito berbeda untuk kedua cara?",
         "Pajak final bunga deposito dipotong dari setiap pembayaran bunga dengan tarif yang sama, jadi tidak mengubah perbandingan. Contoh di halaman ini belum memperhitungkan pajak."),
    ],
    promo_title="Merencanakan tabungan?",
)

D["th"] = dict(
    path="/fincal/dokbia-rai-duean-rue-khrop-kamnot/", ct="web-fincal-article-deposit-th",
    title="ฝากประจำ รับดอกเบี้ยรายเดือนหรือครบกำหนด แบบไหนได้มากกว่า | Fincal",
    h1="ฝากประจำ รับดอกเบี้ยรายเดือนหรือรับตอนครบกำหนด แบบไหนได้มากกว่า",
    desc="ฝาก 1,000,000 บาท 12 เดือน: รับดอกเบี้ยตอนครบกำหนดได้เท่าไร รับรายเดือนแล้วนำไปฝากต่อได้เท่าไร และดอกเบี้ยรายเดือนต้องเท่าไรจึงคุ้มทุน มีกราฟ ตาราง และเครื่องคำนวณ",
    crumb="ดอกเบี้ยรายเดือนหรือครบกำหนด", byline="Nanoko Studio · อัปเดต 21 พ.ย. 2026", summary="สรุป",
    A=1_000_000, t=12, E=2, M=1.95, R=1,
    res=[0.25, 1, 1.5, 2], terms=[6, 12, 24, 36],
    fmt=dict(dc=False, cur="บาท", pre=False, dec=0, intl="th-TH", scale=100), sfx="% ต่อปี",
    m1="{n} เดือน", mn="{n} เดือน",
    ticks=["0", "12,000", "24,000"], tick_max=24_000, month_tick="ด.{m}",
    month_tip="เดือนที่ {m}", series=("รายเดือน นำไปฝากต่อ 1%", "ครบกำหนด"),
    tldr="ฝาก <b>1,000,000 บาท</b> ฝากประจำ 12 เดือน สมมติดอกเบี้ย <b>2%</b> ต่อปีถ้ารับตอนครบกำหนด และ <b>1.95%</b> ต่อปีถ้ารับรายเดือน:",
    tile_end="รับครั้งเดียวตอนครบกำหนด", tile_mon="รับรายเดือน นำไปฝากต่อ 1%",
    hero="รับตอนครบกำหนดได้มากกว่า", hero_small="ถ้าทิ้งดอกเบี้ยไว้ในบัญชีออมทรัพย์ 0.25% จะต่างกัน {idle}",
    fig=("ดอกเบี้ยสะสมตลอด 12 เดือน", "แตะกราฟเพื่อดูยอดแต่ละเดือน",
         "ดอกเบี้ยสะสมเมื่อรับตอนครบกำหนด และเมื่อรับรายเดือนแล้วนำไปฝากต่อ"),
    rtbl=("นำดอกเบี้ยรายเดือนไปไว้ที่ไหน", "รวมหลัง 12 เดือน", "น้อยกว่าครบกำหนด"),
    re_name={0.25: "ออมทรัพย์ทั่วไป 0.25%", 1: "ออมทรัพย์ดอกเบี้ยสูง 1%", 1.5: "ออมทรัพย์ดอกเบี้ยสูง 1.5%", 2: "ได้ 2% เท่ากับฝากประจำ"},
    rwin="รายเดือนได้มากกว่า {v}",
    ttbl=("ระยะเวลาฝาก", "ดอกเบี้ยครบกำหนด 2%", "ดอกเบี้ยรายเดือนขั้นต่ำ"),
    calc=dict(title="คำนวณเงินฝากของคุณ", amount="เงินฝาก", term="ระยะเวลาฝาก", term_unit="เดือน",
              end="ดอกเบี้ยรับตอนครบกำหนด", mon="ดอกเบี้ยรับรายเดือน", re="ดอกเบี้ยเมื่อนำดอกเบี้ยรายเดือนไปฝากต่อ", rate_unit="% ต่อปี",
              rows=["ดอกเบี้ยตอนครบกำหนด", "รับต่อเดือน", "รวมเมื่อรับรายเดือนและฝากต่อ", "ส่วนต่าง", "ดอกเบี้ยรายเดือนที่คุ้มทุน"],
              endwins="ครบกำหนดได้มากกว่า {v}", monwins="รายเดือนได้มากกว่า {v}", same="เท่ากัน"),
    body="""
<p>เวลาฝากประจำ บางธนาคารมีให้เลือกว่าจะรับดอกเบี้ยทุกเดือนหรือรับครั้งเดียวตอนครบกำหนด แบบรับรายเดือนมักให้ดอกเบี้ยต่ำกว่าเล็กน้อย คำถามคือการได้เงินเร็วขึ้นชดเชยดอกเบี้ยที่ต่ำกว่านั้นได้หรือไม่</p>

<h2>ทำไมดอกเบี้ยรายเดือนจึงต่ำกว่า</h2>
<p>ถ้ารับตอนครบกำหนด ธนาคารถือดอกเบี้ยทั้งหมดไว้จนจบระยะเวลาฝาก ถ้ารับรายเดือน คุณได้เงินเร็วขึ้นและนำไปใช้หรือฝากต่อได้ ธนาคารจึงลดอัตราดอกเบี้ยลงเพื่อชดเชยข้อได้เปรียบนี้ ถ้าลดอย่างเหมาะสม ผลของสองแบบจะใกล้เคียงกัน และส่วนต่างขึ้นอยู่กับว่าคุณนำดอกเบี้ยรายเดือนไปทำอะไร</p>

<h2>ตัวอย่าง: ฝาก 1,000,000 บาท 12 เดือน</h2>
<p>อัตราดอกเบี้ยในตัวอย่างเป็นสมมติฐานเพื่อเปรียบเทียบ ไม่ใช่ข้อเสนอของธนาคารใด และยังไม่หักภาษี ถ้ารับตอนครบกำหนดที่ 2% ต่อปี หลัง 12 เดือนคุณได้ <b>{end}</b> ในครั้งเดียว ถ้ารับรายเดือนที่ 1.95% ต่อปี คุณได้เดือนละ {each} รวม 12 เดือนเป็น {paid}</p>
<p>ถ้านำดอกเบี้ยแต่ละเดือนไปฝากออมทรัพย์ดอกเบี้ยสูง 1% ต่อปี ดอกเบี้ยส่วนนี้งอกเพิ่มอีก {extra} รวมเป็น {pot} การรับตอนครบกำหนดยังได้มากกว่า <b>{gap}</b></p>
{FIG}
<p>เส้นรายเดือนค่อย ๆ ไต่ขึ้น ส่วนเส้นครบกำหนดอยู่ที่ศูนย์จนถึงเดือนที่ 12 แล้วกระโดดขึ้น เมื่อจบระยะเวลาฝาก เส้นครบกำหนดยังสูงกว่าเล็กน้อย</p>

<h2>ดอกเบี้ยรายเดือนไปอยู่ที่ไหน คือตัวตัดสิน</h2>
<p>ตัวอย่างเดิม เปลี่ยนแค่ที่เก็บดอกเบี้ยรายเดือน:</p>
{RTABLE}
<p>ทิ้งดอกเบี้ยไว้ในออมทรัพย์ทั่วไปเสียเปรียบที่สุด น้อยกว่า {idle} ในตัวอย่างนี้ แม้นำไปฝากต่อได้ที่ 2% เท่ากับฝากประจำ แบบรายเดือนก็ยังได้น้อยกว่าเล็กน้อย เพราะอัตรารายเดือนถูกลดมากกว่าประโยชน์จากการได้เงินเร็ว สำหรับเงินล้าน ส่วนต่างนี้เล็กมากเมื่อเทียบกับความต่างของดอกเบี้ยระหว่างธนาคาร</p>

<h2>ดอกเบี้ยรายเดือนต้องเท่าไรจึงคุ้มทุน</h2>
<p>ลองคำนวณอัตรารายเดือนที่คุ้มทุน คืออัตราที่ถ้านำดอกเบี้ยแต่ละเดือนไปฝากต่อที่ 1% ต่อปี แล้วได้ยอดเท่ากับรับตอนครบกำหนดพอดี ถ้าธนาคารให้สูงกว่านี้ แบบรายเดือนได้มากกว่า</p>
{TTABLE}
<p>ยิ่งฝากนาน อัตราคุ้มทุนยิ่งต่ำลง เพราะดอกเบี้ยครบกำหนดไม่ได้ทบต้นระหว่างทาง ขณะที่ดอกเบี้ยรายเดือนมีเวลางอกเงยนานกว่า ถ้าธนาคารให้อัตราเท่ากันทั้งสองแบบ การรับรายเดือนแล้วนำไปฝากต่อจะได้มากกว่าเล็กน้อยเสมอ</p>

{CALC}

<h2>เมื่อไรควรเลือกรับดอกเบี้ยรายเดือน</h2>
<ul>
<li><b>ต้องการรายได้สม่ำเสมอ</b> เช่น หลังเกษียณ การยอมเสียดอกเบี้ยเล็กน้อยเพื่อได้เงินทุกเดือนเป็นการแลกที่สมเหตุสมผล</li>
<li><b>ฝากระยะยาวและนำดอกเบี้ยไปฝากต่อสม่ำเสมอ</b> ถ้าอัตรารายเดือนสูงกว่าอัตราคุ้มทุนในตาราง</li>
<li>ถ้าไม่ต้องใช้เงิน <b>รับตอนครบกำหนด</b> มักง่ายกว่าและได้มากกว่าเล็กน้อย พอครบกำหนดให้ฝากต่อทั้งเงินต้นและดอกเบี้ย ก็ได้ดอกเบี้ยทบต้น <a href="/fincal/khamnuan-dokbia-thop-ton/">คำนวณเงินออมหลายปี →</a></li>
</ul>
<p>ข้อควรระวัง: การถอนฝากประจำก่อนครบกำหนดมักได้ดอกเบี้ยลดลงหรือไม่ได้เลย และดอกเบี้ยรายเดือนที่รับไปแล้วเกินสิทธิ์อาจถูกหักคืนจากเงินต้น การรับรายเดือนจึงไม่ได้ช่วยเมื่อต้องถอนก่อนกำหนด</p>
""",
    faq=[
        ("ฝากประจำ รับดอกเบี้ยรายเดือนหรือครบกำหนดได้มากกว่า",
         "ถ้าอัตรารายเดือนต่ำกว่า การรับตอนครบกำหนดมักได้มากกว่าเล็กน้อย เช่น ฝาก 1,000,000 บาท 12 เดือน ดอกเบี้ยครบกำหนด 2% หรือรายเดือน 1.95% รับตอนครบกำหนดได้มากกว่าราว 410 บาท ถ้านำดอกเบี้ยรายเดือนไปฝากต่อที่ 1%"),
        ("ทำไมดอกเบี้ยรายเดือนต่ำกว่า",
         "เพราะคุณได้ดอกเบี้ยเร็วกว่าและนำไปใช้หรือฝากต่อได้ ธนาคารจึงลดอัตราลงเพื่อชดเชยข้อได้เปรียบนี้"),
        ("ใครควรเลือกรับดอกเบี้ยรายเดือน",
         "คนที่ต้องการรายได้สม่ำเสมอ เช่น ผู้เกษียณ ถ้าไม่ต้องใช้เงิน การรับตอนครบกำหนดแล้วฝากต่อทั้งต้นและดอกมักได้มากกว่า"),
        ("ถ้าธนาคารให้อัตราเท่ากันทั้งสองแบบล่ะ",
         "ถ้าอัตราเท่ากัน การรับรายเดือนแล้วนำไปฝากที่มีดอกเบี้ยจะได้มากกว่าเล็กน้อย เพราะเงินที่ได้ก่อนงอกเงยเพิ่ม"),
    ],
    promo_title="วางแผนเงินออม?",
)

D["pt-BR"] = dict(
    path="/fincal/juros-mensais-ou-no-vencimento/", ct="web-fincal-article-deposit-pt",
    title="CDB com juros mensais ou no vencimento: qual rende mais? | Fincal",
    h1="Juros mensais ou no vencimento: qual rende mais?",
    desc="R$ 100.000 por 12 meses: quanto rende com juros no vencimento, quanto com juros mensais reinvestidos, e a taxa mensal mínima para empatar. Com gráfico, tabelas e calculadora.",
    crumb="Juros mensais ou no vencimento", byline="Nanoko Studio · Atualizado em 21/11/2026", summary="Resumo",
    A=100_000, t=12, E=12, M=11.6, R=6,
    res=[0, 6, 9, 12], terms=[6, 12, 24, 36],
    fmt=dict(dc=True, cur="R$", pre=True, dec=0, intl="pt-BR", scale=100), sfx="% ao ano",
    m1="{n} mês", mn="{n} meses",
    ticks=["0", "7,5 mil", "15 mil"], tick_max=15_000, month_tick="M{m}",
    month_tip="Mês {m}", series=("Mensal, reinvestido a 6%", "No vencimento"),
    tldr="Aplicar <b>R$ 100.000</b> por 12 meses, supondo <b>12%</b> ao ano com juros no vencimento ou <b>11,6%</b> ao ano com juros mensais:",
    tile_end="recebido de uma vez no vencimento", tile_mon="mensal, reinvestido a 6%",
    hero="No vencimento rende mais", hero_small="a diferença sobe para {idle} se os juros ficarem parados na conta",
    fig=("Juros acumulados em 12 meses", "Toque no gráfico para ver o valor de cada mês.",
         "Juros acumulados com pagamento no vencimento e com juros mensais reinvestidos"),
    rtbl=("Onde ficam os juros mensais", "Total após 12 meses", "Atrás do vencimento"),
    re_name={0: "Conta corrente, 0%", 6: "Rendendo 6%", 9: "Rendendo 9%", 12: "Rendendo 12%, igual à aplicação"},
    rwin="mensal à frente {v}",
    ttbl=("Prazo", "Juros no vencimento a 12%", "Taxa mensal mínima"),
    calc=dict(title="Calcule a sua aplicação", amount="Valor aplicado", term="Prazo", term_unit="meses",
              end="Taxa com juros no vencimento", mon="Taxa com juros mensais", re="Rendimento ao reinvestir os juros", rate_unit="% ao ano",
              rows=["Juros no vencimento", "Recebido por mês", "Total com juros mensais reinvestidos", "Diferença", "Taxa mensal para empatar"],
              endwins="Vencimento à frente {v}", monwins="Mensal à frente {v}", same="Igual"),
    body="""
<p>Alguns CDBs, LCIs e LCAs pagam juros todo mês, outros só no vencimento. A versão com juros mensais costuma oferecer uma taxa um pouco menor. Receber antes compensa essa taxa menor?</p>

<h2>Por que a taxa com juros mensais é menor</h2>
<p>Com juros no vencimento, o emissor fica com todos os juros até o fim do prazo. Com juros mensais, você recebe antes e pode gastar ou reinvestir, então o emissor reduz a taxa para compensar essa vantagem. Se a redução for justa, as duas opções ficam próximas, e a diferença depende do que você faz com os juros mensais.</p>

<h2>Exemplo: R$ 100.000 por 12 meses</h2>
<p>As taxas do exemplo são hipóteses para comparar, não ofertas de nenhum banco, e o cálculo é antes do Imposto de Renda. Com 12% ao ano no vencimento, após 12 meses você recebe <b>{end}</b> de uma vez. Com 11,6% ao ano em juros mensais, você recebe {each} por mês, ou {paid} no ano.</p>
<p>Se cada pagamento for reinvestido rendendo 6% ao ano, esses juros rendem mais {extra}, total de {pot}. Os juros no vencimento ainda ficam <b>{gap}</b> à frente.</p>
{FIG}
<p>A linha mensal sobe aos poucos, e a linha do vencimento fica em zero até o mês 12 e então salta. No fim do prazo, a linha do vencimento ainda está um pouco acima.</p>

<h2>Onde você reinveste decide o resultado</h2>
<p>Mesmo exemplo, mudando só onde ficam os juros mensais:</p>
{RTABLE}
<p>Deixar os juros parados na conta corrente é a pior escolha, {idle} atrás. Com taxas altas como as do exemplo, reinvestir faz muita diferença: se os juros mensais renderem 9% ou mais, a opção mensal passa à frente. Com juros mais baixos, o vencimento costuma ganhar.</p>

<h2>Qual taxa mensal empata</h2>
<p>Para avaliar a oferta, calcule a taxa de empate: a taxa com juros mensais que, reinvestindo cada pagamento a 6% ao ano, chega exatamente ao mesmo total do vencimento. Se a oferta for maior que isso, os juros mensais rendem mais.</p>
{TTABLE}
<p>Quanto mais longo o prazo, menor a taxa de empate, porque os juros no vencimento não são capitalizados durante o prazo nesta comparação, enquanto os juros mensais têm mais tempo para render.</p>

{CALC}

<h2>E o Imposto de Renda?</h2>
<p>Em aplicações tributadas, como CDB, cada pagamento de juros sofre IR pela tabela regressiva conforme o tempo desde a aplicação. Os juros pagos nos primeiros meses caem nas alíquotas mais altas, enquanto no vencimento de 12 meses a alíquota já é menor. Na prática, isso pesa contra os juros mensais. Em LCI e LCA, isentas de IR para pessoa física, essa diferença não existe.</p>

<h2>Quando escolher juros mensais</h2>
<ul>
<li><b>Você precisa de renda mensal</b>, por exemplo na aposentadoria. Abrir mão de um pouco de rendimento por um valor certo todo mês é uma troca razoável.</li>
<li><b>A taxa mensal está acima da taxa de empate</b> e você vai reinvestir os juros com disciplina, de preferência em aplicação isenta.</li>
<li>Se não precisa do dinheiro, <b>juros no vencimento</b> costumam ser mais simples e render um pouco mais. Reaplique principal e juros no vencimento e você tem juros compostos. <a href="/fincal/calculadora-de-juros-compostos/">Veja como o dinheiro cresce em vários anos →</a></li>
</ul>
<p>Lembre também que muitos títulos sem liquidez diária não permitem resgate antes do vencimento, recebendo ou não juros mensais.</p>
""",
    faq=[
        ("Juros mensais ou no vencimento: qual rende mais?",
         "Depende da taxa e de onde você reinveste. Com R$ 100.000 por 12 meses a 12% no vencimento ou 11,6% mensal, o vencimento fica cerca de R$ 76 à frente se os juros forem reinvestidos a 6%, mas os juros mensais ganham se renderem 9% ou mais. Antes do IR."),
        ("Por que a taxa com juros mensais é menor?",
         "Porque você recebe os juros antes e pode usar ou reinvestir. O emissor reduz a taxa para compensar essa vantagem."),
        ("O Imposto de Renda muda a conta?",
         "Sim, em aplicações tributadas. Cada pagamento mensal é tributado pela tabela regressiva conforme o prazo desde a aplicação, então os primeiros juros pagam alíquotas maiores. Em LCI e LCA, isentas para pessoa física, não há essa diferença."),
        ("Quem deve escolher juros mensais?",
         "Quem precisa de renda mensal, como aposentados. Se não precisa do dinheiro, juros no vencimento reaplicados com o principal costumam render mais."),
    ],
    promo_title="Planejando seus investimentos?",
)

D["ms"] = dict(
    path="/fincal/faedah-bulanan-atau-matang/", ct="web-fincal-article-deposit-ms",
    title="Simpanan tetap: faedah bulanan atau semasa matang? | Fincal",
    h1="Simpanan tetap: ambil faedah setiap bulan atau semasa matang?",
    desc="Simpan RM 100,000 selama 12 bulan: berapa faedah semasa matang, berapa jika faedah bulanan disimpan semula, dan kadar bulanan minimum untuk seri. Dengan carta, jadual dan kalkulator.",
    crumb="Faedah bulanan atau matang", byline="Nanoko Studio · Dikemas kini 21/11/2026", summary="Ringkasan",
    A=100_000, t=12, E=3.5, M=3.4, R=2,
    res=[0.25, 2, 3, 3.5], terms=[6, 12, 24, 36],
    fmt=dict(dc=False, cur="RM", pre=True, dec=0, intl="ms-MY", scale=100), sfx="% setahun",
    m1="{n} bulan", mn="{n} bulan",
    ticks=["0", "2,000", "4,000"], tick_max=4_000, month_tick="B{m}",
    month_tip="Bulan {m}", series=("Bulanan, disimpan semula 2%", "Semasa matang"),
    tldr="Simpan <b>RM 100,000</b> dalam simpanan tetap 12 bulan, andaikan faedah <b>3.5%</b> setahun jika dibayar semasa matang atau <b>3.4%</b> setahun jika dibayar bulanan:",
    tile_end="dibayar sekali semasa matang", tile_mon="bulanan, disimpan semula 2%",
    hero="Semasa matang lebih untung", hero_small="bezanya {idle} jika faedah dibiarkan dalam akaun simpanan biasa",
    fig=("Faedah terkumpul dalam 12 bulan", "Sentuh carta untuk melihat jumlah setiap bulan.",
         "Faedah terkumpul jika dibayar semasa matang dan jika dibayar bulanan lalu disimpan semula"),
    rtbl=("Faedah bulanan disimpan di mana", "Jumlah selepas 12 bulan", "Kurang daripada matang"),
    re_name={0.25: "Akaun simpanan biasa, 0.25%", 2: "Akaun simpanan, 2%", 3: "Akaun simpanan, 3%", 3.5: "Faedah 3.5%, sama seperti simpanan tetap"},
    rwin="bulanan lebih {v}",
    ttbl=("Tempoh", "Faedah matang 3.5%", "Kadar bulanan minimum"),
    calc=dict(title="Kira simpanan anda", amount="Jumlah simpanan", term="Tempoh", term_unit="bulan",
              end="Kadar dibayar semasa matang", mon="Kadar dibayar bulanan", re="Kadar untuk faedah bulanan yang disimpan semula", rate_unit="% setahun",
              rows=["Faedah semasa matang", "Diterima setiap bulan", "Jumlah jika bulanan dan disimpan semula", "Beza", "Kadar bulanan untuk seri"],
              endwins="Matang lebih {v}", monwins="Bulanan lebih {v}", same="Sama"),
    body="""
<p>Sesetengah bank menawarkan simpanan tetap dengan faedah dibayar setiap bulan, selain faedah semasa matang. Pilihan bulanan biasanya datang dengan kadar yang sedikit lebih rendah. Adakah menerima wang lebih awal dapat menampung kadar yang lebih rendah itu?</p>

<h2>Mengapa kadar bulanan lebih rendah</h2>
<p>Jika faedah dibayar semasa matang, bank memegang semua faedah hingga akhir tempoh. Jika dibayar bulanan, anda menerima wang lebih awal dan boleh membelanjakan atau menyimpannya semula, jadi bank mengurangkan kadar untuk mengimbangi kelebihan itu. Jika pengurangannya adil, kedua-dua pilihan hampir sama, dan bezanya bergantung pada apa yang anda lakukan dengan faedah bulanan.</p>

<h2>Contoh: RM 100,000 selama 12 bulan</h2>
<p>Kadar dalam contoh ini ialah andaian untuk perbandingan, bukan tawaran mana-mana bank. Pada 3.5% setahun dibayar semasa matang, selepas 12 bulan anda menerima <b>{end}</b> sekali gus. Pada 3.4% setahun dibayar bulanan, anda menerima {each} sebulan, atau {paid} setahun.</p>
<p>Jika setiap bayaran disimpan semula dalam akaun simpanan berfaedah 2% setahun, faedah itu menghasilkan tambahan {extra}, jumlahnya {pot}. Faedah semasa matang masih lebih <b>{gap}</b>.</p>
{FIG}
<p>Garis bulanan naik perlahan, manakala garis matang kekal di sifar sehingga bulan ke-12 lalu melonjak. Pada akhir tempoh, garis matang masih sedikit lebih tinggi.</p>

<h2>Di mana faedah bulanan disimpan menentukan hasilnya</h2>
<p>Contoh yang sama, hanya menukar tempat faedah bulanan disimpan:</p>
{RTABLE}
<p>Membiarkan faedah dalam akaun simpanan biasa ialah pilihan paling rugi, kurang {idle}. Dalam contoh ini, walaupun faedah bulanan disimpan semula pada kadar yang sama 3.5%, pilihan bulanan masih sedikit kurang, kerana kadarnya dipotong lebih daripada manfaat menerima wang lebih awal. Untuk RM 100,000, bezanya kecil, jauh lebih kecil daripada perbezaan kadar antara bank.</p>

<h2>Berapa kadar bulanan untuk seri</h2>
<p>Untuk menilai tawaran bank, kira kadar seri: kadar bulanan yang, jika setiap bayaran disimpan semula pada 2% setahun, memberi jumlah yang sama tepat dengan faedah semasa matang. Jika bank menawarkan lebih tinggi daripada ini, faedah bulanan lebih untung.</p>
{TTABLE}
<p>Semakin panjang tempoh, semakin rendah kadar seri, kerana faedah semasa matang tidak dikompaun sepanjang tempoh, manakala faedah bulanan mempunyai masa lebih lama untuk berkembang. Jika bank memberi kadar yang sama untuk kedua-dua pilihan, faedah bulanan yang disimpan semula sentiasa sedikit lebih untung.</p>

{CALC}

<h2>Bila sesuai memilih faedah bulanan</h2>
<ul>
<li><b>Anda perlukan pendapatan tetap</b>, contohnya selepas bersara. Melepaskan sedikit faedah demi wang bulanan yang pasti adalah pertukaran yang munasabah.</li>
<li><b>Tempoh panjang dan anda pasti akan menyimpan semula faedah</b>, jika kadar bulanan lebih tinggi daripada kadar seri dalam jadual.</li>
<li>Jika tidak memerlukan wang itu, <b>faedah semasa matang</b> biasanya lebih mudah dan sedikit lebih untung. Perbaharui pokok bersama faedah dan anda mendapat faedah kompaun. <a href="/fincal/kalkulator-faedah-kompaun/">Lihat pertumbuhan simpanan beberapa tahun →</a></li>
</ul>
<p>Satu peringatan: mengeluarkan simpanan tetap sebelum matang biasanya mengurangkan atau menghapuskan faedah. Bagi pilihan bulanan, faedah yang sudah dibayar melebihi hak anda boleh ditolak daripada pokok, jadi faedah bulanan tidak melindungi anda jika perlu keluarkan awal.</p>
""",
    faq=[
        ("Simpanan tetap: faedah bulanan atau semasa matang lebih untung?",
         "Jika kadar bulanan lebih rendah, faedah semasa matang biasanya sedikit lebih untung. Untuk RM 100,000 selama 12 bulan pada 3.5% semasa matang atau 3.4% bulanan, matang lebih kira-kira RM 69 jika faedah bulanan disimpan semula pada 2%, dan kira-kira RM 96 jika dibiarkan dalam akaun simpanan biasa."),
        ("Mengapa kadar faedah bulanan lebih rendah?",
         "Kerana anda menerima faedah lebih awal dan boleh menggunakannya atau menyimpannya semula. Bank merendahkan kadar untuk mengimbangi kelebihan itu."),
        ("Siapa yang sesuai memilih faedah bulanan?",
         "Mereka yang perlukan pendapatan tetap, seperti pesara. Jika tidak memerlukan wang itu, faedah semasa matang yang diperbaharui bersama pokok biasanya lebih baik."),
        ("Bagaimana jika bank memberi kadar yang sama?",
         "Jika kadarnya sama, faedah bulanan yang disimpan semula di tempat berfaedah akan sedikit lebih untung, kerana wang yang diterima awal menjana faedah tambahan."),
    ],
    promo_title="Merancang simpanan anda?",
)
