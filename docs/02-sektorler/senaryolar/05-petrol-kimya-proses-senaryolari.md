# Petrol, Doğal Gaz ve Kimya Prosesleri: Saldırgan ve Savunma Senaryoları

[Katalog Ana Sayfası](README.md) · [Petrol, Gaz ve Kimya Temel Rehberi](../05-petrol-gaz-ve-kimya.md) · [Su ve Atıksu Senaryoları](01-su-ve-atiksu-senaryolari.md)

Bu belgede petrol ve doğal gaz boru hatları, rafineriler, petrokimya tesisleri, kimyasal reaktörler ve depolama terminallerindeki siber-fiziksel süreçlere yönelik **10 ayrıntılı saldırgan senaryosu** ve her senaryoya karşılık gelen **çok katmanlı mühendislik ve siber savunma çözümleri** yer almaktadır.

---

## Senaryo Özeti ve Matris

| Senaryo Kodu | Proses Alanı | Saldırganın Amacı | Fiziksel Risk / Sonuç | Birincil Savunma Mekanizması |
|---|---|---|---|---|
| `PET-01` | Boru Hattı / Kompresör | PSV kilitliyken basma basıncını artırma | Boru hattının yırtılması ve gaz patlaması | Mekanik yaylı basınç emniyet ventili (PSV) |
| `PET-02` | Rafineri Distilasyon | Kaskat sıcaklık ve reflü döngüsünü bozma | Kolon aşırı basıncı, termal taşkın ve yangın | Mekanik patlama diski ve bağımsız SIS |
| `PET-03` | Acil Duruş (ESD / SIS) | SIL 3 emniyet lojik bloklarını baypas etme | Tehlike anında tesisin güvenli duramaması | Hardwired emniyet köprüsü anahtarı & Safety PLC |
| `PET-04` | Gaz & Yangın Algılama (F&G) | H2S ve LEL dedektörlerini sıfırda dondurma | Zehirli gaz zehirlenmesi, tespitsiz patlama | 4-20mA arıza akımı (2mA) denetimi & 2oo3 |
| `PET-05` | Boru Hattı Pigging Kapanı | Kapan basınçlıyken kapak kilidini açma | Yüksek basınçlı kapağın fırlaması, can kaybı | Mekanik kilitli interlock (Trapped Key Interlock) |
| `PET-06` | Gaz Kompresörü | Anti-surge vana setpointini bozma | Kompresörde şiddetli surge ve kanat kırılması | Bağımsız donanımsal anti-surge kontrolörü |
| `PET-07` | Ekzotermik Kimyasal Reaktör | Ceket soğutma vanasını kapatıp ısıtma | Kontrolden çıkan reaksiyon (runaway) ve infilak | Bağımsız reaktör acil kimyasal söndürme/boşaltma |
| `PET-08` | Akaryakıt Depolama Tankı | Radar seviye sensörünü düşükte sabitleme | Tank taşması, hidrokarbon yangını | Bağımsız yüksek-yüksek seviye mekanik şamandırası |
| `PET-09` | Boru Hattı Korozyon Önleme | Katodik koruma potansiyelini düşürme | Yer altı borusunun delinmesi ve çevre kirliliği | Periyodik bağımsız kupon ölçümü & akım izleme |
| `PET-10` | Meşale Sistemi (Flare) | Alev sensörünü (flame scanner) spoof etme | Yanmamış zehirli gazların atmosfere salınımı | Çoklu optik spektrum dedektörü & pilot alev |

---

## Ayrıntılı Senaryolar ve Savunma Mühendisliği

### PET-01: Boru Hattı Basınç Tahliyesinin Kilitlenmesi ve Kompresör Aşırı Basıncı ile Boru Yırtılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Doğal gaz iletim boru hattı kompresör istasyonunda, saldırgan ana boru hattı basınç sensörü (Pressure Transmitter) registerını 65 bar (normal) olarak sabitler. Eşzamanlı olarak gaz türbini tahrikli santrifüj kompresör hızını maksimuma çıkarır ve otomatik deşarj tahliye vanalarını (Blowdown Valve) yazılımsal olarak kilitler.

#### 2. Fiziksel ve Süreç Hasarı
Boru hattı basıncı borunun maksimum izin verilen işletme basıncını (MAOP: 80 bar) aşarak 120 bar üzerine tırmanır. Çelik boru kaynak dikişlerinden yırtılır; yüz binlerce metreküp yüksek basınçlı metan gazı çevreye yayılır ve patlayarak devasa bir krater ve yangın fırtınası oluşturur.

