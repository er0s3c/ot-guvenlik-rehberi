# Katkı rehberi

OT Güvenliği Rehberi, operasyonel teknolojiyi ve kritik altyapı güvenliğini Türkçe anlatan açık bir belge deposudur. Ürün değil, öğrenme ve başvuru metnidir. Bu dosya bir katkının hangi koşullarda birleştirilebilir sayıldığını açıklar: kaynak izlenebilirliği, içerik sınırları ve biçim tutarlılığı.

Katkı vermeden önce [ana sayfayı](README.md), [araştırma yöntemini](research/YONTEM.md) ve [kaynak kataloğunu](KAYNAKLAR.md) okumak yararlıdır.

## Kabul edilen katkı türleri

| Katkı türü | Örnek | Beklenen ek kanıt |
|---|---|---|
| Düzeltme | Hatalı terim, kopuk bağlantı, yanlış tarih, tutarsız tablo | Doğru bilgiyi gösteren birincil kaynak veya dosya içi tutarsızlığın gösterimi |
| Kaynak güncellemesi | Taslak bir yayının nihai sürümle değişmesi, adres değişikliği | Yeni bağlantı, yayın tarihi, erişim tarihi ve eski kaydın durumu |
| Çeviri terimi | Sözlükte karşılığı eksik veya tartışmalı bir terim | Terimi kullanan resmî veya standart kaynak; yoksa gerekçe notu |
| Yeni sektör bölümü | Mevcut dört sektörün dışında bir alan | Kaynak tablosu, güven sınırı çözümlemesi, tehdit modeli tablosu, kontrol listesi |
| Laboratuvar | Yeni çevrimdışı alıştırma ve çözüm anahtarı | Sentetik veri, öğrenme hedefi, değerlendirme ölçütü |
| Yapısal iyileştirme | Gezinme, tutarlılık, denetim betiği, şablon alanı | Değişikliğin etkilediği dosyaların listesi |

Küçük düzeltmeler için doğrudan değişiklik önerilebilir. Yeni bölüm, yeni laboratuvar veya yapısal değişiklik gibi geniş katkılarda önce konu açmak kapsam tartışmasını kolaylaştırır.

## Kaynak disiplini

Bu deponun temel kuralı şudur: her olgusal iddia ya bir kaynağa bağlanır ya da açıkça bu deponun özgün önerisi olarak işaretlenir.

- **Birincil kaynak esastır.** Yayıncının kendi belgesi, standardı veya resmî sayfası kullanılır. Haber derlemesi, blog özeti veya ikinci elden aktarım tek dayanak yapılmaz.
- **Yayın tarihi ile erişim tarihi ayrı yazılır.** Bir sayfanın görüntülenme günü, belgenin yayın günü değildir. Adresteki yıl/ay klasörü de yayın tarihi sayılmaz.
- **Tarih belirlenemiyorsa belirtilir.** "Sayfada tarih belirtilmiyor" ifadesi, uydurulmuş bir tarihten iyidir.
- **Taslak ile nihai sürüm ayrılır.** Taslak yayın "taslak" olarak adlandırılır; nihai sürüm çıktıysa eski kaydın durumu (yerini aldı, geçerliliğini yitirdi) yazılır.
- **Ücretli veya lisanslı standartların tam metni depoya kopyalanmaz.** Kapsam, amaç ve kamuya açık tanıtım bilgisi özetlenir; katalog kaydına bağlantı verilir.
- **İddia başına kaynak verilir.** Bölüm sonundaki toplu liste yeterli değildir; kaynak, iddianın yanında da görünmelidir.
- **Özgün içerik işaretlenir.** Matris, kontrol listesi, tatbikat kartı, mimari çizim ve ölçüt önerileri "bu deponun özgün önerisi" veya "özgün eğitim sentezi" olarak adlandırılır.
- **Belirsizlik gizlenmez.** Doğrulanamayan bilgi ya yazılmaz ya da doğrulanacak olarak işaretlenir. Kaynağı olmayan sayı, yüzde ve olay atfı kabul edilmez.

Kaynak satırı biçimi şu alanları içerir:

- [Yayıncı], *[belge adı]*, [sürüm veya yayın tarihi], [bağlantı], erişim: [GG.AA.YYYY]; [desteklediği iddia ve kapsam notu].

