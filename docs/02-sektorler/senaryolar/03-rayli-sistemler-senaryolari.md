# Raylı Sistemler ve Sinyalizasyon: Saldırgan ve Savunma Senaryoları

[Katalog Ana Sayfası](README.md) · [Raylı Sistemler Temel Rehberi](../03-rayli-sistemler.md) · [Telekomünikasyon Senaryoları](04-telekom-baz-istasyonu-senaryolari.md)

Bu belgede demiryolu sinyalizasyonu, anklaşman (interlocking), ETCS/CBTC tren kontrol sistemleri, cer gücü ve tünel emniyet sistemlerine yönelik **12 ayrıntılı saldırgan senaryosu** ve her senaryoya karşılık gelen **çok katmanlı mühendislik ve siber savunma çözümleri** yer almaktadır.

---

## Senaryo Özeti ve Matris

| Senaryo Kodu | Proses Alanı | Saldırganın Amacı | Fiziksel Risk / Sonuç | Birincil Savunma Mekanizması |
|---|---|---|---|---|
| `RAY-01` | Hat Boyu Algılama | Dingil sayıcı sahte sıfırlama (reset) | Dolu bloğa tren girişi ve arkadan çarpışma | Koşullu reset mantığı & fiziksel izleme |
| `RAY-02` | Hat Makası (Point Switch) | Makas son konum kontağını dondurma | Yarım kalmış makastan geçiş ve derayman | Bağımsız mekanik kilit & sürgü kontrol kontağı |
| `RAY-03` | ETCS / RBC | Baliz / RBC telgrafı yeniden oynatma | Hız sınırının aşılması ve virajda devrilme | Kriptografik zaman damgası & Euroradio anahtar |
| `RAY-04` | CBTC Telsiz Ağı | WLAN/LTE-R DoS veya Jamming | Acil frenleme, hat tıkanması ve yolcu tahliyesi | Çift yedekli frekans bandı & kayıpsız handover |
| `RAY-05` | Hemzemin Geçit | Bariyer durum telemetrisini spoof etme | Tren yaklaşırken bariyer açılması, kaza | SIL 4 emniyet rölesi & optik engel algılama |
| `RAY-06` | Cer Gücü SCADA | Katener kesicilerini dengesiz açma | Lokomotif inverterlerinin patlaması, duruş | Nötr bölge (neutral section) donanımsal interlock |
| `RAY-07` | Tünel Emniyet / Havalandırma | Jet fanlarını kaçış rotasına üfletme | Yangında yolcuların zehirli dumana boğulması | Hardwired duman yön algılama & SIL 3 havalandırma |
| `RAY-08` | Otomatik Tren Durdurma (ATS) | Hat boyu mıknatıs bobinlerini susturma | Kırmızı sinyal ihlalinde trenin durmaması | Fail-safe rezonans devresi & sürekli enerji besleme |
| `RAY-09` | Hat Altyapısı / Isıtma | Makas ısıtıcı ve sıcaklık sensörü bozma | Kışın makas donması, yazın ray bükülmesi | Bağımsız yerel termostatik mekanik şalter |
| `RAY-10` | Tren Üstü (TCMS) | Kapı kilit durum sinyalini baypas etme | Yüksek hızda tren kapısının açılması | Hardwired kapı kapalı döngüsü (Traction Interlock) |
| `RAY-11` | Anklaşman (Interlocking) | Çakışan rota kilitlerini zorlama | İki trenin aynı makasa girmesi (kafa kafaya) | SIL 4 Emniyet Mantığı (Vital Safety Computer) |
| `RAY-12` | Ray Devresi (Track Circuit) | Alıcı empedansını değiştirme | Hayalet tren veya görünmez tren oluşması | Kodlu ses frekanslı (AF) ray devresi & 2oo3 |

---

## Ayrıntılı Senaryolar ve Savunma Mühendisliği

### RAY-01: Dingil Sayıcı (Axle Counter) Sahte Sıfırlama ile Tren Çarpışması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Demiryolu bloklarında trenin varlığı hatta giren ve çıkan tekerlek dingillerinin sayılmasıyla ($Giriş - Çıkış = 0$) belirlenir. Saldırgan, hat bakım arayüzünden veya saha modülünden sahte bir `AXLE_COUNTER_RESET` komutu enjekte ederek blok içinde bir tren durmaktayken dingil sayacını sıfırlar. Anklaşman sistemi bloğu "BOŞ" kabul eder ve arkadan gelen trene "YEŞİL" sinyal açar.

