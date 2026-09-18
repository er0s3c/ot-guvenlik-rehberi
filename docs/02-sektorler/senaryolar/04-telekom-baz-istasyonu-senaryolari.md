# Telekomünikasyon ve Baz İstasyonu Altyapıları: Saldırgan ve Savunma Senaryoları

[Katalog Ana Sayfası](README.md) · [Telekomünikasyon Temel Rehberi](../04-telekom-ve-baz-istasyonlari.md) · [Petrol ve Kimya Senaryoları](05-petrol-kimya-proses-senaryolari.md)

Bu belgede hücresel baz istasyonları (BTS/eNodeB/gNodeB), telekom santralleri, transmisyon düğümleri ve veri merkezi fiziksel altyapılarına (HVAC, DC güç, akü, jeneratör, PTP zaman senkronizasyonu) yönelik **10 ayrıntılı saldırgan senaryosu** ve her senaryoya karşılık gelen **çok katmanlı mühendislik ve siber savunma çözümleri** yer almaktadır.

---

## Senaryo Özeti ve Matris

| Senaryo Kodu | Proses Alanı | Saldırganın Amacı | Fiziksel Risk / Sonuç | Birincil Savunma Mekanizması |
|---|---|---|---|---|
| `TEL-01` | Kabinet HVAC / CRAC | Klima kompresörünü kapatma, fanı durdurma | BBU/RF kartlarının yanması, iletişim kesintisi | Bağımsız mekanik termostat acil fan rölesi |
| `TEL-02` | -48V DC Doğrultucu | Çıkış voltajını 48V'tan 65V üzerine çıkarma | Telekom kartlarının yanması, akü patlaması | Donanımsal aşırı voltaj kesici (OVP Crowbar) |
| `TEL-03` | Akü Grubu (Li-Ion/VRLA) | Akü şarj durumunu (SoC) sahte %100 gösterme | Elektrik kesintisinde istasyonun anında çökmesi | Donanımsal deşarj voltaj izleme devresi |
| `TEL-04` | Yedek Jeneratör | Yakıt seviyesini dolu gösterip jeneratörü kilitleme | Şebeke kesintisinde sahanın enerjisiz kalması | Mekanik şamandıralı bağımsız yakıt seviye anahtarı |
| `TEL-05` | Kule İkaz Işıkları | Kule tepe lambası kontrolörünü karartma | Helikopter/uçak kuleye çarpma riski, can kaybı | Fotosel ve lamba akım izleme emniyet rölesi |
| `TEL-06` | Saha Çevre Güvenlik | Manyetik kapı ve PIR sensörlerini dondurma | Fiziksel ekipman hırsızlığı ve kablo sabotajı | Denetimli sonlandırma direnci (EOL) & bağımsız kamera |
| `TEL-07` | PTP / SyncE Zamanlama | IEEE 1588 zaman paketlerini kaydırma/bozma | 5G TDD hücreler arası girişim ve çağrı kopması | Bağımsız rubidyum/atomik saat & GNSS cross-check |
| `TEL-08` | Dış Kabinet Havalandırma | Filtre diferansiyel basınç sensörünü dondurma | Kabinet içine toz/nem dolması, kısa devre | Otomatik basınç farkı mekanik mikro sviçi |
| `TEL-09` | Akıllı PDU / DC Kesici | Transmisyon router DC besleme portunu kapatma | Sahanın ve bağlı alt istasyonların izole olması | Donanımsal manuel kilit & uzaktan kapatma yasağı |
| `TEL-10` | Hibrit Solar/Rüzgar MPPT | Şarj algoritmasını manipüle etme | Solar akülerin aşırı kaynaması ve yangın | Donanımsal zener diyotlu aşırı şarj koruma modülü |

---

## Ayrıntılı Senaryolar ve Savunma Mühendisliği

