# Su ve Atıksu Sistemleri: Saldırgan ve Savunma Senaryoları

[Katalog Ana Sayfası](README.md) · [Su ve Atıksu Temel Rehberi](../01-su-ve-atiksu.md) · [Elektrik ve Enerji Senaryoları](02-elektrik-enerji-senaryolari.md)

Bu belgede su temini, arıtma tesisleri, terfi istasyonları ve atıksu işleme tesislerindeki siber-fiziksel süreçlere yönelik **15 ayrıntılı saldırgan senaryosu** ve her senaryoya karşılık gelen **çok katmanlı mühendislik ve siber savunma çözümleri** yer almaktadır.

---

## Senaryo Özeti ve Matris

| Senaryo Kodu | Proses Alanı | Saldırganın Amacı | Fiziksel Risk / Sonuç | Birincil Savunma Mekanizması |
|---|---|---|---|---|
| `SU-01` | Temiz Su Deposu / Terfi | Seviye sensörü manipülasyonu | Pompanın kuru çalışması ve motorun yanması | Hardwired akış anahtarı & termistör rölesi |
| `SU-02` | İletim Ana Boru Hattı | Vana aktüatörü ani kapatma | Su koçu (water hammer) ve boru patlaması | Hidrolik yavaşlatıcı & yaylı darbe vanası |
| `SU-03` | Kimyasal Arıtma | Klor dozaj setpointini artırma | Aşırı klorlama ve kimyasal zehirlenme | Bağımsız analizör & dozajlama akış kısıtlayıcı |
| `SU-04` | Dezenfeksiyon | Klor dozajını sıfırlama | Arıtılmamış su salınımı ve patojen yayılımı | 2oo3 klor ölçümü & minimum dozaj interlocku |
| `SU-05` | pH Dengeleme | pH elektrot verisini dondurma | Asit taşkını, boru korozyonu ve toksisite | Rate-of-change denetimi & bağımsız pH sensörü |
| `SU-06` | Hızlı Kum Filtresi | Bulanıklık değerini düşük gösterme | Filtre tıkanması, taşma ve proses duruşu | Diferansiyel basınç anahtarı (d/p switch) |
| `SU-07` | Filtre Geri Yıkama | Eşzamanlı geri yıkama başlatma | Tesis hidrolik kapasite aşımı ve su basması | PLC geri yıkama sıra kilidi (interlock) |
| `SU-08` | Biyolojik Havalandırma | Çözünmüş oksijen (DO) sahteciliği | Blower kapatma ve biyolojik çamur ölümü | Akım/hava debi çapraz kontrolü & bağımsız DO |
| `SU-09` | Çamur Çürütücü (Digester) | Basınç/sıcaklık verisi bozma | Metan gazı birikmesi ve patlama tehlikesi | Mekanik ağırlıklı patlama diski ve alev tutucu |
| `SU-10` | UV Dezenfeksiyon | UV sensörünü yanıltma | Dezenfekte edilmemiş atıksu deşarjı | Lamba akım izleme & debi-oranlı emniyet kesicisi |
| `SU-11` | Terfi Çekvalfleri | Çekvalf kapalı sinyalini spoof etme | Pompanın ters dönmesi ve mil kırılması | Mekanik ters dönüş kilit mandalı (anti-reverse) |
| `SU-12` | Koagülasyon / Flokülasyon | Şap/demir klorür dozajı durdurma | Çökeltme yetersizliği ve çamurlu su dağıtımı | Zeta potansiyeli & akış doğrulama mantığı |
| `SU-13` | Dağıtım Şebekesi | Basınç Düşürücü Vana (PRV) bozma | Aşırı basınçla şehir şebeke borusu patlatma | Pilot mekanik basınç emniyet ventili |
| `SU-14` | Yağmur Suyu / Taşkın | Savak ve terfi kapaklarını kapatma | Geri tepme, kentsel alan su baskını | Bağımsız seviye şamandıralı acil durum bypassı |
| `SU-15` | Laboratuvar / LIMS | Kalite telemetrisini dondurma | Kirlenmenin fark edilmesini geciktirme | İmzalı LIMS verisi & saha numune korelasyonu |

---

## Ayrıntılı Senaryolar ve Savunma Mühendisliği