#### 2. Fiziksel ve Süreç Hasarı
İkinci tren dolu bloğa tam hızla girer ve duran trene arkadan çarpar. Yıkıcı tren kazası, kitlesel can kaybı, lokomotif ve vagonların hurdaya dönmesi meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma (Layer 0/1)
- **Koşullu Hazırlık Reset Devresi (Preparatory Reset):** Sıfırlama komutu gelse bile blok doğrudan yeşile dönemez. Hat, kısıtlı hızla (maksimum 20 km/s) geçen ilk trenin tekerleklerini mekanik olarak sayıp bloğu terk ettiğini doğrulamadan tam hız serbestisi vermez.

#### 4. Yazılımsal ve Mantıksal Savunma (Anklaşman Seviyesi)
- **Çift Kişi Onaylı Sıfırlama (SIL 4):** Dingil sayıcı sıfırlama işlemi dispeçer ve saha istasyon şefinin iki farklı fiziksel konsoldan eşzamanlı anahtar çevirmesi ve gerekçe girmesi ile mümkündür.

#### 5. Ağ, Protokol ve Erişim Savunması
- Dingil sayıcı saha değerlendirme üniteleri (Evaluator) ile anklaşman arasındaki haberleşme RaSTA (Rail Safe Transport Application) protokolü üzerinden şifreli ve sıra numarası kontrollü yürütülür.

#### 6. Algılama ve OT SOC İmzası
- Trafik yönetim sisteminde (TMS) blokta tren göründüğü halde gelen reset komutları SOC tarafından kritik anomali olarak yakalanır.

---

### RAY-02: Makas Motoru Durum Kontaklarının Spoof Edilmesi ile Derayman

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, elektromekanik makas motorunun (Point Machine) dillerinin tam oturmadığı (orta konumda sıkıştığı) durumda, PLC/I/O kartındaki "Makas Düz Konumda Kilitli" (`Point_Locked_Normal`) dijital girişini sahte olarak enerjilendirir.

#### 2. Fiziksel ve Süreç Hasarı
Makas dili ile ray arasında 15-20 mm boşluk varken tren makasa 100+ km/s hızla girer. Tekerlek flanşı makas diline çarparak raydan çıkar (derayman); tren devrilir, hat boyu katener direkleri yıkılır.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik İğne ve Sürgü Kilit Düzeneği (Mechanical Point Lock / Facing Point Lock):** Makas dili milimetrik olarak tam yerine oturmadıkça mekanik kilit dili yuvasına giremez ve kontak devresini fiziksel olarak tamamlayamaz.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Makas Motor Akımı ve Zaman Eğrisi İzleme:** Makas çevrilirken motor akımı $I(t)$ profili kaydedilir; akım piki ve hareket süresi (örneğin 3.5 s) nominal değerden saptığında sistem makası arızaya geçirir.

#### 5. Ağ ve Protokol Savunması
- Saha kontrol üniteleri (Object Controller) güvenli donanımsal mantık devreleriyle korunur.

#### 6. Algılama ve OT SOC İmzası
- Makas pozisyon değişiklikleri ile motor sürücü telemetrisi arasındaki uyuşmazlıklar izlenir.

---

### RAY-03: ETCS / RBC Telgrafının Yeniden Oynatılması (Replay) ile Hız Aşımı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Avrupa Tren Kontrol Sistemi'nde (ETCS Seviye 2) Radyo Blok Merkezi (RBC) ile tren arasındaki GSM-R / FRMCS bağlantısına müdahale edilir. Düz hat için üretilmiş yüksek hızlı Hareket İzni (Movement Authority - MA) paketi kaydedilip, tren keskin bir viraja yaklaşırken yeniden enjekte edilir.

#### 2. Fiziksel ve Süreç Hasarı
Araç üstü EVC (European Vital Computer) hız sınırını 160 km/s olarak okur. Tren 60 km/s sınır olan viraja 160 km/s ile girerek merkezkaç kuvvetiyle devrilir.

