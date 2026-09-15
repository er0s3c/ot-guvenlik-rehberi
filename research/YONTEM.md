# Araştırma yöntemi

[Ana sayfa](../README.md) · [Kaynak kataloğu](../KAYNAKLAR.md) · [Katkı rehberi](../CONTRIBUTING.md)

Bu dosya, depodaki metinlerin nasıl araştırıldığını anlatır: hangi kaynak hangi koşulda kabul edilir, bir iddia metinde nasıl işaretlenir, doğrulanamayan bilgiye ne yapılır ve kayıtlar nasıl tazelenir. Amaç basittir. Okuyucu bir cümlenin arkasında ne kadar dayanak olduğunu, o cümleyi okurken görebilmelidir.

Araştırma kesim ve erişim tarihi **13.09.2026**. Kaynakların tek listesi [kaynak kataloğundadır](../KAYNAKLAR.md); gerekçeler dört araştırma kaydındadır: [su ve elektrik](su-elektrik-kaynaklar.md), [raylı sistemler ve telekom](rayli-telekom-kaynaklar.md), [tehdit modelleme ve vakalar](tehdit-kaynaklar.md), [standartlar ve Türkiye](standartlar-kaynaklar.md). Burası yöntemi açıklar; katkıların kabul koşulları [katkı rehberindedir](../CONTRIBUTING.md) ve bir çelişki durumunda katkı rehberi esas alınır.

## Kaynak seçimi

### Birincil kaynak önceliği

Sıra şudur: yayıncının kendi belgesi, yayıncının resmî katalog veya yayın kaydı, kurumun kendi açıklayıcı sayfası, olayı inceleyen ekibin birinci el yayını. Haber derlemesi, blog özeti ve ikinci elden aktarım tek dayanak yapılmaz.

Bir belgenin başka bir kurumun arşivinde bulunan kopyası kullanıldığında yayıncı değiştirilmez. Arşiv kurumu olayın araştırmacısı değildir; kaynak satırında bu ayrım yazılır.

Üretici sayfaları yalnızca kendi ürününün kavramsal tanımı için kullanılır. Pazarlama sayfasından üstünlük, performans veya güvenlik garantisi çıkarılmaz.

### Yayın tarihi ile erişim tarihi

Bir sayfanın görüntülendiği gün, belgenin yayımlandığı gün değildir. İki tarih ayrı yazılır.

- Adresteki yıl/ay klasörü yayın tarihi sayılmaz. Örneğin dağıtım tabanı raporunun adresinde 2025-01 geçer; belgenin tarihi Şubat 2024'tür ([kayıt](su-elektrik-kaynaklar.md)).
- Arama motorunun tarama veya dizinleme tarihi yayın tarihi sayılmaz.
- Belge içi tarih ile listeleme sayfasındaki tarih çakışırsa belge içi tarih esas alınır ve fark not edilir.
- Tarih belirlenemiyorsa "sayfada tarih belirtilmiyor" yazılır. Bu ifade, uydurulmuş bir tarihten iyidir.
- Sürümü olan belgelerde sürüm numarası tarihle birlikte verilir; sabit bir sürüm referansı "en yeni sürüm" diye sunulmaz.

### Taslak, nihai ve ikame ayrımı

Taslak yayın "taslak" olarak adlandırılır. Nihai sürüm çıkmışsa eski kaydın durumu yazılır: yerini aldı, geçerliliğini yitirdi, mülga. Örnek olarak eski bir NIST teknik not taslağının yerini nihai bir yayın almıştır; eski kayıt silinmeyip durumuyla birlikte tutulur ([kayıt](su-elektrik-kaynaklar.md)).

Bir yayın aşamasının adı da korunur. Taslak öncesi görüş çağrısı, indirilebilir taslak metni bulunan bir yayın değildir; bu ayrım [standartlar bölümünde](../docs/05-standartlar-ve-turkiye.md) açık yazılır.

### Ücretli ve lisanslı standartlar

Ücretli standartların tam metinlerine erişilmez, kopyalanmaz ve çevrilmez. Kullanılan bilgi, kamuya açık katalog kaydındaki kod, başlık, kapsam özeti, edisyon, tarih ve durum alanlarıyla sınırlıdır. Bu alanlardan madde bazında uygunluk veya gereksinim listesi çıkarılmaz.

Yayıncının kendi katalog sayfası açılamadığında aynı ortak yayının başka bir resmî katalog kaydı kullanılır ve hangi alanların görülemediği yazılır.

