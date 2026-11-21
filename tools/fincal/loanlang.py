"""Content for the id, th, pt-BR and ms loan calculator pages. Terms follow the Fincal app's own translations."""

LANGS = {}

LANGS["id"] = dict(
    path="/fincal/simulasi-kredit/", og="id_ID", faq_h="Pertanyaan umum", name="Bahasa Indonesia", short="ID",
    title="Simulasi Kredit dan Kalkulator Bunga Pinjaman - Cicilan per Bulan | Fincal",
    desc="Kalkulator pinjaman gratis: masukkan jumlah pinjaman, suku bunga dan tenor untuk melihat cicilan per bulan, total bunga, grafik dan tabel angsuran. Bandingkan anuitas, pokok tetap dan bunga flat.",
    h1="Simulasi kredit dan kalkulator bunga pinjaman",
    intro="Masukkan jumlah pinjaman, suku bunga dan tenor untuk mengetahui cicilan per bulan, total bunga dan tabel angsuran. Semua dihitung di browser Anda - tidak ada data yang disimpan atau dikirim.",
    crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="Simulasi kredit",
    amount="Jumlah pinjaman", currency="Rp", cur_pre=True, sep=".", comma=True,
    chips=[(50_000_000, "50 jt"), (100_000_000, "100 jt"), (500_000_000, "500 jt"), (1_000_000_000, "1 M")],
    rate="Suku bunga", rate_unit="% per tahun", term="Tenor", years="tahun", months="bulan",
    method="Metode perhitungan",
    methods=[("annuity", "Anuitas (cicilan tetap)", "Cicilan sama setiap bulan, bunga dari sisa pinjaman. Umum untuk KPR dan kredit bank."),
             ("flat", "Bunga flat", "Bunga selalu dihitung dari pokok awal. Umum untuk KTA, kredit motor dan mobil."),
             ("equal", "Pokok tetap (bunga efektif)", "Pokok dibayar sama rata, bunga dari sisa pinjaman. Cicilan pertama paling besar.")],
    default=dict(amount=500_000_000, rate=11, term=15, unit="y", method="annuity"),
    interest="Total bunga", lbl_i="Bunga", total="Total yang dibayar", principal="Pokok",
    cmp_title="Bandingkan 3 metode", cmp_note="Jumlah, bunga dan tenor sama. Ketuk satu baris untuk melihat detailnya.",
    cmp_method="Metode", cmp_first="Cicilan pertama", cmp_interest="Total bunga",
    cmp_names={"annuity": "Anuitas", "equal": "Pokok tetap", "flat": "Bunga flat"},
    chart_title="Pokok dan bunga dari waktu ke waktu", chart_note="Setiap batang adalah jumlah yang dibayar dalam setahun (atau sebulan, untuk pinjaman pendek). Ketuk batang untuk melihat detail.",
    sched_title="Tabel angsuran", sched_cols=["Pokok", "Bunga", "Total bayar", "Sisa pinjaman"],
    sched_more="Tahun pertama dirinci per bulan. Tabel angsuran per bulan untuk semua tahun tersedia di aplikasi Fincal.",
    promo_title="Pinjaman Anda lebih rumit?",
    promo_lead="Aplikasi Fincal menghitung yang benar-benar diterapkan bank:",
    promo_items=[("Suku bunga berjenjang", "bunga promo di bulan-bulan awal, lalu bunga baru, berapa pun periodenya"),
                 ("Pelunasan dipercepat", "sekali atau berkala, termasuk biaya penalti; lihat bunga yang dihemat dan bulan yang dipersingkat"),
                 ("Skenario tersimpan", "beri nama, buka lagi dan duplikat untuk mencoba opsi lain; riwayat tersimpan otomatis"),
                 ("Tabel angsuran bulanan", "untuk semua tahun, dan bagikan hasil beserta grafik sebagai gambar")],
    get_on="TERSEDIA DI", dl_on="DOWNLOAD DI", ct="web-fincal-calc-loan-id",
    footer_privacy="Kebijakan Privasi", footer_support="Dukungan",
    article="""
<h2>Cara menghitung cicilan anuitas</h2>
<p>Hampir semua KPR dan kredit bank memakai metode anuitas: cicilan setiap bulan sama besar, tetapi di awal sebagian besar cicilan adalah bunga, lalu porsi pokok makin besar seiring waktu.</p>
<div class="formula">Cicilan per bulan = P × r ÷ (1 − (1 + r)<sup>−n</sup>)<br>P: jumlah pinjaman · r: bunga per tahun ÷ 12 · n: jumlah bulan</div>
<h2>Bunga flat vs bunga efektif</h2>
<p>Dengan bunga flat, bunga selalu dihitung dari jumlah pinjaman awal walaupun pokok sudah dicicil. Karena itu angka bunga flat terlihat kecil padahal biayanya jauh lebih tinggi. Contoh: pinjaman Rp 50 juta selama 24 bulan dengan bunga flat 12% per tahun, total bunganya Rp 12 juta - setara bunga efektif sekitar <b>21,57%</b> per tahun. Kalkulator di atas menampilkan angka setara ini saat Anda memilih bunga flat. <a href="/fincal/bunga-flat-vs-bunga-efektif/">Baca penjelasan lengkap dan tabel konversinya →</a></p>
<div class="formula">Bunga per bulan = Pokok awal × Bunga per tahun ÷ 12<br>Cicilan = Pokok awal ÷ Tenor + Bunga per bulan</div>
<h2>Pokok tetap (bunga efektif)</h2>
<p>Pokok dibagi rata setiap bulan dan bunga hanya dihitung dari sisa pinjaman, jadi cicilan terbesar ada di bulan pertama lalu terus turun. Total bunganya paling kecil di antara ketiga metode.</p>
<h2>Contoh: KPR Rp 500 juta, bunga 11% per tahun, tenor 15 tahun</h2>
<table class="cmp">
<thead><tr><th>Metode</th><th>Cicilan pertama</th><th>Total bunga</th></tr></thead>
<tbody>
<tr><td>Anuitas</td><td>Rp 5.682.985</td><td>Rp 522.937.145</td></tr>
<tr><td>Pokok tetap</td><td>Rp 7.361.111</td><td>Rp 414.791.633</td></tr>
<tr><td>Bunga flat</td><td>Rp 7.361.111</td><td>Rp 824.999.940</td></tr>
</tbody></table>
<p>Anuitas lebih ringan sekitar Rp 1,7 juta per bulan di awal, tetapi total bunganya sekitar Rp 108 juta lebih besar dibanding pokok tetap.</p>
<h2>Apakah pelunasan dipercepat menguntungkan?</h2>
<p>Melunasi sebagian pinjaman mengurangi bunga, tetapi biasanya ada penalti 1-3%, dan bank akan bertanya mau mengurangi tenor atau cicilan. <a href="/fincal/pelunasan-dipercepat/">Lihat contoh dan hitung apakah penaltinya sepadan →</a></p>
""",
    faq=[
        ("Apa bedanya bunga flat, bunga efektif dan anuitas?",
         "Bunga flat dihitung dari pokok awal sepanjang tenor. Bunga efektif dihitung dari sisa pinjaman, sehingga lebih murah pada angka bunga yang sama. Anuitas juga memakai sisa pinjaman, tetapi cicilannya dibuat sama setiap bulan, jadi total bunganya sedikit lebih besar daripada pokok tetap."),
        ("Bunga 1% per bulan berapa per tahun?",
         "1% per bulan sama dengan 12% per tahun. Jika itu bunga flat, bunga efektifnya jauh lebih tinggi, sekitar 21-22% per tahun untuk pinjaman 2 tahun. Pilih \"Bunga flat\" di atas untuk melihat angka pastinya."),
        ("Apakah hasilnya sama dengan perhitungan bank?",
         "Kalkulator menghitung bunga per bulan (bunga tahunan ÷ 12) dan membulatkan ke rupiah setiap bulan, sama seperti aplikasi Fincal. Bank yang menghitung bunga berdasarkan jumlah hari bisa sedikit berbeda."),
        ("Bagaimana dengan bunga floating atau pelunasan dipercepat?",
         "Halaman ini memakai satu suku bunga tetap. Untuk bunga promo di awal lalu bunga floating, atau pelunasan dipercepat dengan penalti, gunakan aplikasi Fincal gratis di Android dan iOS."),
        ("Apakah data yang saya masukkan dikirim ke mana pun?",
         "Tidak. Semua perhitungan berjalan di browser Anda. Angka hanya muncul di alamat halaman agar hasilnya bisa dibagikan."),
    ],
)