### SU-01: Depo Seviye Sensörü Manipülasyonu ile Pompa Kuru Çalıştırma ve Motor Hasarı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, emme deposundaki ultrasonik veya hidrostatik seviye sensöründen PLC'ye gelen analog 4-20 mA sinyali (veya Modbus/TCP register değerini `0x0104 - Tank_Level`) manipüle eder. Depo fiilen boş olmasına (%5 su seviyesi) rağmen PLC register değerini sahte olarak %85 (dolu) seviyesinde sabitler. Ardından HMI üzerinden veya doğrudan PLC kontrol kelimesini (`0x0001 - Pump_Start_CMD`) yazarak ana transfer pompasını tam kapasite çalıştırır.

#### 2. Fiziksel ve Süreç Hasarı
Santrifüj pompa susuz çalıştığında (dry-running), suyun sağladığı soğutma ve yağlama ortadan kalkar. Mekanik salmastralar saniyeler içinde 200°C üzerine çıkarak erir ve kırılır. Çark (impeller) sürtünmeden dolayı aşırı ısınır, mil yamulur ve motor aşırı akım çekerek sargı izolasyonu yanar (termal tahribat). Tesis su basamaz hale gelir.

#### 3. Donanımsal ve Mekanik Savunma (Layer 0/1)
- **Hardwired Düşük Akış / Kuru Çalışma Anahtarı (Flow Switch):** Pompa emme veya basma hattına doğrudan monte edilen kalorimetrik veya mekanik akış anahtarı, pompa kontaktör bobini devresine seri bağlanır. PLC'den bağımsız olarak 5 saniye içinde akış görmezse motor sürücüsünü (VFD) veya kontaktörü donanımsal olarak açar.
- **Motor Termistör / PTC Rölesi:** Motor sargılarına gömülü PTC sıcaklık sensörleri doğrudan bir motor koruma rölesine bağlanır; aşırı ısınmada güç devresi mekanik olarak kesilir.

#### 4. Yazılımsal ve Mantıksal Savunma (PLC Seviyesi)
- **Motor Akımı ve Güç Faktörü (Cos $\phi$) Kontrolü:** Boşta dönen pompa motoru nominal akımın %30'undan az çeker ve $\cos\phi$ düşer. PLC mantığı, pompa çalışıyor komutuna rağmen akım/güç düşükse 3 saniye içinde `ERR_DRY_RUN` alarmı üreterek pompayı kilitler.
- **2oo3 Seviye Sensörü Oylaması:** Depoda 1 hidrostatik basınç sensörü, 1 ultrasonik sensör ve 1 bağımsız mekanik seviye şamandırası kullanılır. Seviye şamandırası "Kritik Düşük" veriyorsa analog değer yüksek görünse dahi pompa çalıştırılamaz.

#### 5. Ağ, Protokol ve Erişim Savunması
- PLC register yazma işlemleri için IEC 62351-8 Rol Tabanlı Erişim Kontrolü (RBAC) uygulanır.
- Pompa çalıştırma komutları yalnızca operatör panelinden çift doğrulama (two-person rule veya challenge-response) ile kabul edilir.

#### 6. Algılama ve OT SOC İmzası
- **Suricata/Zeek Kuralı:** Modbus Function Code 06/16 ile `Pump_Start_CMD` registerına yazma gerçekleştiğinde, historian seviye verisi ile korelasyon kurulur.
- **SOC Alarmı:** Seviye değişimi sıfır iken pompa durumunun `RUNNING` olması ve deşarj basıncının sıfır kalması durumunda Seviye 1 Kritik Proses Sapması alarmı üretilir.

---

### SU-02: Hızlı Vana Kapatma Komutu ile Su Koçu (Water Hammer) ve Boru Patlatılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yüksek debili ana isale hattında (örneğin 1200 mm çaplı çelik boru, 3 m/s hız) çalışan motorlu kelebek vana aktüatörünün PLC kontrol yazılımındaki vana kapanma rampa süresi (travel time) parametresi (`0x0210 - Valve_Closure_Ramp`) 120 saniyeden 1 saniyeye indirilir ve `EMERGENCY_CLOSE` komutu gönderilir.

#### 2. Fiziksel ve Süreç Hasarı
Akan su kütlesinin ani durdurulması Joukowsky denklemine göre devasa bir basınç dalgası üretir ($\Delta P = \rho \cdot a \cdot \Delta v$). Boru içi basınç nominal 10 bar seviyesinden 60+ bar seviyesine aniden fırlar. Boru flanşları yarılır, boru patlar, pompa istasyonunu su basar ve ana hat günlerce devre dışı kalır.

