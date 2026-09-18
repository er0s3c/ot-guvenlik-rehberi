# Elektrik ve Enerji Sistemleri: Saldırgan ve Savunma Senaryoları

[Katalog Ana Sayfası](README.md) · [Elektrik ve Enerji Temel Rehberi](../02-elektrik-ve-enerji.md) · [Raylı Sistemler Senaryoları](03-rayli-sistemler-senaryolari.md)

Bu belgede elektrik üretimi, iletimi, dağıtımı ve dağıtık enerji kaynaklarında (DER/BESS) yer alan siber-fiziksel sistemlere yönelik **15 ayrıntılı saldırgan senaryosu** ve her senaryoya karşılık gelen **çok katmanlı mühendislik ve siber savunma çözümleri** yer almaktadır.

---

## Senaryo Özeti ve Matris

| Senaryo Kodu | Proses Alanı | Saldırganın Amacı | Fiziksel Risk / Sonuç | Birincil Savunma Mekanizması |
|---|---|---|---|---|
| `ENE-01` | Yüksek Gerilim Kesici | Kesiciyi peş peşe açıp kapama (thrashing) | Ark patlaması, gaz sızıntısı, kesici imhası | Mekanik anti-pumping rölesi & açma sayacı kilit |
| `ENE-02` | Jeneratör Senkronizasyonu | Senkroçek (ANSI 25) baypas | Jeneratör rotoru mil kırılması, yangın | Hardwired senkroçek rölesi & faz açısı interlock |
| `ENE-03` | Güç Trafosu / LTC | Kademe değiştiriciyi uç değerlere sürme | Aşırı gerilim, izolasyon delinmesi, çökme | Mekanik kademe limit sviçleri & gerilim rölesi |
| `ENE-04` | Trafo Merkezi Otomasyonu | Sahte IEC 61850 GOOSE Trip mesajı | Fiderlerin haksız açılması, bölgesel karartma | IEC 62351-6 GOOSE kimlik doğrulama & VLAN |
| `ENE-05` | Koruma Rölesi (IED) | CT/PT dönüştürme oranını değiştirme | Kısa devrede rölenin açmaması, trafo yangını | Röle ayar dosyası kriptografik imza & kilit |
| `ENE-06` | Dağıtık Enerji (Güneş/Rüzgar) | Ters güç ve frekans limitlerini bozma | Dağıtım trafolarının aşırı yüklenmesi, ada modu | Donanımsal ters güç rölesi (ANSI 32R) |
| `ENE-07` | İletim SCADA / AGC | Frekans/yük sapma sinyalini bozma | Enterkonnekte frekans salınımı ve blackout | Bağımsız yerel droop kontrolü & AGC filtreleme |
| `ENE-08` | Senkrofazör (PMU / WAMS) | GPS zaman sinyali spoofing | Faz açısı hesaplama hatası, yanlış yük atma | Çoklu takımyıldız GNSS alıcı & PTP yedekleme |
| `ENE-09` | Batarya Depolama (BESS) | BMS şarj/sıcaklık limitlerini baypas | Lityum-iyon bataryada termal kaçak ve yangın | Bağımsız analog aşırı sıcaklık/gaz kesme sistemi |
| `ENE-10` | İletim Hattı Koruma | Mesafe rölesi (21) zonlarını genişletme | Yük akımında hatalı açma, kaskat karartma | Yük istilası (load encroachment) blokaj mantığı |
| `ENE-11` | Gaz İzoleli Şalt (GIS) | SF6 gaz basıncını normal gösterme | Ark sönümlenememesi, şalt patlaması | Hardwired SF6 mekanik basınç düşüş kilidi |
| `ENE-12` | Trafo Diferansiyel Koruma | 2. harmonik inrush blokajını kapatma | Enerjilendirme anında trafonun haksız açması | Donanımsal 87T röle gömülü algoritma koruması |
| `ENE-13` | Dağıtım Şebekesi | Anti-islanding korumasını devre dışı bırakma | Hatta gerilim kalması, bakım personeli can kaybı | Pasif RocoF & aktif frekans kaydırma kiti |
| `ENE-14` | Şebeke Kararlılığı (STATCOM) | Reaktif güç kazanç parametrelerini bozma | Sub-senkron rezonans, şebeke aşırı gerilimi | Fiziksel rezonans sönümleme filtresi & sınır kiti |
| `ENE-15` | Acil Durum Yük Atma | UFLS frekans açma eşiklerini bozma | Frekans çöküşünde kritik hastanelerin kesilmesi | Korumalı IED firmware & yerel frekans kilitleri |

