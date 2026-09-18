# Endüstriyel protokoller

Protokol, iki sistemin veri ve işlevleri hangi kurallarla paylaştığını belirler. Güvenlik değerlendirmesinde adını veya portunu bilmekten daha önemli sorular vardır: Uçlar birbirini tanıyor mu, kullanıcı neye yetkili, veri güncel mi, değişiklik kayıt altına alınıyor mu?

Bu sayfa başlangıç çerçevesidir. Ayrıntılı okuma ve belge alıştırmaları:

- [Endüstriyel Protokol Seçim ve Karşılaştırma Rehberi](../07-protokoller/00-secim-ve-karsilastirma.md): Taşıma, port, latans ve kriptografi profilleri.
- [Modbus Güvenliği ve İstismar Önleme](../07-protokoller/01-modbus-guvenligi-ve-istismar.md): Function code, register manipülasyonu ve DPI kontrolleri.
- [OPC UA ve OPC Classic Güvenliği](../07-protokoller/05-opc-ua-ve-opc-classic.md): SecureChannel, sertifika yaşam döngüsü ve Part 18 RBAC.
- [Trafik Analizi ve Protokol Seçimi](../07-protokoller/08-trafik-analizi-ve-protokol-secimi.md): Çevrimdışı filtreler, sentetik normal trafik profili ve karar matrisi.

## Başlıca aileler

| Aile | Tipik işlev | Güvenlik değerlendirmesi |
|---|---|---|
| Modbus RTU / TCP | Ölçüm ve kontrol verisinin cihazlar arasında paylaşılması | Klasik kullanım ile Modbus Security desteğini ayır; ağda bulunmayı yetki sayma |
| OPC UA | Yapılandırılmış endüstriyel veri ve servisler | Güvenlik profili, uygulama sertifikası ve kullanıcı yetkisini ayrı doğrula |
| MQTT | Broker üzerinden yayımla–abone ol mesajlaşması | TLS, istemci kimliği ve konu bazlı yayın/abonelik izinlerini kontrol et |
| DNP3 | Uzak saha telemetrisi ve kontrolü | Güvenli kimlik doğrulama desteğini sürüm ve kurulum özelinde incele |
| IEC 60870-5-104 | Enerji sistemlerinde telekontrol | Profil, uç yetkisi ve korunan iletişim mimarisi tesis özelinde doğrulanır |
| IEC 61850 | Güç sistemleri için veri modelleri ve iletişim servisleri | Tek port veya tek paket türü değildir; servis ve kullanım profiliyle değerlendir |
| PROFINET / EtherNet/IP | Endüstriyel Ethernet üzerinde otomasyon | Gerçek zaman davranışı, cihaz profili, mühendislik ve veri trafiği ayrılır |
| Üreticiye özgü protokoller | Programlama, tanılama, cihaz yönetimi | Kamuya açık genel bilgi yetersizse üretici belgesi ve onaylı yapılandırma esas alınır |

Tablo bir tanıma haritasıdır. DNP3 ve enerji protokollerinin sektör bağlamı [elektrik bölümünde](../02-sektorler/02-elektrik-ve-enerji.md), bütün ailelerin teknik kaynakları [protokol seçim rehberinde](../07-protokoller/00-secim-ve-karsilastirma.md) yer alır. Doğrudan seri hat veya Ethernet L2 düzeyinde taşınan iletiler TCP/UDP portuyla tanımlanmaz; IEC 61850 ve PROFINET gibi aileler tek porta indirgenmez. Bir ürünün aileyi desteklemesi, güvenli profilin desteklendiği veya etkin olduğu iddiası değildir.

## Modbus: klasik protokol ile güvenli profil ayrımı

