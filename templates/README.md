# Çalışma şablonları

[Ana sayfa](../README.md) · [Varlık envanteri ve görünürlük](../docs/04-savunma/01-envanter-ve-gorunurluk.md) · [Çevrimdışı laboratuvarlar](../labs/README.md)

Bu dizindeki on üç şablon, rehberdeki bölümlerin çıktısını yazılı bir kayda dönüştürmek içindir. İlk altı form işletme kayıtlarına, 07-09 arası ders, değerlendirme ve final proje çalışmalarına, 10-13 arası ise denetim, standart uyumu, RBAC tasarımı ve güvenli kodlama çalışmalarına yöneliktir. İçlerindeki örnek değerler kurgusaldır; uygunluk beyanı veya yapılmış saha testi yerine geçmez.

## Nasıl kullanılır

1. **Kopyalayın.** İlgili dosyayı kurumun kontrollü kayıt sistemine (belge yönetimi, bakım/varlık sistemi veya erişim kontrollü paylaşım alanı) kopyalayın. Doldurma bu kopya üzerinde yapılır; depodaki dosya boş kalır.
2. **Başlığı tanımlayın.** Her kopyada kapsam (hangi saha, hangi sistem), sahip rolü, hazırlama tarihi, sürüm ve gözden geçirme tarihi bulunsun.
3. **Gerçek tesis verisini herkese açık yere koymayın.** Doldurulmuş kopya herkese açık bir depoya, genel erişimli ortak sürücüye veya sohbet kanalına konulmaz. Bu depoya katkı gönderirken de doldurulmuş kopya paylaşılmaz; katkı kuralları [CONTRIBUTING.md](../CONTRIBUTING.md) dosyasındadır.
4. **Hassas alanları referansla taşıyın.** Koordinat, açık adres, ağ adresi, hesap adı, proje dosyası ve koruma ayarı gibi bilgiler şablonun gövdesine yazılmaz; bunlara kurum içi kayıt kimliğiyle atıf yapılır (örnek: `PRJ-TERFI-2026-03`).
5. **Kaynağı ve tarihi birlikte yazın.** Doldurulan her alan, bilginin nereden geldiği ve ne zaman doğrulandığı bilgisiyle birlikte anlam kazanır.

Şablonları gerçek bir tesise dokunmadan denemek için [çevrimdışı laboratuvarlardaki](../labs/README.md) kurgusal veri kullanılabilir.

## Çalışma şablonları listesi

