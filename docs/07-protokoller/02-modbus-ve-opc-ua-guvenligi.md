# Modbus ve OPC UA güvenliği

Bu bölüm iki soruya odaklanır: “İleti ne istiyor?” ve “Bu uygulama/kullanıcı bunu yapmaya yetkili mi?” [Katalog](01-protokol-katalogu.md) protokol ailesini tanıtır; burada işlem, güvenlik katmanı ve kabul kanıtı incelenir. Örnekler kurgusaldır ve yalnız belge üzerinden değerlendirilir.

## Modbus işlemini doğru okumak

Modbus, istemcinin başlattığı istek ve sunucu yanıtı üzerinden çalışır. İşlem türü function code alanıyla belirtilir. Coils ve discrete inputs bit; holding/input registers 16 bit kelime tabanlı veri tablolarıdır. Register'ın proses karşılığı ve ölçeği cihazın veri haritasına bağlıdır. [Modbus Application Protocol V1.1b3, bölümler 4–6](https://www.modbus.org/file/secure/modbusprotocolspecification.pdf)

| Kod, ondalık / hexadecimal | İşlem | İnceleme anlamı |
|---|---|---|
| 1 / `0x01` | Read Coils | Bit okuma |
| 2 / `0x02` | Read Discrete Inputs | Girdi biti okuma |
| 3 / `0x03` | Read Holding Registers | Register okuma |
| 4 / `0x04` | Read Input Registers | Girdi register'ı okuma |
| 5 / `0x05` | Write Single Coil | Tek bit yazma isteği |
| 6 / `0x06` | Write Single Register | Tek register yazma isteği |
| 15 / `0x0F` | Write Multiple Coils | Birden çok bit yazma isteği |
| 16 / `0x10` | Write Multiple Registers | Birden çok register yazma isteği |
| 22 / `0x16` | Mask Write Register | Maske kullanarak değişiklik isteği |
| 23 / `0x17` | Read/Write Multiple Registers | Hem okuma hem yazma; yalnız okuma sayılmaz |

Tablo yaygın işlemlerin özetidir; tam kod listesi değildir. Tanılama ve üreticiye özgü işlemleri adı veya sayısından “zararsız” saymayın. Bir yazma isteğinin görülmesi, işlemin başarılı olduğunu veya fiziksel çıktının değiştiğini kanıtlamaz. Yanıt, uygulama kaydı ve süreç durumu ayrı kanıtlardır. Bu yorumlama ayrımı deponun özgün önerisidir.

### Güvenli profil ve ağ geçidi