LANGS["th"] = dict(
    path="/fincal/khamnuan-sinchuea/", og="th_TH", faq_h="คำถามที่พบบ่อย", name="ไทย", short="TH",
    title="คำนวณสินเชื่อ ค่างวดและดอกเบี้ยต่อเดือน พร้อมตารางผ่อนชำระ | Fincal",
    desc="เครื่องคำนวณสินเชื่อฟรี ใส่วงเงินกู้ อัตราดอกเบี้ย และระยะเวลา เพื่อดูค่างวดต่อเดือน ดอกเบี้ยรวม กราฟ และตารางผ่อนชำระ เปรียบเทียบงวดเท่ากัน เงินต้นเท่ากัน และดอกเบี้ยคงที่ (flat rate)",
    h1="คำนวณสินเชื่อและค่างวดต่อเดือน",
    intro="ใส่วงเงินกู้ อัตราดอกเบี้ย และระยะเวลากู้ เพื่อดูว่าต้องผ่อนเดือนละเท่าไร ดอกเบี้ยรวมเท่าไร พร้อมตารางผ่อนชำระ คำนวณบนเบราว์เซอร์ของคุณทั้งหมด ไม่มีการบันทึกหรือส่งข้อมูลไปที่ใด",
    crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="คำนวณสินเชื่อ",
    amount="วงเงินกู้", currency="฿", cur_pre=False, sep=",", comma=False,
    chips=[(500_000, "5 แสน"), (1_000_000, "1 ล้าน"), (3_000_000, "3 ล้าน"), (5_000_000, "5 ล้าน")],
    rate="อัตราดอกเบี้ย", rate_unit="% ต่อปี", term="ระยะเวลากู้", years="ปี", months="เดือน",
    method="วิธีคิดดอกเบี้ย",
    methods=[("annuity", "งวดเท่ากัน (ลดต้นลดดอก)", "ผ่อนเท่ากันทุกเดือน ดอกเบี้ยคิดจากเงินต้นคงเหลือ ใช้กับสินเชื่อบ้านเกือบทั้งหมด"),
             ("flat", "ดอกเบี้ยคงที่ (flat rate)", "ดอกเบี้ยคิดจากเงินต้นตั้งต้นตลอดสัญญา พบบ่อยในสินเชื่อรถยนต์และเงินกู้ส่วนบุคคล"),
             ("equal", "เงินต้นเท่ากัน", "ตัดเงินต้นเท่ากันทุกเดือน ดอกเบี้ยคิดจากยอดคงเหลือ งวดแรกสูงที่สุด")],
    default=dict(amount=3_000_000, rate=6.5, term=30, unit="y", method="annuity"),
    interest="ดอกเบี้ยรวม", lbl_i="ดอกเบี้ย", total="ยอดชำระรวม", principal="เงินต้น",
    cmp_title="เปรียบเทียบ 3 วิธี", cmp_note="วงเงิน ดอกเบี้ย และระยะเวลาเท่ากัน แตะที่แถวเพื่อดูรายละเอียด",
    cmp_method="วิธี", cmp_first="งวดแรก", cmp_interest="ดอกเบี้ยรวม",
    cmp_names={"annuity": "งวดเท่ากัน", "equal": "เงินต้นเท่ากัน", "flat": "ดอกเบี้ยคงที่"},
    chart_title="เงินต้นและดอกเบี้ยตามระยะเวลา", chart_note="แต่ละแท่งคือยอดที่จ่ายในหนึ่งปี (หรือหนึ่งเดือนสำหรับเงินกู้ระยะสั้น) แตะที่แท่งเพื่อดูรายละเอียด",
    sched_title="ตารางผ่อนชำระ", sched_cols=["เงินต้น", "ดอกเบี้ย", "ค่างวด", "ยอดคงเหลือ"],
    sched_more="ปีแรกแสดงรายเดือน ตารางผ่อนชำระรายเดือนของทุกปีมีในแอป Fincal",
    promo_title="สินเชื่อของคุณซับซ้อนกว่านี้?",
    promo_lead="แอป Fincal คำนวณสิ่งที่ธนาคารใช้จริงได้:",
    promo_items=[("อัตราดอกเบี้ยหลายช่วง", "ดอกเบี้ยโปรโมชันช่วงแรก แล้วเปลี่ยนเป็นอัตราใหม่ กี่ช่วงก็ได้"),
                 ("ชำระก่อนกำหนด (โปะ)", "ครั้งเดียวหรือเป็นประจำ รวมค่าธรรมเนียม ดูดอกเบี้ยที่ประหยัดได้และจำนวนเดือนที่ลดลง"),
                 ("บันทึกสถานการณ์", "ตั้งชื่อ เปิดใหม่ และทำสำเนาเพื่อลองทางเลือกอื่น ประวัติการคำนวณบันทึกอัตโนมัติ"),
                 ("ตารางผ่อนรายเดือน", "ครบทุกปี และแชร์ผลลัพธ์พร้อมกราฟเป็นรูปภาพ")],
    get_on="ดาวน์โหลดจาก", dl_on="ดาวน์โหลดจาก", ct="web-fincal-calc-loan-th",
    footer_privacy="นโยบายความเป็นส่วนตัว", footer_support="ช่วยเหลือ",
    article="""
<h2>วิธีคำนวณค่างวดแบบงวดเท่ากัน (ลดต้นลดดอก)</h2>
<p>สินเชื่อบ้านเกือบทั้งหมดผ่อนแบบงวดเท่ากัน โดยดอกเบี้ยคิดจากเงินต้นคงเหลือ (ลดต้นลดดอก) ช่วงแรกค่างวดส่วนใหญ่เป็นดอกเบี้ย แล้วส่วนที่ตัดเงินต้นจะมากขึ้นเรื่อย ๆ</p>
<div class="formula">ค่างวดต่อเดือน = P × r ÷ (1 − (1 + r)<sup>−n</sup>)<br>P: วงเงินกู้ · r: ดอกเบี้ยต่อปี ÷ 12 · n: จำนวนเดือน</div>
<h2>ดอกเบี้ยคงที่ (flat rate) แพงกว่าที่เห็น</h2>
<p>แบบ flat rate ดอกเบี้ยคิดจากเงินต้นตั้งต้นตลอดสัญญา แม้จะผ่อนเงินต้นไปแล้วบางส่วน ตัวอย่างเช่น สินเชื่อรถยนต์ 500,000 บาท ผ่อน 5 ปี ดอกเบี้ย flat 3% ต่อปี มีดอกเบี้ยรวม 75,000 บาท เทียบเท่าดอกเบี้ยแบบลดต้นลดดอกประมาณ <b>5.64%</b> ต่อปี เครื่องคำนวณด้านบนจะแสดงอัตรานี้เมื่อเลือกดอกเบี้ยคงที่ <a href="/fincal/flat-rate-kap-lot-ton-lot-dok/">อ่านคำอธิบายเต็มและตารางแปลงอัตรา →</a></p>
<div class="formula">ดอกเบี้ยต่อเดือน = เงินต้นตั้งต้น × ดอกเบี้ยต่อปี ÷ 12<br>ค่างวด = เงินต้นตั้งต้น ÷ จำนวนงวด + ดอกเบี้ยต่อเดือน</div>
<h2>ตัวอย่าง: กู้ซื้อบ้าน 3 ล้านบาท ดอกเบี้ย 6.5% ต่อปี 30 ปี</h2>
<table class="cmp">
<thead><tr><th>วิธี</th><th>งวดแรก</th><th>ดอกเบี้ยรวม</th></tr></thead>
<tbody>
<tr><td>งวดเท่ากัน</td><td>18,962.04 ฿</td><td>3,826,335.14 ฿</td></tr>
<tr><td>เงินต้นเท่ากัน</td><td>24,583.33 ฿</td><td>2,933,126.18 ฿</td></tr>
<tr><td>ดอกเบี้ยคงที่</td><td>24,583.33 ฿</td><td>5,850,000.00 ฿</td></tr>
</tbody></table>
<p>แบบงวดเท่ากันผ่อนเบากว่าในช่วงแรกประมาณ 5,600 บาทต่อเดือน แต่ดอกเบี้ยรวมสูงกว่าแบบเงินต้นเท่ากันประมาณ 890,000 บาท</p>
<h2>โปะหนี้ก่อนกำหนดคุ้มไหม</h2>
<p>การโปะช่วยลดดอกเบี้ย แต่บางสัญญามีค่าธรรมเนียม และธนาคารจะถามว่าจะลดระยะเวลาหรือลดค่างวด <a href="/fincal/poppit-ni-kon-kamnot/">ดูตัวอย่างและคำนวณว่าค่าธรรมเนียมคุ้มไหม →</a></p>
""",
    faq=[
        ("ดอกเบี้ย flat rate กับลดต้นลดดอกต่างกันอย่างไร",
         "flat rate คิดดอกเบี้ยจากเงินต้นตั้งต้นตลอดสัญญา ส่วนลดต้นลดดอกคิดจากยอดคงเหลือที่ลดลงทุกเดือน ที่ตัวเลขดอกเบี้ยเท่ากัน flat rate จึงแพงกว่ามาก เลือก \"ดอกเบี้ยคงที่\" ด้านบนเพื่อดูอัตราเทียบเท่า"),
        ("ผ่อนแบบงวดเท่ากันหรือเงินต้นเท่ากันดีกว่า",
         "เงินต้นเท่ากันเสียดอกเบี้ยรวมน้อยกว่า แต่งวดแรก ๆ สูง ส่วนงวดเท่ากันวางแผนง่ายและเริ่มต้นเบากว่า ถ้ารายได้พอจ่ายงวดแรกได้ แบบเงินต้นเท่ากันมักประหยัดกว่า"),
        ("ผลลัพธ์ตรงกับธนาคารไหม",
         "เครื่องคำนวณคิดดอกเบี้ยรายเดือน (ดอกเบี้ยต่อปี ÷ 12) และปัดเศษทุกงวดเหมือนแอป Fincal ธนาคารที่คิดดอกเบี้ยตามจำนวนวันจริงอาจต่างเล็กน้อย และค่างวดที่ธนาคารกำหนดมักปัดขึ้นเป็นหลักร้อย"),
        ("ดอกเบี้ยโปรโมชันหรือการโปะบ้านคำนวณอย่างไร",
         "หน้านี้ใช้อัตราดอกเบี้ยเดียวตลอดสัญญา ถ้าต้องการคำนวณดอกเบี้ยโปรโมชันช่วงแรกแล้วเปลี่ยนเป็นอัตราลอยตัว หรือการโปะพร้อมค่าธรรมเนียม ใช้แอป Fincal ฟรีบน Android และ iOS"),
        ("ข้อมูลที่กรอกถูกส่งไปที่ไหนหรือไม่",
         "ไม่ การคำนวณทั้งหมดทำงานบนเบราว์เซอร์ของคุณ ตัวเลขจะอยู่ในที่อยู่ของหน้าเท่านั้น เพื่อให้คุณแชร์ผลลัพธ์ได้"),
    ],
)