| Şablon | Ne zaman kullanılır? | Kim doldurur? | Çıktı neye yarar? | İlgili bölüm |
|---|---|---|---|---|
| [01 Envanter ve akış](01-envanter-ve-akis.md) | Envanter çalışmasının başında ve her mimari değişiklikte | Varlık sahibi, otomasyon/bakım ve ağ sorumlusu birlikte | İşlev, sahip, bağımlılık ve akış eşlemesi; diğer şablonların girdisi | [Varlık envanteri ve görünürlük](../docs/04-savunma/01-envanter-ve-gorunurluk.md) |
| [02 Tehdit modeli](02-tehdit-modeli.md) | Yeni sistem, yeni bağlantı veya dönemsel gözden geçirmede | Güvenlik ekibi, süreç mühendisi ve işletme temsilcisi | Hedef, ön koşul, aşılan güven sınırı, olası etki, belirti ve kontrol eşlemesi | [Saldırgan bakış açısı](../docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md) |
| [03 Algılama kartı](03-algilama-karti.md) | Yeni bir alarm veya analitik önerildiğinde ve ölçüm gözden geçirmesinde | SOC analisti ile OT işlev sorumlusu | Bağlamı, sahibi ve normal açıklaması tanımlı alarm; yanlış pozitif incelemesi | [İzleme ve algılama](../docs/04-savunma/03-izleme-ve-algilama.md) |
| [04 Olay ve kurtarma](04-olay-ve-kurtarma.md) | Tatbikat sırasında, olay anında ve olay sonrası değerlendirmede | Olay yöneticisi, vardiya amiri, proses mühendisi | Zaman çizelgesi, karar ve kanıt kaydı; mühendis onaylı geri dönüş kapıları | [Olay müdahalesi ve kurtarma](../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md) |
| [05 Değişiklik ve kabul](05-degisiklik-ve-kabul.md) | Yama, proje/ayar değişikliği, cihaz değişimi ve devreye almada | Değişiklik sahibi, onaylayan ve testi yürüten | Onay, test planı, geri dönüş yolu ve kabul kanıtı | [Zafiyet ve değişiklik yönetimi](../docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) |
| [06 Tedarikçi ve uzak erişim](06-tedarikci-ve-uzak-erisim.md) | Tedarikçi sözleşmesinde, yeni uzak erişim yolunda ve dönemsel incelemede | Sözleşme sahibi, güvenlik ekibi ve işletme | Kişi, hedef, süre, kayıt ve iptal koşulu tanımlı erişim kaydı | [Segmentasyon ve uzak erişim](../docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md) |
| [07 Ders ve değerlendirme](07-ders-ve-degerlendirme.md) | Bir konu çalışılırken | Okur ve değerlendirici | Yirmi alan, beş aşamalı teslim ve düzeltme kaydı | [Konu haritası](../docs/11-konu-haritasi.md) |
| [08 Değerlendirme ve risk](08-degerlendirme-ve-risk-kaydi.md) | Değerlendirme kapsamı hazırlanırken | Değerlendiren ve işlev sahibi | RoE, bulgu, risk ve yönetici özeti | [Değerlendirme yöntemi](../docs/09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) |
| [09 Final proje teslimleri](09-final-proje-teslimleri.md) | Belgeler bütünleştirilirken | Proje hazırlayan ve gözden geçiren | Yirmi üç çıktının alanları, kanıtları ve kabul durumu | [Su tesisi örneği](../labs/05-butunlesik-su-tesisi.md) |
| [10 BİGR EKS denetimi](10-bigr-eks-denetim-matrisi.md) | Cumhurbaşkanlığı DDO BİGR denetimlerinde | EKS denetçisi ve kurum CISO'su | BİGR EKS 12 tedbirinin kanıtları ve uyum skorlama | [Standartlar ve Türkiye](../docs/05-standartlar-ve-turkiye.md) |
| [11 IEC 62443 öz değerlendirme](11-iec-62443-oz-degerlendirme.md) | Zone/Conduit güvenlik seviyesi belirlemede | OT siber güvenlik mühendisi ve mimar | 7 Temel Gereksinimde (FR 1-7) SL-T vs SL-A fark analizi | [Standartlar ve Türkiye](../docs/05-standartlar-ve-turkiye.md) |
| [12 OT RBAC ve UMC tasarımı](12-ot-rbac-ve-umc-tasarim-sablonu.md) | Kimlik yönetimi, RBAC ve SIMATIC UMC mühendisliğinde | OT sistem mühendisi ve kimlik mimarı | AD $\to$ UMC $\to$ PLC/HMI yetki matrisi, break-glass ve audit | [Zero Trust ve RBAC](../docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md), [Siemens UMC](../docs/10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md) |
| [13 Güvenli PLC kodlama denetimi](13-guvenli-plc-kodlama-denetim-matrisi.md) | PLC yazılım devreye alma ve güvenlik denetiminde | Otomasyon mühendisi ve OT denetçisi | Top 20 kuralına göre kod seviyesi zafiyet ve uyum analizi | [Güvenli PLC kodlama](../docs/08-mimari-ve-erisim/04-guvenli-plc-programlama-top20.md) |

Sıra zorunlu değildir. Yine de envanter ve akış şablonu doldurulmadan tehdit modeli, algılama kartı ve erişim kaydı çoğunlukla eksik kalır; hepsi aynı varlık ve akış kimliklerine atıf yapar.

## Doldurma disiplini