#### 3. Donanımsal ve Mekanik Savunma
- **Hidrolik Amortisörlü Çekvalf ve Yavaş Kapanma Dişli Kutusu:** Vana aktüatörüne mekanik hidrolik fren (dashpot) eklenir; aktüatör sinyali ne olursa olsun vananın mekanik olarak 60 saniyeden daha hızlı kapanması fiziksel olarak engellenir.
- **Hızlı Tahliye Basınç Emniyet Ventili (Surge Anticipator Valve):** Ani basınç yükselmesinde mekanik yay kuvvetiyle milisaniyeler içinde açılarak fazla suyu tahliye eden hidrolik koruma vanası.

#### 4. Yazılımsal ve Mantıksal Savunma
- PLC lojiğinde vana kapanma eğrisi donanımsal zamanlayıcıya (hardware timer) kilitlenir; yazılım üzerinden minimum 45 saniyenin altında kapanma komutları PLC firmware seviyesinde reddedilir.
- Basınç sensöründen gelen ani artış ($dP/dt > 2\text{ bar/s}$) algılandığında hat üzerindeki tahliye by-pass vanaları otomatik olarak açılır.

#### 5. Ağ ve Protokol Savunması
- Vana aktüatör konfigürasyon parametreleri sadece kilitli mühendislik anahtarı (Physical Key Switch) aktifken değiştirilebilir.

#### 6. Algılama ve OT SOC İmzası
- Vana kapanma süresi komutlarındaki değişiklikler mühendislik istasyonu syslog kayıtlarında denetlenir. Ağda ani `Valve_Closure_Rate` değişikliği tespit edildiğinde SOC analistine acil bülten iletilir.

---

### SU-03: Klor Dozajlama Pompası Setpoint Manipülasyonu (Aşırı Klorlama)

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, dezenfeksiyon ünitesindeki sodyum hipoklorit dozajlama pompasının PLC registerındaki setpoint değerini (`0x0350 - Chlorine_Setpoint_mgL`) normal değer olan 1.5 mg/L seviyesinden maksimum kapasite olan 25.0 mg/L seviyesine çeker. Aynı zamanda serbest klor analizörünün geri bildirim registerını 1.2 mg/L değerinde sabit tutarak operatör ekranında her şeyin normal görünmesini sağlar.

#### 2. Fiziksel ve Süreç Hasarı
Şebekeye yüksek konsantrasyonda klor verilir. İçme suyunda koku, tat bozulması, cilt/göz tahrişi ve solunum yolu rahatsızlıkları oluşur; uzun süreli maruziyette kanserojen trihalometan (THM) bileşikleri kritik seviyeleri aşar.

#### 3. Donanımsal ve Mekanik Savunma
- **Fiziksel Orifis / Mekanik Dozaj Kısıtlayıcı:** Klor enjeksiyon hattına takılan mekanik debi sınırlayıcı diyafram, pompanın fiziksel olarak 3.0 mg/L üzerinde klor basmasını hidrolik olarak imkânsız kılar.
- **Bağımsız Analizör Acil Kesme Rölesi:** PLC'den tamamen bağımsız çalışan bir kolorimetrik klor analizörü, 4.0 mg/L üzerinde klor algıladığında dozaj pompasının besleme elektriğini keser.

#### 4. Yazılımsal ve Mantıksal Savunma
- **PLC Setpoint Üst Sınırı (Clamping):** PLC kodu içinde klor setpointi donanımsal sabit (constant) ile maksimum 2.5 mg/L ile sınırlandırılır.
- **Kütle Dengesi ve Tüketim Korelasyonu:** PLC, klor tankındaki seviye düşüşü (tüketilen kg) ile su debisini ($m^3/h$) karşılaştırarak teorik klor dozajını hesaplar. Analizör verisi ile hesaplanan kütle dengesi uyuşmazsa alarm verir.

#### 5. Ağ ve Protokol Savunması
- Kimyasal dozaj bölgesi (Level 1) ayrı bir VLAN'a ayrılır ve sadece şifreli OPC UA bağlantıları üzerinden yetkili operatör profiliyle setpoint değişikliğine izin verilir.

