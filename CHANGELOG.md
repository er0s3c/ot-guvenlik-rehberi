# Değişiklik kaydı

Bu dosya deponun sürümler arasındaki değişikliklerini insan okuru için kaydeder. Düzen, [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) yaklaşımına benzer; başlıklar Türkçeleştirilmiştir. Sürüm başlıklarındaki tarihler `YYYY-AA-GG` biçimindedir; gövde metninde deponun kesim tarihi GG.AA.YYYY biçimiyle yazılır. En yeni sürüm en üstte yer alır.

## Değişiklik türleri

| Başlık | Ne için kullanılır? |
|---|---|
| Eklendi | Yeni bölüm, laboratuvar, şablon, kaynak kaydı veya araç |
| Değişti | Mevcut içeriğin yeniden yazılması, yapı veya adlandırma değişikliği |
| Kaldırıldı | Yayından çıkarılan dosya, bölüm veya kaynak |
| Düzeltildi | Hatalı olgu, tarih, bağlantı veya biçim düzeltmesi |

Kaynak güncellemeleri, hangi belgenin hangi sürümle değiştiği ve eski kaydın durumu yazılarak kaydedilir.

## Sürümleme politikası

Depo [anlamsal sürümleme](https://semver.org/lang/tr/) mantığını içerik deposuna uyarlar. Sürüm numarası `BÜYÜK.KÜÇÜK.YAMA` biçimindedir:

| Bileşen | Artış nedeni | Örnek |
|---|---|---|
| BÜYÜK | Yapısal değişiklik: dizin düzeninin, öğrenme yolunun veya dosya adlandırmasının yeniden kurulması; dış bağlantıları kıran taşımalar | Bölüm numaralarının yeniden düzenlenmesi |
| KÜÇÜK | Kapsam genişlemesi: yeni sektör bölümü, yeni laboratuvar, yeni şablon, yeni başvuru dosyası | Beşinci bir sektörün eklenmesi |
| YAMA | İçeriği koruyan düzeltmeler: kaynak güncellemesi, tarih ve bağlantı düzeltmesi, üslup uyumu, yazım hatası | Taslak bir yayının nihai sürümle değiştirilmesi |

`0.y.z` aralığı, yapının hâlâ oturmakta olduğunu gösterir: bu aralıkta dosya düzeni KÜÇÜK sürümlerde de değişebilir. Yayımlanan bir sürümün metni geriye dönük olarak sessizce değiştirilmez; düzeltme yeni bir sürüm girdisiyle kaydedilir.

## [0.1.0] — 2026-09-13

İlk herkese açık yayın. Araştırma kesim ve kaynak erişim tarihi: 13.09.2026.

### Eklendi

- **Temeller:** OT/IT/ICS/SCADA ayrımı, kontrol döngüsü ve bileşenler, Purdue modeli ve güven bölgeleri, endüstriyel protokoller, risk ve altyapı bağımlılıkları bölümleri.
- **Sektörler:** su ve atıksu, elektrik ve enerji, raylı sistemler, telekom ve baz istasyonları bölümleri ile sektör karşılaştırması.
- **Tehdit modelleme:** saldırgan bakış açısı, MITRE ATT&CK for ICS eşleştirmeleri ve kamuya açık kaynaklara dayanan vaka incelemeleri.
- **Savunma ve işletme:** varlık envanteri ve görünürlük, segmentasyon ve uzak erişim, izleme ve algılama, zafiyet ve değişiklik yönetimi, olay müdahalesi ve kurtarma, ilk 90 gün yol haritası.
- **Laboratuvarlar:** sentetik veriyle çevrimdışı kayıt analizi, mimari inceleme ve masa başı tatbikatı; her biri için çözüm ve değerlendirme anahtarı.
- **Şablonlar:** envanter ve akış, tehdit modeli, algılama kartı, olay ve kurtarma, değişiklik ve kabul, tedarikçi ve uzak erişim.
- **Başvuru:** standartlar ve Türkiye'de resmî başvuru noktaları bölümü, Türkçe–İngilizce sözlük, kaynak kataloğu ve araştırma yöntemi notu.
- **Depo dosyaları:** katkı rehberi, güvenlik bildirimi, bu değişiklik kaydı, ikili lisans dosyası, ağ bağlantısı gerektirmeyen belge denetim betiği, aynı denetimi sürekli tümleştirmede çalıştıran GitHub Actions iş akışı, `.gitignore` ve sekiz haftalık öğrenme yolu.

### Değişti, Kaldırıldı, Düzeltildi

İlk yayın olduğu için bu başlıklara ait girdi yoktur.

### Bu sürümün sınırları

- İçerik eğitim amaçlıdır; tesis tasarımı, uygunluk beyanı veya denetim raporu değildir.
- Bütün mimariler, tehdit matrisleri, tatbikatlar ve sentetik veri kurgusaldır ve metinde böyle işaretlenmiştir.
- Kaynaklar 13.09.2026 tarihinde incelenmiştir; standart sürümleri ve resmî sayfalar bu tarihten sonra değişmiş olabilir.
- Türkiye'ye özgü mevzuat ve bildirim yükümlülükleri özet düzeyindedir; bağlayıcı yorum için yetkili kurumun güncel yayını esastır.

## Gelecek sürümlerde planlanan

Aşağıdakiler **niyet beyanıdır, taahhüt değildir**; sırası ve kapsamı katkılara göre değişir.

- Ek sektör bölümleri: örneğin doğal gaz ve boru hatları, bina otomasyonu ve soğutma zinciri.
- Ek laboratuvarlar: kurtarma önceliklendirme alıştırması ve tedarikçi erişimi gözden geçirme alıştırması.
- Kaynak tazeleme: kaynak kataloğunun düzenli aralıklarla yeniden okunması, taslak yayınların nihai sürümle karşılaştırılması ve erişim tarihlerinin yenilenmesi.
- Sözlüğün genişletilmesi ve bölümler arası terim tutarlılığının gözden geçirilmesi.
- Belge denetim betiğinin kapsamının genişletilmesi: kaynak bölümü varlığı ve şablon alan adlarının tutarlılığı gibi henüz denetlenmeyen kurallar. (Tek H1, tablo sütun sayısı ve satır sonu boşluğu denetimleri betikte hâlihazırda vardır.)
- Zaman kaynağı ve saat kalitesi: zaman hizmetinin güven sınırı, saat sapmasının izlenmesi ve kayıtlarda zaman belirsizliğinin yazılması konusunun [izleme ve algılama](docs/04-savunma/03-izleme-ve-algilama.md) bölümünde ele alınması. Depo bu kavramı kayıt analizi laboratuvarında kullanıyor, ancak hiçbir bölümde anlatmıyor.
- Kayıt toplama ve temel davranış: merkezî kayıt/korelasyon çözümü, temel davranış çıkarmanın OT'deki sınırları ve “öğrenen” ürün iddialarının kabul kanıtına çevrilmesi.
- Kablosuz ve saha radyo taşıyıcıları: uzak sahaların telemetrisini taşıyan bağlantıların güven sınırı, kapsama ve yeniden bağlanma davranışı, abonelik sahipliğinin envantere yazılması. Depodaki örneklerin çoğu personelsiz saha olduğu hâlde [protokoller](docs/01-temeller/04-endustriyel-protokoller.md) bölümü kablolu bağlantı varsayımıyla yazılmıştır.
- Fiziksel erişim ve saha kabinleri: pano erişiminin yetkilendirilmesi, mühür ve ziyaret kaydının dijital kayıtla aynı zaman çizelgesine konması. Konu masa başı tatbikatında karar olarak soruluyor, [segmentasyon ve uzak erişim](docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md) bölümünde karşılığı yok.
- Dışarıda barındırılan hizmetler ve IIoT ağ geçitleri: giden telemetri yolunun da bir güven sınırı olduğu, hizmet kesildiğinde kontrol döngüsünün etkilenip etkilenmediği ve verinin sahipliği; [mimari ve güven bölgeleri](docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) bölümünde bir cümleyle anılıp bırakılmıştır.
- İnsan yoluyla erişim ve taşınabilir medya: [saldırgan bakışı](docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md) matrisinin kategori düzeyinde bu iki giriş yolunu da adlandırması; kurum içi hesap yaşam döngüsünün savunma tarafında karşılanması.
- Yazılım bileşen envanteri: terimin ne olduğu, hangi soruya cevap verdiği ve gelen bilginin envanterle nasıl eşleneceği; [zafiyet ve değişiklik yönetimi](docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) bölümünde şimdilik yalnızca bir tedarik sorusudur.
- Kontrol listelerinin kanıt bağı: bölüm kontrol listelerinin kanıt, doğrulayan ve tarih alanıyla birlikte doldurulmasını isteyen ortak bir düzene getirilmesi.

## Kapsam notu

Bu dosyanın düzeni ve sürümleme kuralları bu deponun özgün politikasıdır. Bağlantı verilen Keep a Changelog ve anlamsal sürümleme belgeleri kendi telif ve kullanım koşullarına tabidir; buradaki uyarlama onların çevirisi değildir. Katkı ve kayıt kuralları için [katkı rehberine](CONTRIBUTING.md) bakın. Erişim: 13.09.2026.