### TEL-01: Hassas Klima (CRAC/HVAC) Sabotajı ile BBU ve RF Kartlarında Termal Hasar

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saldırgan, baz istasyonu konteynerindeki iklimlendirme kontrolörüne (HVAC PLC / Modbus RTU ağ geçidi) sızarak oda sıcaklığı setpointini +18°C'den +45°C'ye yükseltir veya kompresör sürücüsüne `SHUTDOWN` komutu gönderir. Eşzamanlı olarak sıcaklık sensörü registerını +20°C değerinde sabitler.

#### 2. Fiziksel ve Süreç Hasarı
Baseband Unit (BBU) ve transmisyon cihazları kabinet içinde hızla ısı biriktirir. Ortam sıcaklığı 65°C üzerine fırlar. RF güç amplifikatörleri ve FPGA işlemcileri termal hasara uğrayarak yanar, lehimler erir ve baz istasyonu kalıcı olarak devre dışı kalır; bölgede acil çağrılar (112 vb.) dahil tüm hücresel iletişim kesilir.

#### 3. Donanımsal ve Mekanik Savunma (Layer 0/1)
- **Hardwired Bağımsız Mekanik Termostat:** PLC'den bağımsız, doğrudan acil durum DC tahliye fanlarına bağlı bimetal mekanik termostat kullanılır. Oda sıcaklığı +35°C'yi aştığında mekanik kontak kapanarak acil fanları çalıştırır ve temiz hava damperini açar.
- Cihaz raflarına entegre bağımsız sıcaklık kesicileri (Thermal Cutoff Fuses).

#### 4. Yazılımsal ve Mantıksal Savunma
- **BBU Dahili Termal Gözetim:** BBU işlemci içi sıcaklık sensörü ($T_j$) +85°C'ye ulaştığında yazılımdan bağımsız olarak işlemci saat hızını düşürür (thermal throttling) ve güvenli kapanmaya geçer.
- Klima kompresör akımı ile oda sıcaklığı arasında korelasyon denetimi.

#### 5. Ağ, Protokol ve Erişim Savunması
- Saha ortam izleme kontrolörleri (Site Management Controller) yönetim ağı VLAN'ında izole edilir; SNMPv3 ve şifreli SSH harici erişime kapatılır.

#### 6. Algılama ve OT SOC İmzası
- HVAC güç tüketimi sıfırlanırken BBU trafik yükünün sürmesi OT SOC'ta korelasyon kuralıyla tespit edilir.

---

### TEL-02: DC Güç Doğrultucu Voltajının Artırılması ile Ekipman İmhası

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Baz istasyonu ana DC güç sistemi (-48V DC nominal) doğrultucu (rectifier) ünitesinin SNMP veya Modbus/TCP arayüzüne sızılarak çıkış voltajı setpointi 68.0V DC seviyesine çıkartılır ve aşırı voltaj alarm eşikleri yükseltilir.

#### 2. Fiziksel ve Süreç Hasarı
Telekom ekipmanlarının giriş filtre kapasitörleri ve DC-DC dönüştürücüleri aşırı voltaj nedeniyle patlar. -48V DC akü grubunda elektrolit kaynaması ve hidrojen gazı birikmesi gerçekleşir; akü hücreleri şişip patlar ve santral odasında yangın çıkar.

#### 3. Donanımsal ve Mekanik Savunma
- **Donanımsal Aşırı Voltaj Koruma Devresi (Hardwired OVP Crowbar):** Doğrultucu çıkış barasına paralel bağlı tristörlü mekanik aşırı gerilim koruma devresi, bara voltajı -58.5V DC'yi aştığında 5 milisaniye içinde barayı toprağa şöntler ve ana giriş sigortasını attırarak enerjiyi fiziksel olarak keser.

#### 4. Yazılımsal ve Mantıksal Savunma
- Doğrultucu mikrodenetleyici firmware'inde maksimum çıkış voltajı donanımsal salt-okunur (read-only) sabitiyle sınırlandırılır.

#### 5. Ağ ve Protokol Savunması
- Doğrultucu yönetim kartında fabrika varsayılan SNMP community stringleri (public/private) iptal edilir, IPsec tünelleme zorunlu tutulur.

