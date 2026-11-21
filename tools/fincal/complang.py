"""Content for the compound interest calculator pages. Terms follow the Fincal app's own translations.
Article placeholders ({fv}, {put}, ...) are filled with numbers computed by the engine for the page defaults."""

C = {}

C["en"] = dict(
    path="/fincal/compound-interest-calculator/", og="en_US",
    title="Compound Interest Calculator - With Monthly Contributions | Fincal",
    desc="Free compound interest calculator: enter a starting amount, monthly contributions, rate and years to see the future value, total interest, a growth chart and a year-by-year table.",
    h1="Compound interest calculator",
    intro="See how a starting amount and regular contributions grow with compound interest. Everything runs in your browser - nothing is stored or sent anywhere.",
    crumb_page="Compound interest",
    initial="Initial investment", contrib="Regular contribution",
    every={"m": "per month", "q": "per quarter", "y": "per year"},
    chips=[(1_000, "1K"), (10_000, "10K"), (50_000, "50K"), (100_000, "100K")],
    rate="Annual interest rate", rate_unit="% a year", years="Duration", years_unit="years",
    adv="Advanced options", kfreq="Compounding frequency", freq={"m": "Monthly", "q": "Quarterly", "y": "Yearly"},
    timing="Contribution timing", timings={"end": "End of period", "begin": "Beginning of period"},
    default=dict(initial=10_000, contrib=500, every="m", rate=7, years=20),
    put="Total put in", interest="Total interest",
    l_initial="Initial", l_contrib="Contributions", l_interest="Interest",
    cmp_title="How often is interest compounded?", cmp_note="Same amounts, rate and duration. Tap a row to use it.",
    cmp_cols=["Compounding", "Final value", "Total interest"],
    chart_title="Growth over time", chart_note="Each bar is your balance at the end of a year. Tap a bar for details.",
    sched_title="Year-by-year breakdown", sched_cols=["Year", "Contributed", "Interest", "End value"],
    sched_more="Interest is added at the end of each compounding period and rounded to the cent, the same as the Fincal app.",
    promo_title="Plan more than one goal?",
    promo_lead="The Fincal app keeps your plans with you, even offline:",
    promo_items=[("Saved scenarios", "name, reopen and duplicate them to compare plans side by side"),
                 ("Automatic history", "every calculation is kept so you can come back to it"),
                 ("Share as an image", "send the result with its charts to family or a partner"),
                 ("Loans too", "rate changes over time and prepayments with fees")],
    ct="web-fincal-calc-compound",
    loan_link="Loan calculator", compound_name="Compound interest calculator",
    article="""
<h2>What is compound interest?</h2>
<p>With compound interest, the interest you earn is added to your balance and starts earning interest itself. The longer the money stays invested, the faster it grows: in the example below more than half of the final value is interest.</p>
<div class="formula">FV = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: initial amount · PMT: contribution each period · r: annual rate · k: compounding periods a year · t: years</div>
<p>The formula is exact when you contribute once per compounding period, at the end of it. The calculator also handles contributions and compounding at different frequencies, by simulating every month.</p>
<h2>Example: 10,000 plus 500 a month at 7% for 20 years</h2>
<table class="cmp">
<thead><tr><th></th><th>Amount</th></tr></thead>
<tbody>
<tr><td>Total put in</td><td>{put}</td></tr>
<tr><td>Interest earned</td><td>{int}</td></tr>
<tr><td>Final value</td><td>{fv}</td></tr>
</tbody></table>
<p>Start 10 years earlier and keep going for 30 years, and the same plan reaches <b>{early}</b> - you put in only {early_put} in total, but the balance more than doubles.</p>
<h2>Does compounding frequency matter?</h2>
<p>A little. With the same inputs, monthly compounding gives {kf_m}, quarterly {kf_q} and yearly {kf_y}. Time and the rate matter far more than how often interest is added.</p>
<h2>Fixed deposit: interest monthly or at maturity?</h2>
<p>Monthly interest usually comes with a slightly lower rate, so if you don't need the income, interest at maturity rolled over with the principal tends to earn a little more. <a href="/fincal/monthly-interest-vs-at-maturity/">See the example and the break-even rate →</a></p>
<h2>The rule of 72</h2>
<p>Divide 72 by the annual rate to estimate how many years it takes to double your money. At 7% that is about 10 years; at 10%, about 7 years.</p>
""",
    faq=[
        ("What is the difference between simple and compound interest?",
         "Simple interest is paid only on the money you put in. Compound interest is also paid on interest you have already earned, so the balance grows faster every year."),
        ("How is the annual rate applied each month?",
         "The annual rate is divided by the number of compounding periods: 7% compounded monthly is 7% ÷ 12 per month. This is the nominal rate most savings accounts and calculators use."),
        ("What does contribution timing change?",
         "Contributions at the beginning of each period earn interest for that period too, so they end up slightly higher than contributions made at the end."),
        ("Can I use it for stocks or funds?",
         "Yes, as an estimate: enter the average yearly return you expect. Real returns go up and down from year to year, so treat the result as a projection, not a promise."),
        ("Is what I type sent anywhere?",
         "No. Every calculation runs in your browser. The numbers only appear in the page address so you can share your result."),
    ],
)

