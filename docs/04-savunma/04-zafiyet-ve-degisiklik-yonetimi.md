# Zafiyet ve değişiklik yönetimi

Zafiyet yönetiminin çıktısı yalnızca bir CVE listesi değil, belirli bir varlık için gerekçeli işlem kararıdır. Doğru ürünü ve sürümü eşleştirmek, erişim koşullarını anlamak ve uygulanacak değişikliğin süreç etkisini değerlendirmek gerekir.

## Bir duyurudan iş kaydına

1. Üreticinin duyurusundaki model, donanım ve firmware koşullarını envanterle karşılaştırın.
2. Etkilenen işlevin gerçekten etkin olup olmadığını onaylı yapılandırmadan doğrulayın.
3. Mevcut erişim yolları ve telafi kontrollerini kaydedin.
4. Hizmet, emniyet ve kurtarma etkisini süreç sahibiyle değerlendirin.
5. Yama, yapılandırma değişikliği, erişim azaltma veya ürün yenileme kararını gerekçesiyle kaydedin.
6. Geçici önlemin sahibi, bitiş tarihi ve doğrulama kanıtını belirleyin.

CISA KEV kataloğu, gerçek dünyada istismar edildiği bilinen zafiyetleri izlemek için bir başvuru kaynağıdır. Katalogda bulunmamak güvenli olmanın kanıtı değildir. ABD federal kurumlarına yönelik süreler Türkiye'deki her işletme için kendiliğinden yükümlülük oluşturmaz. [CISA KEV kataloğu](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Yama öncesi kabul planı

| Kontrol kapısı | Tamamlanma kanıtı |
|---|---|
| Uygunluk | Ürün/sürüm eşleşmesi ve üretici desteği |
| Yedek | Proje, yapılandırma ve bağımlılıkların geri yüklenebilir kopyası |
| Test | Temsil kabiliyeti bilinen ortamda işlev ve haberleşme incelemesi |
| İşletme | Bakım zamanı, görevli roller ve geçici çalışma koşulları |
| Geri alma | Başarısızlık ölçütü, yetki, eski sürüm ve gerekli araçlar |
| Gözlem | Değişiklik sonrası izlenecek süreç ve güvenlik belirtileri |
| Kapanış | Sürüm, envanter, yedek ve belgelerin birlikte güncellenmesi |

Tablo özgün uygulama şablonudur. Test ortamının üretimi temsil etmediği noktalar açık bırakılır. Örneğin gerçek saha haberleşmesi veya yedeklilik davranışı denenmediyse “test geçti” ifadesi bunları kapsamamalıdır.

## Tedarikte sorulacak sorular

CISA ve ortaklarının Ocak 2025 *Secure by Demand* rehberi, OT ürünleri satın alınırken güvenli tasarım özelliklerinin talep edilmesini ele alır. [Resmi ortak rehber](https://www.cisa.gov/sites/default/files/2025-01/joint-guide-secure-by-demand-priority-considerations-for-ot-owners-and-operators-508c.pdf)

Bu depo için özgün satın alma soru listesi:

- Destek süresi ve güvenlik güncellemesi teslim koşulu yazılı mı?
- Kişiye özel yetki, günlük dışa aktarımı ve güvenli erişim hangi model/lisans kapsamında?
- Güncelleme bütünlüğü nasıl doğrulanır; başarısız olursa hangi geri dönüş desteklenir?
- Yazılım bileşen bilgisi, zafiyet bildirim kanalı ve etkilenen sürüm açıklaması sağlanıyor mu?
- Varsayılan hesapların ve gereksiz servislerin yönetimi açıklanmış mı?
- İnternet veya tedarikçi portalı kullanılamadığında bakım/kurtarma nasıl yürür?
- Sertifika, lisans ve mühendislik araçlarının yaşam döngüsü kime bağlı?

## Acil zafiyet baskısı

“Hemen yama” ile “hiç dokunma” arasında seçenekler bulunabilir: gereksiz dış erişimi azaltmak, yönetim yolunu daraltmak, kişiye özel ve süreli erişim uygulamak, daha sık kayıt incelemek veya yenileme planını hızlandırmak. Her seçeneğin etkinliği ve yan etkisi ayrıca doğrulanır. Geçici kontroller kalıcı bakım borcunu görünmez yapmamalıdır.

## Kaynaklar

- CISA, *Known Exploited Vulnerabilities Catalog*, [dinamik katalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), erişim denemesi: 13.09.2026. Doğrudan sayfa erişimi 403 verdi; genel katalog işlevi CISA'nın [BOD 22-01 açıklamasından](https://www.cisa.gov/sites/default/files/publications/Reducing_the_Significant_Risk_of_Known_Exploited_Vulnerabilities_20211103.pdf) doğrulandı. Bu depoda güncel CVE listesi veya son tarihler yeniden üretilmez.
- CISA ve ortaklar, *Secure by Demand: Priority Considerations for OT Owners and Operators when Selecting Digital Products*, 13 Ocak 2025, [PDF](https://www.cisa.gov/sites/default/files/2025-01/joint-guide-secure-by-demand-priority-considerations-for-ot-owners-and-operators-508c.pdf), erişim: 13.09.2026. Satın almada güvenli tasarım bağlamı; işlem adımları ve tablolar özgün sentezdir.