Klasik Modbus TCP'de uygulama kimliği/şifreleme mekanizması yoktur. Modbus Security, Modbus'u TLS ile korur ve X.509 sertifikaları kullanır; TCP/802 profil için ayrılmıştır. TCP/502 gördüğünüz bir kayda yalnız ürünün başka bir arayüzünde TLS bulunduğu için “şifreli Modbus” yazmayın. [Modbus güvenlik açıklaması](https://www.modbus.org/modbus-specifications)

```text
Kurgusal tasarım:
Veri istemcisi == doğrulanmış güvenli profil ==> Geçit -- klasik seri hat --> PLC
                      güven sınırı 1                    güven sınırı 2
```

**Özgün mimari incelemesi:** İlk bağlantı korunurken ikinci bağlantı aynı korumayı taşımayabilir. Geçidin sertifikası PLC'nin kimliğini tek başına doğrulamaz. Kayıtta güvenli oturumun sonlandığı uç, seri cihaz eşlemesi, izinli istemci, izinli işlem ve kalan fiziksel erişim riski ayrı alanlar olmalıdır.

| Tasarım kararı | Kazanım | Sınır / maliyet kalemi |
|---|---|---|
| Desteklenen uçlarda Modbus Security | Uçlar arasında kriptografik koruma | Sertifika dağıtımı, yenileme, uyum ve arıza davranışı |
| Geçit veya korunan tünel | Eski cihazı değiştirmeden yolun bir kısmını koruma olanağı | Sonlandırmadan sonraki bölüm; geçit bakımı ve ek bağımlılık |
| Uç ve işlem izinlerini sınırlandırma | Gereksiz erişimin azaltılması | Cihazın veya ara kontrolün işlem ayrımını gerçekten desteklemesi |
| Pasif algılama ve kayıt eşleme | Beklenmeyen iletişimin incelenmesi | Görünürlük, şifreli içerik ve bakım bağlamı eksikleri |

Bu karşılaştırma özgün tasarım önerisidir; ürün özelliği veya fiyat iddiası değildir. Tünel, kullanıcının hangi register'a yazabileceğini kendi başına belirlemez.

### Algılama mantığı

Aşağıdaki mantık çalıştırılabilir IDS kuralı değildir; [algılama kartına](../../templates/03-algilama-karti.md) yazılacak özgün kontrol tasarımıdır.

| Gözlem | Gerekli ek bağlam | Aday bulgu | Yanlış sonuca yol açan durum |
|---|---|---|---|
| İzinli listede olmayan istemci | Varlık envanteri, geçit/NAT eşlemesi | Yeni Modbus istemcisi | Onaylı yedek sunucunun devreye girmesi |
| Okuma rolünden yazma işlemi | Rol ve işlem matrisi; isteğin yönü | Yetkiyle çelişen istek | Rol kaydının güncel olmaması |
| İzinli istemciden bakım dışında değişiklik | Onay kaydı ve zaman kalitesi | Değişiklik penceresi ihlali adayı | Saat farkı veya kaydı eksik acil bakım |
| Artan exception yanıtları | Toplam işlem sayısı ve eski normal dönem | İletişim/uyumluluk sorunu veya inceleme ihtiyacı | Başarısız saldırı olduğunun doğrudan varsayılması |

Exception oranını yalnız sayı olarak vermeyin: gözlem aralığı, toplam uygun istek/yanıt sayısı ve eşleştirilemeyen kayıtları belirtin. Oranın yükselmesi nedenin saldırı olduğunu göstermez.

## OPC UA güvenlik katmanları

OPC Classic COM/DCOM temeline dayanır. OPC UA farklı bir mimaridir; Classic'in işletim sistemi izinleri ile UA'nın uygulama sertifikaları aynı şey değildir. [OPC Classic açıklaması](https://opcfoundation.org/about/opc-technologies/opc-classic/)

OPC UA client/server modelinde **SecureChannel** uygulamalar arasındaki iletişimi korur; **Session** kullanıcı bağlamını taşır. Uygulama sertifikası ve kullanıcı kimliği ayrı doğrulanır. **SecurityPolicy** kriptografik algoritma/parametre seçimini, **MessageSecurityMode** korumanın uygulanma biçimini ifade eder. `None` mesaj koruması sağlamaz; `Sign` bütünlük için imzalama, `SignAndEncrypt` buna ek gizlilik sağlar. UA'nın her taşıma eşlemesini “TLS” diye adlandırmak doğru değildir. [OPC UA Part 2, bölüm 4](https://reference.opcfoundation.org/specs/OPC-10000-2/4)

```text
Kurgusal client/server incelemesi:
Uygulama sertifikası + güven listesi → uygulamaya güven
Kullanıcı kimliği → rol → servis/nesne izinleri
SecurityPolicy + MessageSecurityMode → mesajın korunması
Oturum ve denetim kaydı → işlemin izlenebilirliği
```

### Sertifika ve güven yaşam döngüsü

Bir sertifikanın mevcut olması güvenilir olduğu anlamına gelmez. OPC UA sertifika denetimleri biçim, imza zinciri, güven, geçerlilik ve ilgili kullanım kontrollerini içerir. Güven listesi yönetimi ile iptal bilgisi ayrıca ele alınır. [OPC UA Part 4, 6.1.3](https://reference.opcfoundation.org/specs/OPC-10000-4/6.1.3)

Self-signed sertifika, CA tarafından imzalanmış sertifika ve GDS ile yönetim farklı işletme modelleridir. Hangisinin kullanılacağına cihaz sayısı, destek ve yönetim süreciyle karar verilir; CA kullanmak hatalı güven listelerini kendiliğinden düzeltmez. [OPC UA Part 2, bölüm 9](https://reference.opcfoundation.org/specs/OPC-10000-2/9)

| Aşama | Özgün belge kontrolü | Beklenen kanıt |
|---|---|---|
| Kaydetme | Sertifika hangi uygulamaya ait; özel anahtarın sahibi kim? | Envanter, sorumlu ve uygulama kimliği |
| Güven kurma | Hangi sertifika/CA neden kabul ediliyor? | Onaylı TrustList ve dağıtım kaydı |
| İşletme | Geçerlilik, saat, hata ve iptal bilgisi nasıl izleniyor? | İzleme sahibi, olay örneği ve kayıt saklama kararı |
| Yenileme | Yeni sertifika karşı uçlara nasıl tanıtılacak? | Bağımlılık listesi, değişiklik penceresi, geri dönüş planı |
| Devreden çıkarma | Eski güven ve anahtar erişimi nasıl kaldırılacak? | İptal/kaldırma kaydı ve sahip onayı |

### Güvenli deployment kontrol listesi

Bu liste özgün kabul önerisidir; ürünün desteklediği özelliklerle doldurulur. OPC Foundation'ın timeout, anahtar koruması, denetim ve en az yetki konuları tasarım dayanağıdır. [OPC UA Part 2, bölüm 6](https://reference.opcfoundation.org/specs/OPC-10000-2/6)

- [ ] Ürün/firmware, UA profili, taşıma eşlemesi ve endpoint listesi belgeli.
- [ ] Üretim için seçilen güvenlik modu ve desteklenen güncel politika gerekçeli; korumasız erişim için varsa istisna sahibi ve kapsamı yazılı.
- [ ] Bilinmeyen sertifikaların otomatik kabul edilmediği yapılandırma incelemesiyle doğrulanmış.
- [ ] Sertifika zinciri, uygulama kimliği, süre ve iptal davranışı için kabul kanıtı var.
- [ ] Özel anahtar erişimi ve yedekleme sorumlusu belirli; anahtar belge deposuna konmamış.
- [ ] Anonim erişim kararı gerekçeli; gözlemci hesabının yazma/metot çağırma yetkisi ayrı değerlendirilmiş.
- [ ] Uygulama sertifikası güveni, kullanıcı rolü yerine kullanılmıyor.
- [ ] Sertifika yenileme, saat sapması ve bağlantı kaybı davranışı kayıtlı.
- [ ] Oturum, yetki reddi ve yapılandırma değişikliği için beklenen kayıt alanları belirli.
- [ ] Bağlantı/abonelik sınırları, bakım ve yedeklilik davranışı üretici gereksinimleriyle eşleşiyor.

Örnek belge matrisi:

| Rol | Okuma / abonelik | Değer değiştirme | Yönetim / güven listesi | Onay kanıtı |
|---|---|---|---|---|
| Gözlemci | Atanmış veriyle sınırlı | Ret | Ret | Rol incelemesi |
| Operatör | Görev kapsamı | Yalnız atanmış işletme işlemleri | Ret | İşletme yetkisi |
| Mühendis | Proje kapsamı | Onaylı değişiklik kapsamında | Ayrı yönetim rolü gerekir | Değişiklik kaydı |
| Sertifika yöneticisi | Görev gerektirmedikçe yok | Yok | Atanmış güven yönetimi | İki tarafın güncelleme kaydı |

Bu matris kurgusaldır; rol adlarının her UA sunucusunda hazır bulunduğu iddia edilmez.

## Tehdit ve savunma

| Hedef | Ön koşul | Aşılan güven sınırı | Olası hizmet/fiziksel etki | Gözlenebilir belirti | Karşılık gelen kontrol |
|---|---|---|---|---|---|
| Yetkisiz Modbus işlemi | Bir istemcinin sunucuya erişimi var | Bağlantı izni ile işlem izni | Kontrol verisinin değişmesi | Rol dışı function code; yanıt ve süreç farkı | Uç/işlem izinleri ve onay kaydı |
| Güvenilmeyen UA uygulamasının kabulü | Sertifika otomatik kabul ediliyor | Yeni uygulama ile güven listesi | Veriye veya servislere erişim | Yeni güven kaydı; beklenmeyen oturum | Yönetilen TrustList ve kabul gerekçesi |
| Geçerli kullanıcıyla fazla işlem | Rol gereğinden geniş | Kullanıcı kimliği ile nesne/servis yetkisi | Yetki dışı değişiklik | Başarılı ama rol matrisiyle çelişen işlem | Servis ve nesne düzeyinde en az yetki |
| Sertifika yenileme sonrası kesinti | Karşı uçlar yeni sertifikaya hazırlanmamış | Değişiklik ile işletme sürekliliği | Veri akışının kesilmesi | Güven/sertifika hataları | Önceden planlanan yenileme ve geri dönüş |

Tablo kurgusal, özgün tehdit modelidir. Son satır kötü niyet gerektirmeyen işletme riskini de gösterir.

## Belge alıştırması ve çözüm ölçütü

**Girdi:** A gözlemcisi PLC-B'ye yalnız FC03 gönderebilir. Kayıt özeti FC23 isteği ve exception yanıtı içerir. C UA istemcisinin sertifikası güvenilir; kullanıcısı `Gözlemci`dir. UA incelemesinde `SignAndEncrypt`, “sertifikaları otomatik kabul et” ve gözlemci için yazma yetkisi aynı anda işaretlenmiştir. Bunlar sentetik belge girdileridir; cihaz veya paket kaydı verilmemiştir.

| Aşama | Görev / çıktı |
|---|---|
| THEORY | FC03/FC23, SecureChannel/Session ve kimlik/yetki ayrımlarını altı cümleyle açıklayın |
| LAB | Girdileri iki akış ve bir UA rol matrisine dönüştürün |
| TEST | Her çelişkiyi bulgu, kanıt, bilinmeyen sonuç ve ek kanıt sütunlarıyla yazın |
| DEFENSE | Modbus işlem kısıtı, TrustList yönetimi ve UA rol daraltması önerin |
| REPORT | Bir sayfada üç bulgu, öncelik gerekçesi ve kabul ölçütü sunun |

**Beklenen sonuç:** FC23 okuma sınırını ihlal eden istektir; exception yanıtı fiziksel değişiklik kanıtı değildir. Şifreleme, otomatik sertifika kabulünü veya fazla yetkiyi düzeltmez. Düzeltmenin kabulü için rol matrisi, güven listesi ve ilgili kayıtların tutarlılığı gösterilmelidir. Her doğru ayrım bir puandır: işlem sınıfı, sonuç belirsizliği, uygulama güveni, kullanıcı yetkisi ve doğrulama kanıtı; toplam beş puan. Kritik bir ayrım eksikse rapor düzeltilir.

## Kaynaklar ve kapsam

Modbus V1.1b3: 26.04.2012; OPC UA Part 2: görüntülenen v1.05.06; diğer kaynakların ayrıntıları [araştırma kaydında](../../research/protokol-kaynaklar.md). Erişim: 16.09.2026. Şemalar, kontrol listeleri, algılama mantığı ve alıştırmalar bu deponun özgün önerisidir. Komut, payload, canlı bağlantı veya PLC yazma prosedürü içermez.