#### 3. Donanımsal ve Mekanik Savunma (Layer 0/1)
- **Mekanik Yaylı Basınç Emniyet Ventili (Pressure Safety Valve - PSV):** Hiçbir elektrik, yazılım veya PLC kontrolüne bağlı olmayan, doğrudan boru iç basıncı yay kuvvetini (85 bar) aştığında mekanik olarak açılan tam orantılı tahliye ventili.
- Boru hattı aşırı basınç patlama diskleri (Rupture Discs).

#### 4. Yazılımsal ve Mantıksal Savunma (SIS Seviyesi)
- **SIL 3 Emniyet Enstrümanlı Sistemi (High-Integrity Pressure Protection System - HIPPS):** Ana proses kontrol DCS'inden tamamen bağımsız, 2oo3 oylamalı 3 adet bağımsız basınç transmitteri ve 100 milisaniye içinde kapanan hidrolik aktüatörlü çift izolasyon vanası.

#### 5. Ağ, Protokol ve Erişim Savunması
- HIPPS ve ESD sistemleri Purdue Seviye 1 emniyet bölgesinde (Safety Zone) tutulur; dış ağlardan veya kurumsal SCADA'dan programlanamaz.

#### 6. Algılama ve OT SOC İmzası
- Kompresör giriş debisi ve gaz türbini yakıt tüketimi artarken boru hattı basıncının değişmemesi durumu SOC anomali motorunda kritik alarm oluşturur.

---

### PET-02: Distilasyon Kolonu Kaskat Sıcaklık Döngüsünün Bozulması ile Termal Taşkın

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Rafineri ham petrol distilasyon kolonunda dip ısıtıcı (Reboiler) buhar vanası %100 açılırken, tepe reflü (Reflux) pompası hızı sıfırlanır. Kolon tepe sıcaklık transmitteri normal değerde dondurulur.

#### 2. Fiziksel ve Süreç Hasarı
Kolon tepsilerinde ani buharlaşma ve köpürme (foaming) meydana gelir. Kolon içi basınç hızla yükselir, hafif hidrokarbon sıvıları tepe gaz hattına taşar (flooding); kolon mekanik tepsileri çöker, tepe boruları aşırı basınçla çatlar ve yüksek sıcaklıkta hidrokarbon yangını başlar.

#### 3. Donanımsal ve Mekanik Savunma
- Kolon tepe kubbesine doğrudan monte edilen mekanik yaylı çift emniyet ventilleri (PSV) gazı doğrudan kapalı meşale (flare) sistemine yönlendirir.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Kolon Diferansiyel Basınç ve Sıcaklık Profili Doğrulaması:** Kolon alt, orta ve üst sıcaklık/basınç gradyanları matematiksel modelle izlenir; profilden sapma durumunda reboiler buharı anında kesilir.

#### 5. Ağ ve Protokol Savunması
- Rafineri DCS kontrol düğümleri arasında Foundation Fieldbus / HART-IP şifreli profilleri kullanılır.

#### 6. Algılama ve OT SOC İmzası
- Reboiler buhar debisi ile kolon dip sıcaklığı arasındaki ısı transferi denklem sapmaları izlenir.

---

### PET-03: Acil Duruş Sistemi (ESD / SIS) Lojik Bloklarının Baypas Edilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Triconex veya HIMA Safety PLC mühendislik arayüzüne sızan saldırgan, kritik reaktör acil durdurma fonksiyon bloklarına `FORCE_BYPASS` komutu gönderir.

#### 2. Fiziksel ve Süreç Hasarı
Tehlikeli proses durumu (örneğin yüksek basınç veya zehirli gaz kaçağı) oluştuğunda tesis otomatik olarak emniyetli duruşa geçemez; operatör butona bassa dahi acil kapatma vanaları (ESDV) açık kalır ve felaket boyutunda kaza gerçekleşir.

#### 3. Donanımsal ve Mekanik Savunma
- **Hardwired Emniyet Baypas Anahtarı (Physical Bypass Key):** Safety PLC yazılımında mantıksal baypas yapılabilmesi için kontrol odasındaki kilitli panoda bulunan fiziksel anahtarın çevrilmesi zorunludur.
- Saha acil duruş butonları (Emergency Push Button) doğrudan güvenlik vanası solenoit bobin gücünü keser.