#### 3. Donanımsal ve Mekanik Savunma
- Hat boyuna yerleştirilen sabit Eurobalise'lar, tren üzerinden geçerken manyetik indüksiyonla en güncel hat topoğrafyasını ve hız limitini fiziksel olarak araç üstü bilgisayara yükler.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Euroradio Güvenlik Katmanı (Subset-037):** Her RBC mesajı oturuma özgü dinamik oturum anahtarları (Session Key), artan sıra numarası ve milisaniyelik zaman damgası içerir. Eski paketler EVC tarafından reddedilir.

#### 5. Ağ ve Protokol Savunması
- Kriptografik Anahtar Yönetim Sistemi (KMS) ile güvenli anahtar dağıtımı.

#### 6. Algılama ve OT SOC İmzası
- GSM-R baz istasyonlarında sıra dışı sinyal tekrarları IDS ile tespit edilir.

---

### RAY-04: CBTC Telsiz Ağı Üzerinde DoS/Jamming ile Hat Kilitlenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Kent içi metro CBTC sisteminde tren ile hat boyu erişim noktaları (AP) arasındaki 5.8 GHz WLAN bandına RF Jamming yapılır veya ağ anahtarlarına sahte paket seli (UDP flood) gönderilir.

#### 2. Fiziksel ve Süreç Hasarı
CBTC'de haberleşme 1.5 saniyeden uzun kesilirse emniyet kuralı gereği tüm trenler acil imdat freni (Emergency Brake) uygular. Tünellerde onlarca tren aniden durur, yolcular vagonlarda mahsur kalır, metro hattı saatlerce felç olur.

#### 3. Donanımsal ve Mekanik Savunma
- Sızıntılı kablo (Leaky Feeder / Radiax) altyapısı ile tünel içi RF sinyalinin dış müdahalelerden fiziksel olarak korunması.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Yedekli İletişim Kanalları (Redundant WLAN / LTE-R):** Sistem eşzamanlı olarak iki bağımsız frekansta (A ve B ağı) veri aktarır; bir kanal jam edilse bile diğeri kesintisiz sürer.

#### 5. Ağ ve Protokol Savunması
- WPA3-Enterprise, 802.11r hızlı geçiş ve haberleşmede IEEE 1474 CBTC standart güvenlik profilleri.

#### 6. Algılama ve OT SOC İmzası
- Telsiz ağında paket kaybı ve sinyal/gürültü oranı (SNR) düşüşleri SOC telsiz telemetrisinde izlenir.

---

### RAY-05: Hemzemin Geçit Telemetrisinin Spoof Edilmesi ile Bariyerlerin Açılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Tren hemzemin geçide yaklaşırken, geçit kontrol PLC'sindeki tren yaklaşma sensörü (Approach Sensor) verisi yazılımsal olarak susturulur ve bariyer kaldırma motoruna `OPEN_BARRIER` komutu verilir.

#### 2. Fiziksel ve Süreç Hasarı
Bariyerler kalkar ve karayolu araçları rayların üzerine çıkar; tren hemzemin geçitteki araçlara tam hızla çarparak can kaybı ve araç tahribatına neden olur.

#### 3. Donanımsal ve Mekanik Savunma
- **SIL 4 Emniyet Röle Grubu:** Bariyer motoru ve flaşör devreleri doğrudan hatta yaklaşan trenin tekerlek yüküyle enerjilenen mekanik ray kontaklarına bağlıdır; yazılımdan bağımsız olarak tren geçerken bariyer fiziksel olarak açık tutulamaz.

#### 4. Yazılımsal ve Mantıksal Savunma
- Hemzemin geçit kapalı bilgisi teyit edilmeden makinist sinyali kırmızıda tutulur (CCTV / Radar Engel Algılama Entegrasyonu).

#### 5. Ağ ve Protokol Savunması
- Hemzemin geçit RTU'su ayrı bir emniyet ağı segmentinde tutulur.

#### 6. Algılama ve OT SOC İmzası
- Tren yaklaşma telemetrisi ile bariyer durum kayıtları arasındaki mantıksal uyumsuzluklar kaydedilir.

---

### RAY-06: Cer Gücü SCADA Manipülasyonu ile Katener Dengesizliği ve İnverter Hasarı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Demiryolu Cer Gücü Trafo Merkezi SCADA sistemine sızılarak, lokomotif bir nötr bölgeden (Neutral Section) geçerken komşu faz kesicileri aynı anda kapatılır.