Araştırma notlarında ayrıca hangi bölümün okunduğu ve hangi iddianın bilinçli olarak **kullanılmadığı** yazılır. Bu ayrım, sonraki okuyucunun aynı kaynağı gereğinden geniş yorumlamasını önler.

## İçerik sınırları

Aşağıdakiler kabul edilmez:

- Gerçek tesis verisi: kurum veya saha adı, adres, koordinat, IP adresi, ağ şeması, kontrol projesi, koruma ayarı, alarm eşiği, hesap bilgisi, ekran görüntüsü.
- Çalıştırılabilir saldırı adımı, istismar kodu, yük (payload), tarama veya keşif komutu, araç kullanım prosedürü, cihaz sorgulama talimatı.
- Belirli bir ürün zafiyetinin istismar yolu veya "şu sürümde şu komutla" biçiminde ayrıntı.
- Doğrulanmamış olay atfı, isim vererek suçlama, kaynağı olmayan istatistik.
- Ürün tavsiyesi, pazarlama dili ve hizmet reklamı.

Saldırgan bakış açısı içeren katkılar tehdit modelleme düzeyinde kalır. Kullanılan tablo aşağıdaki örnek düzendedir. Sütun adları bölümden bölüme kısalabilir; değişmeyen şey bu altı bilginin her satırda bulunmasıdır:

| Hedef | Ön koşul | Aşılan güven sınırı | Olası hizmet/fiziksel etki | Gözlenebilir belirti | Karşılık gelen kontrol |
|---|---|---|---|---|---|
| [saldırganın amacı] | [mevcut kabul edilen erişim veya koşul] | [hangi varsayım bozuluyor] | [sonuç aralığı, kesinlik iddiası olmadan] | [savunmanın görebileceği iz] | [kontrol ve doğrulama kanıtı] |

Bütün örnekler kurgusaldır ve metinde kurgusal olduğu yazılır. Ön koşul mevcut kabul edilerek hangi denetimin eksik kalabileceği tartışılır; o ön koşulun nasıl sağlanacağı anlatılmaz.

## Üslup kılavuzu

- Dil Türkçe, cümleler kısa ve sade. Pazarlama dili, abartı ve ünlem kullanılmaz.
- "Mutlaka", "asla", "kesinlikle", "tamamen güvenli" gibi mutlak kalıplardan kaçınılır. Koşul ve kapsam yazılır.
- Bir özelliğin var olması ile etkin ve doğru kurulmuş olması ayrı ayrı ele alınır.
- Ölçütler verilirken paydası ve sınırı açıklanır; hedef değerlerin tesise özgü olduğu belirtilir.
- Terim ilk geçtiği yerde açıklanır; karşılıklar [sözlükte](docs/06-sozluk.md) tutulur.

Dosya ve başlık düzeni:

- Dosya adları küçük harf, Türkçe karakter içermez, kelimeler tire ile ayrılır ve sıralı dosyalarda iki haneli önek kullanılır: `04-endustriyel-protokoller.md`.
- Her dosyada tek bir H1 bulunur. Alt başlıklar cümle düzenindedir; başlık sırası atlanmaz.
- Dosya, "Kaynak" veya "Kaynaklar" bölümüyle ya da kapsam notuyla biter. Özgün içerik burada da belirtilir.
- Tablolar `|---|` ayraç satırı taşır. Kontrol listeleri `- [ ]` biçimindedir.
- Şablonlarda doldurulacak alanlar köşe parantezle gösterilir: `[varlık kodu]`.
- Kod blokları kapatılır, satır sonunda boşluk bırakılmaz, dosyalar UTF-8 kodlanır.
- Bağlantılar göreli yolla verilir ve hedef dosya depoda bulunmalıdır. Dış bağlantılar tam adres olarak yazılır.
- Mermaid diyagramı yalnızca anlatımı taşıdığında eklenir; süsleme amaçlı çizim eklenmez.

## Yerelde denetim

Değişiklik önermeden önce ağ bağlantısı gerektirmeyen belge denetimini çalıştırın:

```console
python3 scripts/check_docs.py
```

