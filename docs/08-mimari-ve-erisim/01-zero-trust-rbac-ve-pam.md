# OT'de Zero Trust, RBAC ve ayrıcalıklı erişim

[Ana sayfa](../../README.md) · [Mimari ve güven bölgeleri](../01-temeller/03-mimari-ve-guven-bolgeleri.md) · [Firewall, DMZ ve uzak erişim](02-firewall-dmz-ve-uzak-erisim.md) · [Araştırma kaydı](../../research/mimari-erisim-kaynaklar.md)

Bir bakım kullanıcısının ağa girebilmesi, PLC programını değiştirmeye yetkili olduğu anlamına gelmez. Kimlik doğrulama, bir kişinin veya cihazın kimliğini sınar; yetkilendirme, belirli bir kaynak üzerinde hangi işlemi yapabileceğini belirler. OT tasarımında bu kararın kontrol döngüsüne ve arıza sırasında işletmeye etkisi de incelenir. NIST, Zero Trust uygulamalarında eski OT bileşenlerinin uyumsuzluğunu, ek gecikmeyi ve erişim bileşenlerinin kullanılamamasını özellikle ele alır. [NIST SP 800-82r3, §5.2.3.4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

Bu bölüm, 50 konulu kapsamın **4 — Zero Trust OT, 5 — RBAC ve 6 — PAM** başlıklarını birlikte işler. Tablolar ve belge alıştırması kurgusal bir su işletmesi için **bu deponun özgün eğitim sentezidir**; ürün ayarı veya canlı sistem talimatı değildir.

## Zero Trust hangi soruyu değiştirir?

Zero Trust, ağ konumundan veya cihazın kurum mülkiyetinde olmasından hareketle örtük güven verilmemesini esas alır. Kaynak erişiminde kullanıcı ve cihaz kimliği ile yetki değerlendirilir; tek bir ürün satın almak bu mimariyi kurmuş olmak anlamına gelmez. [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)

OT'ye uyarlarken aşağıdaki tasarım kararları birlikte verilir:

| İlke | Kurgusal OT karşılığı | İncelenecek kanıt | Sınır / işletme etkisi |
|---|---|---|---|
| Kullanıcı kimliği | Her bakım oturumu tek kişiye ve iş emrine bağlanır | Kullanıcı–oturum–iş emri eşlemesi | Hedef ortak hesap kullanıyorsa aracı kaydı gerekir; hedefte kişi bazında kimlik oluşmuş sayılmaz |
| Cihaz kimliği | Bakım bilgisayarı yönetilen cihaz kaydına, destekliyorsa sertifikaya bağlanır | Envanter, sertifika sahibi ve iptal kaydı | IP/MAC eşleşmesi tek başına güçlü kimlik doğrulama değildir |
| En az yetki | Operatörün proses kullanım yetkisi mühendislik değişikliği yetkisinden ayrılır | Rol ve işlem matrisi | Ekranın gizlenmesi arka uç yetkilendirmesinin kanıtı değildir |
| Bölgelere ayırma | Kullanıcı erişimi, mühendislik ve saha kontrol yolları ayrı sınırlanır | Bölge/akış matrisi ve kural incelemesi | VLAN etiketi tek başına geçiş denetimi sağlamaz |
| Mikrosegmentasyon | Uygun sunucular arasında ihtiyaç duyulan uygulama akışları sınırlandırılır | Sunucu çiftleri ve izinli hizmet listesi | Her PLC'ye ajan kurulabileceği veya her akışın araya cihaz eklenmesini kaldıracağı varsayılmaz |
| Sürekli değerlendirme | Yetki süresi, cihaz durumu ve kayıt toplayıcı sağlığı izlenir | Süresi dolmuş yetki ve eksik kayıt bildirimi | Şüpheli oturumun kesilmesi ile çalışan kontrol döngüsünün kesilmesi aynı karar değildir |

Bu uyarlama, kontrol döngüsünün her çevriminde uzak kimlik sunucusundan onay beklemesini önermez. Mühendislik ve uzaktan bakım erişimi için uygulanan kontrol ile PLC'nin yerel proses davranışı ayrı tasarlanır. Uygun kontrol noktaları ve gecikme/bağımlılık incelemesi için [NIST'in OT Zero Trust değerlendirmesi](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) esas alınır; tabloda seçilen uygulamalar özgün öneridir.