### Erişilemeyen kaynak

Erişim kısıtı gizlenmez. HTTP 403, 404 veya 500 yanıtı, bot koruması, istemci tarafında oluşturulan sayfa, çözümlenmeyen alan adı ve kesilen uzun metin kayda geçer. Sonra iki yoldan biri seçilir: ya kısıtı belirtilen bir ikame kaynak kullanılır ya da iddia hiç yazılmaz. Kısıtların toplu listesi [kaynak kataloğunun](../KAYNAKLAR.md) sonundadır.

### İkincil kaynağın kabul edildiği durumlar

İkincil bir kayıt şu üç koşulun birlikte sağlandığı durumda kullanılır: birincil sayfaya erişilememiştir, kayıt aynı resmî metnin dizinlenmiş veya arşivlenmiş hali gibi izlenebilir bir kopyadır ve yalnızca künye düzeyinde bilgi (başlık, sürüm, tarih, konu) alınmaktadır. Bu durumda kısıt ile kullanılan kopya kaynak satırında yazılır.

İkincil kaynak şunlar için kullanılmaz: bir olgunun tek dayanağı, sayı veya oran, olay atfı, yürürlük veya hukuki statü tespiti, bir ürünün özelliğinin sahada etkin olduğu iddiası.

## İddia sınıflandırması

Depodaki her cümle dört sınıftan birine girer. Sınıf, metnin kendisinde görünür.

| Sınıf | Metinde nasıl görünür | Örnek | Sınırı |
|---|---|---|---|
| (a) Kaynaklı olgu | İddianın yanında bağlantı, bölüm sonunda kaynak satırı | Modbus Security'nin TLS ve X.509 sertifikalarıyla tanımlanması: [endüstriyel protokoller](../docs/01-temeller/04-endustriyel-protokoller.md) | Kaynağın söylediğiyle sınırlıdır; bir üründe bu özelliğin bulunduğu veya etkin olduğu anlamına gelmez |
| (b) Kaynaklı olgudan türetilen yorum | Dayanak gösterilir, yorum olduğu cümlede belirtilir | Fonksiyonel emniyet standartlarının katalog kapsamında siber güvenliğin geçmemesinden hareketle SIL'in saldırı direncini ölçmediğinin yazılması: [standartlar ve Türkiye](../docs/05-standartlar-ve-turkiye.md) | Yorum kaynağın lafzı değildir; ters yönde genelleme de yapılmaz |
| (c) Deponun özgün eğitim sentezi | "Bu deponun özgün önerisi" veya "özgün eğitim sentezi" ibaresi | Laboratuvar verileri ve çözüm anahtarları ([laboratuvarlar](../labs/README.md)), şablonlar ([şablonlar](../templates/README.md)), [90 günlük yol haritası](../docs/04-savunma/06-90-gunluk-yol-haritasi.md) | Bir standardın resmî formu, çevirisi veya denetim ölçütü değildir |
| (d) Doğrulanamamış bilgi | **doğrulanacak** işareti ve araştırma kaydında ayrı madde | IEC 63452'nin yayın durumu; 2013 tarihli tebliğin güncel yürürlük durumu: [standartlar ve Türkiye](../docs/05-standartlar-ve-turkiye.md), [kayıt](standartlar-kaynaklar.md) | Açık bir iştir; kapandığında hem bölüm metni hem araştırma kaydı birlikte güncellenir |

Üç ek kural bu sınıflandırmayı ayakta tutar.

- Bir cümlede iki sınıf karışıyorsa cümle bölünür. Kaynaklı kısım ayrı, öneri ayrı yazılır.
- Sayı, oran, tarih ve olay atfı yalnızca (a) sınıfında olabilir. Kaynağı olmayan sayı yazılmaz.
- Bir özelliğin var olması ile o özelliğin doğru kurulmuş olması ayrı cümlelerdir; ikincisi tesis özelinde kanıt ister.

## Kullanılmayan ve sınırlandırılan iddialar

Her araştırma kaydının sonunda, o kaynaklardan çıkarılabilecek ama bilinçli olarak çıkarılmamış iddiaların listesi vardır. Bu bölüm üç işe yarar: okuyucu kaynağın nerede bittiğini görür, sonraki katkı veren mevcut atfı gereğinden geniş yorumlamaz, çözülmemiş soru görünür kalır.

Bu uygulamanın örnekleri:

- Bir bilgi notunun varlığı tehdit istatistiğine dönüştürülmedi ([su ve elektrik kaydı](su-elektrik-kaynaklar.md)).
- ETCS, ERTMS ve CBTC eş anlamlı sunulmadı; ürün ve uygulama farkları korundu ([raylı ve telekom kaydı](rayli-telekom-kaynaklar.md)).
- Bir denetim programının sonucu ürün veya üretici sertifikası gibi anlatılmadı ([raylı ve telekom kaydı](rayli-telekom-kaynaklar.md)).
- Vaka belgelerinde gözlenen etki, kurum değerlendirmesi ve belirsizlik ayrı tutuldu ([tehdit kaydı](tehdit-kaynaklar.md)).
- Mevzuatta çözülemeyen yetki ve yürürlük soruları "doğrulanamadı" olarak bırakıldı ([standartlar kaydı](standartlar-kaynaklar.md)).

Bir iddia kullanılmadıysa nedeni de yazılır: erişim kısıtı, kapsam dışılık, doğrulanamama veya bu deponun içerik sınırı.

## Kaynak tazeleme

Bu kayıt tek bir günün fotoğrafıdır. Bazı satırlar diğerlerinden hızlı eskir.

| Kaynak türü | Neden eskir | Neye bakılır |
|---|---|---|
| Mevzuat ve düzenlemeler | Yeni metin yayımlanır, bir hüküm mülga olur, kurum ve yetki dağılımı değişir | Konsolide metin, mülga şerhi, dayanak maddeleri, düzenleyicinin kendi mevzuat listesi |
| Standart sürümleri | Yeni edisyon, tashih, ulusal uyarlama farkı | Katalog kaydındaki edisyon, tarih, durum ve ikame alanları |
| Kurum sayfaları ve yayın dizinleri | Site yeniden düzenlenir, bağlantı kırılır, sayfa içeriği sessizce değişir | Bağlantının çalışması ve sayfanın hâlâ aynı iddiayı desteklemesi |
| Canlı matrisler ve kataloglar | İçerik sürekli güncellenir | İçerik sürümü, teknik sürümü ve son değişiklik alanı |
| Vaka analizleri | Sonraki resmî değerlendirmeler atfı veya ayrıntıyı değiştirebilir | Aynı olaya ilişkin daha yeni birincil yayın |
| "Doğrulanacak" satırları | Açık iş olarak bırakılmıştır | Sorunun kapanıp kapanmadığı |

Gözden geçirme önerisi, bu deponun özgün önerisidir: yılda en az bir kez tam tur; mevzuat ve canlı matris satırları için daha sık; ayrıca bir bölüm değiştirilecekse önce o bölümün kaynak satırları kontrol edilir.

Bir tazeleme turu şöyle yürütülebilir:

1. Yapısal denetimi çalıştırın: `python3 scripts/check_docs.py`. Bu betik göreli bağlantıları, kodlamayı, başlık ve tablo yapısını denetler; dış bağlantıların erişilebilirliğini denetlemez.
2. Kaynak kataloğundaki satırı açın ve yayıncının kendi kaydında sürüm, tarih ve durum alanlarını karşılaştırın.
3. Bir şey değişmişse üç dosyayı birlikte güncelleyin: bölüm metni, ilgili araştırma kaydı ve kaynak kataloğu. Gerekiyorsa [sözlük](../docs/06-sozluk.md) ve [değişiklik kaydı](../CHANGELOG.md) da güncellenir.
4. Eski kaydı silmeyin; durumunu yazın. "Yerini aldı" bilgisi, kaynağın neden değiştiğini sonraki okuyucuya anlatır.
5. Yenilenen satırın erişim tarihini yazın ve metindeki genel kesim tarihi ifadelerini gözden geçirin.
6. Kapanan bir "doğrulanacak" maddesini hem bölümden hem araştırma kaydından kaldırın; kapanmadıysa olduğu gibi bırakın.

## Etik ve kapsam sınırları

- Gerçek tesis verisi toplanmaz ve depoya taşınmaz: kurum veya saha adı, adres, koordinat, ağ adresi, ağ şeması, kontrol projesi, koruma ayarı, alarm eşiği, hesap bilgisi, ekran görüntüsü.
- Araştırma sırasında internete açık cihaz aranmaz, tarama veya sorgulama yapılmaz; böyle bir yöntem tarif edilmez. Bir kaynakta bu tür ayrıntı varsa eğitim metnine aktarılmaz.
- Saldırı prosedürü üretilmez. Saldırgan bakışı; hedef, ön koşul, aşılan güven sınırı, olası etki, gözlenebilir belirti ve karşılık gelen kontrol sütunlarıyla sınırlı kalır. Ön koşulun nasıl sağlanacağı yazılmaz.
- Vaka anlatımında doğrulanmış olgu, kurum değerlendirmesi ve belirsizlik ayrı tutulur. Gerçekleşmemiş zarar gerçekleşmiş gibi anlatılmaz; kaynağı olmayan atıf yapılmaz.
- Zafiyet bildirimi ve sorumluluk sınırları [güvenlik bildirimi](../SECURITY.md) dosyasındadır.

