# Endüstriyel protokol kataloğu

Bu bölüm, on dört protokol ailesini aynı inceleme düzenine yerleştirir. Amaç port ezberlemek değil; verinin işlevini, taşıma biçimini ve gerçekten etkin olan güvenlik mekanizmasını ayırmaktır. Önkoşul: [temel protokol bölümü](../01-temeller/04-endustriyel-protokoller.md). Devam: [Modbus ve OPC UA güvenliği](02-modbus-ve-opc-ua-guvenligi.md), [trafik analizi ve seçim](03-trafik-analizi-ve-protokol-secimi.md).

## Katman, port ve güvenlik profili

**Uygulama katmanı** verinin ve işlemin anlamını, **taşıma katmanı** TCP/UDP gibi iletişimi, **veri bağı katmanı** yerel ağdaki çerçeveleri tanımlar. Seri hatların elektriksel özellikleri fiziksel katmana aittir. Bir aile birden çok katmanı kapsayabilir: Modbus RTU, Modbus TCP ile aynı uygulama işlemlerini farklı bir taşıma düzeninde kullanır. PROFINET'in çevrimsel gerçek zaman trafiği doğrudan Ethernet üzerinde taşınabilir. Bu nedenle her protokole tek OSI katmanı ve TCP portu yazmak yanıltıcıdır. [Modbus uygulama belirtimi](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf), [PI PROFINET sistem açıklaması](https://www.profibus.com/download/profinet-technology-and-application-system-description)