## RBAC ve ABAC

**RBAC**, kaynak üzerindeki işlem izinlerini rollerle ilişkilendirir; kullanıcı bu rollere atanır. **ABAC**, özne, kaynak, işlem ve ortamın niteliklerini bir politikayla değerlendirir. Örneğin mühendis rolü, yalnız kendisine atanmış PLC üzerinde ve onaylı bakım penceresinde değişiklik yapabilir. Son iki koşul rol adından daha fazla bağlam gerektirir. [NIST RBAC sözlüğü](https://csrc.nist.gov/glossary/term/role_based_access_control), [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)

| Yaklaşım | Sorduğu soru | Avantaj | Sınırlama |
|---|---|---|---|
| RBAC | Kullanıcı hangi görevi üstleniyor, bu görevin işlem izinleri neler? | Görev değişikliği ve yetki incelemesi anlaşılır olur | Çok sayıda saha/iş türü için kontrolsüz rol çoğalması oluşabilir |
| ABAC | Rolün yanında hedef, zaman, iş emri ve cihaz koşulları uygun mu? | Geçici erişimi daha ayrıntılı sınırlar | Yanlış veya eski nitelik yanlış izin/ret üretir; veri sahipliği gerekir |
| Birlikte kullanım | Rol izin veriyor mu ve ek koşullar sağlanıyor mu? | Kalıcı görev ile geçici bağlamı ayırır | Uygulama, aracı ve hedefteki kararların tutarlı olması gerekir |

### Sekiz rol için örnek matris

Hücreler yalnız belirtilen işlemleri kapsar. **Yok**, bu senaryoda izin verilmediğini; **onaylı**, ayrı değişiklik kaydı ve işletme onayı gerektiğini belirtir. Görüntüleme izni ham veritabanı erişimi veya yapılandırma okuma izni değildir. Bir kişinin birden çok rolü varsa birleşen yetkiler ayrıca incelenir.

| Rol | HMI / SCADA | EWS ve PLC | Historian | Windows, firewall, switch | SIEM / IDS | Erişim onayı ve sınır |
|---|---|---|---|---|---|---|
| Operator | Atanmış ünitenin proses ekranını kullanır, alarmı prosedüre göre kabul eder | Doğrudan mühendislik erişimi yok | Kendi ünitesinin trendini okur | Yok | Yok | Vardiya ve ünite kapsamı; program/firmware değişikliği yok |
| Engineer | Onaylı ekran ve alarm yapılandırması | EWS'de proje hazırlar; atanmış PLC'de onaylı değişikliği uygular | Teknik trend okur | Gerekli proje paylaşımını kullanır; altyapı yönetmez | İlgili teknik olayları okur | Kendi talebini tek başına onaylamaz |
| Maintenance | Atanmış ekipmanın tanı ekranını okur | İş emri kapsamındaki tanı belgelerini kullanır; program aktarımı yok | Bakım trendini okur | Genel yönetim yok | Yok | Fiziksel bakım yetkisi siber yönetim yetkisi sayılmaz |
| Supervisor | İşletme görünümünü okur; yetkili işletme kararını kaydeder | Değişiklik gerekçesini değerlendirir; programı aktarmaz | İşletme raporu okur | Yok | Kendisine sunulan olay özetini okur | İşletme onayı verir; teknik uygunluk ayrıca doğrulanır |
| Administrator | Sunucu hizmetlerini onaylı bakımda yönetir; proses komutu vermez | EWS işletim sistemini yönetir; PLC proje yetkisi yok | Sunucu/hesap yönetimi; veri değişikliği ayrı yetki | Atanmış altyapıyı değişiklik kaydıyla yönetir | Platform işletimini yapar; kanıt silme yetkisi verilmez | Hesap açma ile erişim onayı farklı rollerce yürütülür |
| Vendor | Yalnız iş emrindeki hedefe geçici tanı erişimi | Aracı üzerinden belirli EWS; PLC değişikliği ayrı mühendislik yetkisi ve onay ister | Gerekçeli tanı verisiyle sınırlı | Genel yönetim yok | Yok | Kişisel kimlik, MFA, süre, hedef, refakat ve kapanış kaydı |
| Security Analyst | Güvenlik kayıtlarını okur; proses kullanımı yok | Proje değişiklik kayıtlarını okur; program aktarmaz | Olayla ilgili, yetkili veri kopyasını inceler | Kayıt ve yapılandırma kopyasını okur | Alarm inceler; kural değişikliği ayrı onaylı süreç | Alarm üzerine PLC kapatma yetkisi verilmez |
| Read-only Auditor | Onaylı ekran/ayar kanıt paketini okur | Proje ve yetki inceleme kanıtını okur | Onaylı rapor kopyasını okur | Onaylı kural/yapılandırma kanıtını okur | Sınırlandırılmış raporları okur | Canlı yönetim oturumu yerine süreli, salt okunur kanıt paketi |

Bu tablo üreticinin yerleşik rol adlarını temsil etmez. Bir uygulamada "administrator" hesabının geniş teknik yetkileri bulunabilir; tabloda belirtilen görev ayrımı o üründe uygulanamıyorsa bu açık yazılır ve aracı, çift onay, kayıt veya ayrı hesapla telafi edilir. [NIST SP 800-82r3, §6.2.1 ve Ek F, AC-6](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

## Endüstriyel platformlarda RBAC uygulamaları

OT sistemlerinde RBAC yalnızca dosya veya menü gizleme değildir; doğrudan kontrolör komutlarına, I/O zorlamaya (force), firmware yüklemeye ve emniyet parametrelerine bağlanır.

| Platform / Standart | RBAC Mekanizması | Kimlik Doğrulama Kaynağı | Tanımlanan Temel İzin ve Roller | Emniyet ve Kritik İşlem Denetimi |
|---|---|---|---|---|
| **Siemens SIMATIC (UMAC & UMC)** | Proje bazlı UMAC ve merkezi SIMATIC UMC bileşeni | Yerel veritabanı veya Active Directory / LDAP (SADS) | *Engineering, Safety Program, Hardware Config, HMI Download, Diagnostics* | S7-1500 (FW 4.0+) CPU seviyesinde merkezi oturum açma (`Logon of Central Users`) ve yerel rol eşleme |
| **Rockwell Automation (FTSEC)** | FactoryTalk Security (Action-Based Security) | Windows Active Directory veya FactoryTalk Local Directory | *Tag Write, Online Edit, Firmware Flash, Logic Download, Recipe Management* | *Safety Engineer* rolü zorunluluğu; Deny-over-Allow önceliği ve AssetCentre audit entegrasyonu |
| **Schneider Electric (CAE & Control Expert)** | Cybersecurity Admin Expert & Security Editor | Merkezi LDAP/AD veya yerel şifreli profil | *Full Control, Program Modification, Data Modification, Monitoring* | Modicon M580/M340 PACSec ve EIFE modüllerine merkezi güvenlik profili dağıtımı |
| **ABB (System 800xA)** | Aspect Directory Security & Role Definitions | Windows Domain Kullanıcı ve Güvenlik Grupları | *Operator, Senior Operator, Application Engineer, System Engineer* | Proses Alanı (Area/Unit) ve Tesis Hiyerarşisi (Plant Structure) bazında kumanda sınırlandırması |
| **Emerson (DeltaV)** | Workstation/Area Security Administration | Windows Active Directory & DeltaV User Accounts | *Can Operate, Can Tune, Can Configure, Can Download, Master Security* | 21 CFR Part 11 uyumlu elektronik imza ve kritik setpoint değişikliklerinde çift onay (Four-Eyes) |
| **OPC UA (Part 18 - Role-Based Security)** | Adres Uzayı (AddressSpace) NodeId RolePermissions | X.509 İstemci Sertifikası, Kullanıcı Adı/Parola veya JWT Token | *Anonymous, AuthenticatedUser, Observer, Operator, Engineer, Supervisor, ConfigureAdmin* | Her NodeId için bit maskesiyle denetlenen `Read`, `Write`, `Browse`, `Call`, `WriteRolePermissions` hakları |

## PAM ayrıcalığı nasıl yönetir?

PAM, ayrıcalıklı hesapların, kimlik sırlarının ve yönetim oturumlarının yaşam döngüsünü yönetmek için kullanılan süreç ve yetenekler bütünüdür. Aşağıdaki tasarım ayrımı özgün eğitim sentezidir; bir ürünün tüm yetenekleri içerdiği varsayılmaz.

| Yetenek | Çözdüğü problem | OT için sorulacak soru |
|---|---|---|
| Credential vault — kimlik bilgisi kasası | Parola/anahtarların denetimsiz paylaşılması | Kasaya erişilemiyorsa yetkili acil bakım nasıl yürür; yedek sır kaydı nerede tutulur? |
| JIT — gerektiği süre için yetki | Bakım bitince açık kalan kalıcı ayrıcalık | Bitiş saati yalnız yeni oturumu mu engeller, açık oturuma ne olur; işletme bunu nasıl onaylar? |
| Session recording — oturum kaydı | Hangi kişinin ne yaptığının izlenememesi | Kayıt hedef oturumuyla eşleşiyor mu; kayıt arızası nasıl görülür; kim kaydı okuyabilir? |
| Hesap yaşam döngüsü | İşten ayrılan veya sözleşmesi biten kişinin erişimi | Dizin, aracı ve hedef yerel hesapta iptal tamamlandı mı? |
| Sır yenileme | Aynı parolanın uzun süre çok kişide kalması | Parolayı kullanan servis veya eski uygulama kesilir mi; değişiklik ve geri dönüş kanıtı var mı? |

Paylaşılan hedef hesap tamamen kaldırılamıyorsa her kullanıcı aracıda ayrı kimlikle doğrulanır ve hedef oturumuna bağlanır. Bu telafi, hedefin doğrudan veya yerel erişim yolları açıkken yeterli değildir. Oturum videosu da tek başına bütün işlemlerin veya proses etkisinin kanıtı sayılmaz; hedef kayıtları, proje sürümü ve iş emriyle ilişkilendirilir. Uzak erişimin gerekçeli, sınırlı, izlenen ve ihtiyaç sonunda kaldırılan olması için [NIST §6.2.10](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) dayanak alınır.

Örnek iş akışı:

```mermaid
flowchart LR
    T["İş emri: kişi, hedef, işlem, süre"] --> O["İşletme ve teknik onay"]
    O --> K["Kimlik ve cihaz doğrulama"]
    K --> Y["Geçici yetki ve aracı oturum"]
    Y --> H["Onaylı hedefte çalışma"]
    H --> D["Değişiklik ve hedef kayıtlarıyla doğrulama"]
    D --> I["Yetki iptali ve kapanış kanıtı"]
```

## Dizin veya PAM hizmeti kesilirse

Active Directory (AD) bir dizin hizmetidir; AD kullanılması tek başına PAM veya güvenli OT erişimi sağlamaz. Aşağıdaki kesinti davranışları bu kurgusal tasarımın açık kararlarıdır; Windows sürümleri ve uygulamalar için varsayılan davranış iddiası değildir.

| Durum | Tasarımda önceden kararlaştırılan davranış | Belgeyle doğrulama |
|---|---|---|
| Yeni vendor oturumu sırasında dizin/MFA yok | Yeni uzak ayrıcalık verilmez; yetkili yerel bakım süreci değerlendirilir | Ret nedeni, bildirim sahibi, acil bakım planı |
| Çalışan operatör oturumunda dizin yok | İşletme sürekliliği ve ekran kullanımı için uygulamaya özgü davranış tanımlanır | Kabul ortamının kesinti raporu; oturum ve alarm görünürlüğü |
| Kasa erişilemiyor | Önceden onaylı, sınırlı acil hesap süreci; kullanım sonrasında inceleme | Erişimi veren ve kullanan roller, saklama, yenileme ve kayıt planı |
| Saat kaynağı bozuluyor | Sertifika/kimlik doğrulama ve kayıt sırası etkileri incelenir | Saat sapması, kaynağın durumu, olay çizelgesindeki belirsizlik |
| Oturum kaydı kesiliyor | Yeni oturum ve mevcut bakım için ayrı karar; kritik işlem yarıda bırakılmaz | İşletme sorumlusu, durdurma/bitirme koşulu ve alternatif kanıt |

Merkezi hizmet kaybında bütün ağı açmak da bütün OT işlevlerini otomatik durdurmak da bu tablonun yerine geçmez. İşletme, kimlik hizmeti ve zaman bağımlılıkları birlikte değerlendirilir. [NIST SP 800-82r3, §5.2.3.4 ve §6.2.12](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

## Artılar, sınırlamalar ve maliyet

Rol ve süre kısıtları erişim incelemesini kolaylaştırır; oturum–iş emri bağlantısı belirsizliği azaltır. Buna karşılık kimlik altyapısı, sertifika yenilemesi, istisna yönetimi ve acil bakım süreçleri yeni işletme yükü getirir. Maliyet hesabına yalnız lisans değil; hesap temizliği, entegrasyon, yedeklilik, kayıt saklama ve görev ayrımını sürdürecek personel zamanı eklenir.

Ürün bağımsız rol matrisi, süreli erişim kaydı ve hesap incelemesi lisans almadan başlatılabilecek belge çalışmalarıdır. Açık kaynak bir kimlik sağlayıcı veya erişim aracısı değerlendirilse bile eski protokol uyumu, sır yenileme ve kayıt kapsamı ayrıca kanıtlanır. Bu bölüm ticari PAM ile açık kaynak bileşenleri eşdeğer saymaz ve fiyat tahmini vermez. [Tedarikçi ve uzak erişim şablonu](../../templates/06-tedarikci-ve-uzak-erisim.md) seçim için gereksinimleri toplamaya yardımcı olur.

## Belge alıştırması ve kabul ölçütü

**Kurgusal girdi:** Vendor bakım kaydında yalnız "PLC bakımı" yazıyor; bitiş saati yok. Hedefte paylaşılan hesap var. AD bağlantısı kesildiğinde yerel operatör ekranının davranışı belgelenmemiş. Aracı oturum kaydı tutuluyor, hedef hesapla eşleşme bilgisi yok.

| Aşama | Teslim | Kabul ölçütü |
|---|---|---|
| THEORY | Kimlik doğrulama, RBAC, ABAC ve PAM farkını bu örnekle açıkla | Ağ erişimi ile PLC işlem yetkisi ayrı açıklanmış |
| LAB | Yukarıdaki sekiz rol için hedef/işlem/süre kaydı oluştur | Vendor yetkisi belirli hedef ve iş emrine bağlanmış; kendi onayını veren rol yok |
| TEST | Üç belge kontrolü tasarla: geçerli iş, süresi dolmuş iş, dizin kesintisi | Her kontrolde beklenen izin/ret veya işletme kararı ve gereken kanıt yazılmış |
| DEFENSE | Eksikler için erişim ve telafi kontrollerini seç | Paylaşılan hesabın kalan sınırı ve kayıt arızası ele alınmış |
| REPORT | Bir sayfalık bulgu ve düzeltme kaydı hazırla | Her bulgunun sahibi, kabul kanıtı ve kalan belirsizliği var |

Alıştırmada sisteme bağlanılmaz. Kanıt sunulmadan "çalışıyor" veya "geçti" yazılmaz; tasarlanan test ile yürütülmüş test ayrılır. Portföyde "OT erişim tasarımı ve belge incelemesi" olarak gösterilebilir; canlı tesis deneyimi diye sunulmaz. İleri çalışma: görev ayrımı çatışmaları, sertifika yaşam döngüsü, servis kimlikleri ve kimlik hizmeti kesintisinin tatbikatı.

## Kaynaklar ve kapsam

- NIST, *SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security*, Eylül 2023, [nihai metin](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf), erişim: 16.09.2026; §5.2.3.4, §6.2.1, §6.2.10, §6.2.12 ve Ek F/AC-6.
- NIST, *SP 800-207: Zero Trust Architecture*, Ağustos 2020, [yayın kaydı](https://csrc.nist.gov/pubs/sp/800/207/final), erişim: 16.09.2026; Zero Trust tanımı ve kaynak merkezli erişim yaklaşımı.
- NIST, *Role-based access control (RBAC)*, [sözlük](https://csrc.nist.gov/glossary/term/role_based_access_control), sayfada yayın tarihi belirtilmiyor, erişim: 16.09.2026; rol–işlem izinleri ayrımı.
- NIST, *SP 800-162: Guide to Attribute Based Access Control Definition and Considerations*, Ocak 2014; 02.08.2019 güncellemelerini içeren kayıt, [yayın kaydı](https://csrc.nist.gov/pubs/sp/800/162/upd2/final), erişim: 16.09.2026; ABAC tanımı.

Matrisler, kesinti kararları, maliyet değerlendirmesi ve alıştırma özgün eğitim sentezidir. Kapsam ve kullanılmayan iddialar [araştırma kaydındadır](../../research/mimari-erisim-kaynaklar.md).