---

## Ayrıntılı Senaryolar ve Savunma Mühendisliği

### ENE-01: Kesici Avlanması (Circuit Breaker Thrashing) ile Ark Patlaması ve Kesici İmhası

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, trafo merkezi RTU veya koruma rölesine (IED) IEC 60870-5-104 veya DNP3 protokolü üzerinden saniyede 5-10 kez ardışık `TRIP` (aç) ve `CLOSE` (kapa) komutları gönderir. Kesicinin açma-kapama yay kurma mekanizması (spring charge motor) ve kesme hücreleri aşırı zorlanır.

#### 2. Fiziksel ve Süreç Hasarı
Yüksek gerilim (154 kV / 380 kV) kesicileri her açmada yüksek enerjili elektrik arkına maruz kalır. Kesici kontakları erir, SF6 gazı ayrışarak toksik gazlara dönüşür, söndürme hücresinde dielektrik dayanım sıfırlanır ve kesici gövdesi büyük bir patlamayla parçalanarak etrafa şarapnel saçar.

#### 3. Donanımsal ve Mekanik Savunma (Layer 0/1)
- **Mekanik Anti-Pumping (Pompalama Önleme) Rölesi (ANSI 94):** Kesici kontrol panosuna hardwired olarak bağlanan anti-pumping rölesi, kesici kapama komutu aktifken açma sinyali gelirse kapama devresini mekanik olarak kilitler; komut kesilip yeniden verilmedikçe kesicinin tekrar kapanmasına izin vermez.
- **Kesici Açma Sayısı / Enerji Akümülasyon Kilidi:** Kısa sürede 3'ten fazla açma-kapama yapıldığında kesici kapama bobininin enerjisini kesen mekanik/termal koruma rölesi.

#### 4. Yazılımsal ve Mantıksal Savunma (IED Seviyesi)
- **IED Minimum Ölü Zaman (Dead-Time) Kuralı:** IED mantığında iki açma/kapama işlemi arasına minimum 300 ms - 3 saniye gecikme zorunluluğu konur; peş peşe gelen komutlar firmware seviyesinde yok sayılır.
- **Yay Kurulma Durum İnterlocku:** Kesici yay mekanizması tam kurulmadan (`Spring_Charged == TRUE`) kapama komutu bloke edilir.

#### 5. Ağ, Protokol ve Erişim Savunması
- IEC 60870-5-104 haberleşmesinde IEC 62351-3/5 TLS ve kriptografik kimlik doğrulama zorunlu tutulur.
- Kesici kumanda komutları için "Select-Before-Operate" (SBO) mekanizması ve PAM üzerinden oturum kaydı işletilir.

#### 6. Algılama ve OT SOC İmzası
- **Suricata/Zeek:** Aynı IED adresine 10 saniye içinde birden fazla 104 `Single Command (C_SC_NA_1)` veya `Double Command (C_DC_NA_1)` akışı tespit edildiğinde yüksek öncelikli alarm üretilir.

---