C["vi"] = dict(
    path="/fincal/tinh-lai-kep/", og="vi_VN",
    title="Tính lãi kép online - Gửi góp hằng tháng, xem tiền tăng theo năm | Fincal",
    desc="Máy tính lãi kép miễn phí: nhập vốn ban đầu, số tiền góp hằng tháng, lãi suất và số năm để xem giá trị tương lai, tổng lãi, biểu đồ tăng trưởng và bảng chi tiết từng năm.",
    h1="Tính lãi kép",
    intro="Xem vốn ban đầu và tiền góp định kỳ tăng lên bao nhiêu nhờ lãi kép. Tính ngay trên trình duyệt, không lưu hay gửi dữ liệu đi đâu.",
    crumb_page="Tính lãi kép",
    initial="Vốn ban đầu", contrib="Góp thêm định kỳ",
    every={"m": "mỗi tháng", "q": "mỗi quý", "y": "mỗi năm"},
    chips=[(10_000_000, "10 triệu"), (50_000_000, "50 triệu"), (100_000_000, "100 triệu"), (500_000_000, "500 triệu")],
    rate="Lãi suất", rate_unit="%/năm", years="Thời gian", years_unit="năm",
    adv="Tùy chọn nâng cao", kfreq="Tần suất gộp lãi", freq={"m": "Tháng", "q": "Quý", "y": "Năm"},
    timing="Thời điểm góp", timings={"end": "Cuối kỳ", "begin": "Đầu kỳ"},
    default=dict(initial=100_000_000, contrib=5_000_000, every="m", rate=7, years=15),
    put="Tổng tiền bỏ vào", interest="Tổng tiền lãi",
    l_initial="Vốn ban đầu", l_contrib="Tiền góp", l_interest="Lãi",
    cmp_title="Gộp lãi theo tháng, quý hay năm?", cmp_note="Cùng số tiền, lãi suất và thời gian. Bấm một dòng để chọn.",
    cmp_cols=["Gộp lãi", "Giá trị cuối", "Tổng lãi"],
    chart_title="Tiền tăng theo thời gian", chart_note="Mỗi cột là số dư cuối năm. Chạm vào cột để xem chi tiết.",
    sched_title="Chi tiết theo năm", sched_cols=["Năm", "Gửi vào", "Lãi", "Cuối năm"],
    sched_more="Lãi được cộng vào cuối mỗi kỳ gộp lãi và làm tròn đến từng đồng, giống app Fincal.",
    promo_title="Muốn lên nhiều kế hoạch?",
    promo_lead="App Fincal lưu kế hoạch của bạn, dùng được cả khi không có mạng:",
    promo_items=[("Lưu kịch bản", "đặt tên, mở lại, nhân bản để so sánh các phương án"),
                 ("Lịch sử tự lưu", "mọi lần tính đều được giữ lại để xem lại sau"),
                 ("Chia sẻ dạng ảnh", "gửi kết quả kèm biểu đồ cho gia đình hoặc người cùng kế hoạch"),
                 ("Tính cả lãi vay", "lãi suất theo giai đoạn, trả trước hạn có phí phạt")],
    ct="web-fincal-calc-compound-vi",
    loan_link="Tính lãi vay", compound_name="Tính lãi kép",
    article="""
<h2>Lãi kép là gì?</h2>
<p>Lãi kép là lãi được cộng vào gốc, rồi kỳ sau chính phần lãi đó lại sinh lãi. Tiền để càng lâu thì tăng càng nhanh: trong ví dụ bên dưới, gần một nửa số tiền cuối cùng là tiền lãi.</p>
<div class="formula">FV = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: vốn ban đầu · PMT: tiền góp mỗi kỳ · r: lãi suất năm · k: số kỳ gộp lãi trong năm · t: số năm</div>
<p>Công thức này chính xác khi mỗi kỳ gộp lãi bạn góp một lần vào cuối kỳ. Máy tính phía trên mô phỏng từng tháng nên tính được cả khi chu kỳ góp và chu kỳ gộp lãi khác nhau.</p>
<h2>Ví dụ: 100 triệu, góp thêm 5 triệu mỗi tháng, lãi 7%/năm trong 15 năm</h2>
<table class="cmp">
<thead><tr><th></th><th>Số tiền</th></tr></thead>
<tbody>
<tr><td>Tổng tiền bỏ vào</td><td>{put}</td></tr>
<tr><td>Tiền lãi</td><td>{int}</td></tr>
<tr><td>Giá trị cuối</td><td>{fv}</td></tr>
</tbody></table>
<p>Nếu bắt đầu sớm hơn 10 năm và duy trì 25 năm, cùng kế hoạch đó đạt <b>{early}</b>, trong khi tổng tiền bỏ vào chỉ là {early_put}.</p>
<h2>Gộp lãi theo tháng hay theo năm có khác nhiều không?</h2>
<p>Có nhưng không lớn. Cùng các con số trên, gộp lãi hằng tháng được {kf_m}, hằng quý {kf_q}, hằng năm {kf_y}. Thời gian và lãi suất quan trọng hơn nhiều so với tần suất gộp lãi.</p>
<h2>Gửi tiết kiệm nên nhận lãi hằng tháng hay cuối kỳ?</h2>
<p>Lãi nhận hằng tháng thường được niêm yết thấp hơn lãi nhận cuối kỳ, nên nếu không cần tiền chi tiêu, nhận cuối kỳ rồi gửi lại cả gốc lẫn lãi thường lời hơn một chút. <a href="/fincal/lai-hang-thang-hay-cuoi-ky/">Xem ví dụ và tính mức lãi hòa vốn →</a></p>
<h2>Quy tắc 72</h2>
<p>Lấy 72 chia cho lãi suất năm để ước lượng số năm tiền tăng gấp đôi. Lãi 7%/năm thì khoảng 10 năm, lãi 10%/năm thì khoảng 7 năm.</p>
""",
    faq=[
        ("Lãi kép khác lãi đơn thế nào?",
         "Lãi đơn chỉ tính trên số tiền bạn bỏ vào. Lãi kép tính cả trên phần lãi đã nhận, nên số dư tăng nhanh hơn qua từng năm."),
        ("Gửi tiết kiệm ngân hàng có phải lãi kép không?",
         "Nếu chọn tái tục cả gốc và lãi khi đáo hạn thì đó là lãi kép, với kỳ gộp lãi bằng kỳ hạn gửi. Ví dụ gửi kỳ hạn 3 tháng và tái tục thì chọn gộp lãi theo quý. Nếu rút lãi ra mỗi kỳ thì chỉ là lãi đơn."),
        ("Lãi suất năm được chia thế nào cho mỗi kỳ?",
         "Lãi suất năm chia cho số kỳ gộp lãi: 7%/năm gộp lãi hằng tháng là 7% ÷ 12 mỗi tháng. Đây là cách tính lãi suất danh nghĩa mà ngân hàng và hầu hết máy tính dùng."),
        ("Góp đầu kỳ hay cuối kỳ khác gì?",
         "Tiền góp đầu kỳ được tính lãi luôn cho kỳ đó, nên kết quả cao hơn một chút so với góp cuối kỳ."),
        ("Dữ liệu tôi nhập có bị gửi đi không?",
         "Không. Mọi phép tính chạy ngay trên trình duyệt của bạn. Các con số chỉ nằm trên đường dẫn của trang để bạn chia sẻ lại được kết quả."),
    ],
)