#### 4. Yazılımsal ve Mantıksal Savunma
- Safety PLC firmware'inde herhangi bir mantık baypası aktifken 8 saat sonra otomatik iptal olma (Auto-Timeout) kuralı.

#### 5. Ağ ve Protokol Savunması
- Safety PLC mühendislik portları fiziksel olarak hava boşluklu (Air-Gapped) tutulur veya sadece onaylı geçici bakım cihazıyla erişilir.

#### 6. Algılama ve OT SOC İmzası
- Safety PLC konfigürasyon değişiklikleri ve `Bypass_Active` bayrakları SOC güvenlik paneline anında düşer.

---

### PET-04: Yanıcı/Zehirli Gaz (LEL CH4, H2S) Dedektörlerinin Dondurulması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Gaz işleme tesisindeki Hidrojen Sülfür ($H_2S$) ve Patlayıcı Gaz (% LEL) dedektörlerinin analog 4-20 mA sinyalleri saha I/O kartı üzerinde 4.0 mA (%0 gaz) değerinde kilitlenir.

#### 2. Fiziksel ve Süreç Hasarı
Tesiste büyük bir $H_2S$ veya hidrokarbon gaz sızıntısı başladığında hiçbir alarm çalmaz, acil havalandırma çalışmaz. Sahadaki işletme personeli birkaç nefeste $H_2S$ zehirlenmesinden hayatını kaybeder; gaz kıvılcım alarak tüm tesisi havaya uçurur.

#### 3. Donanımsal ve Mekanik Savunma
- **Donanımsal Arıza Akımı Seviyesi (Under-Range Fault Level):** Endüstriyel gaz dedektörleri arıza, kablo kopması veya donmada 2.0 mA altına iner (NAMUR NE 43 standardı). I/O kartı 2.0 mA algıladığı anda bunu otomatik "Dedektör Arızası / Acil Durum" sayar.
- Personel üzerinde taşınan bağımsız taşınabilir mekanik/elektrokimyasal kişisel gaz dedektörleri.

#### 4. Yazılımsal ve Mantıksal Savunma
- **2oo3 Gaz Algılama Oylaması:** Aynı alanda 3 ayrı gaz dedektörü kullanılır; 2 tanesi LEL algıladığında acil durum eylemleri otomatik başlar.

#### 5. Ağ ve Protokol Savunması
- Gaz & Yangın (F&G) paneli bina otomasyonu ve standart IT ağından tamamen yalıtılmış SIL 3 onaylı ağda çalışır.

#### 6. Algılama ve OT SOC İmzası
- Dedektör analog sinyal gürültüsünün (noise) tamamen sıfırlanması sensör manipülasyonu olarak raporlanır.

---

### PET-05: Boru Hattı Pigging Kapanı Emniyet Kilidinin Sahte Sinyalle Açılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Boru hattı temizleme/muayene pistonu (Pig) fırlatma veya alma kapanında (Pig Trap) hat basıncı 70 bar iken, kapan tahliye vanasının açık ve basıncın sıfır olduğu sahte telemetrisi üretilir (`Pig_Trap_Pressure == 0 bar`). Kapan hızlı açılır kapak (Quick Opening Closure) kilit selenoiti enerjilendirilir.

#### 2. Fiziksel ve Süreç Hasarı
Teknisyen kapağı açmaya çalıştığında 70 bar basınç altındaki tonlarca ağırlıktaki çelik kapak füze gibi fırlar; sahadaki personeli parçalar ve yüksek debili gaz fışkırarak alev alır.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Kilitli Anahtar Sistemi (Trapped Key Interlock - Kirk/Castell Key):** Kapan üzerindeki mekanik basınç tahliye vanası elle tam açılmadan anahtar yerinden çıkmaz; bu anahtar olmadan kapağın mekanik açma kolu fiziksel olarak döndürülemez. Hiçbir PLC veya elektrik sinyali bu mekanik kilidi baypas edemez.

#### 4. Yazılımsal ve Mantıksal Savunma
- Çift transmitter ile basınç doğrulaması ve tahliye vanası konum kontağı teyidi.

#### 5. Ağ ve Protokol Savunması
- Saha pigging kumanda panoları yerel fiziksel anahtar yetkilendirmesi gerektirir.