### ENE-02: Senkroçek (ANSI 25) Baypas Edilerek Jeneratörün Faz Dışı Şebekeye Bağlanması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Senkron jeneratör şebekeye bağlanırken gerilim, frekans ve faz açısının şebekeyle tam uyumlu olması gerekir. Saldırgan, jeneratör kesici kontrol lojiğindeki Senkroçek Rölesi (Synchrocheck Relay - ANSI 25) doğrulama kontağını yazılımsal olarak `TRUE` değerine sabitler ve jeneratör şebekeyle 180° faz farkındayken kesici kapama komutu gönderir.

#### 2. Fiziksel ve Süreç Hasarı
Jeneratör kutupları ile şebeke arasındaki devasa gerilim farkı nedeniyle nominal akımın 10-15 katı büyüklüğünde bir kısa devre torku oluşur. Jeneratör şaftı burularak kırılır, türbin kanatları parçalanır, jeneratör statoru yerinden fırlar ve santralde yangın çıkar; milyonlarca dolarlık geri dönülemez fiziksel hasar oluşur.

#### 3. Donanımsal ve Mekanik Savunma
- **Bağımsız Hardwired Senkronizasyon Rölesi:** PLC veya DCS'den bağımsız, doğrudan jeneratör ve şebeke gerilim trafolarına (PT) bağlı mikroişlemcili harici senkroçek rölesi kullanılır. Bu rölenin kuru kontağı, kesici kapama bobinine fiziksel olarak seri bağlanır. $\Delta V > \%5$, $\Delta f > 0.1\text{ Hz}$ veya $\Delta \theta > 10^\circ$ ise kontak fiziksel olarak kapanmaz.

#### 4. Yazılımsal ve Mantıksal Savunma
- Otomasyon yazılımında jeneratör hız regülatörü (Governor) ve otomatik voltaj regülatörü (AVR) değerleri ile şebeke bara değerleri arasında çift kanallı tutarlılık denetimi yapılır.

#### 5. Ağ ve Protokol Savunması
- Jeneratör kontrol sistemi (DCS) ile trafo merkezi şalt sahası arasındaki kumanda hatları ayrı fiziksel fiber optik kablo ve izole protokollerle taşınır.

#### 6. Algılama ve OT SOC İmzası
- Jeneratör bara gerilimi ile şebeke bara gerilimi arasındaki faz açısı historian analizinde izlenir.

---

### ENE-03: Güç Trafosu Kademe Değiştirici (LTC) Limitlerinin Zorlanması ile Gerilim Çökmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Büyük güç trafolarının Yük Altında Kademe Değiştiricisine (Load Tap Changer - LTC) Modbus veya DNP3 üzerinden sürekli `TAP_UP` veya `TAP_DOWN` komutları gönderilerek gerilim seviyesi aşırı yükseltilir veya düşürülür.

#### 2. Fiziksel ve Süreç Hasarı
Aşırı gerilim durumunda tüketici cihazları yanar ve trafo izolasyonu delinir. Düşük gerilim durumunda ise asenkron motorlar aşırı akım çekerek kilitlenir; dağıtım bölgesinde gerilim çökmesi (voltage collapse) ve bölgesel elektrik kesintisi meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Kademe Sınır Anahtarları (Mechanical Limit Switches):** LTC tahrik mekanizması miline bağlanan fiziksel limit sviçleri, kademenin belirlenen güvenli aralık (örneğin $\pm 8$ kademe) dışına çıkmasını elektriksel olarak engeller.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Otomatik Voltaj Regülatörü (AVR) Band-Pass Kilidi:** Çıkış gerilimi nominalin $\pm \%10$'unu aştığında yerel AVR sistemi tüm harici kademe komutlarını kilitler.

#### 5. Ağ ve Protokol Savunması
- Trafo kontrol panelleri IED seviyesinde şifreli haberleşmeyle korunur.

#### 6. Algılama ve OT SOC İmzası
- 5 dakika içinde 3'ten fazla kademe hareketi kaydedildiğinde SCADA ve SOC ekranlarında anomali uyarısı üretilir.

