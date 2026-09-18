# OT güvenliğinde maliyet ve seçim modeli

[Ana sayfa](../../README.md) · [Araç ve ürünler](01-arac-ve-urun-karsilastirmasi.md) · [Siemens UMC](02-siemens-ve-merkezi-kullanici-yonetimi.md) · [Araştırma kaydı](../../research/arac-urun-kaynaklar.md)

**Fiyat araştırması tarihi: 16.09.2026.** Bu bölüm master programın 39. başlığını karşılar. İki ayrı şey sunar: resmî sayfalarda doğrulanan lisans/fiyatlama modelleri ve matematiği gösteren **kurgusal bütçe alıştırması**. Aşağıdaki sayısal örnekler piyasa fiyatı, satıcı teklifi veya satın alma önerisi değildir.

## Ne için ödeme yapıyoruz?

Toplam sahip olma maliyeti, bir aracın satın alınması kadar işletilmesi, güncellenmesi ve gerektiğinde değiştirilmesi için gereken kaynakları kapsar. Bu bölümdeki denklem ve maliyet sınıfları **bu deponun özgün önerisidir**:

```text
TCO(N yıl) = ilk donanım + ilk kurulum/entegrasyon
          + N × (yıllık lisans + dış destek + iç bakım emeği + enerji/depolama)
          + planlı yenileme + geçiş/çıkış maliyeti
```

Bu basit model vergi, enflasyon, kur değişimi ve iskonto içermez. Bunlar gerekiyorsa ayrı varsayımlar eklenir; belirsiz kalem sıfır yazılmaz. Satın alma teklifinde destek zaten aboneliğe dahilse ikinci defa eklenmez.

OT bakım maliyetine protokol içeriği bakımı, üreticiyle uyum kontrolü, çevrimdışı güncelleme, bakım penceresi hazırlığı, geri dönüş kanıtı, yedek cihaz ve rol gözden geçirme emeği de dahil edilmesi **özgün planlama önerisidir**. Lisans bedeli olmayan yazılımın kurulumu ve işletimi ücretsiz varsayılmaz.

## Resmî kaynaklarla doğrulanan maliyet etkenleri

