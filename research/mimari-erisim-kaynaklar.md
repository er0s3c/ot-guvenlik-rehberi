# Mimari, kimlik ve sıkılaştırma kaynak incelemesi

[Araştırma yöntemi](YONTEM.md) · [Kaynak kataloğu](../KAYNAKLAR.md) · [Katkı rehberi](../CONTRIBUTING.md)

**İnceleme ve erişim tarihi: 16.09.2026.** Yayın tarihleri aşağıda ayrıca verilir. Bu kayıt [Zero Trust, RBAC ve PAM](../docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md), [firewall, IDMZ ve uzak erişim](../docs/08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) ve [varlık sınıflarına göre sıkılaştırma](../docs/08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md) belgelerinin dayanaklarını ve sınırlarını tutar.

## İncelenen birincil kaynaklar

| Yayıncı / belge | Yayın / sürüm | Okunan kapsam | Kullanılan iddia / kullanım sınırı |
|---|---|---|---|
| NIST, [SP 800-82 Rev. 3: Guide to Operational Technology (OT) Security](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) | Eylül 2023, nihai Rev. 3 | İçindekiler ve mimari kapsam; §5.2.2 fiziksel güvenlik, §5.2.3.4 Zero Trust, §5.2.4–5.2.5 donanım/yazılım, §5.4.1 DCS/PLC mimarisi, §5.3.7 IIoT, §6.2.5–6.2.7 bakım/kayıt/medya, §6.2.10 uzak erişim, §6.2.11 yama, §6.2.12 zaman; Ek F/AC-6 | OT uyumluluğu/gecikme/erişilebilirlik, IDMZ sınırı, gerekli işlevler, süreli ve izlenen erişim, yama planı, zaman kaynağı izleme. Ayrıntılı listeler standart kontrolü diye sunulmadı |
| NIST, [SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Ağustos 2020 | Yayın kaydı ve özet tanım | Ağ konumuna dayalı örtük güvenin bırakılması, kimlik ve kaynak odaklı yaklaşım. Bir ürün veya OT uygulamasının bu modele uygunluğu çıkarılmadı |
| NIST, [Role-based access control sözlük girdisi](https://csrc.nist.gov/glossary/term/role_based_access_control) | Sayfada yayın tarihi belirtilmiyor | Kaynakları belirtilen RBAC tanımı | Rol–işlem izinleri ilişkisi. Örnek sekiz rol NIST'in zorunlu rol listesi değildir |
| NIST, [SP 800-162: Guide to Attribute Based Access Control Definition and Considerations](https://csrc.nist.gov/pubs/sp/800/162/upd2/final) | Ocak 2014; kayıtta 02.08.2019 güncellemeleri dahil | Yayın kaydı ve ABAC tanımı | Özne, nesne, işlem ve ortam niteliklerinin değerlendirilmesi. İş emri/zaman örneği özgün eğitim sentezi |
| ISA, [ISA/IEC 62443 Series of Standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | Dinamik katalog; tek yayın tarihi belirtilmiyor | Kamuya açık seri parça adları ve paydaş/yaşam döngüsü açıklaması | 3-2 ile sistem tasarımı risk değerlendirmesi, 3-3 ile sistem gereksinimleri ilişkisi; madde metni veya uygunluk kontrol listesi çıkarılmadı |
| ISA, [ISA-95 Standard: Enterprise-Control System Integration](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard) | Dinamik tanıtım; tek yayın tarihi belirtilmiyor | Kamuya açık tanıtım ve üretim/kurum bütünleştirme kapsamı | MES/ERP işlev bağlamı; belirli ürün için zorunlu Purdue seviyesi çıkarılmadı |
| Siemens, [Functional description of S7-1500 CPUs: Settings for access levels](https://docs.tia.siemens.cloud/r/en-us/v20/functional-description-of-s7-1500-cpus-s7-1500/setting-the-operating-behavior-s7-1500/protection-security-s7-1500/settings-for-access-levels-s7-1500) | STEP 7 V20, 11/2024 | Künye ve menü/içerik başlıkları; ayrıntı gövdesi alınamadı | Yalnız sürüm ve konu başlıkları. Erişim seviyeleri/rollerin belirli CPU/firmware'de desteklendiği iddia edilmedi |

Tablodaki her kaynağa erişim tarihi 16.09.2026'dır. NIST'in sabit Rev. 3 metni bu çalışmanın teknik referansıdır; burada "en yeni sürüm" iddiası yapılmaz. Diğer NIST kayıtlarının tarihleri yayın/son güncelleme ayrımı korunarak yazılmıştır.

## Erişim kısıtları

- Siemens'in [CPU 1515-2 PN ekipman kılavuzu PDF adresi](https://support.industry.siemens.com/cs/attachments/109972211/s71500_cpu1515_2_pn_manual_en-US_en-US.pdf) açılmaya çalışıldı; HTTP 403 nedeniyle metin alınamadı. Arama sonucundaki parçalar CPU özelliğine teknik dayanak yapılmadı.
- Siemens çevrimiçi V20 sayfası açıldı; ürün, sürüm, yayın ayı ve içerik menüsü görüldü. Bu görünüm ayrıntılı özellik ve uyumluluk tablosunun okunması yerine sayılmadı.
- Lisanslı ISA/IEC standartlarının tam metni alınmadı. Kamuya açık katalog/özet ile özgün örnekler açıkça ayrıldı.

## Özgün içerik ve doğrulama sınırı

Sekiz rolün işlem matrisi; kimlik hizmeti kesintisi tablosu; su işletmesi Mermaid çizimleri; sembolik firewall izin/ret matrisi; yedi varlık sınıfı için kontrol listeleri; maliyet etkenleri ve THEORY → LAB → TEST → DEFENSE → REPORT belge alıştırmaları **bu deponun özgün eğitim sentezidir**.

Firewall tablosundaki `P_...` alanları bilinmeyen hedef port/port kümeleridir. Bunlar gerçek port numarası gibi sunulmadı. Taşıma, port, nesne, sıra, NAT, yönlendirme ve cihaz yeteneği doğrulanmadan tablonun doğrudan uygulanamayacağı yazıldı. Bilinmeyen alanı tahminle doldurmak yerine belge incelemesinin girdisi yapmak tercih edildi.

Kontrol listeleri belge üzerinden uygulanır. Madde yanında istenen yapılandırma kaydı veya kabul raporu burada üretilmiş/yürütülmüş sayılmaz. VM, güvenlik ürünü, PLC simülatörü veya gerçek cihaza kurulum/bağlantı yapılmadı.

## Kullanılmayan iddialar

- Purdue'nin bütün tesisleri ve bulut/IIoT bağımlılıklarını tek başına yeterli açıklaması; 3.5/5 gösterimlerinin evrensel zorunlu seviyeler olması.
- Zone veya VLAN adının tek başına yetkilendirme, kontrol doğrulaması veya IEC 62443 uygunluğu sağlaması.
- VPN, MFA, ZTNA veya PAM ürününün diğer bütün erişim kontrollerinin yerine geçmesi.
- Bütün PLC'lerin sertifika, şifreleme, kişisel hesap, MFA, firmware imzası veya merkezi dizin desteklemesi.
- Siemens S7-1200/S7-1500 ailesindeki bütün modellerin aynı erişim özellikleri veya aynı menüleri sunması; firmware destek eşiği ve varsayılan ayarlar.
- Belirli Siemens, Schneider, ABB veya Rockwell çözümünün fiyatı, üstünlüğü veya tüm ürün ailesi için uyumluluğu. Bu belgelerde ürün satın alma karşılaştırması yapılmadı.
- Yedek sunucunun temiz kurtarma kopyası olması; oturum kaydının tek başına bütün işlemleri veya proses etkisini kanıtlaması.
- Bir açık kaynak bileşenin ticari industrial firewall veya PAM paketinin bütün yeteneklerini sağlaması; lisanssız kullanımın işletme maliyetini sıfırlaması.
- Tasarlanmış kabul adımlarının gerçek sistemde başarıyla uygulanmış olduğu; belge alıştırmasının saha deneyimi veya mesleki sertifika sayılması.

## Gözden geçirme gereksinimi

Ürün/sürüm örneği genişletilirken erişilebilen üretici kılavuzu, hedef ürün kodu, firmware ve mühendislik yazılımı birlikte kaydedilmelidir. Yeni protokol/port satırı eklendiğinde kullanılan profil ve yapılandırma kaynağı belirtilmelidir. Kaynak değişikliği, ilgili ders ve kaynak kataloğuyla birlikte güncellenir.

## Kapsam notu

Bu kayıt araştırmanın izini tutar; standardın çevirisi, ürün tavsiyesi veya tesis devreye alma belgesi değildir. Son inceleme: 16.09.2026.