---

### ENE-04: Sahte IEC 61850 GOOSE Trip Mesajı Enjeksiyonu ile Trafo Merkezinin Karartılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, trafo merkezi istasyon veriyoluna (Station Bus) sızarak koruma röleleri arasındaki IEC 61850 GOOSE (Generic Object Oriented Substation Events) mesajlarını dinler. Ardından artırılmış durum numarası (`stNum`) ve sıra numarası (`sqNum`) ile sahte bir `Busbar_Protection_TRIP` (Bara Koruma Açması) GOOSE çerçevesi yayınlar (multicast).

#### 2. Fiziksel ve Süreç Hasarı
Bara koruma rölesinden geldiği sanılan mesajı alan tüm fider kesicileri milisaniyeler içinde açılarak trafo merkezine bağlı yüz binlerce abonenin ve sanayi tesisinin elektriği anında kesilir.

#### 3. Donanımsal ve Mekanik Savunma
- Kritik açma devrelerinde GOOSE mesajına ek olarak fiziksel yardımcı kontak doğrulaması aranır (Hardwired Cross-Trip).

#### 4. Yazılımsal ve Mantıksal Savunma
- **IEC 62351-6 Dijital İmzalı GOOSE:** Her GOOSE mesajı simetrik anahtarlar ve HMAC-SHA256 ile kriptografik olarak imzalanır. İmzası doğrulanmayan sahte paketler IED işlemcisi tarafından doğrudan atılır.
- **GOOSE Zaman ve Sıra Tutarlılığı:** Gelen mesajın `stNum` değeri beklenmedik şekilde zıplamışsa veya zaman damgası geride kalmışsa röle mesajı reddeder.

#### 5. Ağ ve Protokol Savunması
- Trafo merkezinde IEEE 802.1Q VLAN segmentasyonu uygulanır; GOOSE trafiği sadece ilgili koruma IED'lerinin portlarına sınırlandırılır ve port güvenliği (MAC filtering / 802.1X) uygulanır.

#### 6. Algılama ve OT SOC İmzası
- İstasyon ağına bağlı OT IDS sensörü, beklenmeyen kaynak MAC adreslerinden gelen GOOSE paketlerini veya `stNum` anomalilerini anında raporlar.

---

### ENE-05: Akım/Gerilim Trafosu (CT/PT) Oran Manipülasyonu ile Korumanın Körleştirilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Mesafe veya aşırı akım koruma rölesinin (ANSI 50/51) ayar dosyası (CID/SCL dosyası) uzaktan değiştirilerek Akım Trafosu (CT) dönüştürme oranı 1000/5 A değerinden 5000/5 A değerine çekilir.

#### 2. Fiziksel ve Süreç Hasarı
Hatta 2000 A gibi yıkıcı bir kısa devre akımı aktığında röle bu akımı 400 A olarak ölçer ve arıza akımını normal yük akımı sanarak kesiciyi açtırmaz. Kısa devre trafoları patlatır, iletim hatları eriyip kopar ve geniş çaplı yangın çıkar.

#### 3. Donanımsal ve Mekanik Savunma
- **Fiziksel Ayar Kilidi Anahtarı (Hardwired Key-Switch):** Röle parametrelerinin değiştirilmesi için ön paneldeki fiziksel anahtarın `UNLOCKED` konumuna getirilmesi zorunludur.

#### 4. Yazılımsal ve Mantıksal Savunma
- **Ayar Dosyası Hash Bütünlük Denetimi:** Röle konfigürasyonunun SHA-256 hash değeri periyodik olarak doğrulanır; onaylı mühendislik temel sürümünden sapan ayarlar durumunda röle `ALARM_SETTING_MISMATCH` verir.

#### 5. Ağ ve Protokol Savunması
- Röle konfigürasyon portlarına erişim sadece yetkili PAM sunucusu üzerinden çift faktörlü kimlik doğrulama ile sağlanır.