#### 6. Algılama ve OT SOC İmzası
- Klor tankı seviye azalma hızındaki anomali ($dL/dt$) ile debi arasındaki korelasyon kopması OT SIEM üzerinde alarm tetikler.

---

### SU-04: Klor Dozajının Sıfırlanması ile Biyolojik Kirlilik Salınımı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, dozaj pompası sürücüsüne `STOP` komutu gönderir veya klor akış kontrol vanasını %0 konumuna getirir. Analizör telemetrisi ise normal klor seviyesini taklit edecek şekilde döngüsel sinyalle beslenir.

#### 2. Fiziksel ve Süreç Hasarı
Dezenfeksiyon tamamen durur. Şebekeye koliform bakteriler, Giardia ve Cryptosporidium gibi patojenler karışır; halk sağlığı krizi ve kitlesel salgın hastalıklar ortaya çıkar.

#### 3. Donanımsal ve Mekanik Savunma
- **Klor Enjeksiyon Akış Sensörü ve Interlock:** Enjeksiyon borusuna takılı elektromanyetik akış ölçer (magmeter), sıfır akış gördüğü anda tesis ana çıkış vanasını otomatik olarak kapatarak arıtılmamış suyun şehre basılmasını engeller.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Minimum Klor Emniyet Kilidi:** Ham su giriş vanası ile klor dozaj pompası arasına yazılımsal interlock konur: Klor pompası çalışmıyorsa ana giriş vanası açılamaz.
- **2oo3 Farklı Nokta Ölçümü:** Karıştırma havuzu çıkışı, temas tankı çıkışı ve şebeke besleme noktasında 3 ayrı sensör bulunur; herhangi birinde 0.5 mg/L altı ölçüm olursa sistem güvenli duruşa (Fail-Safe Shutdown) geçer.

#### 5. Ağ ve Protokol Savunması
- Dozaj durdurma komutları için iki yetkili mühendisin ayrı oturumlardan onay vermesi (4-Eyes Principle) zorunlu tutulur.

#### 6. Algılama ve OT SOC İmzası
- Zeek ICS analizörü ile `Chlorine_Pump_Status == STOPPED` iken `Main_Effluent_Flow > 0` durumu yakalandığında yüksek öncelikli güvenlik alarmı üretilir.

---

### SU-05: pH Dengeleme Sürecinde Asit/Kostik Sensörü Dondurma ile Şebeke Korozyonu

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, pH analizörünün analog giriş değerini PLC bellek alanında (örneğin `%IW204`) zorla (force) pH 7.2 olarak kilitler. Ardından sülfürik asit dozaj pompasını manuel modda maksimum hızda çalıştırır.

#### 2. Fiziksel ve Süreç Hasarı
Suyun pH'ı hızla 4.0'ın altına düşer (aşırı asidik). Asidik su iletim borularındaki koruyucu kalsiyum karbonat tabakasını söker, borulardan suya kurşun/bakır çözünür, boru hatlarında delinmeler oluşur ve dağıtım şebekesi ağır hasar görür.

#### 3. Donanımsal ve Mekanik Savunma
- Asit dozajlama boru hattına mekanik pH limitörü ve maksimum akış orifisi yerleştirilir.
- Bağımsız pH seviye emniyet şalteri 6.0 altı ölçümde asit dozaj pompasının kontaktörünü mekanik olarak açar.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Sensör Değer Donması (Freezing) Tespiti:** Canlı bir proses sıvısında pH değeri sürekli mikroskobik dalgalanmalar gösterir. PLC mantığı, 120 saniye boyunca standart sapması $\sigma = 0$ olan sensör verisini "arızalı/manipüle edilmiş" kabul eder ve pompayı durdurur.
- **Asit Tüketimi / pH Değişim Oranı Kontrolü:** Asit pompası çalışırken pH'ın değişmemesi imkânsızdır; bu durum doğrudan proses alarmı oluşturur.

#### 5. Ağ ve Protokol Savunması
- PLC I/O force (değer sabitleme) fonksiyonları çalışma modunda (RUN Mode) devre dışı bırakılır; sadece fiziksel anahtarla `STOP/PROGRAM` modunda izin verilir.