Modbus Organization, Modbus Security'yi TLS ve X.509 sertifikalarıyla geleneksel Modbus iletişimini koruyan bir protokol olarak tanımlar; bu profil için 802 portunu belirtir. Klasik Modbus TCP'nin varlığı, bu profilin desteklendiği veya kullanıldığı anlamına gelmez. [Modbus Security duyurusu](https://www.modbus.org/news/modbus-security-new-protocol-to-improve-control-system-security)

Özgün inceleme soruları: İki uçta hangi ürün/sürüm var? Profil değişikliği için sertifikalar nasıl dağıtılacak? Ağ geçidi güvenli iletişimi nerede sonlandırıyor? Kontrolöre kadar olan son bölüm nasıl korunuyor? Bağlantı başarısız olduğunda süreç ne yapıyor? Yanıt yoksa “şifreli” etiketiyle tüm yol güvenli kabul edilmez.

## OPC UA: özellik bulunması ile doğru kurulum farklıdır

OPC UA güvenlik modeli `None`, `Sign` ve `SignAndEncrypt` modlarını; uygulama kimlik doğrulamasını ve kullanıcı kimliğini ayrı ele alır. Güven listeleri ve sertifika doğrulaması uygulama güveninin parçasıdır. `None`, UA mesajlarının imzalanmasını veya şifrelenmesini sağlamaz. [OPC UA Part 2, bölüm 4](https://reference.opcfoundation.org/specs/OPC-10000-2/4)

Örnek kabul incelemesi: onaylanmayan istemci reddediliyor mu, gözlemci kullanıcı değişiklik yapamıyor mu, süresi dolan veya iptal edilen sertifikaya ilişkin davranış biliniyor mu? Bu denemeler üretimde doğaçlama uygulanmaz; ürünle uyumlu test ortamında ve tanımlanmış kabul planında yapılır. Sertifika yenileme süreci, gece vardiyasının bilmediği ani bir hizmet kesintisine dönüşmemelidir.

## MQTT: konu yetkisi ve mesajın anlamı

OASIS MQTT 5.0 standardı kimlik doğrulama, yetkilendirme ve güvenli iletişim seçeneklerini ele alır; konuya yayın ve konu filtresine abonelik yetkilerinin sınırlandırılmasını açıklar. MQTT kullanılması tek başına şifreleme garantisi değildir. [MQTT 5.0, bölüm 5](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)

Özgün değerlendirme: Telemetri yayımlayan bir istemcinin yönetim konusuna yayın yapabilmesi gerekiyor mu? Mesaj gecikmişse tüketici bunu anlayabiliyor mu? Broker kimliğine ek olarak mesajı üreten uç güvenilir mi? Eski bir mesajın yeni durum sanılmasını önleyen uygulama kuralı var mı? Yayın/abonelik yapısı veri akışını kolaylaştırır; süreç anlamını uygulama tasarımı belirler.

## Bir protokolü incelerken doldurulacak kart

1. İşlev, varlık sahibi, kaynak ve hedef.
2. Protokol ailesi, sürüm ve ürün desteği.
3. Oturumu başlatan uç ve gerekli dönüş trafiği.
4. Uygulama ve kullanıcı kimliği; okuma/değişiklik ayrımı.
5. Bütünlük, gizlilik, tazelik ve denetim izi.
6. Sertifika/anahtar ömrü ve yenileme sorumlusu.
7. Bağlantı kaybı, gecikme ve yeniden bağlanma davranışı.
8. Kabul kanıtı ve kalan belirsizlikler.

Port numaraları hedef keşfi için bir liste olarak kullanılmaz. Aynı portta farklı servis bulunabilir; şifreli tünel içinde görünmeyen OT akışları da olabilir. Envanter ve onaylı mimari, gözlenen trafiği yorumlamanın başlangıcıdır.

## Kaynaklar

- Modbus Organization, *Modbus Security: New Protocol to Improve Control System Security*, [duyuru](https://www.modbus.org/news/modbus-security-new-protocol-to-improve-control-system-security), 2018; profilin TLS/sertifika niteliği.
- OPC Foundation, *OPC UA Part 2: Security Model*, v1.05.06 görüntülenen sürüm, [bölüm 4](https://reference.opcfoundation.org/specs/OPC-10000-2/4); modlar ve güven yönetimi.
- OASIS, *MQTT Version 5.0*, 7 Mart 2019, [standart](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html); bölüm 5 güvenlik çerçevesi.

İlk kaynak incelemesi: 13.09.2026. Ayrıntılı protokol genişletmesi ve ek kaynak kontrolü: 16.09.2026; [araştırma kaydı](../../research/protokol-kaynaklar.md). Kabul kartları ve örnek sorular bu deponun özgün önerileridir.