C["id"] = dict(
    path="/fincal/kalkulator-bunga-majemuk/", og="id_ID",
    title="Kalkulator Bunga Majemuk - Simulasi Investasi Bulanan | Fincal",
    desc="Kalkulator bunga majemuk gratis: masukkan modal awal, setoran bulanan, suku bunga dan jangka waktu untuk melihat nilai masa depan, total bunga, grafik pertumbuhan dan rincian per tahun.",
    h1="Kalkulator bunga majemuk",
    intro="Lihat seberapa besar modal awal dan setoran rutin tumbuh dengan bunga majemuk. Semua dihitung di browser Anda - tidak ada data yang disimpan atau dikirim.",
    crumb_page="Bunga majemuk",
    initial="Investasi awal", contrib="Setoran berkala",
    every={"m": "per bulan", "q": "per triwulan", "y": "per tahun"},
    chips=[(1_000_000, "1 jt"), (10_000_000, "10 jt"), (50_000_000, "50 jt"), (100_000_000, "100 jt")],
    rate="Suku bunga tahunan", rate_unit="% per tahun", years="Jangka waktu", years_unit="tahun",
    adv="Opsi lanjutan", kfreq="Frekuensi penggabungan bunga", freq={"m": "Bulanan", "q": "Triwulanan", "y": "Tahunan"},
    timing="Waktu setoran", timings={"end": "Akhir periode", "begin": "Awal periode"},
    default=dict(initial=10_000_000, contrib=1_000_000, every="m", rate=6, years=15),
    put="Total dana disetor", interest="Total bunga",
    l_initial="Investasi awal", l_contrib="Setoran", l_interest="Bunga",
    cmp_title="Bunga digabung bulanan, triwulanan atau tahunan?", cmp_note="Jumlah, bunga dan jangka waktu sama. Ketuk satu baris untuk memilihnya.",
    cmp_cols=["Penggabungan", "Nilai akhir", "Total bunga"],
    chart_title="Pertumbuhan dari waktu ke waktu", chart_note="Setiap batang adalah saldo di akhir tahun. Ketuk batang untuk melihat detail.",
    sched_title="Rincian tahunan", sched_cols=["Tahun", "Disetor", "Bunga", "Nilai akhir"],
    sched_more="Bunga ditambahkan di akhir setiap periode penggabungan dan dibulatkan ke rupiah, sama seperti aplikasi Fincal.",
    promo_title="Punya lebih dari satu rencana?",
    promo_lead="Aplikasi Fincal menyimpan rencana Anda, bahkan tanpa internet:",
    promo_items=[("Skenario tersimpan", "beri nama, buka lagi dan duplikat untuk membandingkan rencana"),
                 ("Riwayat otomatis", "setiap perhitungan disimpan agar bisa dibuka lagi"),
                 ("Bagikan sebagai gambar", "kirim hasil beserta grafik ke keluarga atau pasangan"),
                 ("Juga untuk pinjaman", "bunga berjenjang dan pelunasan dipercepat dengan penalti")],
    ct="web-fincal-calc-compound-id",
    loan_link="Simulasi kredit", compound_name="Kalkulator bunga majemuk",
    article="""
<h2>Apa itu bunga majemuk?</h2>
<p>Pada bunga majemuk, bunga yang Anda dapat ditambahkan ke saldo lalu ikut menghasilkan bunga di periode berikutnya. Makin lama uang diinvestasikan, makin cepat pertumbuhannya.</p>
<div class="formula">FV = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: modal awal · PMT: setoran per periode · r: bunga per tahun · k: jumlah periode penggabungan per tahun · t: tahun</div>
<p>Rumus ini tepat jika Anda menyetor sekali per periode penggabungan, di akhir periode. Kalkulator di atas menyimulasikan setiap bulan, jadi frekuensi setoran dan penggabungan bunga boleh berbeda.</p>
<h2>Contoh: Rp 10 juta ditambah Rp 1 juta per bulan, bunga 6% selama 15 tahun</h2>
<table class="cmp">
<thead><tr><th></th><th>Jumlah</th></tr></thead>
<tbody>
<tr><td>Total dana disetor</td><td>{put}</td></tr>
<tr><td>Bunga</td><td>{int}</td></tr>
<tr><td>Nilai akhir</td><td>{fv}</td></tr>
</tbody></table>
<p>Jika dimulai 10 tahun lebih awal dan dijalankan 25 tahun, rencana yang sama mencapai <b>{early}</b>, padahal total dana yang disetor hanya {early_put}.</p>
<h2>Apakah frekuensi penggabungan bunga berpengaruh?</h2>
<p>Sedikit. Dengan angka yang sama, penggabungan bulanan menghasilkan {kf_m}, triwulanan {kf_q} dan tahunan {kf_y}. Lamanya waktu dan besarnya bunga jauh lebih menentukan.</p>
<h2>Bunga deposito: bulanan atau saat jatuh tempo?</h2>
<p>Jika bunga bulanan dipasang lebih rendah, bunga saat jatuh tempo yang diperpanjang bersama pokok biasanya sedikit lebih untung. Jika suku bunganya sama, bunga bulanan yang ditempatkan lagi yang unggul. <a href="/fincal/bunga-deposito-bulanan-atau-jatuh-tempo/">Lihat contoh dan bunga impas →</a></p>
<h2>Aturan 72</h2>
<p>Bagi 72 dengan suku bunga tahunan untuk memperkirakan berapa tahun uang Anda berlipat dua. Pada 6% sekitar 12 tahun; pada 9% sekitar 8 tahun.</p>
""",
    faq=[
        ("Apa bedanya bunga tunggal dan bunga majemuk?",
         "Bunga tunggal hanya dihitung dari uang yang Anda setor. Bunga majemuk juga dihitung dari bunga yang sudah diterima, sehingga saldo tumbuh makin cepat setiap tahun."),
        ("Apakah deposito bank termasuk bunga majemuk?",
         "Ya, jika deposito diperpanjang otomatis bersama bunganya (ARO pokok + bunga). Periode penggabungannya sama dengan tenor deposito, misalnya pilih triwulanan untuk deposito 3 bulan."),
        ("Bagaimana bunga tahunan dibagi per periode?",
         "Bunga tahunan dibagi jumlah periode penggabungan: 6% per tahun yang digabung bulanan berarti 6% ÷ 12 per bulan. Ini adalah bunga nominal yang dipakai bank dan kebanyakan kalkulator."),
        ("Bisa dipakai untuk reksa dana atau saham?",
         "Bisa sebagai perkiraan: masukkan rata-rata imbal hasil tahunan yang Anda harapkan. Imbal hasil sebenarnya naik turun, jadi anggap hasilnya sebagai proyeksi, bukan jaminan."),
        ("Apakah data yang saya masukkan dikirim ke mana pun?",
         "Tidak. Semua perhitungan berjalan di browser Anda. Angka hanya muncul di alamat halaman agar hasilnya bisa dibagikan."),
    ],
)