#### 6. Algılama ve OT SOC İmzası
- Kapan basınç değeri sıfır görünürken ana hat izolasyon vanasının açık olması anomalisi yakalanır.

---

### PET-06: Kompresör Anti-Surge Kontrolünün Manipülasyonu ile Kompresörün Parçalanması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Doğal gaz santrifüj kompresöründe gaz debisi düştüğünde kompresörün ters akışa (surge) girmesini engelleyen Anti-Surge vana kontrol algoritmasındaki güvenlik marjı (Safety Margin) eğrisi kaydırılır ve vana kapalı tutulur.

#### 2. Fiziksel ve Süreç Hasarı
Kompresör saniyede 10-15 kez şiddetli basınç ve akış geri tepmelerine (surge döngüsü) girer. Kompresör rotor kanatları kopar, radyal ve eksenel yataklar parçalanır; kompresör gövdesi çatlar ve milyonlarca dolarlık ekipman hurdaya döner.

#### 3. Donanımsal ve Mekanik Savunma
- **Hızlı Açılan Pnömatik Yaylı Geri Dönüşlü Vana:** Yay kuvvetiyle 0.5 saniye içinde tam açılan mekanik arıza-güvenli (Fail-Open) anti-surge vanası.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Bağımsız Donanımsal Anti-Surge Kontrolörü (CCC / Woodward):** DCS'ten bağımsız, 20 milisaniye çevrim süreli özel mikroişlemcili kontrolör; surge tespit ettiği an DCS komutlarını ezerek vanayı tam açar.

#### 5. Ağ ve Protokol Savunması
- Turbomakine kontrol sistemi ağ segmenti DCS kontrol veriyolundan güvenlik duvarıyla ayrılır.

#### 6. Algılama ve OT SOC İmzası
- Kompresör giriş-çıkış diferansiyel basınç salınımları SOC tarafından titreşim telemetrisiyle korele edilir.

---

### PET-07: Ekzotermik Kimyasal Reaktör Soğutmasının Kesilmesi ve Runaway İnfilakı

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yüksek derecede ekzotermik (ısı açığa çıkaran) polimerizasyon reaktöründe ceket soğutma suyu kontrol vanası kapatılır, reaktör karıştırıcı motoru durdurulur ve hammadde besleme pompaları maksimum hızda tutulur. Sıcaklık sensörü ise 80°C (normal) değerinde kilitlenir.

#### 2. Fiziksel ve Süreç Hasarı
Reaktör içinde kontrolsüz ısı ve basınç artışı (Runaway Reaction) başlar. Sıcaklık katlanarak artar, solventler kaynar, reaktör iç basıncı çelik gövdenin dayanım sınırını aşar ve reaktör devasa bir patlamayla havaya uçar; zehirli kimyasallar şehre yayılır.

#### 3. Donanımsal ve Mekanik Savunma
- **Reaktör Acil Kimyasal İnhibitör / Söndürme Enjeksiyonu (Short-Stop System):** Mekanik patlama diski yırtıldığında azot gazı basıncıyla reaksiyonu anında durduran kimyasal inhibitörü milisaniyeler içinde reaktöre basan mekanik sistem.
- Reaktör mekanik patlama diski ve tahliye havuzu (Quench Tank).

#### 4. Yazılımsal ve Mantıksal Savunma
- Çok noktalı deri ve kılıf termokuplları (Skin Thermocouples) ile 2oo4 sıcaklık oylaması. Karıştırıcı motor akımı kesilirse hammadde beslemesi donanımsal olarak durdurulur.

#### 5. Ağ ve Protokol Savunması
- Reaktör acil emniyet sistemi PROFIsafe üzerinden izole çalışır.

#### 6. Algılama ve OT SOC İmzası
- Hammadde besleme debisi pozitif iken soğutma suyu debisinin sıfır olması alarmı.

---

### PET-08: Akaryakıt Tankı Radar Seviye Sensörü Sahteciliği ile Tank Taşması ve Yangın

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
50.000 tonluk benzin depolama tankı dolum yapılırken, tank radar seviye transmitteri registerı 12.0 metre (maksimum 18 metre) seviyesinde sabitlenir. Dolum pompaları tam kapasite çalıştırılmaya devam eder.

#### 2. Fiziksel ve Süreç Hasarı
Benzin tankın tavanından taşar, yüzer tavan contalarından dışarı fışkırarak tank bendi (bund wall) havuzuna dökülür. Geniş bir alana yayılan benzin buharı kıvılcım alarak devasa bir depolama terminali yangınına yol açar.

