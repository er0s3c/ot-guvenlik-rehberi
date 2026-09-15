# Türkçe–İngilizce OT güvenliği sözlüğü

[Ana sayfa](../README.md) · [Öğrenme yolu](00-ogrenme-yolu.md) · [Standartlar ve Türkiye](05-standartlar-ve-turkiye.md)

Bu sözlük, depodaki bölümlerde geçen terimleri tek yerde toplar ve iki soruyu ayrı tutar: terim İngilizce kaynaklarda ne anlatır, Türkçede hangi karşılıkla ve hangi dayanakla kullanılır?

Üç ilke metnin tamamında geçerlidir.

**Türkçe karşılığı yerleşmemiş terimlerde İngilizcesi korunur.** Bir terimin resmî Türkçe metinlerde karşılığı yoksa, sözlük uydurma bir karşılık önermez. Bu durumda kullanım önerisi şudur: İngilizce terim korunur, ilk geçtiği yerde bir cümlelik açıklama yazılır ve karşılığın tartışmalı olduğu belirtilir. Türkçesi olmayan terimi zorlayarak çevirmek, iki ekibin aynı kelimeyle farklı şeyi kastetmesine yol açar.

**Aynı terim sektöre göre farklı anlam taşır.** ATS kısaltması demiryolunda bir tren durdurma veya gözetim işlevini, enerji tarafında bir besleme geçiş şalterini anlatır. "Switch" ağ tarafında anahtar, demiryolunda makastır. "Röle" sözcüğü genel sözlükte bir dönüştürücüyü, elektrik korumasında arıza algılayan cihazı anlatır. IEC 60870-5 ailesinde kumanda eden ve kumanda edilen istasyon denirken DNP3 tarafında master ve outstation denir; iki terminoloji birbirinin çevirisi gibi kullanılamaz. Bu nedenle her satırda terimin hangi alana ait olduğu ve neyle karıştırılmaması gerektiği yazılır.