#### 6. Algılama ve OT SOC İmzası
- Güç yönetim telemetrisinde voltajın -54V üzerine çıkması acil olay olarak NOC/SOC ekranına yansıtılır.

---

### TEL-03: Akü Yönetim Sistemi (BMS) Telemetrisinin Körleştirilmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Lityum-iyon veya VRLA akü yönetim sisteminde şarj durumu (State of Charge - SoC) telemetrisi yazılımsal olarak %100 dolu gösterilirken, akü kontaktörleri açılarak akülerin şarj alması engellenir ve akülerin kendiliğinden derin deşarja uğraması sağlanır.

#### 2. Fiziksel ve Süreç Hasarı
Şebeke elektriği kesildiği anda yedek güç devreye giremez; baz istasyonu 1 saniye içinde tamamen kapanır ve bölge aniden kapsama alanı dışı kalır.

#### 3. Donanımsal ve Mekanik Savunma
- Akü barasına doğrudan bağlı analog voltmetre ve mekanik düşük voltaj kontaktörü (LVD - Low Voltage Disconnect).

#### 4. Yazılımsal ve Mantıksal Savunma
- **Periyodik Otomatik Yük Testi (Battery Discharge Test):** Sistem her 30 günde bir akü grubunu 10 dakika süreyle kontrollü deşarj ederek gerçek kapasiteyi doğrular; SoC verisi testi geçemezse alarm verir.

#### 5. Ağ ve Protokol Savunması
- BMS telemetrisi izole seri haberleşme hattında taşınır.

#### 6. Algılama ve OT SOC İmzası
- Şebeke varken akü akımının sıfır olması durumu SOC analizinde incelenir.

---

### TEL-04: Yedek Dizel Jeneratör Sensör Manipülasyonu ile Gücün Kilitlenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Jeneratör kontrol kartı (DeepSea / ComAp vb.) telemetrisine sızılarak motor bloğu sıcaklığı sahte olarak +120°C (aşırı sıcak) olarak iletilir.

#### 2. Fiziksel ve Süreç Hasarı
Jeneratör kontrolörü motor koruma moduna geçerek marş basmayı reddeder (`CRANK_INHIBIT`). Şebeke kesintisi olduğunda jeneratör devreye giremez ve telekom düğüm noktası enerjisiz kalır.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Manuel Marş ve Otomatik Transfer Şalteri (ATS):** Panoda bulunan fiziksel anahtar mekanik olarak "MANUAL RUN" konumuna alındığında tüm sensör blokajları baypas edilerek yakıt selenoiti doğrudan enerjilenir.
- Bağımsız mekanik seviye şamandırası.

#### 4. Yazılımsal ve Mantıksal Savunma
- Motor çalışmıyorken motor sıcaklığının ortam sıcaklığından yüksek olamayacağı kuralına dayalı mantıksal tutarlılık denetimi.

#### 5. Ağ ve Protokol Savunması
- Jeneratör kontrol paneli yerel hücresel modemi VPN üzerinden sadece NOC IP adreslerine kısıtlanır.

#### 6. Algılama ve OT SOC İmzası
- Jeneratör arıza alarmları ile hava durumu/kesinti alarmları eşleştirilir.

---

### TEL-05: Kule İkaz Aydınlatması Kontrolörünün Karartılması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
80 metre ve üzeri telekom kulelerinin tepesindeki ICAO uyumlu kırmızı/beyaz kule ikaz flaşör kontrolörüne Modbus/IP üzerinden `LIGHT_OFF` komutu gönderilir.

#### 2. Fiziksel ve Süreç Hasarı
Gece veya sisli havalarda alçak uçuş yapan ambulans helikopteri veya hafif uçaklar telekom kulesini fark edemeyerek çarpar; can kaybı, kule yıkılması ve hava aracı infilakı meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- **Mekanik Fotosel ve Donanımsal Lamba Akım Rölesi:** Kule lambası besleme devresine seri bağlı analog fotosel ve akım algılama rölesi. Karanlık algılandığında ve lambadan akım akmadığında mekanik yedek ampul devresini donanımsal olarak devreye alır.