Port kaydı, o porttaki trafiğin ilgili protokol olduğunu veya güvenilir olduğunu kanıtlamaz. Aşağıdaki portlar inceleme ipucudur; firewall izin listesi değildir. [IANA port kayıt uyarısı](https://www.iana.org/assignments/service-names-port-numbers?search=20000)

Güvenlik değerlendirmesinde üç ayrı soruya yanıt verilir:

- **Kimlik doğrulama:** Karşıdaki uygulama, cihaz veya kullanıcı kim?
- **Kriptografik bütünlük:** Mesajın yetkisiz değiştirilmesi saptanabiliyor mu?
- **Gizlilik:** İçerik, yetkisiz bir gözlemci tarafından okunabiliyor mu?

CRC gibi aktarım hatası denetimleri, kriptografik bütünlük veya cihaz kimliği kanıtı yerine yazılmaz. Güvenli profilin standardı bulunabilir; fakat iki uçtaki ürünün bunu desteklediği, etkinleştirdiği ve uyumlu biçimde kullandığı ayrıca gösterilmelidir. Bu ayrımı kayıt altına alma yöntemi deponun özgün eğitim sentezidir.

## On dört protokol ailesi

Tabloda **temel kullanım** ile **güvenli seçenek** ayrı belirtilmiştir. Ürün, firmware, lisans ve yapılandırma görülmeden bir tesiste seçeneklerin etkin olduğu varsayılmaz. İşletme kontrolleri sütunu bu deponun özgün önerisidir.

| Aile | İşlev ve iletişim modeli | Taşıma / port ayrımı | Kimlik, bütünlük ve gizlilik | İncelenecek işletme kontrolü |
|---|---|---|---|---|
| Modbus TCP | İstemci–sunucu; bit ve register işlemleri | Uygulama protokolü, TCP/IP; klasik TCP/502 | Klasik protokol güvenli kimlik/şifreleme sağlamaz; Modbus Security, TLS ve X.509 ile kimlik ve bütünlük koruması ekler; güvenli profil TCP/802'dir. [Modbus](https://www.modbus.org/modbus-specifications) | Hangi istemci hangi işlemi yapabilir; profil nerede sonlanıyor? |
| Modbus RTU | Seri istek–yanıt; eski belgelerde master–slave | Seri çerçeveleme; örneğin RS-485; TCP/UDP portu yok | RTU çerçevesindeki CRC aktarım hatası denetimidir; ağ geçidinin TLS kullanması seri bölümün şifrelendiği anlamına gelmez. [Seri hat rehberi](https://www.modbus.org/file/secure/modbusoverserial.pdf) | Seri hatta fiziksel erişim ve ağ geçidinin yönetimi |
| PROFINET | Denetleyici ile I/O cihazı arasında çevrimsel veri; ayrıca tanılama/parametre servisleri | Gerçek zamanlı çevrimsel trafik Ethernet L2, EtherType `0x8892`; bazı çevrimsel olmayan servisler UDP/IP kullanır; tek port yok | Güvenlik sınıfları ve uzantıları ayrıca değerlendirilir; aile adından şifreleme veya kimlik doğrulama çıkarılmaz. [Sistem açıklaması](https://www.profibus.com/download/profinet-technology-and-application-system-description), [güvenlik kılavuzları](https://www.profibus.com/download/profinet-security-guideline/) | Çevrimsel trafik ile mühendislik trafiği; desteklenen güvenlik sınıfı |
| PROFIBUS | DP/PA profilleriyle saha I/O ve proses iletişimi | Veri bağı ve fiziksel ortam; RS-485, MBP ve optik seçenekler; TCP/UDP portu yok | Sistem açıklamasındaki hata denetimi, kimlik doğrulama/şifreleme kanıtı sayılmaz; ek koruma ürüne ve mimariye göre doğrulanır. [PI sistem açıklaması](https://sea.profibus.com/fileadmin/media/downloadsection/PROFIBUS_Systembeschreibung_ENG_web.pdf) | Pano erişimi, saha bağlantısı, mühendislik istasyonu ve geçit |
| EtherNet/IP | CIP nesne/servisleri; explicit mesajlar ve implicit I/O | Ethernet + TCP/UDP; TCP/UDP 44818 kapsülleme, UDP/2222 implicit I/O. [ODVA rehberi](https://www.odva.org/wp-content/uploads/2020/05/PUB00213R0_EtherNetIP_Developers_Guide.pdf) | CIP Security, TCP için TLS ve UDP için DTLS kullanır; cihaz kimliği ve mesaj bütünlüğü sağlar, şifreleme seçenekleri ayrıca doğrulanır. [ODVA CIP Security](https://www.odva.org/technology-standards/distinct-cip-services/cip-security/) | Güvenli ve klasik bağlantılar, I/O zamanı ve cihaz güven listesi |
| OPC UA | Modellenmiş veri ve servisler; client/server ve PubSub seçenekleri | Birden çok eşleme vardır; `opc.tcp` için TCP/4840 kayıtlıdır; tüm UA trafiği bu porta indirgenmez. [OPC Part 6](https://reference.opcfoundation.org/specs/OPC-10000-6/7.1), [IANA](https://www.iana.org/assignments/service-names-port-numbers?search=4840) | Uygulama sertifikası, kullanıcı kimliği, güvenlik modu ve yetki farklı denetimlerdir. `None`, `Sign`, `SignAndEncrypt` eşdeğer değildir. [OPC Part 2](https://reference.opcfoundation.org/specs/OPC-10000-2/4) | Endpoint politikası, TrustList ve kullanıcı rolü |
| OPC Classic | DA, A&E ve HDA gibi ayrı belirtimlerle veri, olay ve tarihçe erişimi | COM/DCOM temeli; UA ile aynı protokol değildir; uzak iletişimde RPC/DCOM yapılandırması önemlidir | Koruma Windows/DCOM güvenlik ayarlarıyla değerlendirilir; UA SecureChannel özellikleri Classic'e mal edilmez. [OPC Foundation](https://opcfoundation.org/about/opc-technologies/opc-classic/) | Windows kimliği, servis hesabı, DCOM izinleri ve geçiş bağımlılıkları |
| DNP3 | Master–outstation; telemetri ve zaman damgalı olaylar | Seri veya IP; TCP/UDP 20000 kayıtlıdır; seri kullanımda port yok. [DNP özellikleri](https://www.dnp.org/About/Features-of-DNP3), [IANA](https://www.iana.org/assignments/service-names-port-numbers?search=20000) | Secure Authentication belgesi uygulama katmanı kimlik/bütünlük korumasını şifrelemeden ayırır; bu açıklama bütün yeni DNP3 güvenlik profilleri için genellenmez. [DNP-UG açıklaması](https://www.dnp.org/Portals/0/Public%20Documents/DNP3%20Secure%20Authentication%20Talking%20Points.pdf?ver=2016-02-17-113517-000) | Profil/sürüm, kritik işlem tanımı, anahtar yönetimi ve zaman kalitesi |
| IEC 60870-5-104 | Kontrol merkezi–uzak istasyon telekontrolü | Uygulama trafiği TCP/IP; TCP/2404 yaygın kayıt. [Apache PLC4X sürücü belgesi](https://plc4x.apache.org/plc4x/latest/users/protocols/iec-60870.html), [IANA](https://www.iana.org/assignments/service-names-port-numbers?search=2404) | IEC 62351-5 uygulama güvenliği ayrı kapsamdır; temel 104 desteği, bu mekanizmaların kurulduğunu kanıtlamaz. [IEC kataloğu](https://webstore.iec.ch/en/publication/65511) | Uçlar, komut yetkisi, zaman bilgisi, profil ve korunan hat sınırı |
| IEC 61850 | Güç otomasyonu için veri modelleri ve servis eşlemeleri | MMS ve Ethernet çerçevelerine eşlemeler; GOOSE/SV gibi L2 profilleri TCP/UDP portuyla temsil edilmez; tek protokol/port değildir. [IEC 61850-8-1](https://webstore.iec.ch/en/publication/6021), [IEC 62351-6 kapsamı](https://webstore.iec.ch/en/publication/63742) | IEC 62351-6 ilgili güvenlik mekanizmalarını kapsar; destek ve etkinlik servis/profil düzeyinde doğrulanır | Hangi mesaj hangi işlevi etkiler; multicast sınırı, zaman ve yapılandırma dosyaları |
| Siemens S7 iletişimi | Siemens sistemlerinde veri/mühendislik iletişimi; işlev ve nesil ayrımı gerekir | Klasik Ethernet S7 iletişiminde ISO-on-TCP, TCP/102; bütün Siemens servisleri aynı değildir. [Siemens CP kılavuzu](https://cache.industry.siemens.com/dl/files/399/109972399/att_1290227/v1/BA_CP-1243-7-LTE_76_en-US.pdf) | Yeni güvenli iletişim seçenekleri ürün ve sürüm koşulludur; bir S7 ailesi adı tüm iletişimin TLS olduğu anlamına gelmez. [Siemens güvenlik bildirimi](https://cert-portal.siemens.com/productcert/html/ssa-434534.html) | CPU/firmware, TIA ve HMI uyumu, mühendislik erişimi, etkin iletişim biçimi |
| MQTT | Broker üzerinden konu tabanlı yayımla–abone ol | Genellikle TCP/1883; TLS kullanımı için TCP/8883. [IANA](https://www.iana.org/assignments/service-names-port-numbers?search=mqtt) | Kimlik, yetki ve TLS tasarımı uygulamaya bağlıdır; MQTT adının kendisi gizlilik sağlamaz. [OASIS MQTT 5.0, bölüm 5](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | İstemci kimliği, konu izinleri, broker ve eski mesajın ele alınması |
| BACnet | Bina otomasyonu nesneleri ve servisleri | BACnet/IP: varsayılan UDP/47808; MS/TP: RS-485, IP portu yok; BACnet/SC farklı bir veri bağı seçeneği. [BACnet/IP](https://bacnet.org/wp-content/uploads/sites/4/2022/06/Building-Wide-Area-Networks-With-BACnet-Part-2.pdf), [MS/TP](https://www.se.com/eg/en/faqs/FA138520/) | BACnet/SC, TLS üzerinde Secure WebSockets ve sertifika temelli güven kullanır; arkasındaki klasik BACnet bölümü otomatik korunmaz. [BACnet/SC mimari açıklaması](https://bacnet.org/wp-content/uploads/sites/4/2022/06/B-SC-Whitepaper-v15_Final_20190521.pdf) | Hub/geçit sınırı, sertifika yönetimi ve eski bölüme erişim |
| CAN / CANopen | CAN veri bağı; CANopen bunun üzerinde nesne sözlüğü ve iletişim profilleri | CAN veri bağı/fiziksel ortam; CANopen üst katman protokolleri; yerel CAN hattında TCP/UDP portu yok. [CiA CANopen](https://www.can-cia.org/can-knowledge/canopen) | CAN veri bağı kendi başına siber güvenlik sağlamaz; CANopen güvenlik seçenekleri profil/uygulamaya bağlıdır. [CiA güvenlik açıklaması](https://can-cia.org/services/publications/can-community-news/09-2025) | Fiziksel hat, geçit, nesne sözlüğü erişimi ve desteklenen güvenlik profili |

## OT bağlamında yorumlama

Bir ofis uygulamasında bağlantı kesintisi kullanıcı işlemini geciktirebilir; bir kontrol bağlantısında ölçümün yaşlanması veya komutun gecikmesi süreç kararını etkileyebilir. Etki işlev ve tesis tasarımına bağlıdır. Aşağıdaki ayrım teknik bir performans sıralaması değil, özgün inceleme yöntemidir:

| Akış | Önce sorulacak soru | Belgeye yazılacak kanıt |
|---|---|---|
| Çevrimsel I/O | Kabul edilen güncelleme süresi ve kayıp davranışı nedir? | Süreç gereksinimi, cihaz profili, kabul raporu |
| Telemetri | Ölçümün zamanı, kalitesi ve bağlantı kesintisi sonrası anlamı korunuyor mu? | Veri sözlüğü, zaman kaynağı ve tamponlama varsayımı |
| Mühendislik | Kim, hangi değişiklik kaydıyla, hangi cihaz üzerinde çalışabilir? | Yetki matrisi, onay, oturum ve değişiklik kayıtları |
| Üst sistem veri aktarımı | Hangi veri gerekli; kontrol yetkisi aktarılıyor mu? | Kaynak/hedef/servis/amaç akış matrisi |

## Tehdit ve savunma matrisi

Aşağıdaki örnekler kurgusaldır; önkoşulun nasıl elde edileceği anlatılmaz. Tablo bu deponun özgün eğitim sentezidir.

| Hedef | Ön koşul | Aşılan güven sınırı | Olası hizmet/fiziksel etki | Gözlenebilir belirti | Karşılık gelen kontrol |
|---|---|---|---|---|---|
| Yetkisiz işlem isteğinin kabulü | Yetkisiz uç kontrol ağına erişebiliyor | Ağ erişimi ile işlem yetkisi | Süreç değerinin istenmeyen değişimi | Yeni iletişim ortağı; onay dışı işlem | İzinli uç/işlem matrisi, kimlik doğrulama ve değişiklik kaydı |
| Ölçümün güvenilir görünmesi | İleti yolunda değiştirme olanağı mevcut kabul ediliyor | Veri üreticisi ile tüketici | Hatalı işletme kararı | Mesaj doğrulama hatası; diğer ölçümlerle çelişki | Bütünlük denetimi, veri kalitesi ve bağımsız süreç karşılaştırması |
| Geçit üzerinden eski bölüme erişim | Güvenli üst bağlantı geçitte sonlanıyor | Güvenli profil ile klasik saha hattı | Yetkisiz saha erişimi | Geçit tarafında izinli, saha tarafında onaysız işlem | Her iki tarafın ayrı akış ve yetki incelemesi |
| Şifreli bağlantının fazla yetkili olması | Geçerli sertifika var, kullanıcı rolü geniş | Uygulama kimliği ile kullanıcı yetkisi | İzin dışı yapılandırma değişimi | Başarılı oturum ve beklenmeyen servis | En az yetki; uygulama ve kullanıcı denetimlerini ayırma |

## Belge alıştırması

**Kurgusal girdi:** A pompa kontrolörü Modbus RTU ile B geçidine bağlıdır. B ile C veri sunucusu arasındaki belge “TLS etkin” der; TLS profili ve sertifika sahibi yazmaz. D HMI için yalnız “OPC” notu vardır. E I/O satırında “PROFINET, TCP/8892” yazmaktadır.

| Aşama | Görev | Teslim |
|---|---|---|
| THEORY | Port, EtherType, uygulama ve güvenli profil farkını açıklayın | Dört kısa tanım |
| LAB | Beş varlığı ve akışları kâğıt üzerinde modelleyin | A → B → C ve D/E ilişkilerinin belirsizliklerini gösteren çizim |
| TEST | Belgede doğrulanamayan veya yanlış olan alanları bulun | Bulgu, gerekçe ve doğrulama kaynağı tablosu |
| DEFENSE | Her akış için kimlik, bütünlük, gizlilik ve işlem yetkisi kanıtı isteyin | Tamamlayıcı kontrol listesi |
| REPORT | “Güvenli” sonucu verilip verilemeyeceğini gerekçelendirin | Bir sayfalık protokol envanteri ve açık sorular |

**Kabul ölçütleri:** RTU'ya IP portu atanmamalı; `0x8892` EtherType olarak düzeltilmeli; OPC Classic/UA ayrımı açık bırakılmalı; TLS'nin sonlandığı nokta ve seri bölüm ayrı yazılmalı; eksik alanlar tahminle doldurulmamalıdır. Bu beş ölçütün her biri bir puandır. Beş puan, yalnız bu belge alıştırmasının tamamlandığını gösterir; cihaz üzerinde doğrulama yapıldığı anlamına gelmez.

## Kaynaklar ve kapsam

Tablodaki resmî kaynakların sürüm, tarih, okunan bölüm ve kullanılmayan iddia kayıtları [protokol araştırma notundadır](../../research/protokol-kaynaklar.md). Erişim: 16.09.2026. Eski temel protokol belgeleri yalnız değişmeyen çerçeve/işlev bilgisi için kullanılmıştır. Ticari ürün uyumluluğu, performans, lisans ve saha uygunluğu bu katalogdan çıkarılamaz.