#### 6. Algılama ve OT SOC İmzası
- PLC konfigürasyon değişiklik günlükleri (Change Logs) izlenir; `Force_Variable` komutu görüldüğü an SOC ekranına acil bildirim düşer.

---

### SU-06: Bulanıklık Sensörü Sahteciliği ile Filtre Tıkanması ve Taşma

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Hızlı kum filtrelerinin giriş ve çıkışındaki bulanıklık (turbidity - NTU) sensör değerleri sahte olarak 0.1 NTU (mükemmel berrak) olarak bildirilir. Filtre yatağında katı madde birikmesine rağmen geri yıkama döngüsü başlatılmaz.

#### 2. Fiziksel ve Süreç Hasarı
Kum yatağı tamamen tıkanır, filtre havuzunda hidrolik yük kaybı artar, su havuz kenarlarından taşarak galeri katındaki elektrik motorlarını ve elektrik panolarını su basmasına yol açar.

#### 3. Donanımsal ve Mekanik Savunma
- Filtre kum yatağı giriş-çıkış arasına bağlanan mekanik diferansiyel basınç anahtarı (d/p switch), basınç farkı 0.8 barı aştığında otomatik geri yıkama vanasını pnömatik olarak açar.
- Filtre üst kotuna yerleştirilen acil durum savak tahliye borusu taşkın suyunu drenaj kanalına iletir.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Zaman Tabanlı Yedekleme Mantığı:** Bulanıklık sensörü ne gösterirse göstersin, maksimum çalışma süresi (örneğin 48 saat) dolduğunda filtre zorunlu geri yıkamaya alınır.
- **Hidrolik Seviye - Basınç Tutarlılığı:** Filtre su seviyesi yükselirken çıkış debisinin düşmesi durumu filtre tıkanması olarak algılanır.

#### 5. Ağ ve Protokol Savunması
- Analizör cihazları ile PLC arasındaki haberleşmede Modbus RTU yerine dijital teşhis verisi taşıyan HART veya güvenli Fieldbus protokolleri kullanılır.

#### 6. Algılama ve OT SOC İmzası
- Filtre çalışma saati ile sensör ölçümleri arasındaki tutarsızlık historian analiz algoritması ile taranır.

---

### SU-07: Kum Filtrelerinin Eşzamanlı Geri Yıkamaya Sokulması ile Arıtma Kapasitesinin Çökertilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Tesis bünyesindeki 12 adet kum filtresinin tamamına aynı anda `START_BACKWASH` komutu gönderilir.

#### 2. Fiziksel ve Süreç Hasarı
Geri yıkama pompaları aşırı su çekerek temiz su deposunu boşaltır, geri yıkama atık kanalları devasa debiyi kaldıramayarak taşar ve tesisin içme suyu üretimi sıfıra düşer.

#### 3. Donanımsal ve Mekanik Savunma
- Geri yıkama suyu basma borusuna sadece 2 filtrenin debisini sağlayabilecek kapasitede mekanik debi kısıtlayıcı vana konur.

#### 4. Yazılımsal ve Mantıksal Savunma
- **PLC Sıra ve Karşılıklı Kilit (Mutual Exclusion Lock):** PLC mantığında aynı anda en fazla 1 (veya maksimum 2) filtrenin geri yıkamada olmasına izin veren yazılımsal token mekanizması kurulur. Diğer filtrelerin komutları sıraya alınır.

#### 5. Ağ ve Protokol Savunması
- Toplu komut gönderimleri (broadcast command) ağ anahtarlarında (switch) ACL kuralları ile engellenir.

#### 6. Algılama ve OT SOC İmzası
- Aynı saniye içinde birden fazla filtre ünitesine komut yazılması kural tabanlı IDS ile yakalanır.

---

### SU-08: Havalandırma Havuzunda Çözünmüş Oksijen (DO) Sahteciliği ile Biyolojik Çamur Ölümü

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Atıksu arıtma biyolojik havalandırma havuzundaki Çözünmüş Oksijen (Dissolved Oxygen - DO) sensörü registerı sahte olarak 6.0 mg/L (yüksek oksijen) olarak sabitlenir. PID kontrol döngüsü hava ihtiyacı olmadığını varsayarak devasa havalandırma blowerlarını (kompresörlerini) durdurur.