LANGS["pt-BR"] = dict(
    path="/fincal/calculadora-de-emprestimo/", og="pt_BR", faq_h="Perguntas frequentes", name="Português (Brasil)", short="PT",
    title="Calculadora de Empréstimo e Financiamento - SAC e Price | Fincal",
    desc="Calculadora de empréstimo grátis: informe o valor, a taxa de juros e o prazo para ver a parcela mensal, o total de juros, um gráfico e a tabela de amortização. Compare SAC, Price e taxa flat.",
    h1="Calculadora de empréstimo e financiamento",
    intro="Informe o valor, a taxa de juros e o prazo para ver a parcela mensal, o total de juros e a tabela de amortização. Tudo é calculado no seu navegador - nada é salvo ou enviado.",
    crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="Calculadora de empréstimo",
    amount="Valor do empréstimo", currency="R$", cur_pre=True, sep=".", comma=True,
    chips=[(20_000, "20 mil"), (50_000, "50 mil"), (300_000, "300 mil"), (500_000, "500 mil")],
    rate="Taxa de juros", rate_unit="% ao ano", term="Prazo", years="anos", months="meses",
    method="Sistema de amortização",
    methods=[("equal", "SAC (amortização constante)", "Amortização igual todo mês, juros sobre o saldo devedor. As parcelas começam altas e caem. Comum no financiamento imobiliário."),
             ("annuity", "Price (parcelas fixas)", "A mesma parcela todo mês. Comum em empréstimo pessoal, consignado e financiamento de veículos."),
             ("flat", "Taxa flat", "Juros sempre sobre o valor inicial. Aparece em algumas ofertas de crédito e parcelamentos.")],
    default=dict(amount=300_000, rate=11.5, term=30, unit="y", method="equal"),
    interest="Total de juros", lbl_i="Juros", total="Total pago", principal="Amortização",
    cmp_title="Compare os 3 sistemas", cmp_note="Mesmo valor, taxa e prazo. Toque em uma linha para ver os detalhes.",
    cmp_method="Sistema", cmp_first="1ª parcela", cmp_interest="Total de juros",
    cmp_names={"equal": "SAC", "annuity": "Price", "flat": "Taxa flat"},
    chart_title="Amortização e juros ao longo do tempo", chart_note="Cada barra é o que você paga em um ano (ou em um mês, para prazos curtos). Toque em uma barra para ver os detalhes.",
    sched_title="Tabela de amortização", sched_cols=["Amortização", "Juros", "Parcela", "Saldo devedor"],
    sched_more="O primeiro ano aparece mês a mês. A tabela mensal de todos os anos está no app Fincal.",
    promo_title="Seu financiamento é mais complicado?",
    promo_lead="O app Fincal calcula o que os bancos fazem de verdade:",
    promo_items=[("Taxas por período", "taxa promocional nos primeiros meses e depois uma nova taxa, quantos períodos quiser"),
                 ("Amortizações antecipadas", "única ou recorrente, com tarifa; veja os juros economizados e quantos meses a menos"),
                 ("Cenários salvos", "dê um nome, reabra e duplique para testar outras opções; o histórico é salvo automaticamente"),
                 ("Tabela mês a mês", "para todos os anos, e compartilhe o resultado com os gráficos como imagem")],
    get_on="DISPONÍVEL NO", dl_on="BAIXAR NA", ct="web-fincal-calc-loan-pt",
    footer_privacy="Privacidade", footer_support="Suporte",
    article="""
<h2>Como funciona o SAC</h2>
<p>No Sistema de Amortização Constante, o valor financiado é dividido igualmente pelos meses e os juros incidem só sobre o saldo devedor. As parcelas começam mais altas e caem todo mês, e o total de juros é menor que na tabela Price. É o sistema mais usado no financiamento imobiliário.</p>
<div class="formula">Amortização mensal = Valor financiado ÷ Número de meses<br>Juros do mês = Saldo devedor × Taxa anual ÷ 12</div>
<h2>Como funciona a tabela Price</h2>
<p>Na tabela Price todas as parcelas são iguais. No início a maior parte da parcela é juros e, com o tempo, a amortização aumenta.</p>
<div class="formula">Parcela = P × i ÷ (1 − (1 + i)<sup>−n</sup>)<br>P: valor financiado · i: taxa anual ÷ 12 · n: número de meses</div>
<h2>Por que a taxa flat engana</h2>
<p>Com a taxa flat, os juros são sempre calculados sobre o valor inicial, mesmo depois de você ter pago parte da dívida. Um empréstimo de R$ 20.000 em 24 meses com taxa flat de 24% ao ano custa R$ 9.600 de juros - o mesmo que uma taxa sobre o saldo devedor de cerca de <b>40,88%</b> ao ano. A calculadora mostra essa taxa equivalente quando você escolhe taxa flat. <a href="/fincal/taxa-flat-x-saldo-devedor/">Veja a explicação completa e a tabela de conversão →</a></p>
<h2>Exemplo: R$ 300.000 a 11,5% ao ano em 30 anos</h2>
<table class="cmp">
<thead><tr><th>Sistema</th><th>1ª parcela</th><th>Total de juros</th></tr></thead>
<tbody>
<tr><td>SAC</td><td>R$ 3.708,33</td><td>R$ 518.939,56</td></tr>
<tr><td>Price</td><td>R$ 2.970,87</td><td>R$ 769.525,18</td></tr>
<tr><td>Taxa flat</td><td>R$ 3.708,33</td><td>R$ 1.035.000,00</td></tr>
</tbody></table>
<p>A Price começa cerca de R$ 737 mais barata por mês, mas custa cerca de R$ 250 mil a mais em juros ao longo do contrato.</p>
<h2>Vale a pena amortizar antes?</h2>
<p>A amortização antecipada reduz os juros, e o banco vai perguntar se você prefere reduzir o prazo ou a parcela. <a href="/fincal/amortizacao-antecipada/">Veja um exemplo e compare as duas opções →</a></p>
""",
    faq=[
        ("SAC ou Price: qual é melhor?",
         "O SAC paga menos juros no total porque amortiza mais rápido, mas as primeiras parcelas são maiores. A Price tem parcelas fixas e começa mais leve. Se a renda cobre a primeira parcela do SAC, ele costuma sair mais barato."),
        ("O banco informa a taxa ao mês. Como converto?",
         "Esta calculadora usa a taxa nominal anual, dividida por 12 a cada mês. Para uma taxa de 1% ao mês, informe 12% ao ano. Se o banco informa a taxa efetiva anual, o resultado pode variar um pouco."),
        ("Os valores incluem seguros e tarifas?",
         "Não. A calculadora mostra só amortização e juros. O CET do banco inclui também seguros, tarifas e IOF, por isso a parcela real costuma ser maior."),
        ("E se a taxa mudar ou eu fizer amortizações extras?",
         "Esta página usa uma taxa fixa. Para taxa promocional seguida de outra taxa, ou amortizações antecipadas com tarifa, use o app Fincal grátis no Android e iOS."),
        ("Os dados que digito são enviados para algum lugar?",
         "Não. Todo o cálculo roda no seu navegador. Os números ficam apenas no endereço da página para você poder compartilhar o resultado."),
    ],
)