#### 6. Algılama ve OT SOC İmzası
- Trafo merkezi mühendislik erişim loglarında `WriteParameter` komutları SOC tarafından taranır.

---

### ENE-06: Dağıtık Enerji Kaynaklarında (DER) Ters Güç ve Anti-Islanding Korumasının Bozulması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Büyük ölçekli güneş (GES) veya rüzgar (RES) santrallerindeki merkezi güç kontrolörüne (Power Plant Controller - PPC) sızılarak IEEE 1547 / şebeke kodu parametreleri bozulur; şebeke koptuğunda santralin üretimi kesmesi engellenir.

#### 2. Fiziksel ve Süreç Hasarı
Ana iletim hattı enerjisiz kalmasına rağmen santral dağıtım şebekesini kontrolsüz olarak beslemeye devam eder (islanding). Şebeke tamirine çıkan bakım teknisyenleri hatta enerji yok sanırken yüksek gerilime kapılarak hayatını kaybedebilir. Şebeke tekrar bağlandığında faz dışı bağlanma ile santral inverterleri patlar.

#### 3. Donanımsal ve Mekanik Savunma
- Trafo bağlantı noktasına monte edilen bağımsız mekanik/analog frekans ve ters güç koruma rölesi (ANSI 32R).

#### 4. Yazılımsal ve Mantıksal Savunma
- Aktif frekans kaydırma (Active Frequency Drift) ve RocoF ($df/dt$) algılama algoritmaları inverter DSP firmware seviyesinde kilitlenir.

#### 5. Ağ ve Protokol Savunması
- DER ağ geçidi (Gateway) ile SCADA arasında DNP3 SAv5 veya IEEE 2030.5 güvenli profilleri kullanılır.

#### 6. Algılama ve OT SOC İmzası
- Şebeke fider kesicisi açıkken DER çıkış akımının sıfırlanmaması durumu SCADA'da yüksek öncelikli güvenlik alarmı tetikler.

---

### ENE-07: Otomatik Üretim Kontrolü (AGC) Sinyal Manipülasyonu ile Enterkonnekte Kararsızlık

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Yük Tevzi Merkezi (EMS) ile büyük santraller arasındaki Otomatik Üretim Kontrolü (AGC) telemetri hattına müdahale edilerek frekans hatası ($ACE$ - Area Control Error) ters yönde manipüle edilir; santrallere talep yokken aşırı yük artırma komutu gönderilir.

#### 2. Fiziksel ve Süreç Hasarı
Şebeke frekansı 50.0 Hz nominal değerinden 51.5 Hz üzerine çıkar; aşırı frekans nedeniyle diğer santraller korumaya geçerek peş peşe devreden çıkar (kaskat çökme ve enterkonnekte sistemin bölünmesi).

#### 3. Donanımsal ve Mekanik Savunma
- Türbin hız regülatörlerinde (Governor) mekanik santrifüj ağırlıklı aşırı hız trip sistemi (Overspeed Trip Mechanism).

#### 4. Yazılımsal ve Mantıksal Savunma
- **Yerel Droop Kontrolü Önceliği:** Türbin kontrolörü yerel frekans ölçümünü AGC komutunun üzerinde tutar; AGC ile yerel frekans çelişirse yerel ölçüm baz alınır.

#### 5. Ağ ve Protokol Savunması
- EMS ile santraller arasındaki ICCP / TASE.2 protokolünde IEC 62351-4 güvenli bağlantı ve sertifika tabanlı kimlik doğrulama uygulanır.

#### 6. Algılama ve OT SOC İmzası
- TASE.2 oturumlarındaki veri paketlerinin kriptografik doğrulaması ve ACE sinyalinin rate-of-change analizi yapılır.

---