C["th"] = dict(
    path="/fincal/khamnuan-dokbia-thop-ton/", og="th_TH",
    title="คำนวณดอกเบี้ยทบต้น ออมรายเดือน ดูเงินเติบโตรายปี | Fincal",
    desc="เครื่องคำนวณดอกเบี้ยทบต้นฟรี: ใส่เงินต้น เงินออมรายเดือน อัตราดอกเบี้ย และจำนวนปี เพื่อดูมูลค่าในอนาคต ดอกเบี้ยรวม กราฟการเติบโต และรายละเอียดรายปี",
    h1="คำนวณดอกเบี้ยทบต้น",
    intro="ดูว่าเงินต้นและเงินที่ออมเพิ่มเป็นประจำจะเติบโตเท่าไรด้วยดอกเบี้ยทบต้น คำนวณในเบราว์เซอร์ของคุณ ไม่มีการเก็บหรือส่งข้อมูลไปที่ใด",
    crumb_page="ดอกเบี้ยทบต้น",
    initial="เงินลงทุนเริ่มต้น", contrib="เงินสมทบประจำ",
    every={"m": "ต่อเดือน", "q": "ต่อไตรมาส", "y": "ต่อปี"},
    chips=[(10_000, "1 หมื่น"), (100_000, "1 แสน"), (500_000, "5 แสน"), (1_000_000, "1 ล้าน")],
    rate="อัตราดอกเบี้ยต่อปี", rate_unit="% ต่อปี", years="ระยะเวลา", years_unit="ปี",
    adv="ตัวเลือกขั้นสูง", kfreq="ความถี่ทบต้น", freq={"m": "รายเดือน", "q": "รายไตรมาส", "y": "รายปี"},
    timing="ช่วงเวลาสมทบ", timings={"end": "สิ้นงวด", "begin": "ต้นงวด"},
    default=dict(initial=100_000, contrib=5_000, every="m", rate=5, years=20),
    put="เงินที่ลงไปทั้งหมด", interest="ดอกเบี้ยรวม",
    l_initial="เงินเริ่มต้น", l_contrib="เงินสมทบ", l_interest="ดอกเบี้ย",
    cmp_title="ทบต้นรายเดือน รายไตรมาส หรือรายปี?", cmp_note="จำนวนเงิน ดอกเบี้ย และระยะเวลาเท่ากัน แตะที่แถวเพื่อเลือก",
    cmp_cols=["ทบต้น", "มูลค่าสุดท้าย", "ดอกเบี้ยรวม"],
    chart_title="การเติบโตตามเวลา", chart_note="แต่ละแท่งคือยอดเงินสิ้นปี แตะที่แท่งเพื่อดูรายละเอียด",
    sched_title="รายละเอียดรายปี", sched_cols=["ปี", "สมทบ", "ดอกเบี้ย", "มูลค่าสิ้นปี"],
    sched_more="ดอกเบี้ยถูกบวกเข้าเมื่อสิ้นแต่ละรอบทบต้นและปัดเศษเป็นสตางค์ เหมือนในแอป Fincal",
    promo_title="มีหลายแผนการออม?",
    promo_lead="แอป Fincal เก็บแผนของคุณไว้ ใช้ได้แม้ไม่มีอินเทอร์เน็ต:",
    promo_items=[("บันทึกสถานการณ์", "ตั้งชื่อ เปิดใหม่ และทำสำเนาเพื่อเปรียบเทียบแผน"),
                 ("ประวัติอัตโนมัติ", "ทุกการคำนวณถูกเก็บไว้ให้กลับมาดูได้"),
                 ("แชร์เป็นรูปภาพ", "ส่งผลลัพธ์พร้อมกราฟให้ครอบครัวหรือคู่ของคุณ"),
                 ("คำนวณสินเชื่อด้วย", "ดอกเบี้ยหลายช่วงและการโปะหนี้พร้อมค่าธรรมเนียม")],
    ct="web-fincal-calc-compound-th",
    loan_link="คำนวณสินเชื่อ", compound_name="คำนวณดอกเบี้ยทบต้น",
    article="""
<h2>ดอกเบี้ยทบต้นคืออะไร</h2>
<p>ดอกเบี้ยทบต้นคือการนำดอกเบี้ยที่ได้รับไปรวมกับเงินต้น แล้วงวดถัดไปดอกเบี้ยนั้นก็ให้ดอกเบี้ยต่อ ยิ่งเก็บเงินไว้นาน เงินยิ่งโตเร็วขึ้น</p>
<div class="formula">FV = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: เงินต้น · PMT: เงินสมทบต่องวด · r: ดอกเบี้ยต่อปี · k: จำนวนรอบทบต้นต่อปี · t: จำนวนปี</div>
<p>สูตรนี้แม่นยำเมื่อคุณสมทบหนึ่งครั้งต่อรอบทบต้นตอนสิ้นงวด เครื่องคำนวณด้านบนจำลองทุกเดือน จึงใช้ได้แม้รอบสมทบกับรอบทบต้นต่างกัน</p>
<h2>ตัวอย่าง: เงินต้น 100,000 บาท ออมเพิ่มเดือนละ 5,000 บาท ดอกเบี้ย 5% นาน 20 ปี</h2>
<table class="cmp">
<thead><tr><th></th><th>จำนวนเงิน</th></tr></thead>
<tbody>
<tr><td>เงินที่ลงไปทั้งหมด</td><td>{put}</td></tr>
<tr><td>ดอกเบี้ย</td><td>{int}</td></tr>
<tr><td>มูลค่าสุดท้าย</td><td>{fv}</td></tr>
</tbody></table>
<p>ถ้าเริ่มเร็วขึ้น 10 ปีและออมต่อเนื่อง 30 ปี แผนเดียวกันจะได้ <b>{early}</b> โดยใส่เงินไปทั้งหมดเพียง {early_put}</p>
<h2>ความถี่ทบต้นมีผลมากไหม</h2>
<p>มีผลเล็กน้อย ด้วยตัวเลขเดียวกัน ทบต้นรายเดือนได้ {kf_m} รายไตรมาส {kf_q} และรายปี {kf_y} ระยะเวลาและอัตราดอกเบี้ยสำคัญกว่ามาก</p>
<h2>ฝากประจำ รับดอกเบี้ยรายเดือนหรือครบกำหนด?</h2>
<p>ดอกเบี้ยรายเดือนมักต่ำกว่าเล็กน้อย ถ้าไม่ต้องใช้เงิน การรับตอนครบกำหนดแล้วฝากต่อทั้งต้นและดอกมักได้มากกว่า <a href="/fincal/dokbia-rai-duean-rue-khrop-kamnot/">ดูตัวอย่างและอัตราคุ้มทุน →</a></p>
<h2>กฎ 72</h2>
<p>นำ 72 หารด้วยอัตราดอกเบี้ยต่อปี จะได้จำนวนปีโดยประมาณที่เงินเพิ่มเป็นสองเท่า ดอกเบี้ย 5% ใช้เวลาประมาณ 14 ปี ส่วน 8% ประมาณ 9 ปี</p>
""",
    faq=[
        ("ดอกเบี้ยเชิงเดียวกับดอกเบี้ยทบต้นต่างกันอย่างไร",
         "ดอกเบี้ยเชิงเดียวคิดจากเงินที่คุณฝากเท่านั้น ส่วนดอกเบี้ยทบต้นคิดจากดอกเบี้ยที่ได้รับแล้วด้วย ยอดเงินจึงโตเร็วขึ้นทุกปี"),
        ("เงินฝากประจำเป็นดอกเบี้ยทบต้นไหม",
         "ใช่ ถ้าฝากต่ออัตโนมัติพร้อมดอกเบี้ยเมื่อครบกำหนด รอบทบต้นเท่ากับระยะฝาก เช่น ฝากประจำ 3 เดือนให้เลือกทบต้นรายไตรมาส"),
        ("ดอกเบี้ยต่อปีถูกแบ่งต่องวดอย่างไร",
         "นำดอกเบี้ยต่อปีหารด้วยจำนวนรอบทบต้น เช่น 5% ต่อปีทบต้นรายเดือนคือ 5% ÷ 12 ต่อเดือน ซึ่งเป็นอัตราดอกเบี้ยที่ตราไว้ที่ธนาคารและเครื่องคำนวณส่วนใหญ่ใช้"),
        ("ใช้กับกองทุนหรือหุ้นได้ไหม",
         "ได้ในฐานะการประมาณการ ใส่ผลตอบแทนเฉลี่ยต่อปีที่คาดไว้ ผลตอบแทนจริงขึ้นลงทุกปี จึงควรมองผลลัพธ์เป็นการคาดการณ์ ไม่ใช่การรับประกัน"),
        ("ข้อมูลที่กรอกถูกส่งไปที่ไหนไหม",
         "ไม่ การคำนวณทั้งหมดทำในเบราว์เซอร์ของคุณ ตัวเลขจะอยู่แค่ในที่อยู่ของหน้าเพื่อให้คุณแชร์ผลลัพธ์ได้"),
    ],
)