#### 4. Yazılımsal ve Mantıksal Savunma
- Gün batımı/doğumu astronomik saat takvimi ile kule ışığı durumu çapraz doğrulanır; gece ışık kapatma komutları kontrolör firmware tarafından reddedilir.

#### 5. Ağ ve Protokol Savunması
- Kule ikaz kontrolörü saha içi yerel ağdan izole edilir.

#### 6. Algılama ve OT SOC İmzası
- Gece saatlerinde kule ikaz ışığı akım telemetrisinin sıfır olması en yüksek öncelikli acil çağrı üretir.

---

### TEL-06: Saha Çevre Güvenlik ve Yangın I/O Modüllerinin Susturulması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Baz istasyonu saha giriş kapısı manyetik kontakları ve duman sensörleri PLC dijital girişlerinde (Digital Input) `NORMAL / CLOSED` konumunda zorla sabitlenir (I/O force).

#### 2. Fiziksel ve Süreç Hasarı
Saldırganlar sahaya fiziksel olarak girip bakır topraklama kablolarını, jeneratör yakıtını ve RF modüllerini çalar; altyapı yangını tespitsiz kalarak konteyner kül olur.

#### 3. Donanımsal ve Mekanik Savunma
- **Hat Sonu Dirençli Denetimli Devreler (EOL Resistor Loop):** Manyetik kontak ve yangın butonları çift dirençli (4k7 / 2k2) devrelerle izlenir; kablo kesilmesi, kısa devre veya değer sabitleme donanımsal hat arızası (Tamper Alarm) üretir.

#### 4. Yazılımsal ve Mantıksal Savunma
- Güvenlik sensörleri ile bağımsız IP kamera hareket algılama akışları çapraz doğrulanır.

#### 5. Ağ ve Protokol Savunması
- Güvenlik kontrol panelleri şifreli SIA DC-09 protokolü ile alarm izleme merkezine bağlanır.

#### 6. Algılama ve OT SOC İmzası
- Saha kapı açılma telemetrisi olmadan kabinet iç sıcaklığında veya RF sinyalinde ani düşüş yaşanması fiziksel sabotaj alarmı üretir.

---

### TEL-07: PTP (IEEE 1588) ve SyncE Zaman/Frekans Dağıtımının Bozulması

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
5G TDD (Time Division Duplex) baz istasyonlarının bağlı olduğu Grandmaster Clock (PTP IEEE 1588v2) sunucusuna müdahale edilerek zaman paketlerindeki `correctionField` veya zaman damgası 3 mikrosaniye kaydırılır.

#### 2. Fiziksel ve Süreç Hasarı
5G TDD hücrelerinde indirme (downlink) ve yükleme (uplink) zaman dilimleri çakışır. Komşu hücreler birbirini boğar (inter-cell interference), çağrılar ve veri transferi kesilir, mobil aboneler servis alamaz.

#### 3. Donanımsal ve Mekanik Savunma
- Her baz istasyonuna entegre yerel atomik saat (Rubidium Atomic Oscillator) veya holdover yetenekli OCXO kristal osilatörler.

#### 4. Yazılımsal ve Mantıksal Savunma
- **PTP ve GNSS Çapraz Doğrulaması:** Sistem yerel GNSS zamanı ile ağdan gelen PTP zamanını sürekli karşılaştırır; fark 1.5 $\mu s$ üzerine çıkarsa harici PTP trafiğini reddeder ve yerel güvenli holdover moduna geçer.

#### 5. Ağ ve Protokol Savunması
- IEEE 1588 Annex P / IPsec ile zaman paketlerinin kriptografik doğrulanması.

#### 6. Algılama ve OT SOC İmzası
- Transmisyon ağında PTP paket gecikme varyansı (PDV) anomalileri SOC'ta izlenir.

---

### TEL-08: Dış Kabinet Filtre Basınç Sensörünün Dondurulması ile Kısa Devre

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Dış ortam telekom kabinetindeki hava filtrelerinin tıkanma durumunu ölçen diferansiyel basınç sensörü temiz filtre durumunda kilitlenir.