#### 3. Donanımsal ve Mekanik Savunma
- **Bağımsız Mekanik Seviye Anahtarı (Level Safety High-High - LSHH):** Tankın en üst kotuna monte edilen, radar sensörden ve PLC'den tamamen bağımsız mekanik çatal veya şamandıralı anahtar, sıvı temas ettiği anda ana dolum boru hattı acil kesme vanasını (MOV/ROSOV) kapatır ve dolum pompasının elektriğini keser.

#### 4. Yazılımsal ve Mantıksal Savunma
- Boru hattı transfer debisi ile tank seviye yükselme hızı ($dh/dt$) arasında sürekli kütle dengesi (Mass Balance) doğrulaması.

#### 5. Ağ ve Protokol Savunması
- Tank çiftliği telemetri ağı şifreli kablosuz ISA100.11a / WirelessHART ile korunur.

#### 6. Algılama ve OT SOC İmzası
- Pompa dolum debisi varken tank seviyesinin yükselmemesi SOC ekranında yüksek öncelikli olay üretir.

---

### PET-09: Boru Hattı Katodik Koruma Potansiyelinin Düşürülmesi ile Hızlandırılmış Korozyon

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yer altı çelik doğal gaz boru hattının katodik koruma trafo/doğrultucu (TR) ünitesine sızılarak koruma potansiyeli -850 mV (CSE) standardından -400 mV seviyesine düşürülür veya DC akım polaritesi ters çevrilir.

#### 2. Fiziksel ve Süreç Hasarı
Boru hattı elektrokimyasal korozyona ve galvanik aşınmaya karşı korumasız kalır; korozyon hızı 10 katına çıkar. Aylar içinde yer altındaki boru delinecek seviyeye incelir, gaz sızıntısı ve zemin kayması meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- Kurbanlık anot yatakları (Galvanic Sacrificial Anodes) harici güç kesilse dahi temel korozyon korumasını mekanik olarak sürdürür.
- Bağımsız korozyon kuponları ve ultrasonik kalınlık ölçüm sensörleri.

#### 4. Yazılımsal ve Mantıksal Savunma
- RTU içinde referans elektrot voltaj sınırları donanımsal firmware seviyesinde kilitlenir.

#### 5. Ağ ve Protokol Savunması
- Katodik koruma uzak izleme üniteleri DNP3 Secure Authentication ile korunur.

#### 6. Algılama ve OT SOC İmzası
- Doğrultucu DC akım ve voltaj trendlerindeki ani düşüşler korozyon mühendisliği izleme paneline iletilir.

---

### PET-10: Yakma Fırını (Flare) Alev Gözetleme Sensörlerinin Spoof Edilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Rafineri meşale bacasında pilot alevin söndüğü durumda, optik alev gözetleme (Flame Scanner) sensörünün dijital çıkışı `FLAME_PRESENT == TRUE` olarak sabitlenir ve otomatik elektrikli kıvılcım ateşleyiciler kapatılır. Tesis acil tahliye vanaları açılarak meşaleye yüksek debili gaz basılır.

#### 2. Fiziksel ve Süreç Hasarı
Ateşlenmeyen zehirli ve patlayıcı hidrokarbon gazları (bütan, propan, $H_2S$) yanmadan ağır bir gaz bulutu halinde yerleşim yerlerine çöker; kitlesel zehirlenmeler ve açık hava gaz bulutu patlaması (UVCE) riski doğar.

#### 3. Donanımsal ve Mekanik Savunma
- **Sürekli Doğal Gaz Beslemeli Mekanik Pilot Alev Nozulu:** Alev sönse bile mekanik sürekli hava-gaz karışımıyla yanan rüzgara dayanıklı pilot alev başlıkları.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Çok Spektrumlu Alev Algılama (UV + IR + Termokupl):** 3 farklı fiziksel prensiple alev varlığı doğrulanır; 1 tanesi bile alev görmezse otomatik yüksek voltajlı ateşleme jeneratörü devreye girer.

#### 5. Ağ ve Protokol Savunması
- Meşale kontrol paneli yerel izole PLC ile yönetilir.

#### 6. Algılama ve OT SOC İmzası
- Meşale gaz akışı varken optik kamera spektrumunda alev ışıması olmaması alarm oluşturur.
