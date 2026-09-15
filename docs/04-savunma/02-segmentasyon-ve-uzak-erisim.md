# Segmentasyon, kimlik ve uzak erişim

Savunma mimarisinin hedefi, gerekli işin tanımlı bir yoldan, doğru kimlikle, uygun süre ve yetkiyle yapılmasıdır. Her yeni geçiş için iş gerekçesi ve hata davranışı bilinmelidir. Buradaki kontrol tasarımları özgün uygulama önerileridir; sahaya göre uyarlanır.

## Erişim yolunu uçtan uca kurmak

Bir bakım oturumu için kullanıcı → kimlik doğrulama → onay → erişim aracısı → hedef sistemi şeklinde bir yol tanımlanabilir. Kimlik sağlayıcısındaki başarılı giriş, hedefteki işlemin yetkili olduğunu tek başına kanıtlamaz. Onaylanan kişi, hedef, süre ve işin hedef kaydıyla eşleşmesi gerekir.

| Kontrol | Beklenen davranış | Kabul kanıtı |
|---|---|---|
| Kişiye özel hesap | Paylaşılan hesap yerine izlenebilir kullanıcı | Oturumla kişi ve iş emri ilişkilendirilebilir |
| Çok faktörlü doğrulama | Uygun erişim kapısında ek kimlik doğrulama | Normal ve başarısız giriş davranışı kayıtlı |
| En az yetki | Yalnız gereken hedef ve işlem | Gözlem rolü ile değişiklik rolü ayrı |
| Süreli erişim | Bakım bittiğinde yetki sona erer | Süre bitimi ve iptal sonrası oturum durumu doğrulanmış |
| Hedef sınırlaması | Onaylanan sistemlerle sınırlı geçiş | İzinli akış çalışır; kapsam dışı akış kontrollü kabul testinde reddedilir |
| Oturum kaydı | Kim, ne zaman, hangi hedefe? | Merkezi ve hedef kayıtları tutarlı |
| Dosya aktarımı | Gerekçeli, bütünlük kontrollü aktarım | Dosya kimliği, kaynak ve onay kaydı var |
| Acil erişim | Kayıtlı ve incelenebilir istisna | Kullanımdan sonra yetki ve kimlik bilgileri gözden geçirilir |

Eski cihaz çok faktörlü doğrulamayı desteklemiyorsa güvenlik gereği ortadan kalkmaz. Kapı ve yönetim istasyonu gibi destekleyen sınırlar değerlendirilir; geride kalan cihaz yetkisi ve fiziksel erişim ayrıca korunur. Bu telafi yaklaşımı cihazın kendisinin aynı güvenceyi verdiği iddiası değildir.

## Segmentasyon nasıl doğrulanır?

Önce [akış matrisi](../../templates/01-envanter-ve-akis.md) hazırlanır. Her akış için şablondaki adlarıyla sahibi, işlev, başlatan uç, çalışma saatleri, protokol ailesi ve kayıt noktası yazılır. Kurallar değişiklik sürecinde uygulanır; test planı hem gerekli iletişimin sürdüğünü hem gereksiz geçişin engellendiğini göstermelidir. Kontrol ağı üzerinde rastgele tarama, bunun yerine geçen bir kabul yöntemi değildir.

Tek yönlü aktarım, uygun kullanımda veri çıkışını sınırlamaya yardım edebilir; dosya aktarımı, bakım ve geri dönüş ihtiyaçları nedeniyle her akış için uygun değildir. Güvenlik duvarı, veri diyodu veya ayrı kablo tek başına süreç güvenliğini ispatlamaz. Kimlik, veri anlamı ve işletme bağımlılıkları da değerlendirilir.

## İnternet görünürlüğü ve tedarikçi bağımlılığı

CISA'nın Haziran 2025 rehberi, yanlış yapılandırılmış ve güncel olmayan internet erişimli OT/ICS ve uzak erişim varlıklarının görünürlüğünün azaltılmasını ele alır. [Internet Exposure Reduction Guidance](https://www.cisa.gov/resources-tools/resources/exposure-reduction)

Bu depo için önerilen uygulama: Kurumun kendi kayıtlı dış erişimlerini ağ ekibi ve hizmet sağlayıcıyla uzlaştırın. Her bağlantının sahibi, iş gerekçesi, kimlik yöntemi, hedef kapsamı ve kapatma koşulu olsun. Kamuya açık üçüncü taraf cihaz araması bu çalışma kapsamına dahil değildir.

Tedarikçi portalı çalışmıyorsa acil bakım nasıl yapılacak? Merkezi kimlik altyapısı kullanılamıyorsa kontrollü yerel erişim nasıl sağlanacak? Kayıt toplama kesilirse bakım tamamen duracak mı, alternatif kanıt nasıl tutulacak? Bu kararlar olay anında doğaçlama verilmemelidir.

## Kontrol listesi

Bir maddenin işaretlenmesi, yalnızca yanına yazılan kanıt ve doğrulama tarihiyle anlam taşır; kanıtı olmayan madde açık kabul edilir.

- [ ] Doğrudan ve dolaylı dış bağlantılar birlikte biliniyor.
- [ ] Her bakım erişimi kişi, iş ve hedef ile eşleşiyor.
- [ ] Geçici yetkinin sona ermesi doğrulanıyor.
- [ ] Erişim kapısının arızası ve kurtarılması planlı.
- [ ] Günlük erişimi ve kişisel veri saklama süreleri yetkili süreçte belirlenmiş.

## Kaynak

- CISA, *Internet Exposure Reduction Guidance*, 4 Haziran 2025, [yayın](https://www.cisa.gov/resources-tools/resources/exposure-reduction), erişim: 13.09.2026. İnternet görünürlüğü bağlamını destekler. Kontrol kartları ve kabul önerileri özgün sentezdir.