#### 2. Fiziksel ve Süreç Hasarı
Farklı faza sahip iki ayrı katener beslemesi lokomotif pantografı üzerinde kısa devre olur. Devasa elektrik arkı pantografı eritir, lokomotif cer inverterleri patlar ve katener teli koparak rayların üzerine düşer.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Nötr Bölge Sinyalizasyon Balizi:** Lokomotif nötr bölgeye girmeden önce ana kesicisini (Vacuum Circuit Breaker - VCB) otomatik açan hat boyu donanımsal baliz.

#### 4. Yazılımsal ve Mantıksal Savunma
- Cer gücü SCADA yazılımında iki farklı faz kesicisinin aynı sekmana enerji vermesini engelleyen katı yazılımsal kilit.

#### 5. Ağ ve Protokol Savunması
- Cer trafo merkezleri IEC 60870-5-104 TLS ile merkez SCADA'ya bağlanır.

#### 6. Algılama ve OT SOC İmzası
- Trafo merkezleri arası faz uyuşmazlığı ve aşırı akım alarmları korelasyonu.

---

### RAY-07: Tünel Duman Tahliye Fanlarının Kaçış Rotasına Yönlendirilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Metro tünelinde tren yangını çıktığında, tünel SCADA sistemine müdahale edilerek duman tahliye jet fanlarının dönüş yönü tersine çevrilir.

#### 2. Fiziksel ve Süreç Hasarı
Zehirli duman ve karbonmonoksit gazı yolcuların kaçtığı tahliye çıkışına ve istasyona doğru üflenir; yolcular dumandan boğularak kitlesel can kayıpları yaşanır.

#### 3. Donanımsal ve Mekanik Savunma
- **Hardwired İtfaiyeci Öncelik Paneli (Firefighter Override Panel):** Tünel girişinde bulunan, fiziksel anahtarlı mekanik kontrol paneli tüm SCADA ve PLC komutlarını donanımsal olarak devreden çıkarır.

#### 4. Yazılımsal ve Mantıksal Savunma
- Yangın algılama sistemi (optik duman ve lineer ısı kablosu) lokasyonu ile fan yönü arasında değiştirilemez SIL 3 senaryo mantığı.

#### 5. Ağ ve Protokol Savunması
- Tünel havalandırma kontrolörleri bina otomasyonu ve yolcu internetinden tamamen izole edilmiş ağda tutulur.

#### 6. Algılama ve OT SOC İmzası
- Yangın alarmı varken fan yön komutlarındaki manuel değişiklikler SOC tarafından anında acil durum olarak işaretlenir.

---

### RAY-08: Otomatik Tren Durdurma (ATS) Sinyallerinin Yazılımsal Olarak Susturulması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Hat boyu ATS / Indusi rezonans devrelerinin kontrol kartına müdahale edilerek sinyal kırmızıdayken 2000 Hz rezonans devresi devre dışı bırakılır.

#### 2. Fiziksel ve Süreç Hasarı
Makinist kırmızı sinyali ihlal ettiğinde tren acil frene geçmez; makas bölgesinde bekleyen başka bir trene çarpar (SPAD - Signal Passed at Danger kazası).

#### 3. Donanımsal ve Mekanik Savunma
- **Fail-Safe Manyetik Rezonans Tasarımı:** ATS bobinleri pasif ayarlı devrelerdir; enerji kesildiğinde veya kablo koptuğunda kendiliğinden "Kırmızı / Açma" modunda kalır (Fail-Safe).

#### 4. Yazılımsal ve Mantıksal Savunma
- Araç üstü sistem, sinyal durumunu telsiz veya ray devresi üzerinden çapraz doğrular.

#### 5. Ağ ve Protokol Savunması
- Sinyalizasyon saha panoları elektronik mühür ve açılma kontakları ile korunur.

#### 6. Algılama ve OT SOC İmzası
- Sinyal lambası durumu ile ATS bobini telemetrisi arasındaki uyumsuzluklar taranır.

---

### RAY-09: Makas Isıtıcı ve Ray Sıcaklık Telemetrisi Manipülasyonu

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Kış şartlarında makas rezistans ısıtıcılarının telemetrisi "Makas Sıcaklığı: +15°C" olarak sabitlenir ve ısıtıcı kontaktörleri kapatılır.

#### 2. Fiziksel ve Süreç Hasarı
Makas dilleri arasına kar ve buz dolarak makas kilitlenir; sabah seferlerinde onlarca tren istasyon çıkışlarında mahsur kalır ve hat tıkanır.