#### 2. Fiziksel ve Süreç Hasarı
Havuzdaki aktif çamur bakterileri anoksik/anaerobik duruma geçer ve birkaç saat içinde toplu bakteri ölümü gerçekleşir. Biyolojik arıtma çöker; tesisin yeniden devreye alınması ve mikroorganizma popülasyonunun oluşması haftalar sürer. Bu sürede arıtılmamış atıksu doğaya akar.

#### 3. Donanımsal ve Mekanik Savunma
- Blower motor kontrol panosuna entegre edilen mekanik minimum çalışma zamanlayıcısı, havuzun hiçbir zaman 15 dakikadan uzun süre havalandırmasız kalmamasını sağlar.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Blower Akımı ve Hava Debisi Doğrulaması:** DO seviyesi yüksek görünse bile, ORP (Oksidasyon İndirgenme Potansiyeli) sensörü ile çapraz kontrol yapılır. ORP negatif değerlere düşüyorsa sistem acil havalandırmayı başlatır.
- Minimum temel hava üfleme hızı (base aeration rate) PLC'de sabit alt sınır olarak korunur.

#### 5. Ağ ve Protokol Savunması
- SCADA sunucusu ile PLC arasındaki telemetri OPC UA Sign & Encrypt ile korunur.

#### 6. Algılama ve OT SOC İmzası
- Blower çalışma süresi sıfır iken atıksu giriş debisinin devam etmesi durumu SOC korelasyon motorunda alarm tetikler.

---

### SU-09: Anaerobik Çamur Çürütücü (Digester) Basınç/Sıcaklık Manipülasyonu ile Metan Patlama Riski

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Çamur çürütücü tankındaki metan ($CH_4$) gazı basınç sensörü değeri düşük gösterilirken gaz yakma meşalesi (flare) ve gaz motoru besleme vanaları kapatılır. Tank içi basınç tahliye edilmeden çamur beslemesi sürdürülür.

#### 2. Fiziksel ve Süreç Hasarı
Çürütücü kubbesinde aşırı biyogaz basıncı oluşur. Betonarme veya çelik kubbede çatlaklar meydana gelir, atmosfere yüksek miktarda patlayıcı metan gazı yayılır; kıvılcım halinde yıkıcı patlama ve yangın meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- **Ağırlıklı Basınç Tahliye Ventili ve Patlama Diski (Rupture Disk):** Tank tepesine monte edilen mekanik patlama diski, basınç 50 mbar üzerine çıktığında fiziksel olarak yırtılarak gazı güvenli tahliye bacasına aktarır.
- **Alev Tutucu (Flame Arrester):** Boru hattındaki olası alev yürümelerini fiziksel olarak durduran mekanik ızgaralar.

#### 4. Yazılımsal ve Mantıksal Savunma
- Bağımsız Emniyet Enstrümanlı Sistemi (SIS - SIL 2): PLC'den bağımsız ayrı bir Safety PLC, yüksek basınç algıladığında çamur besleme pompasını durdurur ve acil meşale vanasını açar.

#### 5. Ağ ve Protokol Savunması
- Safety PLC haberleşmesi PROFIsafe protokolü üzerinden şifreli ve CRC korumalı yürütülür; standart SCADA ağından izole edilir.

#### 6. Algılama ve OT SOC İmzası
- Çürütücü gaz üretim hacmi ile basınç sensörü korelasyonundaki sapmalar kaydedilir.

---

### SU-10: UV Dezenfeksiyon Radyasyon Sensörü Sahteciliği ile Arıtılmamış Deşarj

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Atıksu arıtma tesisi çıkışındaki Ultraviyole (UV) dezenfeksiyon kanalında UV yoğunluk (irradiance - $mW/cm^2$) sensörü değeri maksimum gösterilirken UV lamba balastları kapatılır veya lamba kılıflarındaki silecek mekanizması durdurularak kılıfların yosun/çamurla kaplanması sağlanır.

#### 2. Fiziksel ve Süreç Hasarı
UV ışınımı olmadan tahliye edilen su patojen mikroorganizmalar (E. coli, virüsler) içerir. Alıcı su ortamına (göl, nehir veya deniz) kontrolsüz mikrobiyolojik deşarj gerçekleşir, çevre felaketi ve plaj/tarım alanı kapatmaları yaşanır.

#### 3. Donanımsal ve Mekanik Savunma
- Lamba besleme panolarında her UV lambası için bağımsız akım trafosu (Current Transformer) kullanılır; lamba akımı çekilmiyorsa deşarj savağı kapağı açılmaz.