### ENE-08: Senkrofazör (PMU) GPS Zaman Senkronizasyonu Spoofing ile Analizlerin Yanıltılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Geniş Alan İzleme Sistemlerinde (WAMS) kullanılan Fazör Ölçüm Birimlerine (PMU) sahte GPS/GNSS RF sinyalleri yayınlanarak (spoofing) zaman damgası birkaç mikrosaniye kaydırılır.

#### 2. Fiziksel ve Süreç Hasarı
Senkrofazör faz açısı $\theta = 2\pi f t$ formülüne dayanır. 1 mikrosaniyelik hata, şebekede devasa bir faz açısı farkı gibi görünür. Otomatik şebeke dengeleme sistemleri yanlış güç salınımı varsayımıyla sağlam hatları açtırarak şebekeyi karartabilir.

#### 3. Donanımsal ve Mekanik Savunma
- Çoklu takımyıldız (GPS + Galileo + GLONASS) destekli, anti-jamming/anti-spoofing anten teknolojisine sahip GNSS alıcıları.
- Karasal IEEE 1588 PTP (Precision Time Protocol) fiber optik yedekleme hattı.

#### 4. Yazılımsal ve Mantıksal Savunma
- Komşu trafo merkezlerindeki PMU verileriyle çapraz fazör doğrulama algoritması.

#### 5. Ağ ve Protokol Savunması
- IEEE C37.118 veri akışı TLS tünelleri üzerinden şifrelenir.

#### 6. Algılama ve OT SOC İmzası
- GNSS alıcısının sinyal/gürültü oranı (SNR) değişimleri ve uyduların konum geometrisi (DOP) anomalileri izlenir.

---

### ENE-09: Batarya Enerji Depolama Sistemlerinde (BESS) Termal Kaçak (Thermal Runaway) Tetiklenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Büyük şebeke tipi Batarya Yönetim Sistemi (BMS) kontrolörüne sızılarak maksimum şarj voltajı sınırı yükseltilir, hücre sıcaklık alarmları susturulur ve batarya konteyneri HVAC soğutma sistemi kapatılır.

#### 2. Fiziksel ve Süreç Hasarı
Lityum-iyon batarya hücrelerinde aşırı şarj ve sıcaklık nedeniyle katot bozulması ve iç kısa devre başlar (Termal Kaçak). Zehirli ve yanıcı gazlar (HF, $H_2$, CO) açığa çıkar; kontrol edilemeyen 1000°C+ yangın ve şiddetli patlama meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- **Hardwired Bağımsız Gaz ve Termal Güvenlik Sistemi (F&G):** BMS'den bağımsız hidrojen/karbonmonoksit gaz dedektörleri ve optik alev sensörleri, eşik aşıldığında ana DC kontaktörünü mekanik olarak açar ve Novec 1230 / aerosol yangın söndürmeyi başlatır.
- Batarya modül seviyesinde donanımsal eriyen sigortalar (Pyrofuses).

#### 4. Yazılımsal ve Mantıksal Savunma
- Hücre gerilimleri arasında 50 mV'tan fazla sapma olduğunda şarjı durduran bağımsız güvenlik lojiği.

#### 5. Ağ ve Protokol Savunması
- BESS kontrol ağı, santral SCADA ağından endüstriyel güvenlik duvarıyla ayrılır.

#### 6. Algılama ve OT SOC İmzası
- Batarya şarj akımı varken HVAC gücünün sıfıra düşmesi korelasyonu SOC tarafından izlenir.

---

### ENE-10: İletim Hattı Mesafe Koruma Rölesi (ANSI 21) Zonlarının Bozulması ile Kaskat Karartma

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
380 kV iletim hattı koruma rölesinin Zone-3 empedans ayarı aşırı genişletilir ve yük istilası (load encroachment) blokaj fonksiyonu devre dışı bırakılır.

