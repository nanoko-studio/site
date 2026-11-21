"""Savings example per language for the compound pages (one deposit, no contributions).
Placeholders: {sv_fv} {sv_int} {sv_simple} {sv_link}."""

SAV = {}

SAV["en"] = dict(initial=10_000, rate=4.5, years=5, kf="m", html="""
<h2>Savings example: 10,000 in a savings account for 5 years</h2>
<p>A deposit of 10,000 at 4.5% a year, compounded monthly and left untouched, grows to <b>{sv_fv}</b> in 5 years, of which {sv_int} is interest. If you withdrew the interest every month instead, you would earn only {sv_simple}. The difference is what compounding adds.</p>
<p><a href="{sv_link}">Open this example in the calculator</a>, then enter your own bank's rate. For a certificate of deposit that renews every year, set compounding to yearly. The rate here is only an illustration.</p>
""", faq=("Does a savings account earn compound interest?",
          "Yes, as long as you leave the interest in the account. Set the contribution to 0 and pick the compounding your bank uses: monthly for most savings accounts, or the term length for a certificate of deposit that renews with its interest."),
    desc="Free compound interest calculator for savings and investments: enter a starting amount, monthly contributions, rate and years to see the future value, total interest, a growth chart and a year-by-year table.")

SAV["vi"] = dict(initial=100_000_000, rate=6, years=5, kf="y", html="""
<h2>Gửi tiết kiệm 100 triệu, lãi 6%/năm trong 5 năm được bao nhiêu?</h2>
<p>Gửi 100 triệu kỳ hạn 12 tháng, lãi 6%/năm, đến hạn tái tục cả gốc lẫn lãi thì sau 5 năm bạn có <b>{sv_fv}</b>, trong đó tiền lãi là {sv_int}. Nếu năm nào cũng rút lãi ra thì tổng tiền lãi chỉ là {sv_simple}. Phần chênh lệch chính là nhờ lãi kép.</p>
<p><a href="{sv_link}">Mở ví dụ này trong máy tính</a> rồi nhập lãi suất thực tế của ngân hàng bạn. Gửi kỳ hạn 3 tháng thì chọn gộp lãi theo quý, kỳ hạn 1 tháng thì chọn theo tháng. Lãi suất trong ví dụ chỉ để minh hoạ.</p>
""", title="Tính lãi kép, lãi gửi tiết kiệm online - Góp hằng tháng | Fincal",
    desc="Máy tính lãi kép miễn phí cho gửi tiết kiệm và đầu tư: nhập vốn ban đầu, số tiền góp hằng tháng, lãi suất và số năm để xem giá trị tương lai, tổng lãi, biểu đồ tăng trưởng và bảng chi tiết từng năm.")

SAV["id"] = dict(initial=100_000_000, rate=5, years=5, kf="q", html="""
<h2>Deposito Rp 100 juta selama 5 tahun dapat berapa?</h2>
<p>Deposito Rp 100 juta bertenor 3 bulan dengan bunga 5% per tahun, diperpanjang otomatis bersama bunganya (ARO pokok + bunga), menjadi <b>{sv_fv}</b> setelah 5 tahun, dengan bunga {sv_int}. Jika bunganya diambil setiap jatuh tempo, total bunganya hanya {sv_simple}. Selisihnya adalah hasil bunga majemuk.</p>
<p><a href="{sv_link}">Buka contoh ini di kalkulator</a>, lalu masukkan bunga bank Anda. Untuk tenor 12 bulan pilih penggabungan tahunan, untuk tenor 1 bulan pilih bulanan. Angka di atas sebelum pajak bunga deposito (umumnya 20%) dan sukunya hanya ilustrasi.</p>
""", title="Kalkulator Bunga Majemuk & Deposito - Simulasi Investasi Bulanan | Fincal",
    desc="Kalkulator bunga majemuk gratis untuk deposito, tabungan dan investasi: masukkan modal awal, setoran bulanan, suku bunga dan jangka waktu untuk melihat nilai masa depan, total bunga, grafik dan rincian per tahun.")

SAV["th"] = dict(initial=100_000, rate=2.5, years=5, kf="y", html="""
<h2>ฝากประจำ 100,000 บาท 5 ปี ได้ดอกเบี้ยเท่าไร</h2>
<p>ฝากประจำ 12 เดือน 100,000 บาท ดอกเบี้ย 2.5% ต่อปี และฝากต่ออัตโนมัติทั้งเงินต้นและดอกเบี้ย เมื่อครบ 5 ปีจะมี <b>{sv_fv}</b> เป็นดอกเบี้ย {sv_int} ถ้าถอนดอกเบี้ยออกทุกปี จะได้ดอกเบี้ยรวมเพียง {sv_simple} ส่วนต่างนี้คือผลของดอกเบี้ยทบต้น</p>
<p><a href="{sv_link}">เปิดตัวอย่างนี้ในเครื่องคำนวณ</a> แล้วใส่อัตราดอกเบี้ยจริงของธนาคารคุณ ฝากประจำ 3 เดือนให้เลือกทบต้นรายไตรมาส ตัวเลขข้างต้นเป็นก่อนหักภาษี และอัตราดอกเบี้ยเป็นเพียงตัวอย่าง</p>
""", desc="เครื่องคำนวณดอกเบี้ยทบต้นฟรี สำหรับเงินฝากและการลงทุน: ใส่เงินต้น เงินออมรายเดือน อัตราดอกเบี้ย และจำนวนปี เพื่อดูมูลค่าในอนาคต ดอกเบี้ยรวม กราฟการเติบโต และรายละเอียดรายปี")

SAV["pt-BR"] = dict(initial=10_000, rate=12, years=5, kf="m", html="""
<h2>Quanto rendem R$ 10.000 em 5 anos?</h2>
<p>R$ 10.000 aplicados a 12% ao ano, com os juros reinvestidos todo mês, chegam a <b>{sv_fv}</b> em 5 anos, dos quais {sv_int} são juros. Se você sacasse os juros todo mês, receberia só {sv_simple}. A diferença é o efeito dos juros compostos.</p>
<p><a href="{sv_link}">Abra este exemplo na calculadora</a> e informe a taxa do seu investimento. Os valores são antes do Imposto de Renda e a taxa é apenas ilustrativa.</p>
""", desc="Calculadora de juros compostos grátis para investimentos e poupança: informe o valor inicial, o aporte mensal, a taxa e o prazo para ver o valor futuro, o total de juros, um gráfico de crescimento e a tabela ano a ano.")

SAV["ms"] = dict(initial=10_000, rate=3.5, years=5, kf="y", html="""
<h2>Simpanan tetap RM 10,000 selama 5 tahun dapat berapa?</h2>
<p>Simpanan tetap RM 10,000 bagi tempoh 12 bulan pada 3.5% setahun, diperbaharui secara automatik bersama faedahnya, menjadi <b>{sv_fv}</b> selepas 5 tahun, dengan faedah {sv_int}. Jika faedah dikeluarkan setiap tahun, jumlah faedah hanya {sv_simple}. Perbezaannya ialah hasil faedah kompaun.</p>
<p><a href="{sv_link}">Buka contoh ini dalam kalkulator</a>, kemudian masukkan kadar bank anda. Untuk tempoh 3 bulan pilih kompaun suku tahunan. Kadar di atas hanya sebagai contoh.</p>
""", desc="Kalkulator faedah kompaun percuma untuk simpanan tetap dan pelaburan: masukkan jumlah permulaan, sumbangan bulanan, kadar dan tempoh untuk melihat nilai masa hadapan, jumlah faedah, carta pertumbuhan dan pecahan tahunan.")