#### 4. Yazılımsal ve Mantıksal Savunma
- **UV Dozu Hesaplama Algoritması:** UV Dozu ($mJ/cm^2$) = UV Yoğunluğu $\times$ (Kanal Hacmi / Debi) formülü PLC'de hesaplanır. Debi artarken lamba akımı yoksa otomatik by-pass savağı kilitlenir.

#### 5. Ağ ve Protokol Savunması
- UV kontrol paneli yerel HMI'ı fiziksel anahtar kilidine bağlanır ve harici uzaktan erişim tamamen engellenir.

#### 6. Algılama ve OT SOC İmzası
- Deşarj debisi pozitif iken toplam UV lamba güç tüketiminin sıfır olması alarm olarak üretilir.

---

### SU-11: Terfi Çekvalfleri Durum Geri Bildirimi Manipülasyonu ile Ters Dönüş ve Mil Kırılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yüksek basma yüksekliğine (head) sahip terfi merkezinde durdurulan pompanın basma hattındaki hidrolik kontrollü çekvalfin açık kaldığı bilgisi gizlenir (`Check_Valve_Closed == TRUE` spoof edilir). PLC, çekvalf kapalı sanarak aynı hatta paralel ikinci pompayı devreye alır veya duran pompayı yeniden başlatmaya çalışır.

#### 2. Fiziksel ve Süreç Hasarı
Basma hattındaki tonlarca su duran pompadan geriye doğru akarak çarkı ters yönde aşırı yüksek devirde döndürür. Bu sırada motora yol verildiğinde ters tork nedeniyle pompa mili anında kopar, kaplin parçalanır ve motor sargıları patlar.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Geri Dönüş Önleme Mandalı (Mechanical Backstop):** Pompa ve motor kaplini arasına yerleştirilen mekanik kilit sistemi milin ters yönde dönmesini fiziksel olarak engeller.
- Çekvalf mekanik ağırlık koluna doğrudan bağlı hardwired limit sviçleri.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Giriş-Çıkış Basınç Diferansiyeli Kontrolü:** Pompa basma basıncı hat basıncından düşükse ve akış ters yöndeyse motor yol verme komutu donanımsal olarak bloke edilir.

#### 5. Ağ ve Protokol Savunması
- Saha enstrümanları ile RTU arasındaki dijital I/O modülleri izole edilmiş saha veriyolu üzerinden haberleşir.

#### 6. Algılama ve OT SOC İmzası
- Pompa durduktan sonra basma hattı basıncının düşmemesi ve şebeke debisinin geriye akması durumunda OT SOC alarmı oluşturulur.

---

### SU-12: Koagülant Dozaj Kontrolünün Bozulması ile Çöktürme Havuzu İşlevsizliği

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Ham su girişindeki koagülant (Alüminyum sülfat veya Demir-3-klorür) dozajlama pompası hızı sıfırlanır veya ham su bulanıklık sinyali 0 NTU olarak iletilir.

#### 2. Fiziksel ve Süreç Hasarı
Küçük koloidal parçacıklar floklaşamaz ve çökelmez. Durultucu havuzlarından doğrudan filtrelere geçen çamurlu su, filtreleri dakikalar içinde bozar ve şebekeye bulanık, ağır metaller içeren su verilir.

#### 3. Donanımsal ve Mekanik Savunma
- Koagülant besleme borusuna monte edilen mekanik debimetre çıkış kontağı, kimyasal akışı kesildiğinde ana ham su giriş savak kapaklarını yerçekimi kuvvetiyle otomatik kapatır.

#### 4. Yazılımsal ve Mantıksal Savunma
- Ham su debisi ile kimyasal dozaj pompası strok sayısı arasında zorunlu oran kontrolü (Ratio Control) uygulanır; kimyasal akışı olmadan ham su vanası açılamaz.

#### 5. Ağ ve Protokol Savunması
- Dozaj kontrol PLC'si seviye 1 alt ağında kilitlenir.

#### 6. Algılama ve OT SOC İmzası
- Ham su debisi varken koagülant seviyesinin eksilmemesi analitiği çalıştırılır.

---