| Denetlenen | Denetlenmeyen |
|---|---|
| Göreli bağlantıların hedef dosyasının var olması | Dış bağlantıların erişilebilirliği ve içeriği |
| Dosyaların UTF-8 okunabilirliği | Olgusal doğruluk ve kaynak–iddia eşleşmesi |
| Kapatılmamış kod blokları | Üslup kuralları ve içerik sınırları |
| Temel Markdown yapı kuralları | Kurgusal örneklerin işaretlenmiş olması |

Betiğin güncel denetim kapsamı `scripts/check_docs.py` dosyasının kendi açıklamasında yazılıdır. Denetimden geçmek içeriğin doğru olduğunu göstermez; olgu ve kaynak incelemesi insan işidir.

## Katkı akışı

1. **Konu açın.** Hangi dosya, hangi sorun, hangi kaynak ve hangi kapsam? Geniş katkılarda bu adım önce yapılır.
2. **Dal açın.** Küçük harf ve tire kullanın; önek katkının türünü göstersin: `duzeltme/`, `kaynak/`, `bolum/`, `lab/`, `sablon/`, `yapi/`. Örnek: `kaynak/nist-sp1800-45-tarih`.
3. **Değişikliği yapın ve denetimi çalıştırın.** Etkilenen bağlantıları, sözlük girdilerini ve kaynak tablolarını birlikte güncelleyin.
4. **Commit mesajını biçimlendirin.** Başlık satırı `<alan>: <kısa özet>` düzeninde, etken ve kısa olsun. Örnek: `docs/02-sektorler: telekom bölümüne erişim tarihi eklendi`. Gövdede gerekçe ve kaynak bağlantısı yer alsın.
5. **Değişiklik isteği açın.** Neyin değiştiğini, hangi kaynağa dayandığını ve [değişiklik kaydına](CHANGELOG.md) önerdiğiniz girdiyi yazın.

### Gözden geçirme ölçütleri

- [ ] Her yeni olgusal iddia bir kaynağa bağlı veya özgün içerik olarak işaretlenmiş.
- [ ] Kaynak birincil; yayın tarihi ile erişim tarihi ayrı yazılmış.
- [ ] Taslak/nihai durumu ve sürüm bilgisi doğru.
- [ ] Göreli bağlantıların hedefi var; denetim betiği hatasız çalışıyor.
- [ ] Gerçek tesis verisi, komut, tarama adımı veya istismar ayrıntısı yok.
- [ ] Saldırı içeriği tehdit modelleme düzeyinde; örnekler kurgusal olarak işaretlenmiş.
- [ ] Mutlak ifade, pazarlama dili ve kaynaksız sayı yok; belirsizlikler açıkça yazılmış.
- [ ] Başlık, tablo, kontrol listesi ve dosya adlandırma kurallara uygun.
- [ ] Dosya kaynak bölümü veya kapsam notuyla bitiyor.
- [ ] Gerekiyorsa [kaynak kataloğu](KAYNAKLAR.md) ve [değişiklik kaydı](CHANGELOG.md) güncellendi.

Bir katkı bu ölçütlerin bir kısmını karşılamıyorsa reddedilmek yerine eksiklerin listesiyle geri döner.

## Davranış beklentisi

Eleştiri metne yöneliktir, kişiye değil. Yeni başlayanın sorusu bu deponun varlık nedenidir. Kaynağı olmayan bir iddianın geri çevrilmesi kişisel bir yargı değildir; deponun temel kuralıdır. Kişisel saldırı, taciz ve başkasına ait veriyi paylaşma kabul edilmez. Rahatsız edici bir durum için konu açabilir veya [güvenlik bildirimi](SECURITY.md) dosyasındaki özel bildirim yolunu kullanabilirsiniz.

## Katkı ve lisans

Katkı gönderildiğinde içeriğin depo lisansı altında yayımlanması kabul edilmiş olur: metin, diyagram, şablon ve sentetik veri için CC BY 4.0; `scripts/` altındaki kod için MIT. Ayrıntılar ve üçüncü taraf materyal sınırları [LICENSE.md](LICENSE.md) dosyasındadır. Başka bir eserden alınan içerik, kaynağı ve kullanım koşulu belirtilmeden eklenmez.

## Kapsam notu

Bu dosyadaki kurallar, deponun özgün editoryal politikasıdır; bir standardın veya kılavuzun çevirisi değildir. Kurallar deneyimle güncellenir; değişiklikler [değişiklik kaydına](CHANGELOG.md) işlenir. Son gözden geçirme: 13.09.2026.