#### 2. Fiziksel ve Süreç Hasarı
Yaz aylarında hat aşırı yüklendiğinde ve hat telleri ısınıp sarktığında, yüksek yük akımı arıza empedansı sanılarak röle tarafından açılır. Yük komşu hatlara kayar; diğer hatlar da sırayla açılarak ülke genelinde kaskat sistem çöküşü yaşanır.

#### 3. Donanımsal ve Mekanik Savunma
- İletim hatlarında iki farklı üreticiye ait, bağımsız prensiplerle çalışan çift ana koruma rölesi (Main 1: Mesafe, Main 2: Hat Diferansiyel 87L) kullanımı.

#### 4. Yazılımsal ve Mantıksal Savunma
- IED konfigürasyonunda yük açısı ve empedans karakteristik sınırlarının yazılımsal olarak kilitlenmesi.

#### 5. Ağ ve Protokol Savunması
- Röle ayar yönetim yazılımlarında merkezi yetkilendirme ve çift onay zorunluluğu.

#### 6. Algılama ve OT SOC İmzası
- Koruma ayar dosyalarındaki değişikliklerin periyodik denetimle temel sürümle (baseline) karşılaştırılması.

---

### ENE-11: SF6 Gaz Basınç Telemetrisinin Sabitlenmesi ve Yalıtımsız Kesicinin Açtırılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Gaz İzoleli Şalt (GIS) kesicisinde SF6 gaz kaçağı oluşurken analog basınç sensörü verisi HMI ekranında 6.0 bar (normal) olarak sabitlenir. Ardından kesiciye rutin açma komutu verilir.

#### 2. Fiziksel ve Süreç Hasarı
SF6 gazı olmadan açılan kesici arkı söndüremez; oluşan devasa elektrik arkı kesici gövdesini eritir, gaz genleşmesiyle metal mahfaza patlar ve yangın şalt sahasına yayılır.

#### 3. Donanımsal ve Mekanik Savunma
- Kesici gövdesine doğrudan monte edilen mekanik yaylı SF6 düşük basınç blokaj anahtarı (ANSI 63GL), gaz basıncı 4.5 bar altına düştüğünde açma/kapama bobin devrelerini fiziksel olarak keser.

#### 4. Yazılımsal ve Mantıksal Savunma
- Basınç düşüş eğrisi ($dP/dt$) analizi ile mikro kaçakların otomatik tespiti.

#### 5. Ağ ve Protokol Savunması
- Sensör veriyolunda güvenli endüstriyel fieldbus protokolleri kullanımı.

#### 6. Algılama ve OT SOC İmzası
- Sıcaklık değişimine rağmen gaz basıncının hiçbir dalgalanma göstermemesi sensör manipülasyonu alarmı oluşturur.

---

### ENE-12: Trafo Diferansiyel Koruma (87T) 2. Harmonik Blokajının Bozulması ile Yanlış Açma

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Büyük güç trafosunun diferansiyel koruma rölesindeki (ANSI 87T) trafo devreye girme anı mıknatıslanma akımı (inrush current) 2. harmonik blokaj filtresi kapatılır.

#### 2. Fiziksel ve Süreç Hasarı
Trafo her enerjilendirildiğinde oluşan doğal mıknatıslanma akımı iç arıza sanılarak trafo anında açtırılır; trafo devreye alınamaz ve bölge elektriksiz kalır.

#### 3. Donanımsal ve Mekanik Savunma
- Trafo diferansiyel rölesi firmware koruma algoritmalarının değiştirilemez ROM bellekte tutulması.

#### 4. Yazılımsal ve Mantıksal Savunma
- Diferansiyel akım ile 2. harmonik oranının ($I_{2nd} / I_{fund} > \%15$) donanımsal mantıkta zorunlu kılınması.

#### 5. Ağ ve Protokol Savunması
- Trafo merkezinde yönetim trafiğinin şifrelenmesi.

#### 6. Algılama ve OT SOC İmzası
- Trafo açma olay kayıtlarının (COMTRADE) otomatik analizi.