C["pt-BR"] = dict(
    path="/fincal/calculadora-de-juros-compostos/", og="pt_BR",
    title="Calculadora de Juros Compostos - Com Aportes Mensais | Fincal",
    desc="Calculadora de juros compostos grátis: informe o valor inicial, o aporte mensal, a taxa e o prazo para ver o valor futuro, o total de juros, um gráfico de crescimento e a tabela ano a ano.",
    h1="Calculadora de juros compostos",
    intro="Veja quanto um valor inicial e aportes regulares crescem com juros compostos. Tudo roda no seu navegador - nada é salvo ou enviado.",
    crumb_page="Juros compostos",
    initial="Investimento inicial", contrib="Aporte periódico",
    every={"m": "por mês", "q": "por trimestre", "y": "por ano"},
    chips=[(1_000, "1 mil"), (10_000, "10 mil"), (50_000, "50 mil"), (100_000, "100 mil")],
    rate="Taxa de juros anual", rate_unit="% ao ano", years="Prazo", years_unit="anos",
    adv="Opções avançadas", kfreq="Frequência de capitalização", freq={"m": "Mensal", "q": "Trimestral", "y": "Anual"},
    timing="Momento do aporte", timings={"end": "Fim do período", "begin": "Início do período"},
    default=dict(initial=10_000, contrib=1_000, every="m", rate=10, years=20),
    put="Total investido", interest="Juros totais",
    l_initial="Inicial", l_contrib="Aportes", l_interest="Juros",
    cmp_title="Capitalização mensal, trimestral ou anual?", cmp_note="Mesmos valores, taxa e prazo. Toque em uma linha para usá-la.",
    cmp_cols=["Capitalização", "Valor final", "Juros totais"],
    chart_title="Crescimento ao longo do tempo", chart_note="Cada barra é o saldo no fim do ano. Toque em uma barra para ver os detalhes.",
    sched_title="Detalhamento anual", sched_cols=["Ano", "Aportado", "Juros", "Valor final"],
    sched_more="Os juros entram no fim de cada período de capitalização e são arredondados ao centavo, como no app Fincal.",
    promo_title="Tem mais de um objetivo?",
    promo_lead="O app Fincal guarda seus planos, mesmo sem internet:",
    promo_items=[("Cenários salvos", "dê um nome, abra de novo e duplique para comparar planos"),
                 ("Histórico automático", "cada cálculo fica guardado para você voltar depois"),
                 ("Compartilhe como imagem", "envie o resultado com os gráficos para a família ou o parceiro"),
                 ("Empréstimos também", "taxas que mudam com o tempo e amortizações extras com multa")],
    ct="web-fincal-calc-compound-pt",
    loan_link="Calculadora de empréstimo", compound_name="Calculadora de juros compostos",
    article="""
<h2>O que são juros compostos?</h2>
<p>Nos juros compostos, os juros que você ganha são somados ao saldo e passam a render juros também - os famosos "juros sobre juros". Quanto mais tempo o dinheiro fica investido, mais rápido ele cresce.</p>
<div class="formula">VF = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: valor inicial · PMT: aporte por período · r: taxa anual · k: períodos de capitalização por ano · t: anos</div>
<p>A fórmula é exata quando há um aporte por período de capitalização, no fim do período. A calculadora acima simula mês a mês, então os aportes e a capitalização podem ter frequências diferentes.</p>
<h2>Exemplo: R$ 10.000 mais R$ 1.000 por mês a 10% ao ano por 20 anos</h2>
<table class="cmp">
<thead><tr><th></th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Total investido</td><td>{put}</td></tr>
<tr><td>Juros</td><td>{int}</td></tr>
<tr><td>Valor final</td><td>{fv}</td></tr>
</tbody></table>
<p>Começando 10 anos antes e mantendo por 30 anos, o mesmo plano chega a <b>{early}</b>, com apenas {early_put} investidos no total.</p>
<h2>A frequência de capitalização faz diferença?</h2>
<p>Um pouco. Com os mesmos números, a capitalização mensal dá {kf_m}, a trimestral {kf_q} e a anual {kf_y}. O prazo e a taxa pesam muito mais.</p>
<h2>Taxa nominal ou efetiva?</h2>
<p>A calculadora usa a taxa nominal: 10% ao ano capitalizados mensalmente são 10% ÷ 12 ao mês. Se o seu investimento informa uma taxa efetiva anual (como o CDI), a taxa mensal equivalente é um pouco menor, então o resultado real fica um pouco abaixo. Com uma taxa efetiva, escolha capitalização anual para chegar mais perto do resultado real.</p>
<h2>Juros mensais ou no vencimento?</h2>
<p>A versão com juros mensais costuma ter taxa um pouco menor. O resultado depende de onde você reinveste os juros e, em aplicações tributadas, do Imposto de Renda. <a href="/fincal/juros-mensais-ou-no-vencimento/">Veja o exemplo e a taxa de empate →</a></p>
<h2>A regra dos 72</h2>
<p>Divida 72 pela taxa anual para estimar em quantos anos o dinheiro dobra. A 10% ao ano, cerca de 7 anos; a 6%, cerca de 12 anos.</p>
""",
    faq=[
        ("Qual a diferença entre juros simples e compostos?",
         "Nos juros simples, os juros incidem só sobre o valor investido. Nos compostos, incidem também sobre os juros já recebidos, então o saldo cresce mais rápido a cada ano."),
        ("Posso usar para CDB, Tesouro Direto ou poupança?",
         "Sim, como estimativa: informe a rentabilidade anual esperada. A calculadora não desconta Imposto de Renda nem taxas, então o valor líquido será menor."),
        ("O que muda entre aporte no início ou no fim do período?",
         "O aporte feito no início do período já rende juros naquele período, então o resultado fica um pouco maior que com aportes no fim."),
        ("Os juros são calculados como no banco?",
         "A calculadora soma os juros no fim de cada período de capitalização e arredonda ao centavo, igual ao app Fincal. Investimentos que rendem por dia útil podem ter pequenas diferenças."),
        ("O que eu digito é enviado para algum lugar?",
         "Não. Todo cálculo roda no seu navegador. Os números só aparecem no endereço da página para você compartilhar o resultado."),
    ],
)