### SU-13: Basınç Düşürücü Vana (PRV) Manipülasyonu ile Şehir Şebekesinde Boru Patlaması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yüksek kotlu depodan şehre inen ana besleme hattındaki elektronik kontrollü Basınç Düşürücü Vana (PRV) setpointi 3.5 bardan 16 bara çıkartılır.

#### 2. Fiziksel ve Süreç Hasarı
Şehir içi dağıtım şebekesindeki PVC ve düktil borular, ev bağlantıları ve su sayaçları yüksek basınca dayanamayarak yüzlerce noktadan patlar; sokakları su basar ve şehir genelinde basınçsızlık oluşur.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Pilot Emniyet Vanası:** Elektronik kontrolör arızalansa dahi mekanik pilot yay ayarı vananın çıkış basıncını fiziksel olarak maksimum 5.0 bar ile sınırlar.

#### 4. Yazılımsal ve Mantıksal Savunma
- Çıkış basınç sensörü 5.0 barı aştığında ana izolasyon vanasını kapatan yerel acil durum mantığı.

#### 5. Ağ ve Protokol Savunması
- PRV kontrol RTU'larında DNP3 Secure Authentication (SAv5) zorunlu tutulur.

#### 6. Algılama ve OT SOC İmzası
- Dağıtım bölgelerindeki (DMA) ani basınç yükselmesi alarmları coğrafi bilgi sistemi (GIS) ile eşleştirilir.

---

### SU-14: Yağmur Suyu / Taşkın Savak Kapaklarının Kapatılması ile Şehir İçi Su Geri Tepmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Şiddetli yağış uyarısı sırasında atıksu/yağmur suyu terfi istasyonundaki tahliye savak kapakları kapatılır ve taşkın pompaları devre dışı bırakılır. HMI'da su seviyesi düşük gösterilir.

#### 2. Fiziksel ve Süreç Hasarı
Kanalizasyon hatları taşar; şehir merkezinde caddeleri, alt geçitleri ve binaların bodrum katlarını pis su basar; can ve mal kaybı tehlikesi oluşur.

#### 3. Donanımsal ve Mekanik Savunma
- **Yerçekimli Acil Durum Taşma Savağı (Gravity Overflow Spillway):** Otomasyona bağlı olmayan, belirli kotun üstündeki suyu doğrudan denize/nehre tahliye eden mekanik betonarme savak yapısı.

#### 4. Yazılımsal ve Mantıksal Savunma
- Bağımsız şamandıra seviye anahtarları aktif olduğunda PLC'deki tüm durdurma komutları baypas edilerek pompalar tam güçte çalıştırılır.

#### 5. Ağ ve Protokol Savunması
- Kritik taşkın istasyonlarında hücresel erişim IPsec VPN ve donanımsal kimlik modülleriyle (eSIM / PKI) korunur.

#### 6. Algılama ve OT SOC İmzası
- Meteoroloji radar verisi ile pompa çalışma durumları çapraz denetlenir.

---

### SU-15: Laboratuvar ve LIMS Telemetrisinin Bozulması ile Kritik Kirlenmenin Gizlenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Arıtma tesisi laboratuvar bilgi yönetim sistemindeki (LIMS) su kalitesi analiz sonuçları (ağır metal, arsenik, siyanür, mikrobiyoloji) saldırgan tarafından tahrif edilerek parametreler sınır değerlerin altında gösterilir.

#### 2. Fiziksel ve Süreç Hasarı
Zehirli veya kontamine su saatlerce/günlerce şehre pompalanır; halk sağlığı felaketi meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- Kritik spektrofotometre ve analiz cihazları yerel termal yazıcıdan ıslak imzalı fiziksel çıktı üretir; kağıt kayıtlar yasal arşivde saklanır.

#### 4. Yazılımsal ve Mantıksal Savunma
- LIMS veritabanı kayıtlarında kriptografik blokzincir/HMAC imzalama kullanılır; geçmişe dönük değiştirilen değerler sistem tarafından geçersiz sayılır.

#### 5. Ağ ve Protokol Savunması
- LIMS ağı ile SCADA ağı arasında Veri Diyodu (Data Diode) kullanılır; LIMS üzerinden SCADA'ya çift yönlü erişim engellenir.

#### 6. Algılama ve OT SOC İmzası
- LIMS veri tabanındaki SQL `UPDATE` sorguları audit logları üzerinden SOC tarafından denetlenir.