---

### ENE-13: Dağıtım Şebekesinde Kontrolsüz Ada Modu Tetiklenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Dağıtım fideri başındaki kesici açılarak fider şebekeden izole edilirken, fider üzerindeki dizel jeneratör ve GES'lerin çalışmaya devam etmesi sağlanır.

#### 2. Fiziksel ve Süreç Hasarı
Gerilim ve frekans kontrolsüzce dalgalanır; şebeke üzerinde çalışan hat teknisyenleri elektriğe kapılma riskiyle karşılaşır.

#### 3. Donanımsal ve Mekanik Savunma
- Fider başında ve tüm DER noktalarında Transfer Trip (Aktarmalı Açma) hardwired fiber/pilot tel hattı.

#### 4. Yazılımsal ve Mantıksal Savunma
- Pasif RocoF ve gerilim vektör kayması (Vector Shift) korumaları.

#### 5. Ağ ve Protokol Savunması
- Dağıtım otomasyonunda DNP3 Secure Authentication.

#### 6. Algılama ve OT SOC İmzası
- Ana kesici açıkken hatta gerilim telemetrisinin sürmesi durumunun yakalanması.

---

### ENE-14: STATCOM Reaktif Güç Parametrelerinin Manipülasyonu ile Sub-Senkron Rezonans

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
STATCOM / SVC kontrolöründeki voltaj kontrol kazanç katsayıları ($K_p, K_i$) aşırı yükseltilerek şebekeye yüksek frekanslı reaktif güç salınımları enjekte edilir.

#### 2. Fiziksel ve Süreç Hasarı
Şebekedeki jeneratör şaftları ile elektriksel rezonans (Sub-Synchronous Resonance - SSR) oluşur; jeneratör rotorları rezonans torkuyla mekanik yorulmaya uğrar ve şaftlar çatlar.

#### 3. Donanımsal ve Mekanik Savunma
- Jeneratör şaftlarına monte edilen burulma gerilimi izleme (Torsional Stress Monitoring) koruma röleleri.

#### 4. Yazılımsal ve Mantıksal Savunma
- STATCOM kontrolöründe rezonans frekanslarını süzen aktif çentik filtreleri (Notch Filters).

#### 5. Ağ ve Protokol Savunması
- STATCOM dijital kontrol kartlarına harici ağ erişiminin yasaklanması.

#### 6. Algılama ve OT SOC İmzası
- PMU fazör verilerinde 10-40 Hz arası salınımların spektral analizi.

---

### ENE-15: Düşük Frekans Yük Atma (UFLS) Tablolarının Değiştirilerek Kritik Tesislerin Kesilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Frekans düşüşünde devreye giren otomatik yük atma (UFLS - ANSI 81L) röle tabloları manipüle edilir; sanayi bölgeleri yerine hastaneler, su arıtma tesisleri ve askeri üsler ilk açılacak 1. kademeye (49.5 Hz) yazılır.

#### 2. Fiziksel ve Süreç Hasarı
Küçük bir üretim kaybında şebeke frekansı hafifçe düştüğünde kritik kamu altyapıları anında elektriksiz kalarak can ve mal güvenliği tehlikeye girer.

#### 3. Donanımsal ve Mekanik Savunma
- Kritik tesis fider rölelerinde UFLS açma fonksiyonunun donanımsal köprüyle (jumper) fiziksel olarak iptal edilmesi.

#### 4. Yazılımsal ve Mantıksal Savunma
- Yük atma matrisinin merkezi SCADA tarafından her 24 saatte bir hash kontrolü ile doğrulanması.

#### 5. Ağ ve Protokol Savunması
- Fider IED'lerine konfigürasyon yükleme yetkisinin merkezi PKI sertifikasına bağlanması.

#### 6. Algılama ve OT SOC İmzası
- UFLS açma olaylarının hedef fider isimleriyle karşılaştırmalı analizi.