- Her alanda bilginin **kaynağı** (belge, kayıt, görüşme, gözlem) ve **doğrulama tarihi** bulunur. Tarihsiz bilgi, güncelliği bilinmeyen bilgidir.
- **Tahmin ile doğrulanmış bilgi ayrılır.** Önerilen ölçek: `doğrulandı` (belge ve saha/kayıt teyidi), `belgeye dayanıyor` (tek kaynak, teyit yok), `tahmin` (uzman görüşü). Ölçek kurumca değiştirilebilir; değiştirilirse şablonun başında tanımlanır.
- **Boş bırakmak yerine `doğrulanacak` yazılır.** Yanına sorumlu rol ve hedef tarih eklenir. Boş hücre, bilginin yok olduğunu mu yoksa henüz bakılmadığını mı gösterdiğini söylemez.
- Bilinmeyen bir alan tahminle doldurulduysa, gerekçesi kanıt alanına yazılır. Kritik alanlarda "muhtemelen" ifadesi tek başına bırakılmaz.
- Aynı sistemden türetilmiş iki kayıt bağımsız doğrulama sayılmaz. İkinci kaynak farklı bir yoldan gelmelidir (saha gözlemi, bakım kaydı, ikinci kişi incelemesi).
- Kişi adı yerine **rol** yazılır. Kişiler değişir; sorumluluk kaydı kalıcı olmalıdır. Kişisel veri saklama süreleri kurumun yetkili sürecinde belirlenir.
- Her kopyanın **sürümü ve değiştireni** izlenir. Önceki sürüm silinmez; hangi alanın ne zaman değiştiği bir olay incelemesinde önem kazanır.
- Çelişkiler silinerek değil, bir **iş listesine** alınarak kapatılır. "Kayıt ile saha uyuşmuyor" bulgusu, kaydı sessizce güncellemekten daha değerli bir çıktıdır.

Kontrol listesi:

- [ ] Her doldurulmuş alanda kaynak ve doğrulama tarihi var.
- [ ] Güven düzeyi ölçeği şablonun başında tanımlı.
- [ ] `doğrulanacak` işaretli alanların sorumlusu ve hedef tarihi belli.
- [ ] Hassas içerik yerine kurum içi kayıt kimliği kullanılmış.
- [ ] Sahip, sürüm ve gözden geçirme tarihi güncel.
- [ ] Çelişkiler iş listesine alınmış ve takip ediliyor.

## Veri sınıfı ve saklama

Doldurulmuş şablonlar bir tesisin işleyişini toplu halde anlatır; tek tek parçalarından daha hassastır. Saklama kararı bu birleşik değere göre verilir:

| İçerik | Nerede tutulur? | Şablona ne yazılır? |
|---|---|---|
| Varlık kodu, işlev, sahip rolü | Kontrollü kayıt sistemi | Doğrudan yazılabilir |
| Açık adres, koordinat, saha planı | Erişim kontrollü tesis kayıtları | Saha/konum kodu |
| Ağ adresi, kural dökümü, topoloji çizimi | Ağ ve güvenlik ekibinin kayıt sistemi | Bölge adı ve akış kimliği |
| Hesap adı, kimlik sırrı, sertifika | Kimlik yönetimi ve sır saklama sistemi | Rol adı; kimlik sırrı şablonun hiçbir alanına yazılmaz |
| Kontrol projesi, koruma ayarı, parametre dosyası | Mühendislik kayıt sistemi, yedekle birlikte | Proje/sürüm kimliği |
| Olay kanıtı, kayıt dökümü | Olay kayıt sistemi, delil zinciriyle | Kanıt kimliği ve saklama yeri referansı |

Şablon kopyalarının kendisi de yedeklenir ve erişimi sınırlanır. Bir olay sırasında envanter ve akış kaydı okunamıyorsa, kaydın varlığı karar vermeye yetmez.

## Lisans ve atıf

Bu şablonlar ve içlerindeki kurgusal örnekler bu deponun özgün eğitim sentezidir; belirli bir standardın resmî formu veya çevirisi değildir. Standartlara ilişkin başvuru noktaları için [standartlar ve Türkiye bölümüne](../docs/05-standartlar-ve-turkiye.md) bakılabilir.

Özgün metinler **CC BY 4.0** ile lisanslıdır: kopyalanabilir, değiştirilebilir ve kurum içinde kullanılabilir; koşul, kaynağın belirtilmesidir. Atıf koşulları ve üçüncü taraf materyal sınırları [LICENSE.md](../LICENSE.md) dosyasındadır. Örnek atıf: "OT Güvenliği Rehberi, çalışma şablonları, CC BY 4.0."

Lisans şablonun biçimini kapsar. Doldurduğunuz kopyadaki tesis verisi sizin kurumunuza aittir; bu depo o veriye ilişkin hiçbir hak veya sorumluluk üstlenmez ve doldurulmuş kopyaları görmez.