#### 2. Fiziksel ve Süreç Hasarı
Filtreler toz, polen ve endüstriyel kurumla tıkanır; fanlar vakum yaparak içeriye nemli ve iletken toz çeker. BBU kartları üzerinde iletken köprüler oluşarak kısa devre ve kart patlamaları meydana gelir.

#### 3. Donanımsal ve Mekanik Savunma
- Mekanik yaylı hava akış pervanesi mikro anahtarı (Vane Airflow Switch).

#### 4. Yazılımsal ve Mantıksal Savunma
- Fan devir hızı (RPM) artarken kabinet iç sıcaklığının düşmemesi filtre tıkanıklığı olarak yorumlanır.

#### 5. Ağ ve Protokol Savunması
- Sensör telemetrisi imzalı çerçevelerle taşınır.

#### 6. Algılama ve OT SOC İmzası
- Kabinet soğutma verimlilik katsayısının ($COP$) düşüş trendi izlenir.

---

### TEL-09: Akıllı PDU Portlarının Kapatılması ile Sahanın Kalıcı İzolasyonu

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Saha yönetim ünitesindeki akıllı DC Dağıtım Paneli (Smart PDU) web arayüzüne sızılarak transmisyon mikrodalga radyolink ve fiber switch DC çıkış portları `PORT_POWER_OFF` komutuyla kapatılır.

#### 2. Fiziksel ve Süreç Hasarı
Sahanın tüm dış dünya ile bağlantısı kesilir; sahadan uzaktan yönetim veya telemetri alınamaz hale gelir. Sahanın ayağa kaldırılması için uzak dağ tepelerine fiziksel teknisyen intikali gerekir.

#### 3. Donanımsal ve Mekanik Savunma
- Transmisyon cihazlarının DC besleme hatlarında yazılımla kapatılamayan hardwired manuel sigortalar kullanılır; uzaktan açma/kapama sadece yardımcı yüklere uygulanır.

#### 4. Yazılımsal ve Mantıksal Savunma
- **İletişim Kaybında Otomatik Yeniden Başlatma (Watchdog Auto-Reboot):** PDU, ana router ile ping haberleşmesini 10 dakika kaybederse kapalı portları otomatik olarak tekrar enerjilendirir.

#### 5. Ağ ve Protokol Savunması
- PDU yönetim arayüzlerine HTTP/Telnet kapatılır, sadece mTLS destekli SSH/HTTPS'e izin verilir.

#### 6. Algılama ve OT SOC İmzası
- PDU port durum değişiklikleri syslog üzerinden merkezi SOC'a aktarılır.

---

### TEL-10: Hibrit Solar/Rüzgar MPPT Şarj Regülatörünün Aşırı Yüklenmesi

#### 1. Saldırgan Bakış Açısı ve Teknik Mekanizma
Şebekeden uzak güneş/rüzgar enerjili baz istasyonundaki MPPT regülatörüne sızılarak batarya kimyası parametresi değiştirilir (Lityum profili yerine Kurşun-Asit profili seçilir ve şarj voltajı 60V'a zorlanır).

#### 2. Fiziksel ve Süreç Hasarı
Lityum hücreleri aşırı şarj olur, şişer ve alev alır; sahadaki konteyner ve anten kulesi tamamen yanar.

#### 3. Donanımsal ve Mekanik Savunma
- MPPT çıkışına donanımsal aşırı voltaj koruma sigortası ve eriyen termal bağlantı eklenir.

#### 4. Yazılımsal ve Mantıksal Savunma
- Batarya tipi ve voltaj sınırları MPPT firmware içinde donanımsal DIP switch konumuna kilitlenir.

#### 5. Ağ ve Protokol Savunması
- Yenilenebilir enerji kontrolörleri izole Modbus RTU ağında tutulur.

#### 6. Algılama ve OT SOC İmzası
- Güneş paneli gücü ile akü voltajı arasındaki dengesizlikler kaydedilir.
