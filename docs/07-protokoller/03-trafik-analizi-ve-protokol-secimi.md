# Trafik analizi ve protokol seçimi

Bu bölüm, mevcut bir trafik kaydından hangi sonuçların çıkarılabileceğini ve protokol seçiminin nasıl gerekçelendirileceğini gösterir. [Katalog](01-protokol-katalogu.md) taşıma biçimlerini, [Modbus ve OPC UA bölümü](02-modbus-ve-opc-ua-guvenligi.md) güvenlik denetimlerini açıklar.

Alıştırma Markdown içindeki sentetik kayıt özetiyle tamamlanabilir. Depoda bu bölüm için PCAP dosyası bulunmaz. Wireshark örnekleri, ayrıca elde bulunan ve paylaşılması onaylanmış kurgusal/izole eğitim kaydını **çevrimdışı** incelemek içindir; canlı ağda kayıt alma veya cihazlara paket gönderme adımı değildir.

## Kaydı yorumlama yöntemi

Wireshark display filter, açılmış kayıtta hangi paketlerin görüntüleneceğini seçer; kaydı değiştirmez. Filtrede bir protokol adının kullanılması, o protokolün ayrıştırıcı tarafından tanınmasına bağlıdır. [Wireshark görüntüleme filtresi rehberi](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)

Özgün inceleme sırası:

1. Kayıt kimliği, kaynak, zaman aralığı, saat dilimi ve temsil ettiği işletme durumunu yazın. Dosya verilmediyse “sentetik tablo incelemesi” diye belirtin.
2. Kapsamı kaydedin: gözlem noktası, atlanan trafik, şifreleme, kayıp/eksik kayıt bilgisi. Bilinmeyenleri sıfır kabul etmeyin.
3. Uçları envanterle eşleyin; isim/IP/MAC benzerliğini kimlik doğrulama yerine kullanmayın.
4. Protokolü, yönü, işlem sınıfını ve istek–yanıt ilişkisini birlikte değerlendirin.
5. Normal üretim, başlatma, durdurma, bakım ve yedek sisteme geçiş dönemlerini ayırın.
6. Sapmayı onay, rol, uygulama olayı ve süreç verisiyle karşılaştırın. Paket tek başına niyeti veya fiziksel sonucu kanıtlamaz.
7. Bulguyu “gözlendi / çıkarım / bilinmiyor” alanlarıyla raporlayın.

## Çevrimdışı display filter örnekleri

Filtre adları, erişim tarihinde resmî Wireshark alan referanslarından kontrol edilmiştir. Kullanılan Wireshark sürümü ve ayrıştırıcı desteği rapora yazılmalıdır. Bunlar capture filter değildir.