LANGS["ms"] = dict(
    path="/fincal/kalkulator-pinjaman/", og="ms_MY", faq_h="Soalan lazim", name="Bahasa Melayu", short="MS",
    title="Kalkulator Pinjaman - Ansuran Bulanan dan Jadual Bayaran Balik | Fincal",
    desc="Kalkulator pinjaman percuma: masukkan jumlah pinjaman, kadar faedah dan tempoh untuk melihat ansuran bulanan, jumlah faedah, carta dan jadual bayaran balik. Bandingkan ansuran sama, pokok sama dan kadar rata.",
    h1="Kalkulator pinjaman",
    intro="Masukkan jumlah pinjaman, kadar faedah dan tempoh untuk melihat ansuran bulanan, jumlah faedah dan jadual bayaran balik. Semuanya dikira dalam pelayar anda - tiada data disimpan atau dihantar.",
    crumb_home="Nanoko Studio", crumb_app="Fincal", crumb_page="Kalkulator pinjaman",
    amount="Jumlah pinjaman", currency="RM", cur_pre=True, sep=",", comma=False,
    chips=[(10_000, "10K"), (50_000, "50K"), (300_000, "300K"), (500_000, "500K")],
    rate="Kadar faedah", rate_unit="% setahun", term="Tempoh pinjaman", years="tahun", months="bulan",
    method="Kaedah bayaran balik",
    methods=[("annuity", "Ansuran sama (baki berkurangan)", "Ansuran sama setiap bulan, faedah atas baki pinjaman. Biasa untuk pinjaman perumahan."),
             ("flat", "Kadar rata (flat rate)", "Faedah sentiasa dikira atas jumlah asal. Biasa untuk pinjaman peribadi dan sewa beli kereta."),
             ("equal", "Pokok sama", "Pokok dibayar sama rata, faedah atas baki. Ansuran pertama paling tinggi.")],
    default=dict(amount=500_000, rate=4.2, term=35, unit="y", method="annuity"),
    interest="Jumlah faedah", lbl_i="Faedah", total="Jumlah dibayar", principal="Pokok",
    cmp_title="Bandingkan 3 kaedah", cmp_note="Jumlah, kadar dan tempoh yang sama. Ketik satu baris untuk melihat butirannya.",
    cmp_method="Kaedah", cmp_first="Ansuran pertama", cmp_interest="Jumlah faedah",
    cmp_names={"annuity": "Ansuran sama", "equal": "Pokok sama", "flat": "Kadar rata"},
    chart_title="Pokok dan faedah mengikut masa", chart_note="Setiap bar ialah jumlah yang dibayar dalam setahun (atau sebulan, untuk pinjaman pendek). Ketik bar untuk melihat butiran.",
    sched_title="Jadual bayaran balik", sched_cols=["Pokok", "Faedah", "Jumlah bayar", "Baki pinjaman"],
    sched_more="Tahun pertama diperincikan mengikut bulan. Jadual bulanan untuk setiap tahun ada dalam aplikasi Fincal.",
    promo_title="Pinjaman anda lebih rumit?",
    promo_lead="Aplikasi Fincal mengira apa yang benar-benar diamalkan bank:",
    promo_items=[("Kadar berperingkat", "kadar promosi pada bulan-bulan awal, kemudian kadar baharu, berapa banyak tempoh pun"),
                 ("Bayaran awal", "sekali atau berkala, termasuk yuran; lihat faedah yang dijimat dan bulan yang dipendekkan"),
                 ("Senario disimpan", "beri nama, buka semula dan salin untuk mencuba pilihan lain; sejarah disimpan secara automatik"),
                 ("Jadual bulanan", "untuk setiap tahun, dan kongsi hasil bersama carta sebagai imej")],
    get_on="DAPATKANNYA DI", dl_on="MUAT TURUN DI", ct="web-fincal-calc-loan-ms",
    footer_privacy="Dasar Privasi", footer_support="Sokongan",
    article="""
<h2>Cara ansuran bulanan dikira</h2>
<p>Pinjaman perumahan biasanya menggunakan kaedah baki berkurangan dengan ansuran yang sama setiap bulan. Pada awalnya sebahagian besar ansuran ialah faedah, dan bahagian pokok bertambah dari semasa ke semasa.</p>
<div class="formula">Ansuran bulanan = P × r ÷ (1 − (1 + r)<sup>−n</sup>)<br>P: jumlah pinjaman · r: kadar setahun ÷ 12 · n: bilangan bulan</div>
<h2>Kadar rata lebih mahal daripada yang disangka</h2>
<p>Dengan kadar rata, faedah sentiasa dikira atas jumlah pinjaman asal walaupun sebahagian pokok sudah dibayar. Pinjaman peribadi RM 30,000 selama 5 tahun pada kadar rata 6% setahun mengenakan faedah RM 9,000 - sama seperti kadar baki berkurangan kira-kira <b>10.85%</b> setahun. Kalkulator di atas menunjukkan kadar setara ini apabila anda memilih kadar rata. <a href="/fincal/kadar-rata-vs-baki-berkurangan/">Baca penjelasan penuh dan jadual tukaran →</a></p>
<div class="formula">Faedah sebulan = Jumlah asal × Kadar setahun ÷ 12<br>Ansuran = Jumlah asal ÷ Bilangan bulan + Faedah sebulan</div>
<h2>Contoh: pinjaman rumah RM 500,000 pada 4.2% selama 35 tahun</h2>
<table class="cmp">
<thead><tr><th>Kaedah</th><th>Ansuran pertama</th><th>Jumlah faedah</th></tr></thead>
<tbody>
<tr><td>Ansuran sama</td><td>RM 2,274.25</td><td>RM 455,187.35</td></tr>
<tr><td>Pokok sama</td><td>RM 2,940.48</td><td>RM 368,373.88</td></tr>
<tr><td>Kadar rata</td><td>RM 2,940.48</td><td>RM 735,000.00</td></tr>
</tbody></table>
<p>Ansuran sama bermula kira-kira RM 666 lebih rendah sebulan, tetapi jumlah faedahnya kira-kira RM 87,000 lebih tinggi berbanding pokok sama.</p>
<h2>Berbaloikah bayar pinjaman lebih awal?</h2>
<p>Membayar sebahagian pinjaman lebih awal mengurangkan faedah, tetapi mungkin ada penalti semasa lock-in, dan bank akan bertanya sama ada mahu pendekkan tempoh atau kurangkan ansuran. <a href="/fincal/bayar-pinjaman-awal/">Lihat contoh dan kira sama ada penaltinya berbaloi →</a></p>
""",
    faq=[
        ("Apakah beza kadar rata dan baki berkurangan?",
         "Kadar rata mengira faedah atas jumlah asal sepanjang tempoh. Baki berkurangan mengira faedah atas baki yang tinggal, jadi lebih murah pada kadar yang sama. Pilih \"Kadar rata\" di atas untuk melihat kadar setaranya."),
        ("Pinjaman peribadi saya 5% kadar rata. Berapa kadar sebenarnya?",
         "Bergantung pada tempoh. Untuk 5 tahun, kadar rata 5% bersamaan kira-kira 9.15% baki berkurangan. Masukkan angka anda dan pilih \"Kadar rata\" untuk angka tepat."),
        ("Adakah hasilnya sama dengan pengiraan bank?",
         "Kalkulator mengira faedah bulanan (kadar setahun ÷ 12) dan membundarkan setiap bulan, sama seperti aplikasi Fincal. Bank yang mengira faedah harian mungkin berbeza sedikit."),
        ("Bagaimana dengan perubahan kadar atau bayaran awal?",
         "Halaman ini menggunakan satu kadar tetap. Untuk kadar promosi pada awal kemudian kadar baharu, atau bayaran awal dengan yuran, gunakan aplikasi Fincal percuma di Android dan iOS."),
        ("Adakah data yang saya masukkan dihantar ke mana-mana?",
         "Tidak. Semua pengiraan berjalan dalam pelayar anda. Angka hanya muncul dalam alamat halaman supaya anda boleh berkongsi hasil."),
    ],
)