| Kalem | 16.09.2026 tarihinde doğrulanan model | Halka açık tutar / belirsizlik |
|---|---|---|
| Splunk Enterprise / Enterprise Security | Veri alımı, iş yükü veya ürün/pakete bağlı etkinlik modeli; bulut ve self-managed seçenekleri | İncelenen sayfa teklif ister. Bölgeye özgü birim fiyat doğrulanmadı. [Splunk](https://www.splunk.com/en_us/products/pricing.html) |
| Microsoft Sentinel | Analytics ve data lake katmanı; kullandıkça öde veya taahhüt; ek Azure hizmetleri ayrı ücretlenebilir | Bölge/sözleşme/para birimi seçimi önemlidir. Erişilen metinde sayısal fiyat tablosu yoktu; tek bir evrensel USD/GB fiyatı yazılmadı. [Microsoft](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) |
| IBM QRadar SIEM kurum içi | EPS/FPM veya MVS modeli; abonelik/kalıcı lisans | Kullanım kapasitesi ve sözleşme için **teklif gerekli**. [IBM](https://www.ibm.com/products/qradar-siem/pricing) |
| Elastic self-managed | Basic ve ücretli abonelik kapsamları; özellik matrisi | Basic ücretsiz kapsamı tüm özellikleri içermez; ücretli lisans için **teklif gerekli**. [Elastic](https://www.elastic.co/subscriptions) |
| Defender for IoT OT | Fiziksel tesis ve tesis büyüklüğü temelli lisans | Enterprise IoT ile aynı hesap değildir; **teklif gerekli**. [Microsoft billing](https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/billing) |
| Nozomi / Dragos / Claroty | Sensör/platform/modül kapsamı ürün ailesine bağlı | Okunan sayfalarda kapsamla eşlenebilen kamusal sayısal liste fiyatı bulunmadı; **teklif gerekli**. [Nozomi](https://www.nozominetworks.com/platform/guardian), [Dragos](https://www.dragos.com/cybersecurity-platform/), [Claroty](https://claroty.com/industrial-cybersecurity/ctd) |
| Endüstriyel firewall | Donanım modeli, güvenlik abonelikleri, yönetim ve destek ayrı kalem olabilir | Moxa EDR-G9010 IPS ek lisans ister; diğer markada aynı paket modeli varsayılmaz. **Model bazında teklif gerekli.** [Moxa](https://www.moxa.com/en/products/industrial-network-infrastructure/network-security-appliance/edr-g9010-series) |
| PAM | Seçilen ürün ve oturum/kasa kapsamına göre sözleşme | Ticari ürünler için incelenen kaynaklardan karşılaştırılabilir birim tutar elde edilmedi; **teklif gerekli**. [BeyondTrust](https://www.beyondtrust.com/products/privileged-remote-access), [Idira PAM](https://www.paloaltonetworks.com/idira/human/privileged-access-management) |
| UMC | WinCC Unified V21, 03/2026 belgesinde 10 kullanıcıya kadar ücretsiz lisans; 100/4.000 hesap için 365 günlük rental seçenekleri | Ücretsiz kapsam yalnız UMC yazılım lisansıdır; İngilizce belge ülkeye özgü bedel sunmuyor. Ücretli kapsam için **teklif gerekli**. [Siemens](https://docs.tia.siemens.cloud/r/en-us/v21/configuring-users-and-roles-rt-unified/basics-rt-unified/central-user-management-and-umc-rt-unified) |
| Wazuh / JumpServer topluluk | Açık kaynak kendi barındırma | Yazılım lisans bedeli yok; donanım, destek ve emek ayrıca. [Wazuh](https://documentation.wazuh.com/current/getting-started/index.html), [JumpServer](https://github.com/jumpserver/jumpserver) |

**Fiyat kanıt kartı:** `[satıcı] [ürün/SKU] [sürüm/paket] [tarih] [ülke/bölge] [para birimi] [birim: cihaz/kullanıcı/GB/EPS/yıl] [vergi] [destek dahil mi?] [yenileme koşulu] [URL/teklif kimliği]`. Bu alanları olmayan sayıyı güncel fiyat diye sunma. Bir ürünün sayfasında fiyat görünmemesi, piyasada hiçbir fiyat bulunmadığının kanıtı değildir; bu incelemenin sonucudur.

## Üç mimarinin ortak kapsamı

Karşılaştırma için **kurgusal ve eşit eğitim talebi**: bir tesis, iki gözlem noktası, 100 envanter varlığı, 10 ayrıcalıklı kullanıcı, günlük 10 GB normalize edilmiş log, 90 gün hızlı arama ve toplam 365 gün saklama. Bunlar üretici kapasite tavsiyesi değildir. Tam paket kaydı hacmi 10 GB/gün log hesabına dahil değildir. Mevcut PLC/SCADA üretim sistemi yatırımı karşılaştırma kapsamı dışındadır.

```text
Trafik kopyası → ağ sensörü → kayıt toplayıcı → SIEM → analist
Tedarikçi → erişim onayı → PAM/oturum aracısı → mühendislik istasyonu
Hücreler arası iletişim → kurala bağlı firewall
Güvenlik sunucusu/sensör sağlığı → metrik izleme
```

| Katman | Budget: seçilen güvenlik yazılımları açık kaynak | Professional: karma | Enterprise: ticari lisans ve destek |
|---|---|---|---|
| Donanım | Ayrılmış sunucu/depolama ve gözlem donanımı | Daha fazla kapasite ve yedekleme alanı | Yedekli yönetim/depolama ve yedek cihaz varsayımı |
| Firewall | OPNsense; belgede L3/L4 sınır rolü | Modeli doğrulanmış bir ticari endüstriyel firewall | Yedekli ticari endüstriyel firewall ve merkezi yönetim |
| IDS | Zeek + Suricata; pasif tasarım | Bir ticari OT sensör platformu + açık kaynak inceleme | Ticari OT sensörleri ve merkezi yönetim |
| SIEM | Wazuh | Wazuh veya ihtiyaca göre ticari SIEM; örnek hesapta Wazuh | Splunk ES / Sentinel / QRadar / Elastic Enterprise arasından gereksinimi karşılayan biri |
| PAM | JumpServer topluluk; gerekli özellik kanıtlanmazsa açık eksik | Ticari PAM/uzak erişim | Ticari PAM, yedeklilik ve sözleşmeli destek |
| Monitoring | Prometheus + Grafana OSS | Prometheus + Grafana OSS | Sözleşmeye dahil altyapı sağlığı izleme ürünü |
| İşletme | İç ekip; ücretsiz topluluk desteği SLA değildir | İç ekip + belirli ürünlerde dış destek | İç ekip + belirlenmiş kapsamda üretici/dış destek |

Bu adlar **tasarım sınıflarıdır**, güvenlik seviyesi veya IEC 62443 Security Level değildir. Enterprise satırında ticari destekli ürünlerin iç bileşenlerinde açık kaynak bulunması mümkündür; “tamamen enterprise” seçimi satın alma/işletme modelini ifade eder. Bu üç örnek aynı algılama kapsamını, çalışma süresini veya insan desteğini garanti etmez.

Budget seçeneklerinin işlev kaynakları: [OPNsense](https://docs.opnsense.org/intro.html), [Zeek](https://zeek.org/about/), [Suricata](https://suricata.io/features/), [Wazuh](https://documentation.wazuh.com/current/getting-started/index.html), [JumpServer](https://github.com/jumpserver/jumpserver), [Grafana OSS](https://grafana.com/oss/grafana/), [Prometheus](https://prometheus.io/docs/introduction/overview/). Security Onion'un ELv2 bileşenleri nedeniyle bu “tamamen açık kaynak yazılım” örneğine otomatik eklenmemiştir. [Security Onion lisansı](https://docs.securityonion.net/en/3/main/license/)

## Sayısal alıştırma: piyasa fiyatı olmayan örnek hesap

**Aşağıdaki bütün tutarlar uydurulmuş planlama girdileridir; hiçbir üreticinin fiyatını temsil etmez.** Para birimi sadece ortak hesap yapmak için EUR seçilmiştir; ülke/bölge yoktur. Vergi ve kur dönüşümü uygulanmamıştır. Hücre biçimi **ilk yatırım / yıllık gider** şeklindedir.

| Kalem | Budget örneği (EUR) | Professional örneği (EUR) | Enterprise örneği (EUR) | Çifte sayımı önleyen sınır |
|---|---|---|---|---|
| Hardware | 5.000 / 0 | 8.000 / 0 | 14.000 / 0 | Sunucu, depolama, TAP/aynalama ve UPS; aşağıdaki ayrı cihazlar hariç |
| Firewall | 600 / 0 | 3.000 / 0 | 8.000 / 0 | Firewall cihazı/ayrılmış kaynak; abonelik lisans satırında |
| IDS | 800 / 0 | 2.000 / 0 | 6.000 / 0 | Sensörün ek donanımı; abonelik lisans satırında |
| SIEM | 1.000 / 0 | 2.000 / 0 | 4.000 / 0 | İlk kayıt/alan/kural entegrasyonu; sunucu hardware satırında |
| PAM | 600 / 0 | 1.800 / 0 | 3.500 / 0 | İlk rol, oturum ve onay entegrasyonu |
| Monitoring | 400 / 0 | 800 / 0 | 1.000 / 0 | İlk sensör/sunucu sağlığı panosu ve alarm hazırlığı |
| Licensing | 0 / 0 | 0 / 7.000 | 0 / 22.000 | Tüm yıllık güvenlik yazılımı/servis lisansları; alt dağılım aşağıda |
| Support | 0 / 0 | 0 / 2.500 | 0 / 6.500 | Varsayımsal ayrı dış destek sözleşmesi; lisansa dahil değil kabul edildi |
| Maintenance | 0 / 14.400 | 0 / 12.600 | 0 / 21.600 | İç bakım emeği; SOC'un bütün vardiya personeli değil |
| Enerji ve yedek işletimi | 0 / 900 | 0 / 1.500 | 0 / 2.500 | Elektrik ve ek yedek işletim gideri varsayımı |
| **İlk yatırım toplamı** | **8.400** | **17.600** | **36.500** | Tek seferlik |
| **Yıllık gider toplamı** | **15.300** | **23.600** | **52.600** | Her yıl aynı kabul edildi |
| **İlk yıl toplamı** | **23.700** | **41.200** | **89.100** | İlk yatırım + 1 yıllık gider |
| **Üç yıl toplamı** | **54.300** | **88.400** | **194.300** | İlk yatırım + 3 × yıllık gider |

Bakım hesabı: Budget `480 saat/yıl × 30 EUR/saat = 14.400`; Professional `360 × 35 = 12.600`; Enterprise `480 × 45 = 21.600`. Saat ve ücretler de kurgusaldır. Bunlar bir tesisin gerçek işgücü ihtiyacını veya piyasa ücretini göstermez.

Lisans varsayımının dağılımı, yine **piyasa fiyatı değildir**:

| Yıllık lisans kalemi | Budget (EUR) | Professional (EUR) | Enterprise (EUR) |
|---|---|---|---|
| Firewall servisleri | 0 | 1.200 | 3.000 |
| OT IDS/platform | 0 | 4.000 | 8.000 |
| SIEM | 0 | 0 | 6.000 |
| PAM | 0 | 1.800 | 4.000 |
| Monitoring | 0 | 0 | 1.000 |
| **Toplam** | **0** | **7.000** | **22.000** |

**Sonucun anlamı:** Bu sayılardan hangi ürünün ucuz olduğu çıkarılamaz. Alıştırma, “ücretsiz lisans = sıfır toplam maliyet” hatasını ve donanım/abonelik/emeğin ayrı tutulmasını gösterir. Gerçek teklif alınca ilgili girdiler değiştirilir; teklif kapsamı değişmişse mimari de yeniden karşılaştırılır.

## Kapasite ve duyarlılık hesabı

Bu hesaplar **özgün yaklaşık boyutlandırma alıştırmasıdır**; üretici sizing aracının yerine geçmez.

```text
Ham sıcak log = 10 GB/gün × 90 gün = 900 GB
Ham toplam log = 10 GB/gün × 365 gün = 3.650 GB
Sıcak depolama örneği = 900 × 1,5 indeks katsayısı × 2 kopya = 2.700 GB
Kalan 275 günün ham arşivi = 10 × 275 = 2.750 GB
```

İndeks katsayısı ve kopya sayısı varsayımdır; yedek, sıkıştırma, dosya sistemi payı, arşiv kopyası ve paket kaydı ayrıca eklenir. İkinci kopya ile yedek aynı güvenlik/geri dönüş amacı sayılmaz.

| Değişen varsayım | Hesaba etkisi | Değerlendirme sorusu |
|---|---|---|
| Log 10'dan 20 GB/güne çıkarsa | Hacimle doğrusal varsayılan depolama yaklaşık iki kat olur; bütün TCO iki kat olmaz | SIEM lisansı GB, EPS, MVS veya başka hangi ölçüte bağlı? |
| İç bakım yılda 120 saat artarsa | Budget örneğinde 3 yılda `120 × 30 × 3 = 10.800 EUR` eklenir | Bu ek iş destek sözleşmesiyle gerçekten azalıyor mu? |
| İkinci tesis eklenirse | Tesis lisansı, sensör, seyahat ve gözlem kapsamı yeniden hesaplanır | Mevcut yönetim lisansı yeni tesisi içeriyor mu? |
| Bir yıl ürün değişimi yapılırsa | Dışa aktarım, kural çevirisi, çift işletim ve eğitim eklenir | Veri ve kural dışa aktarımı sözleşmede var mı? |

## Teklif değerlendirme ve çıkış planı

Aşağıdaki liste **özgün değerlendirme önerisidir**. Üç adayın karşılaştırması aynı işlevsel kapsamda yapılır.

- [ ] Aynı tesis/varlık/kullanıcı/log hacmi ve saklama süresi teklifte yazılmış.
- [ ] Donanım, lisans, ilk entegrasyon, destek, bakım ve yenileme ayrı.
- [ ] IDS'nin gözlem noktaları ile firewall'ın uygulama noktaları açık.
- [ ] Gerekli endüstriyel protokol alanları ve sürümleri için örnek kanıt istenmiş.
- [ ] Pasif kipte hangi verilerin alınamadığı ve aktif seçeneğin gerekip gerekmediği belli.
- [ ] SIEM bağlayıcı/API hakları, veri çıkış ücretleri ve geçiş biçimi belli.
- [ ] Yerel/bulut yönetim, veri bölgesi ve çevrimdışı çalışma koşulları belli.
- [ ] Lisans süresi dolunca izleme, arama, güncelleme ve dışa aktarım davranışı ayrı sorulmuş.
- [ ] Destek saatleri, yanıt hedefi, eskalasyon ve yerel saha işi sınırı yazılmış.
- [ ] Donanım yaşam döngüsü ve yedek parça erişimi teklif tarihine göre doğrulanmış.
- [ ] Açık kaynak seçenekte güncelleme, geri yükleme, içerik ve olay inceleme sahipleri atanmış.

## Belge alıştırması: aynı ihtiyaca üç bütçe

1. **THEORY:** İlk yatırım, yıllık lisans, destek ve bakım emeğini tanımla; neden ayrı olduklarını yaz.
2. **LAB:** Ortak kurgusal kapsamı kullanarak üç mimariyi çiz. Her katmana bu bölümden bir ürün ailesi veya açık kaynak bileşeni yerleştir; kurulmuş gibi anlatma.
3. **TEST:** Üç yıllık toplamları yeniden hesapla. Budget bakımına 120 saat/yıl ekle ve yeni toplamı bul. Bir teklifin desteği lisansa dahil etmesi durumunda çifte sayımı düzelt.
4. **DEFENSE:** Her mimaride eksik veya doğrulanmamış iki güvenlik gereksinimi yaz; maliyeti düşük olanı otomatik seçme.
5. **REPORT:** Maliyet tablosunu “resmî lisans modeli”, “teklif bekleyen”, “kurgusal varsayım” etiketleriyle teslim et. CV çıktısını “OT güvenliği için belgesel mimari ve TCO modeli” olarak adlandır.

### Kabul ölçütleri

- [ ] Üç toplam doğru: 54.300, 88.400 ve 194.300 EUR; tümü kurgusal hesap olarak etiketlenmiş.
- [ ] Bakım artışı sonrası Budget toplamı 65.100 EUR; birim ve süre gösterilmiş.
- [ ] Tesis/kullanıcı/GB ölçüleri birbirine karıştırılmamış.
- [ ] Halka açık doğrulanmış bedel bulunmayan ürün için fiyat uydurulmamış.
- [ ] Ücretsiz lisanslı mimaride emek ve altyapı maliyeti görünür.
- [ ] Üç mimarinin işlev/destek farkları ayrıca yazılmış; bütçe adı güvenlik sertifikası sayılmamış.

## Kaynaklar ve kapsam

Ürün kaynakları, yayın/erişim tarihleri, erişim kısıtları ve kullanılmayan iddialar [araştırma kaydındadır](../../research/arac-urun-kaynaklar.md). Erişim: **16.09.2026**. Formüller, bütçe tutarları, kapasite varsayımları, mimari paketler ve kabul ölçütleri bu deponun özgün eğitim sentezidir. Satıcılarla iletişim kurulmamış, ücretli teklif alınmamış ve ürün kurulumu yapılmamıştır.