C["ms"] = dict(
    path="/fincal/kalkulator-faedah-kompaun/", og="ms_MY",
    title="Kalkulator Faedah Kompaun - Simpanan Bulanan | Fincal",
    desc="Kalkulator faedah kompaun percuma: masukkan jumlah permulaan, sumbangan bulanan, kadar dan tempoh untuk melihat nilai masa hadapan, jumlah faedah, carta pertumbuhan dan pecahan tahunan.",
    h1="Kalkulator faedah kompaun",
    intro="Lihat berapa banyak jumlah permulaan dan sumbangan tetap anda berkembang dengan faedah kompaun. Semua dikira dalam pelayar anda - tiada data disimpan atau dihantar.",
    crumb_page="Faedah kompaun",
    initial="Pelaburan permulaan", contrib="Sumbangan berkala",
    every={"m": "sebulan", "q": "setiap suku tahun", "y": "setahun"},
    chips=[(1_000, "1K"), (10_000, "10K"), (50_000, "50K"), (100_000, "100K")],
    rate="Kadar faedah tahunan", rate_unit="% setahun", years="Tempoh", years_unit="tahun",
    adv="Pilihan lanjutan", kfreq="Kekerapan kompaun", freq={"m": "Bulanan", "q": "Suku tahunan", "y": "Tahunan"},
    timing="Masa sumbangan", timings={"end": "Akhir tempoh", "begin": "Awal tempoh"},
    default=dict(initial=10_000, contrib=500, every="m", rate=5.5, years=20),
    put="Jumlah dilaburkan", interest="Jumlah faedah",
    l_initial="Permulaan", l_contrib="Sumbangan", l_interest="Faedah",
    cmp_title="Kompaun bulanan, suku tahunan atau tahunan?", cmp_note="Jumlah, kadar dan tempoh yang sama. Ketik satu baris untuk memilihnya.",
    cmp_cols=["Kompaun", "Nilai akhir", "Jumlah faedah"],
    chart_title="Pertumbuhan dari masa ke masa", chart_note="Setiap bar ialah baki pada akhir tahun. Ketik bar untuk melihat butiran.",
    sched_title="Pecahan tahunan", sched_cols=["Tahun", "Disumbang", "Faedah", "Nilai akhir"],
    sched_more="Faedah ditambah pada akhir setiap tempoh kompaun dan dibundarkan kepada sen, sama seperti aplikasi Fincal.",
    promo_title="Ada lebih daripada satu matlamat?",
    promo_lead="Aplikasi Fincal menyimpan rancangan anda, walaupun tanpa internet:",
    promo_items=[("Senario disimpan", "beri nama, buka semula dan salin untuk membandingkan rancangan"),
                 ("Sejarah automatik", "setiap pengiraan disimpan supaya anda boleh kembali kepadanya"),
                 ("Kongsi sebagai imej", "hantar keputusan berserta carta kepada keluarga atau pasangan"),
                 ("Pinjaman juga", "kadar yang berubah mengikut masa dan bayaran awal dengan penalti")],
    ct="web-fincal-calc-compound-ms",
    loan_link="Kalkulator pinjaman", compound_name="Kalkulator faedah kompaun",
    article="""
<h2>Apakah faedah kompaun?</h2>
<p>Dengan faedah kompaun, faedah yang anda peroleh ditambah ke baki dan turut menjana faedah pada tempoh seterusnya. Semakin lama wang dilaburkan, semakin cepat ia berkembang.</p>
<div class="formula">FV = P × (1 + r/k)<sup>k×t</sup> + PMT × ((1 + r/k)<sup>k×t</sup> − 1) ÷ (r/k)<br>P: jumlah permulaan · PMT: sumbangan setiap tempoh · r: kadar tahunan · k: bilangan tempoh kompaun setahun · t: tahun</div>
<p>Formula ini tepat apabila anda menyumbang sekali bagi setiap tempoh kompaun, pada akhir tempoh. Kalkulator di atas menyimulasikan setiap bulan, jadi kekerapan sumbangan dan kompaun boleh berbeza.</p>
<h2>Contoh: RM 10,000 ditambah RM 500 sebulan pada 5.5% selama 20 tahun</h2>
<table class="cmp">
<thead><tr><th></th><th>Jumlah</th></tr></thead>
<tbody>
<tr><td>Jumlah dilaburkan</td><td>{put}</td></tr>
<tr><td>Faedah</td><td>{int}</td></tr>
<tr><td>Nilai akhir</td><td>{fv}</td></tr>
</tbody></table>
<p>Jika bermula 10 tahun lebih awal dan diteruskan selama 30 tahun, rancangan yang sama mencecah <b>{early}</b>, sedangkan jumlah dilaburkan hanya {early_put}.</p>
<h2>Adakah kekerapan kompaun penting?</h2>
<p>Sedikit sahaja. Dengan angka yang sama, kompaun bulanan memberi {kf_m}, suku tahunan {kf_q} dan tahunan {kf_y}. Tempoh dan kadar jauh lebih penting.</p>
<h2>Simpanan tetap: faedah bulanan atau semasa matang?</h2>
<p>Faedah bulanan biasanya datang dengan kadar sedikit lebih rendah, jadi jika anda tidak perlukan pendapatan itu, faedah semasa matang yang diperbaharui bersama pokok cenderung lebih untung. <a href="/fincal/faedah-bulanan-atau-matang/">Lihat contoh dan kadar seri →</a></p>
<h2>Peraturan 72</h2>
<p>Bahagikan 72 dengan kadar tahunan untuk menganggar berapa tahun wang anda berganda. Pada 5.5% kira-kira 13 tahun; pada 8% kira-kira 9 tahun.</p>
""",
    faq=[
        ("Apakah beza faedah mudah dan faedah kompaun?",
         "Faedah mudah hanya dikira atas wang yang anda masukkan. Faedah kompaun juga dikira atas faedah yang telah diterima, jadi baki berkembang lebih cepat setiap tahun."),
        ("Boleh guna untuk KWSP, ASB atau simpanan tetap?",
         "Boleh sebagai anggaran: masukkan kadar dividen atau faedah tahunan yang dijangka dan pilih kompaun tahunan untuk dividen yang dikreditkan setahun sekali. Kadar sebenar berubah setiap tahun."),
        ("Bagaimana kadar tahunan dibahagikan setiap tempoh?",
         "Kadar tahunan dibahagi dengan bilangan tempoh kompaun: 5.5% setahun dikompaun bulanan ialah 5.5% ÷ 12 sebulan. Ini kadar nominal yang digunakan bank dan kebanyakan kalkulator."),
        ("Apa bezanya sumbangan di awal atau akhir tempoh?",
         "Sumbangan di awal tempoh terus menjana faedah untuk tempoh itu, jadi hasilnya sedikit lebih tinggi berbanding sumbangan di akhir tempoh."),
        ("Adakah data yang saya masukkan dihantar ke mana-mana?",
         "Tidak. Semua pengiraan berjalan dalam pelayar anda. Angka hanya muncul pada alamat halaman supaya anda boleh berkongsi keputusan."),
    ],
)