**Bu tanımlar bu depo için sadeleştirilmiştir; normatif tanım yerine geçmez.** Bir gereksinim tartışmasında, bir sözleşmede veya bir denetimde esas alınacak tanım, ilgili standardın ya da mevzuatın kendi metnidir. Buradaki kısa tanımlar okuma kolaylığı içindir. Ücretli standartların tam metinleri bu çalışmada incelenmemiştir; kullanılan kaynakların kapsamı ve sınırları [Kaynaklar](#kaynaklar) bölümünde satır satır yazılıdır.

## Nasıl okunur

Terim tablolarının dört sütunu vardır.

| Sütun | İçeriği |
|---|---|
| İngilizce | Terimin kaynaklarda geçen İngilizce biçimi; kısaltması varsa parantez içinde |
| Türkçe karşılık | Bu depoda kullanılan Türkçe karşılık ve dayanak işareti; karşılık yoksa "—" |
| Kısa tanım | Terimi benzerlerinden ayıracak kadar kısa açıklama |
| Ayrım / not | Kaynak, karıştırılmaması gereken terim ve kalan belirsizlik |

Türkçe karşılık sütunundaki işaretler şunlardır.

| İşaret | Anlamı |
|---|---|
| **R** | Türkçe karşılık, Kaynaklar bölümündeki resmî bir Türkçe metinde birebir geçer; hangi metin olduğu notta yazılıdır |
| **T** | Türkçe karşılık yalnızca onay künyesi boş bir taslak metinde görülmüştür; yayımlanmış nihai karşılık sayılmaz |
| **D** | Yerleşik Türkçe karşılığı bu çalışmada doğrulanmadı; sütundaki ifade açıklama amaçlı kullanımdır, resmî karşılık değildir |
| işaretsiz | Türkçesi günlük dilde yerleşik olan ve terim tartışması taşımayan sözcükler |

"—" işareti, terimin Türkçeye çevrilmeden kullanıldığını gösterir; protokol ve ürün aileleri için olağan durum budur.

### Bu sözlükte ayrıca işaretlenen belirsizlikler

Aşağıdaki başlıklar, terim araştırmasında çözülemeyen noktalardır. İlgili satırlarda ayrıca tekrarlanır.

| Konu | Durum |
|---|---|
| Aks sayıcı (axle counter) | Ne ERA SUBSET-023 sözlüğünde ne de meslek standardı taslağında bulundu; hem terim tanımı hem Türkçe karşılığı doğrulanmadı |
| SCADA master / outstation | Doğrulanamadı. IEC 60870-5 ailesi kumanda eden / kumanda edilen istasyon ayrımını kullanır; "master / outstation" DNP3 (IEEE 1815) terminolojisidir ve IEEE 1815 kaydı bu çalışmada açılmadı |
| Unidirectional gateway / data diode | Ayrı bir birincil tanım kaynağı doğrulanamadı; hava boşluğu tanımının bulunduğu terim sayfasında geçmez |
| ATS kısaltması | İki ayrı anlam taşır. Demiryolunda Automatic Train Stop açılımı meslek standardı taslağında (K18), CBTC bağlamındaki Automatic Train Supervision açılımı K12 özet metninde doğrulandı. Enerji tarafındaki Automatic Transfer Switch açılımı doğrulanmadı. Her anlam ayrı madde olarak verilmiştir |
| Anklaşman ve balis / baliz | Türkçe karşılıklar yalnızca Resmî Gazete künyesi ve onay tarihi boş bırakılmış bir meslek standardı revizyon taslağında görülmüştür; **T** ile işaretlenmiştir |

Bir satırda kaynak gösterilmiyorsa, tanım bu depoda sadeleştirilmiş bir açıklamadır ve normatif bir metne dayandırılmamıştır.

## 1. Genel OT ve IT terimleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| operational technology (OT) | Operasyonel Teknolojiler **R** | Fiziksel ortamı izleyen veya değiştiren programlanabilir sistem ve cihazların bütünü | Kapsam dayanağı K01. Resmî karşılık K19, Kısaltmalar bölümü, belge içi s. 6: "OT: Operasyonel Teknolojiler". EPDK metinlerinde bu ibare geçmez; oradaki yakın terim EKS'tir (K14) |
| information technology (IT) | bilgi teknolojisi **D** | Kurumsal bilginin işlendiği, saklandığı ve taşındığı sistemler | Mülga 2017 EPDK Yönetmeliği "Kurumsal Bilişim Sistemi (KBS)" tanımını içerir (K15); yürürlükteki metindeki durumu doğrulanmadı |
| industrial control system (ICS) | endüstriyel kontrol sistemi (EKS) **R** | Bir üretim veya hizmet sürecini izleyen ve yöneten kontrol sistemleri bütünü | Yürürlükteki resmî tanım K14, madde 4/1-ç; K19 Kısaltmalar bölümü de "EKS: Endüstriyel Kontrol Sistemi" karşılığını verir. OT şemsiyesinin içinde daha dar bir kümedir |
| SCADA | Veri Tabanlı Kontrol ve Gözetleme Sistemi **R** | Coğrafi olarak dağılmış süreçlerin merkezden gözetlenmesi ve veri toplanması düzeni | Bu depoda kullanılan karşılık K14'tendir. Resmî metinlerde en az üç karşılık bulunur: K14 "Veri Tabanlı Kontrol ve Gözetleme Sistemi", K20 "Veri Tabanlı Merkezi Kontrol ve Gözetleme Sistemi", K19 "Merkezi Kontrol ve Veri Toplama". Şartname dilinde hangi metnin esas alındığı yazılır; Elektrik Şebeke Yönetmeliği terimi çevirmeden kullanır (K16) |
| distributed control system (DCS) | Dağıtılmış Kontrol Sistemi (DKS) **R** | Bir proses tesisindeki kontrol işlevlerinin bütünleşik ve dağıtılmış düzeni | Resmî karşılık K14. Varlık karşılığı A0017 DCS Controller'dır (K06). K20 aynı kısaltmayı "coğrafi olarak Dağınık Kontrol Sistemleri (DKS)" biçiminde kullanır; iki resmî metnin yazımı farklıdır |
| advanced process control (APC) | Gelişmiş Süreç Kontrol Sistemi **R** | Temel kontrolün üzerinde çalışan ileri süreç yönetim katmanı | Türkçe ad K14'te geçer; işlev açıklaması bu depoda sadeleştirilmiştir |
| industrial automation and control systems (IACS) | endüstriyel otomasyon ve kontrol sistemleri **D** | IEC 62443 serisinin kapsam terimi; kontrol sistemi ile onu işleten insan ve süreçleri birlikte anar | Normatif sözlük tanımı IEC 62443-1-1'dedir ve bu çalışmada o kayıt açılmadı |
| industrial internet of things (IIoT) | endüstriyel nesnelerin interneti **D** | Endüstriyel sensör ve hizmetlerin bağlantılı veri ekosistemi | Bu depoda sadeleştirilmiş açıklama; kullanımı için [OT nedir?](01-temeller/01-ot-nedir.md) |
| critical infrastructure | kritik altyapı | Bozulması can, ekonomi veya kamu düzeni açısından geniş sonuç doğurabilecek altyapı | Yürürlükteki tanım 7545 sayılı Kanun'dadır; kaynağıyla birlikte [standartlar bölümünde](05-standartlar-ve-turkiye.md) verilir |
| critical energy infrastructure | kritik enerji altyapısı **R** | Enerji sektöründe kritik sayılan altyapı | Tanım mülga 2017 metnindedir (K15); güncel çerçeve için yukarıdaki satır |
| system under consideration (SUC) | incelenen sistem **D** | Risk değerlendirmesinin sınırlarının çizildiği sistem bütünü | K07 kapsam metninde "SUC" kısaltmasıyla geçer; açılımı ve Türkçe karşılığı bu çalışmada doğrulanmadı |
| field device | saha cihazı **D** | Sürecin fiziksel noktasında bulunan ölçüm, kontrol veya koruma cihazı | Bu depoda sadeleştirilmiş açıklama |
| process | süreç, proses | Kontrol edilen fiziksel olay veya işlem zinciri | Metinlerde iki karşılık da kullanılır |

IEC 62443'ün rol terimleri (varlık sahibi, sistem entegratörü, ürün tedarikçisi) yönetişim bloğundaki 10. bölümde tek yerde toplanmıştır.

## 2. Kontrol ve saha bileşenleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| programmable logic controller (PLC) | Programlanabilir Mantık Kontrolcüsü **R** | Kontrol mantığını döngüsel olarak yürüten endüstriyel kontrolör | Resmî ad K14; varlık kaydı A0003 (K06). K19 aynı kısaltmayı "Programlanabilir Mantıksal Denetleyici" olarak açar; iki resmî metin farklı karşılık kullanır. "Programlanabilir lojik kontrolör" yaygındır ama resmî metinde doğrulanmadı |
| remote terminal unit (RTU) | Uzak Terminal Ünitesi **R** | Uzak sahadan veri toplayan ve saha kontrolünü destekleyen birim | Resmî ad K14; aynı karşılık K19 Kısaltmalar bölümünde de geçer; A0004 (K06). PLC'den farkı ürün sınıfı değil, kullanım yeri ve özerklik beklentisidir |
| intelligent electronic device (IED) | akıllı elektronik cihaz **R** | Elektrik sisteminde koruma, ölçme veya kontrol işlevi yürüten mikroişlemcili cihaz | Resmî karşılık K19, Kısaltmalar bölümü. Varlık kaydı A0005 (K06); bu bir standart tanımı değildir. Koruma rölesi IED'in bir örneğidir |
| human-machine interface (HMI) | operatör arayüzü **D** | Operatörün süreci gördüğü ve izinli işlemleri yaptığı arayüz | A0002 (K06). K19 Kısaltmalar bölümü kısa bir karşılık yerine "Makine ile İnsan Arasında Bilgi Aktarımı Sağlayan Arayüz" açıklamasını verir; "operatör arayüzü" bu depoda kullanılan kısaltılmış biçimdir. Ekranın görünürlüğünü kaybetmek ile kontrol mantığını kaybetmek ayrı olaylardır |
| data historian | historian, süreç veri arşivi **D** | Zaman serisi süreç verisini ve geçmişini saklayan sistem | A0006 (K06). Yedek değildir; amacı analiz, eğilim ve kanıttır |
| engineering workstation | mühendislik istasyonu **D** | Kontrol projesinin yazıldığı, yüklendiği ve yapılandırıldığı bilgisayar | ATT&CK'te ayrı varlık değildir; A0001 Workstation başlığı altında ele alınır (K06) |
| workstation | iş istasyonu **D** | Operatör veya mühendisin kullandığı genel amaçlı bilgisayar | A0001 (K06) |
| control server | kontrol sunucusu **D** | Saha cihazlarıyla haberleşip gözetim ve kumanda işlevini yürüten sunucu | A0007 (K06) |
| DCS controller | DKS kontrolörü **D** | Dağıtılmış kontrol sisteminde kontrol işlevini yürüten birim | A0017 (K06). "DKS" kısaltması K14'ten gelir; birleşik kullanım bu depoda sadeleştirilmiştir |
| programmable automation controller (PAC) | — **D** | Genişletilmiş işlem, haberleşme ve veri yeteneği olan kontrolör sınıfı | A0018 (K06). Türkçe karşılık doğrulanmadı |
| safety controller | emniyet kontrolörü **D** | Emniyet işlevlerini yürüten, temel kontrolden ayrı tasarlanan kontrolör | A0010 (K06); emniyet bağlamı için [emniyet bloğu](#5-emniyet-terimleri) |
| field I/O | saha giriş/çıkış birimi **D** | Sensör ve aktüatör sinyallerinin kontrolöre bağlandığı arayüz | A0013 (K06) |
| data gateway | veri ağ geçidi **D** | Farklı protokol veya ağlar arasında veri çeviren birim | A0009 (K06). Çevirinin anlamı, tamponlama ve yetki sınırı ayrı incelenir |
| sensor | sensör | Fiziksel büyüklüğü ölçen eleman | Ölçümün birimi, tazeliği ve kalite bayrağı değerin kendisi kadar önemlidir |
| transmitter | transmitter, ölçüm vericisi **D** | Ölçümü standart bir sinyale çevirip ileten cihaz | Türkçe karşılık doğrulanmadı; alanda İngilizcesi yaygın kullanılır |
| actuator | aktüatör **D** | Kontrol kararını fiziksel harekete çeviren eleman | TDK Güncel Türkçe Sözlük'te "aktüatör" kaydı yoktur (K17); kullanım yaygındır, genel sözlük dayanağı gösterilemez |
| transducer | transduser **D** | Bir fiziksel büyüklüğü başka bir büyüklüğe çeviren eleman | Birincil tanım kaynağı doğrulanmadı; Türkçe yazımı da yerleşmemiştir |
| setpoint | hedef değer (set-point) **D** | Kontrol döngüsünün ulaşmayı hedeflediği değer | K16 gövde metninde yalnızca "aktif güç hedef üretim değerlerini (set-point)" biçiminde ve otomatik üretim kontrol programı tanımının içinde geçer. "Hedef değer" birebir geçmez, Tanımlar maddesinde tanımlı değildir ve "ayar noktası" karşılığı doğrulanmadı |
| control loop | kontrol döngüsü | Ölç, değerlendir, etki et ve yeniden ölç zinciri | Bu depoda sadeleştirilmiş açıklama; ayrıntısı [kontrol döngüsü bölümünde](01-temeller/02-kontrol-dongusu-ve-bilesenler.md) |
| interlock | interlock, kilitleme mantığı **D** | Belirli koşullar sağlanmadan bir eyleme izin vermeyen mantık | Her interlock doğrulanmış bir emniyet işlevi değildir. Demiryolundaki "anklaşman" ile aynı kavram gibi kullanılmaz |

## 3. Ağ ve mimari terimleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| Purdue model | Purdue modeli **D** | İşlevleri kurumsal katmandan fiziksel sürece doğru katmanlayan referans yaklaşım | K08 katalog kaydı "Purdue" adını geçirmez; ISA-95 / IEC 62264 seviyeleriyle özdeş sayılmaz |
| IEC 62264 / ISA-95 levels | seviye hiyerarşisi **D** | İşletme (4), üretim operasyon yönetimi (3) ve kontrol (2 ile 1) katmanları | K08. Yaygın anlatılan "Seviye 3,5 / DMZ" katmanı bu standartta yoktur; uygulama pratiğidir |
| zone | bölge **D** | Ortak güvenlik gereksinimlerini paylaşan varlık kümesi | K07 kapsamı. Normatif sözlük tanımı IEC 62443-1-1'dedir ve bu çalışmada açılmadı |
| conduit | kanal **D** | Bölgeler arasındaki denetimli iletişim yolu | Aynı sınır. Bölge ile kanal ayrımı için [mimari bölümü](01-temeller/03-mimari-ve-guven-bolgeleri.md) |
| demilitarized zone (DMZ) | sınır ağı, ara bölge **D** | İki farklı güven düzeyi arasında konumlanan denetimli ara ağ | K03 tek bir resmî tanım vermez; en az beş ayrı NIST/CNSS kaynaklı tanım listeler. K19 Kısaltmalar bölümü "Sivil Bölge" karşılığını verir; bu depoda kullanılan "sınır ağı, ara bölge" o metinden alınmamıştır |
| OT DMZ, industrial DMZ | OT sınır bölgesi **D** | Kurumsal ağ ile kontrol bölgeleri arasındaki veri kopyası ve erişim aracısı katmanı | Bu depoda sadeleştirilmiş açıklama; kullanım örneği [segmentasyon bölümünde](04-savunma/02-segmentasyon-ve-uzak-erisim.md) |
| air gap | hava boşluğu **R** | İki sistem arasında fiziksel bağlantının bulunmaması ve mantıksal bağlantının otomatik olmaması; veri yalnızca insan denetiminde elle taşınır | Tanım K04 (CNSSI 4009-2022 kaynaklı). Türkçe karşılık K19 gövde metnindedir: tedbir 3.1.6.36 ve 4.5.2.15 "hava boşluğu" ifadesini kullanır. "İnternete çıkışı yok" ifadesiyle aynı şey değildir; bakım dizüstüsü ve taşınabilir medya bu sınırı kaldırabilir |
| unidirectional gateway | tek yönlü ağ geçidi **D** | Veri akışını tek yöne sınırlayan geçiş düzeni | Ayrı bir birincil tanım kaynağı doğrulanamadı; hava boşluğu terim sayfasında geçmez. K19 aynı bağlamda "tek yönlü veri aktarımı" der, bir cihaz adı vermez |
| data diode | veri diyodu **R** | Aynı kavramın yaygın kullanılan adı | Türkçe karşılık K19 gövde metninde iki yazımla geçer: tedbir 3.1.6.36 "veri diyotu", tedbir 4.5.2.15 "veri diyodu". İngilizce tarafındaki tanım belirsizliği sürer. Tek yönlü aktarım, dosya aktarımı ve geri dönüş ihtiyaçlarını tek başına karşılamaz |
| jump host | sıçrama sunucusu **D** | Yönetim oturumlarının üzerinden geçtiği aracı sistem | A0012 (K06). "Sıçrama sunucusu" karşılığı K19 metninde bulunamadı. "Bastion host" ATT&CK varlık adı değildir; iki ad eş anlamlı gibi kullanılmamalıdır |
| VPN server | VPN sunucusu **D** | Uzak erişim tünelini sonlandıran sunucu | A0011 (K06). K19 yalnızca "VPN: Sanal Özel Ağ" karşılığını verir, sunucu için ayrı bir terim tanımlamaz. Şifreli olması hedef kapsamının ve oturum sahibinin doğrulandığını göstermez |
| firewall | güvenlik duvarı **D** | Ağ akışlarını kurala göre süzen cihaz veya işlev | A0016 (K06) |
| router | yönlendirici **D** | Ağlar arasında paket yönlendiren cihaz | A0014 (K06) |
| switch (network) | ağ anahtarı **D** | Yerel ağda çerçeveleri anahtarlayan cihaz | A0015 (K06). Demiryolundaki "switch / makas" ile karıştırılmamalıdır |
| segmentation | segmentasyon, bölümleme | Ağın güven ve işlev sınırlarına göre ayrılması | Ayrı VLAN'da bulunmak tek başına güvenlik sınırı oluşturmaz |
| remote access | uzak erişim | Saha dışından yapılan yönetim veya bakım bağlantısı | Kimlik, süre, hedef kapsamı ve kayıt birlikte değerlendirilir |
| port mirroring | port aynalama **D** | Gözlem için trafiğin bir kopyasının başka bir porta yönlendirilmesi | Bu depoda sadeleştirilmiş açıklama. Aynalama yapılandırması bir değişikliktir; kapasite ve hata davranışı değerlendirilir |

## 4. Protokol terimleri

Protokol adları özel addır ve çevrilmez; bu blokta Türkçe karşılık sütunu yalnızca terim niteliğindeki sözcükler için doldurulur. Protokollerin güvenlik değerlendirmesi [endüstriyel protokoller bölümündedir](01-temeller/04-endustriyel-protokoller.md).

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| Modbus RTU / Modbus TCP | — | Ölçüm ve kontrol verisini basit okuma/yazma işlevleriyle taşıyan protokol ailesi | Ağda bulunmak yetki sayılmaz; klasik kullanımda kimlik doğrulama beklentisi yoktur |
| Modbus Security | — | TLS ve X.509 sertifikalarıyla korunan Modbus profili | Klasik Modbus TCP'nin varlığı bu profilin desteklendiğini göstermez |
| OPC UA | — | Yapılandırılmış endüstriyel veri ve servisler için mimari | Güvenlik modu, uygulama sertifikası ve kullanıcı yetkisi ayrı doğrulanır |
| MQTT | — | Broker üzerinden yayımla ve abone ol mesajlaşması | Konuya yayın ile konu filtresine abonelik yetkileri ayrıdır |
| DNP3 (IEEE 1815) | — | Uzak saha telemetrisi ve kontrolü için protokol | "Master / outstation" ikilisi bu aileye aittir; IEEE 1815 kaydı bu çalışmada doğrulanmadı |
| IEC 60870-5-104 | — | IEC 60870-5-101'in standart taşıma profilleriyle ağ erişimi | K10. Kapsam: coğrafi olarak geniş yayılmış süreçlerin izlenmesi ve kontrolü |
| telecontrol | telekontrol **D** | Coğrafi olarak yayılmış süreçlerin uzaktan izlenmesi ve kontrolü | Terimin IEC kullanımı K10 başlığından; Türkçe karşılık resmî metinde doğrulanmadı |
| controlling station / controlled station | kumanda eden / kumanda edilen istasyon **D** | IEC 60870-5 ailesinde kumandayı veren ve alan uçlar | Katalog sayfası bu terimleri göstermedi. DNP3'ün master / outstation ikilisiyle eşitlenmemelidir |
| IEC 61850 | — | Güç sistemleri için veri modelleri, mühendislik dili ve haberleşme servisleri ailesi | Tek bir port veya paket türü değildir |
| MMS | — | IEC 61850 istasyon verisinin haberleşme eşlemesi | Açılım K19 Kısaltmalar bölümünden: "Manufacturing Message Specification / Üretim Mesaj Spesifikasyonu". IEC kaynağından ayrıca doğrulanmadı |
| GOOSE | — | Eşler arası olay mesajlaşması | Zaman gereksinimi ile güvenlik profilinin uyumu tesis özelinde doğrulanır |
| sampled values (SV) | örneklenmiş ölçümler **D** | Ölçü değerlerinin örneklenerek yayınlanması | Türkçe karşılık doğrulanmadı |
| ICCP / TASE.2 | — | Kontrol merkezleri arasındaki bilgi alışverişi protokolü | Paylaşılan veri kümesi ve karşı kurum sınırı ayrı yazılır |
| IEC 62351 | — | Enerji haberleşme protokolleri için güvenlik standartları serisi | Protokolün yerine geçmez; ürün desteği tesis özelinde doğrulanır |
| PROFINET / EtherNet/IP | — | Endüstriyel Ethernet üzerinde otomasyon protokolleri | Gerçek zaman davranışı ile mühendislik trafiği ayrı değerlendirilir |
| SCL | — | IEC 61850 kapsamında sistem yapılandırma tanım dili | Proje yapılandırmasının kaynağıdır; değişiklik yönetimine dahildir |

## 5. Emniyet terimleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| safety | emniyet | İstenmeyen fiziksel zararın önlenmesi | Türkçede "güvenlik" (security) sözcüğünden ayrı tutulur; iki disiplinin onay süreçleri farklıdır |
| security | güvenlik | Kasıtlı saldırı ve yetkisiz eyleme karşı koruma | Emniyet kaydı ile güvenlik kaydı aynı belgede birleştirilse bile yetkiler ayrı kalır |
| functional safety | fonksiyonel emniyet **D** | Emniyet işlevinin doğru çalışmasıyla sağlanan emniyet | K09 başlığında "functional safety" geçer; Türkçe karşılık resmî metinde doğrulanmadı |
| safety instrumented system (SIS) | emniyet enstrümanlı sistem **D** | Prosesi emniyetli duruma getiren veya orada tutan, temel kontrolden ayrı enstrümanlı sistem | K09 kapsamı. Türkçe karşılık doğrulanmadı; ATT&CK tarafındaki yakın varlık A0010 Safety Controller'dır (K06) |
| safety integrity level (SIL) | emniyet bütünlük seviyesi **D** | Bir emniyet işlevinden beklenen bütünlük derecesi | Asıl kaynak IEC 61508'dir ve bu çalışmada o katalog kaydı açılmadı. SIL saldırı direncini ölçmez; 62443'ün SL'i ile sayı sayıya eşleştirilemez |
| safe state | emniyetli durum **D** | Prosesin zarar üretmeyen tanımlı durumu | K09 kapsam metninde geçer; Türkçe karşılık doğrulanmadı |
| fail-safe | — **D** | Arıza veya besleme kaybında emniyetli tarafa düşen tasarım | Birincil tanım kaynağı doğrulanmadı; cihaz davranışı üretici belgesinden ve kabul testinden okunur |
| fail-secure | — **D** | Arıza durumunda erişimi kapalı tarafa düşüren tasarım | Aynı belirsizlik. Fail-safe ile aynı anlamda kullanılmaz |
| safety case | emniyet dosyası **D** | Bir sistemin emniyet iddiasının gerekçe ve kanıtla sunulduğu belge | Doğrulanmadı; aday kaynak EN 50129'dur ve bu çalışmada incelenmedi |
| safety lifecycle | emniyet yaşam döngüsü **D** | Emniyet işlevinin şartnameden bakıma kadar izlediği süreç | K09 kapsamı belirtim, tasarım, kurulum, işletme ve bakımı sayar; Türkçe karşılık doğrulanmadı |

## 6. Elektrik terimleri

Bu bloktaki **R** işaretli karşılıklar Elektrik Şebeke Yönetmeliği'nin Tanımlar maddesinden birebir alınmıştır (K16). Aynı maddede tanımı bulunmayan terimler **D** ile işaretlenmiştir. Sektör bağlamı [elektrik ve enerji bölümündedir](02-sektorler/02-elektrik-ve-enerji.md).

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| busbar | bara, ana bara **R** | Fiderlerin kendi kesicisi ve ayırıcıları ile bağlı olduğu ortak iletken | K16: "Ana bara: Fiderlerin kendi kesicisi ve ayırıcıları ile bağlı olduğu barayı" |
| transfer bus | transfer bara **R** | Teçhizatın transfer kesicisi ve/veya ayırıcısı ile bağlandığı bara | K16 |
| feeder | fider **R** | Bir merkez barasından kullanıcıya enerji taşıyan hat veya kablo çıkışı | K16 |
| transfer feeder | transfer fideri **R** | Bir fiderin yerine geçebilen teçhizat | K16 |
| circuit breaker | kesici **R** | Kısa devre dahil elektrik devrelerinde açma ve kapama yapan teçhizat | K16. TDK Güncel Türkçe Sözlük'te "kesici" sözcüğünün elektrik anlamı yoktur (K17); dayanak mevzuattır |
| disconnector, isolator | ayırıcı **R** | Yüksüz elektrik devrelerini açıp kapamak için kullanılan teçhizat | K16. Kesici ile aynı işlevi görmez; yük altında açma amacı taşımaz |
| protective relay | koruma rölesi **D** | Elektriksel arıza veya anormal durumu algılayıp koruma işlemi başlatan cihaz | K16 Tanımlar maddesinde yer almaz. TDK'nın "röle" tanımı bu anlamı karşılamaz (K17); karşılık alan kullanımından gelir |
| instrument transformer | ölçü transformatörü **D** | Yüksek akım ve gerilimi ölçme ile koruma devreleri için ölçekleyen transformatör | K16 Tanımlar maddesinde tanımlı değildir |
| recloser | — **D** | Geçici arıza sonrası hattı otomatik olarak yeniden devreye almayı deneyen kesici düzeni | Türkçe yerleşik karşılık doğrulanmadı; alanda İngilizcesi kullanılır |
| substation | trafo merkezi, şalt merkezi **D** | Gerilim dönüştürme, kesme ve koruma teçhizatının bulunduğu tesis | K16 Tanımlar maddesinden doğrulanmadı; iki karşılık da alanda kullanılır |
| energy management system (EMS) | enerji yönetim sistemi **D** | İletim işletmesinde şebeke durumunun izlenmesi ve yönetimi uygulaması | Türkçe karşılık doğrulanmadı |
| distribution management system (DMS / ADMS) | dağıtım yönetim sistemi **D** | Dağıtım şebekesinin gözetimi ve karar desteği uygulaması | Türkçe karşılık doğrulanmadı |
| distributed energy resources (DER) | dağıtık enerji kaynakları **D** | Dağıtım şebekesine bağlı küçük ölçekli üretim ve depolama varlıkları | Türkçe karşılık doğrulanmadı; yetki sınırı ayrı incelenir |
| uninterruptible power supply (UPS) | kesintisiz güç kaynağı **R** | Besleme kesildiğinde yükü kesintisiz beslemeyi sürdüren sistem | Karşılık ve açılım K19 Kısaltmalar bölümündedir. Terimin normatif bir tanımı bu çalışmada aranamadı |
| rectifier | doğrultucu **D** | Alternatif akımı doğru akıma çeviren birim | Birincil tanım kaynağı doğrulanmadı |
| generator, genset | jeneratör **D** | Şebeke kaybında yerel elektrik üreten yedek kaynak | Birincil tanım kaynağı doğrulanmadı |
| automatic transfer switch (ATS) | otomatik transfer şalteri **D** | Besleme kaynakları arasında otomatik geçiş yapan şalter | Bu açılım ve karşılık incelenen kaynaklarda bulunamadı. Demiryolundaki ATS ile aynı kısaltma, farklı kavramdır |
| HVAC | iklimlendirme **D** | Isıtma, havalandırma ve iklimlendirme sistemleri | Birincil tanım kaynağı doğrulanmadı; saha OT'sinin sık görülen parçasıdır |

## 7. Raylı sistem terimleri

İngilizce tanımların dayanağı ERA SUBSET-023 sözlüğüdür (K11) ve CBTC için IEEE 1474.1-2025'tir (K12). **T** işaretli Türkçe karşılıklar yalnızca onay künyesi boş bir meslek standardı revizyon taslağında görülmüştür (K18). Sektör bağlamı [raylı sistemler bölümündedir](02-sektorler/03-rayli-sistemler.md).

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| interlocking | anklaşman **T** | Sinyal ve makasların emniyetsiz duruma getirilmesini önleyecek biçimde kurulması ve serbest bırakılmasını denetleyen işlev ile bu işlevi gören ekipman | İngilizce tanım K11. Türkçe karşılık yalnızca K18 taslağında; nihai metin doğrulanmadı |
| balise | balis, baliz **T** | Üzerinden geçen trenle haberleşebilen, yola monte edilmiş pasif transponder | İngilizce tanım K11. K18 taslağı iki yazımı birlikte verir |
| Eurobalise | — | ERTMS/ETCS şartnamesine uygun balise | K11. Türkçe karşılık yoktur |
| radio block centre (RBC) | — **D** | Tren konum bilgisini telsizle alan ve trenlere hareket izni gönderen merkezi emniyet birimi | K11. Türkçe karşılık doğrulanmadı; K18 taslağında da bulunamadı |
| movement authority | hareket izni **D** | Trene belirli bir noktaya kadar ilerleme yetkisi veren bilgi | Terim K11'deki RBC tanımında geçer; Türkçe karşılık doğrulanmadı |
| ERTMS | — | Avrupa demiryolu trafik yönetimi çerçevesi | Açılım K11: European Rail Traffic Management System |
| ETCS | Avrupa Tren Kontrol Sistemi **D** | ERTMS'in tren kontrol parçası | Açılım K11: European Train Control System. Türkçe karşılık doğrulanmadı |
| communications-based train control (CBTC) | — **D** | Ray devrelerinden bağımsız, yüksek çözünürlüklü konum belirlemeye ve sürekli, yüksek kapasiteli, çift yönlü tren–yol boyu veri haberleşmesine dayanan sürekli otomatik tren kontrol sistemi | K12. ATP zorunlu, ATO ve ATS opsiyoneldir. ETCS'nin başka adı değildir |
| automatic train protection (ATP) | otomatik tren koruma sistemi **T** | Hız ve hareket iznini denetleyip gerektiğinde müdahale eden koruma işlevi | Türkçe karşılık K18 taslağından; İngilizce açılım K12 özet metninde "automatic train protection (ATP)" olarak geçer |
| automatic train control (ATC) | otomatik tren kontrol sistemi **T** | Tren kontrol işlevlerini yürüten sistem | Aynı sınır |
| automatic train stop (ATS) | otomatik tren durdurma sistemi **T** | Belirli koşullarda treni durduran işlev | Açılım ve Türkçe karşılık K18 taslağından. K12 özet metni, CBTC bağlamındaki opsiyonel ATS işlevini "automatic train supervision" olarak açar; bu, K18'deki "automatic train stop" anlamından farklı bir kavramdır. Enerji tarafındaki ATS ile de karıştırılmamalıdır |
| automatic train operation (ATO) | — **D** | Sürüş işlevlerinin otomatik yürütülmesi | Açılım K12 özet metninde "automatic train operation (ATO)" olarak geçer ve K12 ATO'yu opsiyonel sayar; Türkçe karşılık doğrulanmadı |
| track circuit | ray devresi **D** | Ray üzerinden tren varlığını algılayan devre | Terim K12'de "ray devrelerinden bağımsız" ifadesiyle geçer; Türkçe karşılık doğrulanmadı |
| axle counter | aks sayıcı **D** | Bir kesitten geçen aks sayısını sayarak hat kesiminin boş veya dolu olduğunu belirleyen algılama düzeni | Ne K11'de ne K18'de bulundu; hem tanım hem Türkçe karşılık doğrulanmadı. Aday kaynaklar EN 50617 ve IEC 62290 serileridir, bu çalışmada incelenmedi |
| point, switch (track) | makas **T** | Trenin bir hattan diğerine geçmesini sağlayan hareketli yol elemanı | K18 taslağında tanımlıdır. Ağ anahtarıyla karıştırılmamalıdır |
| signal | sinyal **T** | Sürücüye veya araç üstü sisteme hareket bilgisini veren düzenek | K18 taslağında tanımlıdır |
| traction power | cer gücü **D** | Treni hareket ettiren elektrik beslemesi | Türkçe kullanım alanda yerleşiktir; birincil tanım kaynağı doğrulanmadı |

## 8. Telekom terimleri

Bu bloğun mimari dayanağı ETSI TS 123 501'dir (K13). Uyarı: bu çalışmada belgenin PDF'i açılmamış, yalnızca başlık, sürüm ve tarih doğrulanmıştır; aşağıdaki tanımlar alıntı değil, bu depoda sadeleştirilmiş açıklamalardır. Sektör bağlamı [telekom bölümündedir](02-sektorler/04-telekom-ve-baz-istasyonlari.md).

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| radio access network (RAN) | radyo erişim ağı **D** | Uç cihazın şebekeye radyo üzerinden bağlandığı erişim katmanı | Türkçe karşılık doğrulanmadı |
| core network, 5G Core | çekirdek şebeke **D** | Kimlik, hareketlilik, oturum ve kullanıcı verisi iletimi işlevlerinin bulunduğu katman | Her çekirdek işlevi her sahada bulunmaz |
| user equipment (UE) | uç cihaz **D** | Şebekeye bağlanan telefon veya haberleşen cihaz | Türkçe karşılık doğrulanmadı |
| network slicing | ağ dilimleme **D** | Ortak fiziksel altyapı üzerinde farklı yetenek ve özelliklere sahip mantıksal şebekelerin oluşturulması | Tanım birincil metinden alıntılanmadı; bu depoda sadeleştirilmiştir |
| backhaul | taşıma, backhaul **D** | Erişim tarafını çekirdeğe ve diğer şebeke noktalarına bağlayan taşıma altyapısı | Türkçe karşılık doğrulanmadı |
| base station | baz istasyonu **D** | Radyo erişimini sağlayan saha tesisi | Karşılık yaygındır; birincil kaynaktan doğrulanmadı. Tesisin enerji ve soğutma bölümü ayrı bir OT kapsamıdır |
| control plane / user plane | kontrol düzlemi / kullanıcı düzlemi **D** | Oturum ve kimlik kararlarının alındığı düzlem ile kullanıcı verisinin taşındığı düzlem | Aynı hattaki her bileşen kullanıcı verisinin tamamını işlemez |
| service based architecture (SBA) | servis tabanlı mimari **D** | Çekirdek işlevlerin birbirini servis arayüzleriyle çağırdığı mimari | Türkçe karşılık doğrulanmadı |
| operations support systems (OSS) | — **D** | Şebeke ve hizmet işletimini destekleyen yönetim, orkestrasyon ve güvence işlevleri | 3GPP kaynağından doğrulanmadı; terim alanı TM Forum tarafına daha yakındır |
| business support systems (BSS) | — **D** | Ücretlendirme, faturalama ve sipariş gibi iş süreçleri | Aynı sınır. OSS ile yetkileri ayrı tutulur |
| network operations centre (NOC) | şebeke işletim merkezi **D** | Şebeke ve saha durumunun izlendiği merkez | Türkçe karşılık doğrulanmadı; güvenlik izlemesini yürüten SOC ile aynı işlev değildir |

## 9. Güvenlik operasyonu ve olay yönetimi terimleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| indicator of compromise (IoC) | ihlal göstergesi **D** | Bir saldırının yaklaştığını, sürmekte olduğunu veya bir ihlalin gerçekleşmiş olabileceğini düşündüren teknik iz | Tanım K02 (NIST SP 800-61r3 kaynaklı terim sayfası). Türkçe karşılık doğrulanmadı. Gösterge kanıt değildir; bağlamla birleştirilir |
| baseline configuration | temel yapılandırma **D** | Belirli bir anda resmen incelenmiş ve üzerinde anlaşılmış, yalnızca değişiklik kontrolüyle değiştirilebilen yapılandırma belirtimi | Tanım K02 (NIST SP 800-128 kaynaklı). NIST'te tercih edilen başlık "baseline configuration"dır; "configuration baseline" tercih edilen biçim değildir |
| asset inventory | varlık envanteri **R** | Varlıkların işlev, sahip, bağımlılık ve kanıt bilgisiyle tutulan kaydı | Terim K19 gövde metninde geçer (tedbir 3.1.1.1). Uygulaması [envanter bölümünde](04-savunma/01-envanter-ve-gorunurluk.md) |
| passive monitoring | pasif gözlem **D** | Hedefe sorgu göndermeden, mevcut trafiğin kopyası üzerinden yapılan gözlem | Eksiksiz değildir: sessiz varlıklar, seri bağlantılar ve şifreli içerik görünmeyebilir |
| active scanning | aktif tarama **D** | Hedefe sorgu göndererek bilgi toplama | Bu depoda kontrol ağında varsayılan keşif yöntemi olarak önerilmez; ürün davranışı bilinmeden uygulanmaz |
| threat model | tehdit modeli **D** | Korunacak işlev, saldırganın amacı, ön koşullar ve güven sınırlarını ilişkilendiren çalışma | Türkçe karşılık doğrulanmadı. K05 bir teknik sözlüğüdür, tehdit modeli maddesi tanımlamaz |
| attack surface | saldırı yüzeyi **D** | Bir sisteme erişim veya etki için kullanılabilecek giriş noktalarının toplamı | Aynı sınır; K05 bu terimi sözlük maddesi olarak tanımlamaz |
| tactic | taktik **D** | ATT&CK'te saldırganın ulaşmak istediği amaç | K05: ICS matrisinde 12 taktik bulunur (içerik sürümü v19.2) |
| technique | teknik **D** | ATT&CK'te bir amaca ulaşmak için izlenen yol | K05: ICS matrisinde 90 teknik bulunur. Eşleştirme için [ATT&CK bölümü](03-tehdit-modelleme/02-mitre-attack-ics.md) |
| security operations centre (SOC) | güvenlik operasyon merkezi **D** | Güvenlik olaylarının izlendiği ve yönetildiği ekip ve süreç | Türkçe karşılık doğrulanmadı; şebeke tarafındaki NOC ile aynı işlev değildir |
| incident response | olay müdahalesi **D** | Olayın doğrulanması, sınırlanması, kurtarılması ve öğrenilmesi süreci | Türkçe karşılık doğrulanmadı. OT'de karar yetkisi süreç sahibiyle paylaşılır |
| containment | sınırlama **D** | Etkinin yayılmasını durdurmaya yönelik geçici tedbir | İş istasyonu, kontrolör ve emniyet sistemine aynı sınırlama kuralı uygulanmaz |
| golden image | referans imaj **D** | Yeniden kurulumda esas alınan, onaylanmış kurulum kopyası | Birincil tanım kaynağı doğrulanmadı |
| change window | değişiklik penceresi **D** | Değişikliğin yapılmasına izin verilen planlı zaman aralığı | Birincil tanım kaynağı doğrulanmadı. Uygulaması [değişiklik yönetimi bölümünde](04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) |
| mean time to restore (MTTR) | ortalama geri dönüş süresi **D** | Hizmetin yeniden verilebilmesine kadar geçen sürenin ortalaması | Birincil tanım kaynağı doğrulanmadı. Ortalama, geciken kritik olayları gizleyebilir |
| recovery time objective (RTO) | hedeflenen geri dönüş süresi **D** | Hizmetin ne kadar sürede geri verilmesinin hedeflendiği | Bu depoda sadeleştirilmiş açıklama; OT'de kabul edilebilir süreç durumu ayrıca tanımlanır |
| recovery point objective (RPO) | tolere edilen veri kaybı aralığı **D** | Ne kadar geriye dönük veri kaybının kabul edildiği | Aynı sınır. Ayrıntı [olay müdahalesi ve kurtarma bölümünde](04-savunma/05-olay-mudahalesi-ve-kurtarma.md) |
| vulnerability | zafiyet | Bir varlıkta istismar edilebilecek zayıflık | Tek başına risk değildir; erişilebilirlik ve sonuç ile birlikte değerlendirilir |
| risk | risk | Bir olayın gerçekleşme olasılığı ile sonucunun birlikte değerlendirilmesi | Zafiyet sayısı risk sıralaması vermez |
| backup | yedek | Geri yüklenebilir kopya | Kopyanın varlığı, geri yüklemenin çalıştığını göstermez |
| recovery | kurtarma | Hizmetin doğrulanmış biçimde yeniden verilmesi | Çalışır sunucu ile doğrulanmış süreç ayrı kabul maddeleridir |
| log | kayıt, günlük | Sistem veya kullanıcı olaylarının zaman damgalı kaydı | Aynı sistemden türetilen iki kayıt bağımsız kanıt değildir |
| alarm | alarm | Bir durumun dikkat gerektirdiğini bildiren uyarı | Interlock ile aynı şey değildir; alarm eylemi engellemez |

## 10. Yönetişim, standart ve uyum terimleri

| İngilizce | Türkçe karşılık | Kısa tanım | Ayrım / not |
|---|---|---|---|
| security level (SL) | güvenlik seviyesi **D** | IEC 62443'te güvenlik yeteneği ve hedefinin ifade edildiği seviye kavramı | Tek başına bir "güvenlik notu" değildir; hangi seviye türünden söz edildiği her cümlede yazılır |
| target security level (SL-T) | hedef güvenlik seviyesi **D** | Bir bölge veya kanal için belirlenen hedef seviye | K07 kapsamı: her bölge ve kanal için SL-T belirlenir |
| capability security level (SL-C) | yetenek güvenlik seviyesi **D** | Bir kontrol sisteminin veya bileşenin sağlayabileceği seviye | Ayrıntı ve sürüm bilgisi [standartlar bölümünde](05-standartlar-ve-turkiye.md) |
| achieved security level (SL-A) | erişilen güvenlik seviyesi **D** | Sahada fiilen ulaşılan seviye | Hedef ve yetenek seviyesinden farklıdır; kabul kanıtıyla gösterilir |
| asset owner | varlık sahibi **D** | Sistemi işleten ve güvenlik programından sorumlu taraf | IEC 62443'te gereksinimler role göre ayrılır |
| system integrator | sistem entegratörü **D** | Sistemi tasarlayan ve kuran taraf | Aynı ayrım |
| product supplier | ürün tedarikçisi **D** | Bileşeni geliştiren ve sağlayan taraf | Güvenli geliştirme gereksinimleri bu role yöneliktir |
| standard | standart | Ortak terim, yöntem ve gereksinim listesi sunan belge | Tesisin fiziksel sürecini ve işletme kısıtlarını bilmez |
| technical specification | teknik şartname **D** | Standart olgunluğuna ulaşmamış veya farklı statüde yayımlanan teknik belge | Harmonize standart ile aynı statüde değildir |
| normative | normatif **D** | Uyulması beklenen, gereksinim niteliğindeki hüküm | Bilgilendirici ekten ayrılır. Bu sözlük normatif değildir |
| conformity | uygunluk | Belirli bir kapsamda, belirli gereksinimlerin karşılandığının gösterilmesi | Uygunluk beyanı ile güvenli işletme aynı ölçüm değildir |
| certification | belgelendirme | Uygunluğun üçüncü tarafça belgelenmesi | Sertifika ürüne verilir; güvenlik tesiste kurulur |
| regulation | yönetmelik | Düzenleyicinin çıkardığı bağlayıcı ikincil düzenleme | Hangi kurumun hangi düzenlemeye tabi olduğu bu depoda yorumlanmaz |
| repealed | mülga | Yürürlükten kaldırılmış metin | Terim tarihçesi için kullanılır, güncel dayanak olarak kullanılmaz (örnek: K15) |
| official gazette | Resmî Gazete | Resmi metinlerin yayımlandığı yayın | Künyesi bulunmayan bir metin yayımlanmış nihai metin sayılmaz |
| national occupational standard | ulusal meslek standardı | Bir meslekteki görev, bilgi ve beceri gereklerini tanımlayan belge | K18 bu türden bir belgenin revizyon taslağıdır; nihai metin değildir |
| publication date / access date | yayın tarihi / erişim tarihi | Belgenin yayımlandığı tarih ile kaynağın görüntülendiği tarih | Bu depoda ikisi ayrı tutulur; erişim tarihi 13.09.2026'dır |

## Sık karıştırılan kavram çiftleri

Aşağıdaki çiftler, benzer göründüğü için birbirinin yerine kullanılan kavramlardır. Ayrımın ayrıntısı bağlantı verilen bölümdedir.

| Çift | Tek cümlelik ayrım | Ayrıntı |
|---|---|---|
| koruma rölesi / kesici | Röle arızayı algılayıp karar üretir, kesici ise devreyi mekanik olarak açar; ikisi ayrı bileşendir | [Elektrik ve enerji](02-sektorler/02-elektrik-ve-enerji.md) |
| alarm / interlock | Alarm dikkat çeker ve eylemi engellemez, interlock koşul sağlanmadan eyleme izin vermez | [Kontrol döngüsü ve bileşenler](01-temeller/02-kontrol-dongusu-ve-bilesenler.md) |
| bölge (zone) / kanal (conduit) | Bölge ortak güvenlik gereksinimli varlık kümesidir, kanal bu bölgeler arasındaki denetimli iletişim yoludur | [Mimari ve güven bölgeleri](01-temeller/03-mimari-ve-guven-bolgeleri.md) |
| SIL / SL | SIL emniyet işlevinin bütünlüğünü anlatır, SL güvenlik seviyesi kavramıdır; sayı sayıya eşleştirilmezler | [Standartlar ve Türkiye](05-standartlar-ve-turkiye.md) |
| emniyet / güvenlik | Emniyet istenmeyen fiziksel zararı, güvenlik kasıtlı saldırıyı konu alır; onay süreçleri de ayrıdır | [Risk, emniyet ve bağımlılıklar](01-temeller/05-risk-emniyet-ve-bagimliliklar.md) |
| EKS / OT | EKS mevzuattaki kontrol sistemi terimidir, OT fiziksel süreçle etkileşen teknolojinin daha geniş şemsiyesidir | [OT nedir?](01-temeller/01-ot-nedir.md) |
| SCADA / DCS | SCADA coğrafi olarak dağılmış süreçlerin merkezden gözetimini, DCS bir tesisteki kontrol işlevlerinin bütünleşik düzenini anlatır | [OT nedir?](01-temeller/01-ot-nedir.md) |
| ETCS / ERTMS | ETCS tren kontrol parçasıdır, ERTMS tren kontrolü, haberleşme ve işletme kurallarını birlikte ele alan daha geniş çerçevedir | [Raylı sistemler](02-sektorler/03-rayli-sistemler.md) |
| CBTC / ETCS | CBTC sürekli tren–yol boyu haberleşmesine dayanan tren kontrol sistemidir; ETCS'nin başka adı değildir ve birlikte çalışabilirlik kendiliğinden doğmaz | [Raylı sistemler](02-sektorler/03-rayli-sistemler.md) |
| anklaşman / interlock | Anklaşman sinyal ve makas izin koşullarını denetleyen demiryolu işlevidir; proses tarafındaki interlock genel bir kilitleme mantığıdır | [Raylı sistemler](02-sektorler/03-rayli-sistemler.md) |
| ATS (demiryolu) / ATS (enerji) | Demiryolunda otomatik tren durdurma veya gözetim işlevini, enerji tarafında besleme kaynakları arasında geçiş yapan şalteri anlatır | [Raylı sistemler](02-sektorler/03-rayli-sistemler.md) ve [elektrik ve enerji](02-sektorler/02-elektrik-ve-enerji.md) |
| pasif gözlem / aktif tarama | Pasif gözlem mevcut trafiği dinler, aktif tarama hedefe sorgu gönderir; ikisinin süreç riski aynı değildir | [Envanter ve görünürlük](04-savunma/01-envanter-ve-gorunurluk.md) |
| yedek / kurtarma | Yedek geri yüklenebilir kopyadır, kurtarma hizmetin doğrulanmış biçimde yeniden verilmesidir | [Olay müdahalesi ve kurtarma](04-savunma/05-olay-mudahalesi-ve-kurtarma.md) |
| zafiyet / risk | Zafiyet bir zayıflıktır, risk bu zayıflığın erişilebilirliği ve sonucuyla birlikte değerlendirilmesidir | [Zafiyet ve değişiklik yönetimi](04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) |
| IT DMZ / OT DMZ | IT DMZ kurumsal ağ ile interneti ayırır, OT DMZ kurumsal ağ ile kontrol bölgelerini ayırır; kural sahibi ve hata davranışı farklıdır | [Segmentasyon ve uzak erişim](04-savunma/02-segmentasyon-ve-uzak-erisim.md) |
| hava boşluğu / tek yönlü ağ geçidi | Hava boşluğunda otomatik mantıksal bağlantı yoktur, tek yönlü geçitte otomatik ama tek yöne sınırlı bir akış vardır | [Segmentasyon ve uzak erişim](04-savunma/02-segmentasyon-ve-uzak-erisim.md) |
| historian / mühendislik istasyonu | Historian süreç geçmişini saklar, mühendislik istasyonu kontrol projesini değiştirebilir; yetki sonuçları farklıdır | [Kontrol döngüsü ve bileşenler](01-temeller/02-kontrol-dongusu-ve-bilesenler.md) |
| Purdue modeli / IEC 62264 seviyeleri | Purdue bir referans anlatımdır, IEC 62264 seviyeleri ise katalog kaydı doğrulanmış standart hiyerarşisidir; katalog metni "Purdue" adını geçirmez | [Mimari ve güven bölgeleri](01-temeller/03-mimari-ve-guven-bolgeleri.md) |

## Kısaltmalar

İngilizce açılımı bu çalışmada birincil kaynaktan doğrulanan kısaltmalar şunlardır: HMI, PLC, RTU ve IED (K06 ve K19); PAC (K06); DMZ (K03 ve K19); IoC (K02); SIS (K09); SL-T (K07); RBC, ERTMS, ETCS (K11); CBTC, ATP, ATO ve ATS'nin gözetim anlamı (K12); ATS demiryolu anlamıyla (K18); MMS, SCADA, UPS ve VPN (K19). Türkçe kısaltmalardan EKS, DKS ve KBS'nin karşılıkları resmî metinlerden alınmıştır (K14 ve K15); OT, IED, UPS ve VPN karşılıkları K19'dan gelir. Diğer satırlardaki açılımlar alanda yaygın kullanımdır ve bu çalışmada birincil kaynaktan doğrulanmamıştır. Türkçe sütunundaki işaretler yukarıdaki tablolarla aynı anlamdadır.

| Kısaltma | Açılım | Türkçe karşılık / açıklama |
|---|---|---|
| ADMS | Advanced Distribution Management System | dağıtım yönetim sistemi **D** |
| APC | Advanced Process Control | Gelişmiş Süreç Kontrol Sistemi **R**; açılım doğrulanmadı |
| ATC | Automatic Train Control | otomatik tren kontrol sistemi **T** |
| ATO | Automatic Train Operation | — **D**; açılım K12 özet metnindedir. "Sürüş işlevlerinin otomatik yürütülmesi" bu depoda açıklama amaçlı kullanımdır |
| ATP | Automatic Train Protection | otomatik tren koruma sistemi **T** |
| ATS | Automatic Train Stop (demiryolu) | otomatik tren durdurma sistemi **T**; CBTC bağlamında aynı kısaltma "Automatic Train Supervision" açılımıyla kullanılır (K12) |
| ATS | Automatic Transfer Switch (enerji) | otomatik transfer şalteri **D**; açılım ve karşılık doğrulanmadı |
| ATT&CK | — | MITRE'nin saldırgan davranışı kataloğu; ICS matrisi için K05 |
| BSS | Business Support Systems | — **D**; "ücretlendirme, faturalama ve sipariş süreçleri" bu depoda açıklama amaçlı kullanımdır |
| CBTC | Communications-Based Train Control | — **D**; "haberleşme temelli tren kontrolü" bu depoda açıklama amaçlı kullanımdır |
| DCS | Distributed Control System | Dağıtılmış Kontrol Sistemi **R**; açılım doğrulanmadı |
| DER | Distributed Energy Resources | dağıtık enerji kaynakları **D** |
| DKS | Dağıtılmış Kontrol Sistemi | DCS'nin resmî Türkçe kısaltması **R** |
| DMS | Distribution Management System | dağıtım yönetim sistemi **D** |
| DMZ | demilitarized zone | sınır ağı, ara bölge **D**; K19 "Sivil Bölge" karşılığını verir |
| DNP3 | Distributed Network Protocol 3 | uzak saha telemetrisi protokolü; açılım doğrulanmadı |
| EKS | Endüstriyel Kontrol Sistemi | ICS'nin resmî Türkçe karşılığı **R** (K14 ve K19) |
| EMS | Energy Management System | enerji yönetim sistemi **D** |
| ERTMS | European Rail Traffic Management System | Avrupa demiryolu trafik yönetimi çerçevesi **D** |
| ETCS | European Train Control System | Avrupa Tren Kontrol Sistemi **D** |
| GOOSE | Generic Object Oriented Substation Event | eşler arası olay mesajlaşması; açılım doğrulanmadı |
| GSM-R | GSM for Railways | demiryolu işletme haberleşmesi; açılım doğrulanmadı |
| HMI | Human-Machine Interface | operatör arayüzü **D** |
| HVAC | Heating, Ventilation and Air Conditioning | iklimlendirme **D**; açılım doğrulanmadı |
| IACS | Industrial Automation and Control Systems | endüstriyel otomasyon ve kontrol sistemleri **D** |
| ICCP | Inter-Control Center Communications Protocol | kontrol merkezleri arası protokol; açılım doğrulanmadı |
| ICS | Industrial Control System | endüstriyel kontrol sistemi (EKS) **R** |
| IED | Intelligent Electronic Device | akıllı elektronik cihaz **R** (K19) |
| IIoT | Industrial Internet of Things | endüstriyel nesnelerin interneti **D**; açılım doğrulanmadı |
| IoC | indicator of compromise | ihlal göstergesi **D** |
| IT | Information Technology | bilgi teknolojisi **D**; açılım doğrulanmadı |
| KBS | Kurumsal Bilişim Sistemi | mülga 2017 metnindeki kurumsal sistem tanımı **R** |
| MMS | Manufacturing Message Specification | IEC 61850 haberleşme eşlemesi; açılım K19 Kısaltmalar bölümünden |
| MTTR | Mean Time To Restore | ortalama geri dönüş süresi **D** |
| NOC | Network Operations Centre | şebeke işletim merkezi **D** |
| OPC UA | OPC Unified Architecture | endüstriyel veri ve servis mimarisi; açılım doğrulanmadı |
| OSS | Operations Support Systems | — **D**; "şebeke işletim destek sistemleri" bu depoda açıklama amaçlı kullanımdır |
| OT | Operational Technology | Operasyonel Teknolojiler **R** (K19); EPDK metinlerindeki yakın terim EKS'tir |
| PAC | Programmable Automation Controller | — **D**; "genişletilmiş yetenekli kontrolör sınıfı" bu depoda açıklama amaçlı kullanımdır |
| PLC | Programmable Logic Controller | Programlanabilir Mantık Kontrolcüsü **R** (K14); K19 "Programlanabilir Mantıksal Denetleyici" der |
| RAN | Radio Access Network | radyo erişim ağı **D** |
| RBC | Radio Block Centre | — **D**; "telsiz blok merkezi" bu depoda açıklama amaçlı kullanımdır |
| RPO | Recovery Point Objective | tolere edilen veri kaybı aralığı **D** |
| RTO | Recovery Time Objective | hedeflenen geri dönüş süresi **D** |
| RTU | Remote Terminal Unit | Uzak Terminal Ünitesi **R** |
| SBA | Service Based Architecture | servis tabanlı mimari **D** |
| SCADA | Supervisory Control And Data Acquisition | Veri Tabanlı Kontrol ve Gözetleme Sistemi **R** (K14); açılım ve "Merkezi Kontrol ve Veri Toplama" karşılığı K19'dan, "Veri Tabanlı Merkezi Kontrol ve Gözetleme Sistemi" karşılığı K20'den |
| SCL | System Configuration description Language | IEC 61850 yapılandırma dili; açılım doğrulanmadı |
| SIL | Safety Integrity Level | emniyet bütünlük seviyesi **D**; açılım doğrulanmadı |
| SIS | safety instrumented system | emniyet enstrümanlı sistem **D** |
| SL | Security Level | güvenlik seviyesi **D**; türleri SL-T, SL-C ve SL-A'dır |
| SOC | Security Operations Centre | güvenlik operasyon merkezi **D** |
| SUC | system under consideration | incelenen sistem **D**; açılım doğrulanmadı |
| SV | Sampled Values | örneklenmiş ölçümler **D**; açılım doğrulanmadı |
| TASE.2 | Telecontrol Application Service Element 2 | ICCP'nin standart adı; açılım doğrulanmadı |
| UE | User Equipment | uç cihaz **D**; açılım doğrulanmadı |
| UPS | Uninterruptible Power Supply | kesintisiz güç kaynağı **R** (K19) |
| VPN | Virtual Private Network | sanal özel ağ **R** (K19) |

## İlgili bölümler

- Temel kavramlar: [OT nedir?](01-temeller/01-ot-nedir.md), [kontrol döngüsü](01-temeller/02-kontrol-dongusu-ve-bilesenler.md), [mimari ve güven bölgeleri](01-temeller/03-mimari-ve-guven-bolgeleri.md), [protokoller](01-temeller/04-endustriyel-protokoller.md), [risk ve emniyet](01-temeller/05-risk-emniyet-ve-bagimliliklar.md)
- Sektörler: [su ve atıksu](02-sektorler/01-su-ve-atiksu.md), [elektrik ve enerji](02-sektorler/02-elektrik-ve-enerji.md), [raylı sistemler](02-sektorler/03-rayli-sistemler.md), [telekom](02-sektorler/04-telekom-ve-baz-istasyonlari.md), [karşılaştırma](02-sektorler/05-sektor-karsilastirmasi.md)
- Tehdit modelleme: [saldırgan bakış açısı](03-tehdit-modelleme/01-saldirgan-bakis-acisi.md), [MITRE ATT&CK for ICS](03-tehdit-modelleme/02-mitre-attack-ics.md)
- Savunma: [envanter](04-savunma/01-envanter-ve-gorunurluk.md), [segmentasyon ve uzak erişim](04-savunma/02-segmentasyon-ve-uzak-erisim.md), [izleme ve algılama](04-savunma/03-izleme-ve-algilama.md), [zafiyet ve değişiklik](04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md), [olay ve kurtarma](04-savunma/05-olay-mudahalesi-ve-kurtarma.md)
- Standart ve mevzuat çerçevesi: [standartlar ve Türkiye](05-standartlar-ve-turkiye.md)
- Uygulama: [şablonlar](../templates/README.md) ve [çevrimdışı laboratuvarlar](../labs/README.md)

## Kaynaklar

Aşağıdaki kaynakların tamamı 13.09.2026 tarihinde görüntülenmiştir. Ücretli standartlarda yalnızca kataloğun kamuya açık kayıt sayfası kullanılmış, tam metinlere erişilmemiştir. Bir terimin karşısında kimlik (K01 gibi) yoksa, o satırdaki açıklama bu depoda sadeleştirilmiştir ve normatif bir metne dayandırılmamıştır.

| Kimlik | Kaynak ve bağlantı | Tarih | Bu sözlükte desteklediği | Erişim ve kapsam notu |
|---|---|---|---|---|
| K01 | NIST, *Guide to Operational Technology (OT) Security*, SP 800-82 Rev. 3, [yayın kaydı](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Yayın: Eylül 2023, final | OT kapsamının şemsiye dayanağı | Yalnızca katalog sayfası açıldı; tanım cümleleri PDF tam metninden alıntılanmadı |
| K02 | NIST, [CSRC Glossary](https://csrc.nist.gov/glossary) | Terim güncellemesi: 26 Ağustos 2026 | "indicator of compromise" (SP 800-61r3) ve "baseline configuration" (SP 800-128) tanımları | Sayfa kendisi tanımların resmî veya tercih edilen tanım sayılmaması gerektiğini belirtir; atıf kaynak yayına yapılır |
| K03 | NIST, [CSRC Glossary: demilitarized zone](https://csrc.nist.gov/glossary/term/demilitarized_zone) | Sayfada tarih belirtilmiyor | DMZ için tek bir resmî tanım bulunmadığı bilgisi | En az beş ayrı NIST/CNSS kaynaklı tanım listelenir; Türkçe karşılık bu kaynakta yoktur |
| K04 | NIST, [CSRC Glossary: air gap](https://csrc.nist.gov/glossary/term/air_gap) | Sayfada tarih belirtilmiyor | Hava boşluğunun tanımı (CNSSI 4009-2022 kaynaklı) | "unidirectional gateway" ve "data diode" bu sayfada geçmez |
| K05 | MITRE, [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/) | Sayfada yayın tarihi yok; içerik sürümü v19.2 | ICS matrisindeki 12 taktik ve 90 teknik sayısı | Sürüm sürekli değişir; sürüm numarası ile erişim tarihi birlikte okunmalıdır. "Tehdit modeli" ve "saldırı yüzeyi" burada sözlük maddesi değildir |
| K06 | MITRE, [ATT&CK for ICS Assets](https://attack.mitre.org/assets/) | Sayfada yayın tarihi yok; içerik sürümü v19.2 | A0001–A0018 varlık adları: HMI, PLC, RTU, IED, historian, kontrol sunucusu, emniyet kontrolörü, jump host, saha G/Ç, PAC ve diğerleri | Mühendislik istasyonu ayrı varlık değildir (A0001 altında); "bastion host" varlık adı olarak geçmez. Tanımlar kısa özet düzeyindedir |
| K07 | IEC 62443-3-2:2020, [katalog kaydı](https://webstore.iec.ch/en/publication/30727) | Yayın: 24 Haziran 2020, Ed. 1.0 | Bölge ve kanal ayrımı, SL-T ve incelenen sistem (SUC) kavramları | Ücretli standart; yalnızca katalog kapsamı kullanıldı. Normatif sözlük tanımları IEC 62443-1-1'dedir ve o kayıt açılmadı |
| K08 | IEC 62264-1:2013, [katalog kaydı](https://webstore.iec.ch/en/publication/6675) | Yayın: 22 Mayıs 2013, Ed. 2.0 | Seviye hiyerarşisi (4, 3, 2 ve 1) | Ücretli; yalnızca katalog kaydı. Katalog sayfası "Purdue" adını geçirmez ve "Seviye 3,5 / DMZ" bu standartta yoktur |
| K09 | IEC 61511-1:2016, [katalog kaydı](https://webstore.iec.ch/en/publication/24241) | Yayın: 24 Şubat 2016, Ed. 2.0 | SIS, emniyetli durum ve emniyet yaşam döngüsü terimleri | Ücretli; yalnızca katalog kaydı. SIL tanımı bu sayfada gösterilmez; asıl kaynak IEC 61508'dir ve o kayıt açılmadı |
| K10 | IEC 60870-5-104:2006, [katalog kaydı](https://webstore.iec.ch/en/publication/3746) | Yayın: 13 Haziran 2006, Ed. 2.0 | "telecontrol" teriminin IEC kullanımı ve kapsamı | Ücretli; yalnızca katalog kaydı. "master / outstation" ikilisi bu seriye değil DNP3'e aittir ve IEEE 1815 kaydı doğrulanmadı |
| K11 | ERA, UNISIG ve EEIG ERTMS Users Group, *ERTMS/ETCS Glossary of Terms and Abbreviations*, SUBSET-023, Issue 4.0.0, [PDF](https://www.era.europa.eu/system/files/2023-09/index003_-_SUBSET-023_v400.pdf) | Belge tarihi: 5 Temmuz 2023 | BALISE, EUROBALISE, RADIO BLOCK CENTRE ve INTERLOCKING tanımları; ERTMS ve ETCS açılımları | PDF indirildi ve metni okundu. "axle counter" bu sürümde tanımlı değildir; CBTC de kapsam dışıdır. Türkçe karşılık içermez |
| K12 | IEEE 1474.1-2025, [standart kaydı](https://standards.ieee.org/ieee/1474.1/6959/) | Kurul onayı: 27 Mart 2025; yayım: 13 Haziran 2025 | CBTC tanımı; ATP'nin zorunlu, ATO ve ATS'nin opsiyonel olması | Ücretli; yalnızca katalog ve özet sayfası. Önceki sürümler (1474.1-1999, 1474.1-2004) esas alınmaz. Türkçe karşılık yoktur |
| K13 | ETSI / 3GPP, *5G; System Architecture for the 5G System*, ETSI TS 123 501 V18.8.0, [PDF adresi](https://www.etsi.org/deliver/etsi_TS/123500_123599/123501/18.08.00_60/ts_123501v180800p.pdf) | Sürüm tarihi: 2025-01 | RAN, çekirdek şebeke ve ağ dilimleme kavramlarının kaynak çerçevesi | PDF bu çalışmada açılmadı; yalnızca başlık, sürüm ve tarih doğrulandı. Telekom bölümü aynı belgenin V18.11.0 sürümünü kullanır. Bu sözlükteki telekom tanımları alıntı değildir |
| K14 | EPDK, *Enerji Sektöründe Siber Güvenlik Yetkinlik Modeli Yönetmeliği*, [Resmî Gazete metni](https://www.resmigazete.gov.tr/eskiler/2023/06/20230606-2.htm) | Resmî Gazete: 6 Haziran 2023, sayı 32213 | EKS, SCADA, DKS, APC, PLC ve RTU Türkçe karşılıklarının yürürlükteki dayanağı (madde 4/1-ç) | Tam metin indirilip okundu. Yönetmelik DMZ, HMI, IED, historian, hava boşluğu ve varlık envanteri gibi terimleri tanımlamaz; "operasyonel teknoloji" ibaresi metinde geçmez |
| K15 | EPDK, *Enerji Sektöründe Kullanılan Endüstriyel Kontrol Sistemlerinde Bilişim Güvenliği Yönetmeliği* (mülga), [Resmî Gazete metni](https://www.resmigazete.gov.tr/eskiler/2017/07/20170713-5.htm) | Resmî Gazete: 13 Temmuz 2017, sayı 30123 | Aynı Türkçe karşılıkların ilk yerleşimi; "kritik enerji altyapısı" ve "Kurumsal Bilişim Sistemi (KBS)" tanımları | 2023 tarihli yönetmeliğin 16. maddesiyle yürürlükten kaldırılmıştır; güncel dayanak olarak kullanılmaz, terim tarihçesi için gösterilir |
| K16 | EPDK ve TEİAŞ, *Elektrik Şebeke Yönetmeliği*, madde 4 Tanımlar, [mevzuat.gov.tr metni](https://mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.19722.pdf) | PDF'te yayım künyesi görünmüyor; dayanak 14/3/2013 tarihli 6446 sayılı Kanun | Bara, transfer bara, fider, transfer fideri, kesici ve ayırıcı karşılıkları; "hedef üretim değerlerini (set-point)" kullanımı | 243 sayfalık konsolide metin indirilip okundu. Resmî Gazete tarih ve sayısı doğrulanamadı. Koruma rölesi, SCADA, ölçü transformatörü ve recloser bu maddede tanımlı değildir |
| K17 | Türk Dil Kurumu, [Güncel Türkçe Sözlük sorguları](https://sozluk.gov.tr/gts?ara=r%C3%B6le) | Sayfada güncelleme tarihi belirtilmiyor | "röle" tanımının elektrik koruma anlamını karşılamadığı; "kesici" maddesinde elektrik anlamının bulunmadığı; "aktüatör" kaydının bulunmadığı | Genel sözlük OT terminolojisi için yetkili karşılık kaynağı değildir. TDK'nın alan sözlükleri bu çalışmada sorgulanmadı |
| K18 | MYK, *Raylı Sistemler Sinyalizasyon Bakım ve Onarımcısı (Seviye 4) Ulusal Meslek Standardı*, ref. 12UMS0235-4, Rev. 01 taslak, [TCDD duyuru PDF'i](https://static.tcdd.gov.tr/webfiles/userfiles/files/duyuru/2025/101220251.pdf) | Telif notu 2025; Resmî Gazete künyesi ve onay tarihi boş | Anklaşman, balis/baliz, makas, sinyal, ATS, ATC ve ATP Türkçe karşılıkları | Yayımlanmış nihai metin değil, revizyon taslağıdır; bu nedenle karşılıklar **T** ile işaretlenmiştir. "Aks sayıcı" ve RBC bu taslakta bulunamadı |
| K19 | Siber Güvenlik Başkanlığı, *Bilgi ve İletişim Güvenliği Rehberi*, sürüm 1.1, [PDF](https://cdn.siberguvenlik.gov.tr/public/docs/bg_rehber.pdf) | Sürüm tarihi: 01.03.2026 | OT, IED, UPS ve VPN karşılıkları ile MMS açılımı; DMZ, EKS, HMI, PLC, RTU ve SCADA kısaltmalarının Rehber'deki biçimleri; "hava boşluğu", "veri diyotu/diyodu" ve "varlık envanteri" terimlerinin kullanımı | 235 sayfalık tam metin okundu. Kısaltmalar bölümü belge içi s. 5–6'dadır; gövde kullanımları 3.1.1.1, 3.1.6.36 ve 4.5.2.15 sayılı tedbirlerdendir. "Sıçrama sunucusu" bu belgede bulunamadı |
| K20 | T.C. Resmî Gazete, *Siber Olaylara Müdahale Ekiplerinin Kuruluş, Görev ve Çalışmalarına Dair Usul ve Esaslar Hakkında Tebliğ*, [metin](https://www.resmigazete.gov.tr/eskiler/2013/11/20131111-6.htm) | Resmî Gazete: 11 Kasım 2013, sayı 28818 | Madde 3/1-b'deki "Veri Tabanlı Merkezi Kontrol ve Gözetleme Sistemi (SCADA)" ve "coğrafi olarak Dağınık Kontrol Sistemleri (DKS)" karşılıkları | Tebliğ metni okundu. Güncel yürürlük durumu bu çalışmada kesinleştirilemedi; durum [standartlar bölümünde](05-standartlar-ve-turkiye.md) işaretlidir |

### Bu sözlükte kullanılmayan ve açık bırakılan noktalar

- Bilgi ve İletişim Güvenliği Rehberi (K19) bu çalışmanın standartlar hattında Başkanlığın güncel adresinden okunmuştur; çözümlenemeyen adres yalnızca Rehber'in eski yayın adresidir (cbddo.gov.tr). OT, IED, UPS ve VPN karşılıkları, MMS açılımı ve hava boşluğu, veri diyotu ile varlık envanteri terimleri bu metinden alınmıştır; EKS ve RTU karşılıklarını Rehber de aynı biçimde verir. DMZ, HMI, PLC ve SCADA satırlarında Rehber'in karşılığı notta gösterilmiş, bu depoda başka bir karşılık kullanılmıştır. Rehber'in kurumsal çerçevesi [standartlar bölümündedir](05-standartlar-ve-turkiye.md). Rehber taramasında bulunamayan terim "sıçrama sunucusu"dur; o satır **D** olarak kalmıştır.
- IEC 61508 (SIL'in asıl kaynağı) ve IEC 62443-1-1 (bölge, kanal ve IACS terimlerinin normatif tanımları) katalog kayıtları açılmadı; ilgili satırlar dolaylı dayanakla ve **D** işaretiyle verildi.
- IEEE 1815 (DNP3), EN 50617 ve IEC 62290 serileri ile EN 50129 incelenmedi; master/outstation, aks sayıcı ve emniyet dosyası satırlarındaki belirsizlik bu nedenle açık bırakıldı.
- UPS, doğrultucu, jeneratör ve iklimlendirme terimleri için birincil tanım kaynağı aranamadı; karşılıklar yaygın kullanım olarak verilmiştir.
- TSE'nin Türkçe standart uyarlamaları (TS EN 62264-1, TS EN 61511-1 ve benzerleri) doğrulanmadı. Bu uyarlamalarda farklı Türkçe karşılıklar bulunması mümkündür; sözleşme ve şartname dilinde ilgili TSE metni ayrıca kontrol edilmelidir.
- Sözlükteki hiçbir satır bir ürünün belirli bir özelliği desteklediği veya bir tesiste etkin olduğu iddiasını taşımaz. Tanımlar terim ayrımı içindir; yapılandırma kanıtı tesis özelinde aranır.

Katkı verirken terim eklemenin koşulları [katkı rehberindedir](../CONTRIBUTING.md). Yeni bir satır ya doğrulanmış bir kaynağa bağlanır ya da bu depoda sadeleştirilmiş açıklama olduğu işaretlenir.