Sentetik veri üretme kuralları, bu deponun özgün uygulamasıdır:

- Veri kurgusaldır ve bulunduğu dosyada kurgusal olduğu yazılır.
- Gerçek bir olayın birebir kopyası üretilmez; kurum, marka ve saha adları kurgusaldır.
- Örnek ağ adresleri belgeleme için ayrılmış aralıklardan seçilir; gerçek bir kuruma ait adres kullanılmaz.
- Zaman damgaları, varlık kodları ve kimlikler kendi içinde tutarlı üretilir; alıştırma yalnızca verilen dosyalarla çözülebilmelidir.
- Veriye bilerek boşluk ve çelişki konur. "Veri yetersiz" sonucu da geçerli bir cevaptır.
- Üretilen dosya bir ürünün gerçek kayıt biçimi olarak sunulmaz; öğrenme hedefi ve değerlendirme ölçütüyle birlikte verilir ([laboratuvarlar](../labs/README.md)).

## Katkı verenler için kısa kontrol listesi

Aşağıdaki liste araştırma tarafına odaklanır. Biçim, dosya adlandırma ve gözden geçirme ölçütlerinin tamamı [katkı rehberindedir](../CONTRIBUTING.md).

- [ ] Kaynak, yayıncının kendi belgesi, katalog kaydı veya resmî sayfası mı?
- [ ] Yayın veya sürüm tarihi ile erişim tarihi ayrı yazıldı mı; tarih yoksa belirtilmediği söylendi mi?
- [ ] Taslak, nihai ve ikame durumu doğru mu?
- [ ] Ücretli standartta yalnızca katalog alanları mı kullanıldı?
- [ ] Erişim kısıtı varsa kısıt ve yerine ne yapıldığı yazıldı mı?
- [ ] İddianın sınıfı metinden anlaşılıyor mu: olgu, türetilen yorum, özgün sentez, doğrulanacak?
- [ ] Kullanılmayan veya sınırlandırılan iddia ilgili araştırma kaydına eklendi mi?
- [ ] [Kaynak kataloğuna](../KAYNAKLAR.md) satır eklendi veya mevcut satır güncellendi mi?
- [ ] Gerçek tesis verisi, komut, tarama adımı veya istismar ayrıntısı yok; örnekler kurgusal olarak işaretli mi?
- [ ] `python3 scripts/check_docs.py` hatasız çalışıyor mu?

## Bu yöntemin sınırları

- Depodaki araştırma tek bir çalışma kesitinde yürütüldü. Her kaynağın tam metni okunmadı; hangi bölümlerin okunduğu araştırma kayıtlarında yazılıdır.
- Kaynakların çoğu İngilizcedir. Türkçe resmî metinler dışında ulusal uyarlamalar ve TSE metinleri doğrulanmadı; bu uyarlamalarda farklı karşılıklar bulunması mümkündür.
- Ücretli metinlere erişilmedi; bazı sayfalar erişim kısıtları nedeniyle tam okunamadı. Bu iki sınır, standart ve mevzuat bölümlerindeki ayrıntı düzeyini doğrudan belirler.
- Otomatik denetim yapıyı kontrol eder, olguyu kontrol etmez. Kaynak ile iddianın eşleşmesi, çevirinin doğruluğu ve yorumun makullüğü insan incelemesi gerektirir.
- Sektör kapsamı dört alanla sınırlıdır; karşılaştırmalar bu dört alandan türetilmiştir ve başka sektörlere doğrudan genellenmez.
- Kurgusal örnekler öğretmek içindir. Bir tesisin risk değerlendirmesi, denetimi veya hukuki uygunluk görüşü yerine geçmez.

Bu dosya deponun özgün editoryal yöntemidir; bir standardın veya kılavuzun çevirisi değildir. Kurallar deneyimle güncellenir ve değişiklikler [değişiklik kaydına](../CHANGELOG.md) işlenir. Son gözden geçirme: 13.09.2026.
