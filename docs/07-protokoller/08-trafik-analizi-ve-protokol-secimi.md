# Trafik Analizi ve Protokol Seçimi

[Ana sayfa](../../README.md) · [Seçim ve Karşılaştırma](00-secim-ve-karsilastirma.md) · [Modbus Güvenliği](01-modbus-guvenligi-ve-istismar.md) · [Siemens S7](02-siemens-s7-ve-s7comm-plus.md) · [EtherNet/IP](03-ethernet-ip-ve-cip-security.md)

Bu bölüm, mevcut bir endüstriyel trafik kaydından hangi sonuçların çıkarılabileceğini, Wireshark ile derin paket incelemesini (DPI) ve sentetik baseline analiz yöntemlerini gösterir.

---

## 1. Kaydı Yorumlama Yöntemi

Wireshark display filter, açılmış kayıtta hangi paketlerin görüntüleneceğini seçer; kaydı değiştirmez. Filtrede bir protokol adının kullanılması, o protokolün ayrıştırıcı tarafından tanınmasına bağlıdır.

Özgün inceleme sırası:
1. Kayıt kimliği, kaynak, zaman aralığı, saat dilimi ve temsil ettiği işletme durumunu yazın. Dosya verilmediyse "sentetik tablo incelemesi" diye belirtin.
2. Kapsamı kaydedin: gözlem noktası, atlanan trafik, şifreleme, kayıp/eksik kayıt bilgisi. Bilinmeyenleri sıfır kabul etmeyin.
3. Uçları envanterle eşleyin; isim/IP/MAC benzerliğini kimlik doğrulama yerine kullanmayın.
4. Protokolü, yönü, işlem sınıfını ve istek–yanıt ilişkisini birlikte değerlendirin.
5. Normal üretim, başlatma, durdurma, bakım ve yedek sisteme geçiş dönemlerini ayırın.
6. Sapmayı onay, rol, uygulama olayı ve süreç verisiyle karşılaştırın. Paket tek başına niyeti veya fiziksel sonucu kanıtlamaz.
7. Bulguyu "gözlendi / çıkarım / bilinmiyor" alanlarıyla raporlayın.

---

## 2. Çevrimdışı Display Filter Örnekleri

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

---

## 3. Normal Trafik Profili (Baseline)

Normal trafik profili (baseline), tek bir ortalama değer değil, **belirli bir işletme durumu için beklenen akış ve işlem kümesi** olarak tutulmalıdır.

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

### Sentetik Kayıt Özeti

Kurgusal su tesisi için SCADA-A yalnız FC03 ile PLC-B verisini okur. EWS-C, `D-17` onaylı değişiklik kapsamında 10:05–10:10 arasında FC16 kullanabilir. Uç-D envanterde yoktur.

| Kayıt | Zaman | Başlatan → hedef | İşlem / gözlem | Ek bağlam |
|---|---|---|---|---|
| K1 | 10:00:00 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K2 | 10:00:01 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K3 | 10:00:02 | SCADA-A → PLC-B | FC03 isteği, normal yanıt | Normal işletme |
| K4 | 10:06:00 | EWS-C → PLC-B | FC16 isteği, normal yanıt | D-17 kaydı var |
| K5 | 10:07:00 | Uç-D → PLC-B | FC03 isteği, yanıt özette yok | Envanter eşleşmesi yok |
| K6 | 10:12:00 | SCADA-A → PLC-B | FC16 isteği, exception yanıtı | SCADA-A için değişiklik yetkisi yok |

### Algılama ve Savunma Çıktısı

| Aday kural | Mantık, özgün öneri | Olumlu örnek | Olumsuz / bağlamlı örnek |
|---|---|---|---|
| Yeni iletişim ortağı | Başlatan uç ilgili akışın onaylı uç kümesinde yok | K5 | K1 |
| Yetki dışı işlem | İstek sınıfı ilgili rolün izinli işlem kümesinde yok | K6 | K4, D-17 ve rol kaydıyla birlikte |
| Açıklanamayan değişiklik | İşlem için gereken onay veya zaman kapsamı bulunamıyor | K6 için ayrıca incelenir | K4 |

---

## 4. Kaynaklar ve İlgili Dokümanlar

- [Master Protokol Seçim ve Karşılaştırma Rehberi](00-secim-ve-karsilastirma.md)
- [Modbus Güvenliği ve İstismar Önleme](01-modbus-guvenligi-ve-istismar.md)
- [Siemens S7 İletişimi ve S7comm-Plus](02-siemens-s7-ve-s7comm-plus.md)
- [EtherNet/IP ve CIP Security](03-ethernet-ip-ve-cip-security.md)
- [DNP3 ve IEC 60870-5-104 Güvenliği](04-dnp3-ve-iec-60870-5-104.md)
- [OPC UA ve OPC Classic Güvenliği](05-opc-ua-ve-opc-classic.md)
- [PROFINET, PROFIBUS ve IEC 61850](06-profinet-profibus-ve-iec-61850.md)
- [IEC 62351 Endüstriyel Kriptografi ve Güvenlik](07-iec-62351-kriptografi-ve-guvenlik.md)
- [OT Tehdit Avcılığı ve IDS Kuralları](../09-degerlendirme/05-ot-tehdit-avciligi-ve-ids-kurallari.md)