#### 3. Donanımsal ve Mekanik Savunma
- Makas gövdesine mekanik olarak bağlı bimetal termostatik anahtarlar sıcaklık +3°C altına düştüğünde ısıtıcıyı bağımsız çalıştırır.

#### 4. Yazılımsal ve Mantıksal Savunma
- Hava durumu meteoroloji servisi ile makas ısıtma çalışma süreleri korelasyonu.

#### 5. Ağ ve Protokol Savunması
- Yardımcı tesisat RTU'ları şifreli haberleşir.

#### 6. Algılama ve OT SOC İmzası
- Dış ortam sıcaklığı sıfırın altındayken ısıtıcı akımının sıfır olması alarmı.

---

### RAY-10: TCMS Kapı Kilit İzleme Sinyallerinin Baypas Edilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Tren Kontrol ve İzleme Sistemi (TCMS) araç içi veriyoluna (MVB / CANopen) müdahale edilerek vagon kapısı açıkken "Tüm Kapılar Kilitli" (`All_Doors_Closed == TRUE`) sinyali enjekte edilir.

#### 2. Fiziksel ve Süreç Hasarı
Makinist cer kolunu çektiğinde tren açık kapıyla 120 km/s hızla hareket eder; yolcuların trenden düşme riski doğar.

#### 3. Donanımsal ve Mekanik Savunma
- **Hardwired Çekiş Kilitleme Döngüsü (Traction Interlock Loop):** Tüm vagon kapılarının mekanik mikro sviçleri cer inverteri etkinleştirme hattına fiziksel seri bağlıdır; tek bir kapı açıkken motora güç gitmez.

#### 4. Yazılımsal ve Mantıksal Savunma
- Hız > 3 km/s olduğunda kapı açma butonlarını kilitleyen bağımsız vagon kapı kontrol ünitesi (DCU).

#### 5. Ağ ve Protokol Savunması
- Tren içi Ethernet Omurgası (IEC 61375 TTCN) yolcu Wi-Fi ağından fiziksel olarak izole edilir.

#### 6. Algılama ve OT SOC İmzası
- TCMS veriyolunda yetkisiz CAN/MVB mesaj çerçeveleri izlenir.

---

### RAY-11: Anklaşman (Interlocking) Rota Kilitleme Mantığında Çakışan Rota Onayı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Anklaşman emniyet yazılımındaki rota tablosu manipüle edilerek aynı hatta ters yönden gelen iki trene eşzamanlı hareket rotası tahsis edilir.

#### 2. Fiziksel ve Süreç Hasarı
İki tren tek hatta kafa kafaya (Head-on Collision) çarpışır.

#### 3. Donanımsal ve Mekanik Savunma
- **Vital SIL 4 Emniyet Bilgisayarı:** 2oo3 donanım mimarisi ve mantık kural motoru donanımsal kilitlerle korunur.

#### 4. Yazılımsal ve Mantıksal Savunma
- Coğrafi ve mantıksal emniyet kontrol algoritmaları bağımsız derleyicilerle doğrulanır.

#### 5. Ağ ve Protokol Savunması
- Anklaşman merkezi ile dispeçer çalışma istasyonları arasında sıkı kimlik doğrulama.

#### 6. Algılama ve OT SOC İmzası
- Rota talep ve onay loglarının formal verification araçlarıyla denetimi.

---

### RAY-12: Ray Devresi (Track Circuit) Şöntleme Empedans Manipülasyonu

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Ses frekanslı (AF) ray devresi ayar alıcısına müdahale edilerek tren tekerlek şöntleme algılama eşiği düşürülür.

#### 2. Fiziksel ve Süreç Hasarı
Ray üzerinde tren olmasına rağmen sinyal sistemi treni görmez ("Görünmez Tren"); arkadan gelen tren için hat serbest görünür.

#### 3. Donanımsal ve Mekanik Savunma
- Çift yönlü kodlanmış ray akımı frekans modülasyonu.

#### 4. Yazılımsal ve Mantıksal Savunma
- Dingil sayıcılar ve ray devreleri arasında çapraz doluluk doğrulaması.

#### 5. Ağ ve Protokol Savunması
- Sinyalizasyon saha dolaplarının fiziksel ve siber izlenmesi.

#### 6. Algılama ve OT SOC İmzası
- Ray devresi gerilim seviyesindeki anormallikler OT SOC'ta izlenir.