| Amaç | Display filter | Ne gösterir / sınır | Resmî alan kaynağı |
|---|---|---|---|
| Modbus trafiği | `modbus` | Modbus olarak ayrıştırılmış iletiler; şifreli gövde görünmeyebilir | [Modbus](https://www.wireshark.org/docs/dfref/m/modbus.html) |
| Holding register okuma | `modbus.func_code == 3` | İlgili kodu taşıyan iletiler; yön ayrıca incelenir | [Modbus](https://www.wireshark.org/docs/dfref/m/modbus.html) |
| Seçilmiş Modbus yazma sınıfları | `modbus.func_code in {5 6 15 16 22 23}` | Bir yazma işleminin istek ve yanıtı eşleşebilir; tam yazma kataloğu değildir | [Modbus](https://www.wireshark.org/docs/dfref/m/modbus.html) |
| Modbus exception alanı | `modbus.exception_code` | Ayrıştırılmış hata yanıtları; otomatik saldırı göstergesi değildir | [Modbus](https://www.wireshark.org/docs/dfref/m/modbus.html) |
| Klasik S7 iletişimi | `s7comm` | Bu ayrıştırıcının tanıdığı S7 trafiği; bütün S7 nesilleri ve şifreli kanalları kapsamaz | [S7 Communication](https://www.wireshark.org/docs/dfref/s/s7comm.html) |
| PROFINET gerçek zaman trafiği | `pn_rt` | RT çerçeveleri; bütün tanılama/mühendislik trafiği değildir | [PROFINET RT](https://www.wireshark.org/docs/dfref/p/pn_rt.html) |
| OPC UA Binary | `opcua` | Tanınan UA Binary yapıları; şifreli servis içeriği için tek başına yeterli değildir | [OpcUa Binary](https://www.wireshark.org/docs/dfref/o/opcua.html) |
| DNP3 | `dnp3` | DNP3 olarak ayrıştırılan iletiler; zaman kalitesi ve profil ayrıca incelenir | [DNP3](https://www.wireshark.org/docs/dfref/d/dnp3.html) |
| EtherNet/IP kapsülleme | `enip` | EtherNet/IP ayrıştırıcısıyla tanınan kayıtlar; tüm implicit I/O kapsamı diye sunulmaz | [EtherNet/IP](https://www.wireshark.org/docs/dfref/e/enip.html) |

**Yorumlama hatası:** Bir filtre sıfır paket gösterirse “bu protokol kullanılmıyor” sonucu çıkmaz. Yanlış kayıt noktası, eksik dönem, şifreli içerik, desteklenmeyen profil veya farklı taşıma eşlemesi düşünülebilir. Bu sınırlılık değerlendirmesi deponun özgün önerisidir.

## Normal trafik profili

Normal trafik profili (baseline), tek bir ortalama değer değil, **belirli bir işletme durumu için beklenen akış ve işlem kümesi** olarak tutulmalıdır. Aşağıdaki şablon özgün öneridir; evrensel eşik içermez.

| Alan | Kaydedilecek bilgi | Yanlış yorum örneği |
|---|---|---|
| Dönem ve durum | Başlangıç/bitiş, süre, üretim veya bakım durumu | Bakım kaydını üretim normali saymak |
| Uçlar ve yön | Başlatan uç, hedef, varsa geçit/NAT ilişkisi | Yanıtın kaynağını yeni istemci saymak |
| İşlem kümesi | Protokol, servis/function code, okuma/değişiklik | Her Modbus iletisini yalnız veri okuma sanmak |
| Sıklık ve dağılım | Gözlenen örnek sayısı; periyot/aralık dağılımı | Üç paketle günlük davranış sonucu çıkarmak |
| Yanıt ve hata | Eşleşmiş istek/yanıt sayısı, exception ve eksikler | Eksik yanıtı kesin cihaz arızası saymak |
| Gecikme | Ölçüm tanımı, örnek sayısı ve gözlem noktası | Paket zaman farkını tüm kontrol döngüsü gecikmesi saymak |
| Veri anlamı | Zaman damgası, kalite, birim, güncellik | Eski ama geçerli biçimli veriyi yeni ölçüm saymak |
| Onay bağlamı | Yetki, bakım penceresi ve değişiklik kaydı | İzinli uçtan her işlemi normal saymak |

### Sentetik kayıt özeti

Kurgusal su tesisi için SCADA-A yalnız FC03 ile PLC-B verisini okur. EWS-C, `D-17` onaylı değişiklik kapsamında 10:05–10:10 arasında FC16 kullanabilir. Uç-D envanterde yoktur. Saatlerin eşzamanlı olduğu **yalnız bu alıştırma için varsayılmıştır**.

| Kayıt | Zaman | Başlatan → hedef | İşlem / gözlem | Ek bağlam |
|---|---|---|---|---|
| K1 | 10:00:00 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K2 | 10:00:01 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K3 | 10:00:02 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K4 | 10:06:00 | EWS-C → PLC-B | FC16 isteği, normal yanıt | D-17 kaydı var |
| K5 | 10:07:00 | Uç-D → PLC-B | FC03 isteği, yanıt özette yok | Envanter eşleşmesi yok |
| K6 | 10:12:00 | SCADA-A → PLC-B | FC16 isteği, exception yanıtı | SCADA-A için değişiklik yetkisi yok |

**Çözüm yaklaşımı:** K1–K3 arasında birer saniye gözlenmiştir; bu kısa örnek tüm vardiya için periyot garantisi değildir. K4 onayla eşleşen değişikliktir; süreç sonucunu ayrıca incelemek gerekir. K5 yeni iletişim ortağı bulgusudur; yanıt özette olmadığı için erişimin başarılı olduğu söylenmez. K6 yetkiyle çelişen yazma isteğidir; exception yanıtından fiziksel değişiklik sonucu çıkarılmaz.

### Algılama ve savunma çıktısı

| Aday kural | Mantık, özgün öneri | Olumlu örnek | Olumsuz / bağlamlı örnek |
|---|---|---|---|
| Yeni iletişim ortağı | Başlatan uç ilgili akışın onaylı uç kümesinde yok | K5 | K1 |
| Yetki dışı işlem | İstek sınıfı ilgili rolün izinli işlem kümesinde yok | K6 | K4, D-17 ve rol kaydıyla birlikte |
| Açıklanamayan değişiklik | İşlem için gereken onay veya zaman kapsamı bulunamıyor | K6 için ayrıca incelenir | K4 |

Bu mantık güvenlik ürünü kurulduğunu veya alarm çalıştırıldığını göstermez. Ürüne aktarılacaksa alan eşlemesi, eksik veri davranışı ve pozitif/negatif test kanıtı ayrıca gerekir.

## Protokol seçimi için karar çerçevesi

“En güvenli/en hızlı protokol” şeklinde tek sıralama yerine önce işlev yazılır. Aşağıdaki tablolar [katalogdaki kaynaklı işlev farklarından](01-protokol-katalogu.md) türetilen **özgün karar sorularıdır**; laboratuvar performans ölçümü veya ticari özellik garantisi değildir. Gecikme/bant genişliği sayıları, tüm maliyetler ve ürün uyumu adayların gerçek sürümleriyle doğrulanır.

### Modbus TCP ve OPC UA

| Ölçüt | Modbus TCP açısından inceleme | OPC UA açısından inceleme |
|---|---|---|
| Performans | Sorgu sıklığı ve register haritası iş yükünü karşılıyor mu? | Servis/abonelik ve veri modeli yükü karşılıyor mu? |
| Birlikte çalışma | Birim, ölçek ve adres anlamları iki uçta aynı mı? | Aynı bilgi modeli/profil ve veri tipleri destekleniyor mu? |
| Güvenlik | Klasik/güvenli profil, uç ve işlem kısıtları belli mi? | Mod, politika, uygulama güveni ve kullanıcı yetkileri belli mi? |
| Maliyet | Geçit, harita bakımı ve ek güvenlik ihtiyacı nedir? | Sunucu/istemci, sertifika ve model yönetiminin toplam emeği nedir? |
| Gecikme | Sorgu döngüsü ve hata sonrası davranış uygun mu? | Örnekleme/yayın aralığı ve yeniden bağlanma davranışı uygun mu? |
| Karmaşıklık | Basit veri tablosunun süreç anlamı kimde tutuluyor? | Model ve güven yaşam döngüsünü kim yönetecek? |
| Üretici bağımlılığı | Özel register haritası ve fonksiyonlar taşınabilir mi? | Özel ad alanı ve üretici metotları taşınabilir mi? |
| Eski cihaz uyumu | Mevcut cihaz doğrudan destekliyor mu? | Geçit veya cihaz değişimi gerekiyor mu? |

**Kurgusal karar:** Sabit register haritası olan eski PLC için mevcut Modbus bağlantısı, açık kontrol ve geçiş planıyla sürdürülebilir. Birden fazla üst sistemin anlamlı veri modeli ve ayrı kullanıcı rolleri istediği yeni entegrasyonda OPC UA aday olarak değerlendirilir. Bu karar UA'nın otomatik olarak daha düşük gecikmeli olduğunu söylemez.

### PROFINET ve EtherNet/IP

| Ölçüt | PROFINET açısından inceleme | EtherNet/IP açısından inceleme |
|---|---|---|
| Performans | Gerekli RT/IRT işlevi ve cihaz uygunluk sınıfı nedir? | Gerekli CIP I/O işlevi ve bağlantı kapasitesi nedir? |
| Birlikte çalışma | Denetleyici, I/O ve mühendislik tanımları birlikte doğrulanmış mı? | Denetleyici, cihaz profili ve nesne eşlemeleri uyumlu mu? |
| Güvenlik | Hangi PROFINET Security sınıfı uygulanmış? | Hangi CIP Security profili uygulanmış? |
| Maliyet | Mevcut cihaz/mühendislik yatırımı ve geçiş emeği nedir? | Mevcut cihaz/mühendislik yatırımı ve geçiş emeği nedir? |
| Gecikme | Seçilen sınıf/topoloji için gereksinim karşılanıyor mu? | I/O periyodu ve ağ davranışı gereksinimi karşılıyor mu? |
| Karmaşıklık | L2 ve IP servisleri birlikte yönetilebiliyor mu? | Explicit/implicit akışlar ve unicast/multicast yönetilebiliyor mu? |
| Üretici bağımlılığı | Özel tanılama ve mühendislik araçlarına bağımlılık nedir? | Özel nesne ve mühendislik araçlarına bağımlılık nedir? |
| Eski cihaz uyumu | Mevcut saha I/O'larına geçit gerekiyor mu? | Mevcut saha I/O'larına geçit gerekiyor mu? |

**Kurgusal karar:** Aynı kontrol hücresinde öncelik, süreç gereksinimini karşılayan doğrulanmış cihaz/denetleyici ekosistemidir. Bir protokolün marka ile ilişkilendirilmesi bütün marka ürünlerinin destek garantisi sayılmaz. İki seçeneğin saha kabulü eşitse işletme ekibinin bakım, tanılama ve yedek parça yetkinliği karara eklenir.

### OPC UA ve MQTT

OPC UA'nın PubSub ve broker kullanan modelleri de vardır; bu iki teknoloji her durumda birbirini dışlayan seçenek değildir. [OPC UA Part 2, 4.5.3](https://reference.opcfoundation.org/specs/OPC-10000-2/4)

| Ölçüt | OPC UA açısından inceleme | MQTT açısından inceleme |
|---|---|---|
| Performans | Client/server veya PubSub iş yükü ve veri modeli nedir? | Broker kapasitesi, yayın sıklığı ve abone sayısı nedir? |
| Birlikte çalışma | Ortak bilgi modeli ve profil var mı? | Ortak konu, payload şeması ve anlam sözleşmesi var mı? |
| Güvenlik | Uygulama/kullanıcı güveni ve seçilen modelin koruması nedir? | İstemci kimliği, TLS ve konu yetkisi nasıl doğrulanıyor? |
| Maliyet | Model ve sertifika işletimi ne gerektiriyor? | Broker, mesaj saklama/iletme ve şema yönetimi ne gerektiriyor? |
| Gecikme | Uygulama güncelleme gereksinimi hangi UA modeliyle sağlanacak? | Broker ve yeniden teslim davranışı süreç gereksinimine uygun mu? |
| Karmaşıklık | Servis ve bilgi modeli yönetilebiliyor mu? | Mesaj anlamı, eski mesaj ve yeniden bağlantı yönetilebiliyor mu? |
| Üretici bağımlılığı | Özel bilgi modeli taşınabilir mi? | Özel payload/konu ve broker özellikleri taşınabilir mi? |
| Eski cihaz uyumu | Uygun sunucu/geçit var mı? | Uygun yayıncı/geçit var mı? |

**Kurgusal karar:** Historian'a birimler ve veri tipleriyle erişim için UA client/server; çok sayıda üst sistem tüketicisine telemetri dağıtımı için MQTT adaydır. MQTT teslim kalitesi, fiziksel komutun bir kez ve doğru zamanda uygulandığı garantisi olarak yorumlanmaz; bu, uygulama kabul ölçütü olarak ayrıca tanımlanır. MQTT güvenlik tasarımı seçilen iletişim ve yetki mekanizmalarına bağlıdır. [OASIS MQTT 5.0, bölümler 4–5](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)

### DNP3 ve IEC 60870-5-104

| Ölçüt | DNP3 açısından inceleme | IEC 104 açısından inceleme |
|---|---|---|
| Performans | Olay/tarama yükü ve mevcut bağlantı koşulları nedir? | Telekontrol mesaj yükü ve TCP bağlantı davranışı nedir? |
| Birlikte çalışma | Cihaz alt kümesi, profil ve nesne varyasyonları uyumlu mu? | Veri/komut tipleri, adresleme ve iki uç profili uyumlu mu? |
| Güvenlik | Hangi kimlik/güvenlik profili ve anahtar yönetimi var? | Hangi IEC 62351 mekanizması veya korunan yol var? |
| Maliyet | RTU/SCADA sürücüsü, anahtar ve geçiş emeği nedir? | RTU/SCADA sürücüsü, güvenlik ve geçiş emeği nedir? |
| Gecikme | Olay aktarımı ve hat kesintisi sonrası toparlanma uygun mu? | Mesaj iletimi ve bağlantı toparlanması uygun mu? |
| Karmaşıklık | Olay, zaman ve profil eşlemeleri yönetilebilir mi? | Telekontrol tipleri, zaman ve adres eşlemeleri yönetilebilir mi? |
| Üretici bağımlılığı | Üretici uzantıları ve profil farkları nedir? | Üretici uzantıları ve profil farkları nedir? |
| Eski cihaz uyumu | Seri/IP mevcut kurulumla uyum nedir? | Mevcut 104 uçları veya seri 101 geçitleriyle uyum nedir? |

**Kurgusal karar:** Mevcut RTU ve kontrol merkezi profillerinin karşılıklı desteği, telemetri/olay gereksinimi ve güvenlik profili kanıtı belirleyicidir. Coğrafi yaygınlık veya protokol adı tek başına teknik seçim gerekçesi yapılmaz. DNP3 özellikleri ve 104 TCP/IP kapsamı için [DNP-UG](https://www.dnp.org/About/Features-of-DNP3) ve [Apache PLC4X sürücü belgesi](https://plc4x.apache.org/plc4x/latest/users/protocols/iec-60870.html) temel kaynaklardır.

## Risk, kontrol ve kanıt

Bu kurgusal tablo, trafik incelemesini savunma tasarımına bağlayan özgün öneridir.

| Hedef | Ön koşul | Aşılan güven sınırı | Olası hizmet/fiziksel etki | Gözlenebilir belirti | Karşılık gelen kontrol |
|---|---|---|---|---|---|
| Kontrol ağına yeni istemci ekleme | Yeni ucun erişimi mevcut | Onaylı varlık kümesi | İstenmeyen erişim veya yük | K5 gibi yeni uç | Envanter–akış mutabakatı ve izin incelemesi |
| Beklenmeyen değişiklik | Veri okuyucu rolü değişiklik isteği gönderebiliyor | Okuma ile değişiklik yetkisi | Kontrol değerinde değişiklik olasılığı | K6 gibi rol dışı işlem | İşlem izinleri ve uygulama yetkilendirmesi |
| Sapmayı normal gösterme | Baseline yalnız bakım döneminden çıkarılmış | Referans veri ile işletme kararı | Anormal işlemin fark edilmemesi | Açıklamasız geniş normal işlem kümesi | İşletme durumuna göre ayrı baseline ve sahip onayı |

## THEORY → LAB → TEST → DEFENSE → REPORT

| Aşama | Görev | Kabul ölçütü |
|---|---|---|
| THEORY | L2 trafik, display filter ve istek/yanıt farkını açıklayın | Filtre sonucu protokolün yokluk kanıtı sayılmıyor |
| LAB | K1–K6'yı uç, işlem, sonuç ve belirsizlik alanlarına ayırın | Altı kaydın tümü yer alıyor; gerçek PCAP işlendiği iddia edilmiyor |
| TEST | Üç aday kuralı sentetik tablo üzerinde değerlendirin | K4 bakım bağlamıyla ayrılıyor; K5/K6 için uygun bulgu yazılıyor |
| DEFENSE | İki bulguya kontrol, kontrol sahibi ve doğrulama kanıtı atayın | “Firewall ekle” gibi kapsamı belirsiz tek cümleyle bırakılmıyor |
| REPORT | Kurgusal tesis için dört karşılaştırmadan birini seçip sekiz ölçütle karar yazın | Bir alternatif, bir maliyet kalemi ve bir doğrulanmamış varsayım açık |

Her satır bir puandır; beş puan bu belge çalışmasının kabulüdür. Kısa örnekten tesis geneli sonuç çıkarılması veya yazma isteğinden fiziksel başarı iddia edilmesi kritik düzeltme gerektirir. Portföyde çıktı “sentetik OT trafik analizi ve protokol seçim raporu” diye sunulabilir; saha testi veya ürün kurulumu diye sunulmaz.

## Kaynaklar ve kapsam

Wireshark alan referansları ve kullanım rehberi yaşayan belgelerdir; erişim: 16.09.2026. Tek tek kaynak/sürüm sınırları [araştırma kaydındadır](../../research/protokol-kaynaklar.md). Sentetik veriler, karar matrisleri, eşikler yerine kullanılan sorular ve değerlendirme ölçütleri deponun özgün eğitim sentezidir. Performans karşılaştırması, fiyat teklifi ve sertifikasyon testi yapılmamıştır.

