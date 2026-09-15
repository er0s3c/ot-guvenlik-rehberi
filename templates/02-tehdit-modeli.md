# Tehdit modeli şablonu

[Çalışma şablonları](README.md) · [Saldırgan bakış açısı](../docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md) · [MITRE ATT&CK for ICS](../docs/03-tehdit-modelleme/02-mitre-attack-ics.md)

Bu şablon, bir sistemin, yeni bir bağlantının veya değişen bir erişim yolunun tehdit modelini yazılı bir kayda dönüştürmek içindir. Çıktı; hangi güven varsayımının hangi kanıta dayandığını, o varsayım yanlış çıkarsa hangi işlevin etkilenebileceğini ve bunu ne ile fark edebileceğimizi gösterir. Bir denetim raporu, uygunluk beyanı veya güvence belgesi yerine geçmez. Şablonun tamamı bu deponun özgün eğitim sentezidir.

Doldurma disiplini, güven düzeyi ölçeği ve hassas alanların nasıl referansla taşınacağı [şablon dizininin giriş sayfasında](README.md) tanımlıdır. Girdi olarak [envanter ve akış şablonu](01-envanter-ve-akis.md) kullanılır; çıktı çoğunlukla [algılama kartına](03-algilama-karti.md), [olay ve kurtarma kaydına](04-olay-ve-kurtarma.md) ve [tedarikçi/uzak erişim kaydına](06-tedarikci-ve-uzak-erisim.md) bağlanır.

**Kapsam sınırı.** Bu şablon tehdit modelleme düzeyinde kalır: hedef, ön koşul, aşılan güven sınırı, hizmet etkisi, emniyet sisteminin rolü, gözlenebilir belirti ve karşılık gelen kontrol yazılır. Araç adı, komut, tarama yöntemi, ürün açıklığının istismar yolu veya adım adım saldırı tarifi yazılmaz. Bu ayrıntılar savunma kaydının işine yaramaz ve doldurulmuş kopyanın hassasiyetini gereksiz yere artırır. Kurgusal örneklerdeki tesis, saha, hesap ve varlık adları uydurmadır.

## 1. Korunacak işlevle başlama

Modelleme bir cihaz listesiyle değil, sürdürülmesi gereken işlevle başlar. "Tesisin ağı" incelenemeyecek kadar geniştir; "depo seviyesinin güvenilir biçimde izlenmesi ve pompa işletmesinin sürekliliği" incelenebilir bir işlevdir. Bu ayrım [saldırgan bakış açısı bölümünde](../docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md) ayrıntılı anlatılır.

İşlev tanımlanırken iki farklı bozulma biçimi ayrı yazılır. **Kayıp**, işlevin durmasıdır ve genellikle fark edilir. **Bozulma**, işlevin çalışıyor görünüp güvenilmez sonuç üretmesidir; fark edilmesi bağımsız bir kanıt ister. Savunma tasarımını çoğunlukla ikinci durum zorlar.

| Alan | Ne yazılır? | Kim doğrular? |
|---|---|---|
| İşlev kimliği ve tanımı | Hangi hizmet, hangi sahada, hangi çalışma modunda sürdürülüyor | İşletme ve süreç sorumlusu |
| İşlevin kaybı | İşlev durduğunda ne olur; ne kadar sürede fark edilir | Vardiya ve süreç sorumlusu |
| İşlevin bozulması | İşlev çalışıyor görünürken güvenilmez sonuç nasıl ortaya çıkar | Süreç mühendisi |
| Kabul edilemez sonuç | Hangi sonuç işletme, emniyet, çevre veya hizmet açısından kabul edilmiyor | İşletme yönetimi ve ilgili uzmanlık |
| İlgili emniyet işlevi | Bağımsız koruma veya emniyet işlevi var mı; neyi kapsıyor, neyi kapsamıyor | Emniyet/koruma sorumlusu |
| Bağımsız doğrulama | İşlevin gerçek durumu dijital gösterimden bağımsız olarak nasıl teyit edilir | Saha ve laboratuvar/ölçüm sorumlusu |
| Kabul edilebilir kesinti | Hangi süre sonunda alternatif işletme veya bildirim gerekir | İşletme yönetimi |

Kopyalanacak alan:

- İşlev kimliği: [ISL-01]
- İşlev tanımı: [hangi hizmet, hangi saha, hangi çalışma modu]
- Kaybı ne demek: [gözlenebilir sonuç ve fark edilme süresi]
- Bozulması ne demek: [sessiz hata biçimi ve fark edilme yolu]
- Kabul edilemez sonuç: [işletme/emniyet/çevre/hizmet ifadesiyle]
- İlgili emniyet işlevi: [var/yok; kapsadığı ve kapsamadığı durum]
- Bağımsız doğrulama: [yöntem, sorumlu rol, kayıt kimliği]
- İşlev sahibi rolü: [rol]
- Kaynak ve doğrulama tarihi: [belge/kayıt/görüşme, YYYY-AA-GG]

Emniyet işlevinin bulunması, senaryonun sonucunu kendiliğinden ortadan kaldırmaz. Kapsamı, devrede olduğu çalışma modları ve son işlev testinin tarihi yazılmazsa "koruma var" ifadesi kanıt sayılmaz.

## 2. Güven sınırı envanteri

Güven sınırı, farklı yetki veya güven varsayımlarının karşılaştığı yerdir. Kurumsal ağ ile OT bölgesi arasındaki geçiş kadar, aynı saha içinde operatör hesabından mühendislik yetkisine geçiş de sınırdır. Bölge ve geçiş kavramları için [mimari ve güven bölgeleri](../docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) bölümüne bakılabilir.

| Sınır kimliği | Taraf A | Taraf B | Sınırda varsayılan güven | Doğrulama kanıtı | Doğrulama tarihi ve güven düzeyi |
|---|---|---|---|---|---|
| [GS-01] | [bölge/rol] | [bölge/rol] | [A tarafının B üzerinde neye yetkili sayıldığı] | [izin listesi, yapılandırma incelemesi, gözlenen akış, kabul testi] | [YYYY-AA-GG; doğrulandı / belgeye dayanıyor / tahmin] |

Doldururken dikkat edilecekler:

- "Varsayılan güven" alanına tasarım niyeti değil, **bugün geçerli olan yetki** yazılır. İkisi farklıysa fark bir iş listesine alınır.
- Mimari çizimde bir güvenlik duvarı bulunması ayrım kanıtı değildir. Kanıt; izinlerin sahibi, gerekçesi ve gözlenen kullanımdır.
- Tek yönlü sanılan akışların dönüş trafiği ve yönetim yolu ayrıca incelenir.
- Aynı sistemden türetilmiş iki kayıt bağımsız kanıt sayılmaz.
- Kanıt bulunamayan sınır silinmez; `doğrulanacak` işaretiyle, sorumlu rol ve hedef tarihle bırakılır.

## 3. Senaryo kartı

Her senaryo ayrı bir kart olarak doldurulur. Kart, bir olayın gerçekleştiğini değil, bir varsayımın yanlış çıkması hâlinde ne olabileceğini anlatır.

- **Senaryo kimliği:** [TM-XXX-01]
- **Korunan işlev:** [ISL-01 ve kısa adı]
- **Saldırganın amacı:** [ne elde etmeye çalışıyor; hangi sonucu istiyor]
- **Gereken ön koşullar**
  - Erişim: [hangi bağlantı, hesap veya bakım ilişkisi güvenilir kabul ediliyor]
  - Bilgi: [hangi işlev, yapılandırma veya süreç bilgisi gerekiyor]
  - Zaman: [hangi pencere, vardiya veya işletme modu gerekiyor]
  - Fiziksel: [saha erişimi, pano/kabin, geçici cihaz gerekiyor mu]
- **Geçilen güven sınırları:** [GS-01 → GS-03 sırasıyla]
- **Beklenen hizmet etkisi:** [görünürlük kaybı / kontrol etkisi / hizmet etkisi / kalite etkisi; hangisi gözlenir, hangisi çıkarım]
- **Emniyet sisteminin rolü:** [bağımsız koruma neyi sınırlar, hangi modda devrede, neyi kapsamaz]
- **Gözlenebilir belirtiler**
  - Süreç: [ölçüm, kalite bayrağı, alarm davranışı]
  - Ağ: [yeni iletişim çifti, akış kesilmesi, yönetim oturumu]
  - Kimlik: [oturum zamanı, hedef, yetki kullanımı]
  - Saha: [yerel gösterge, fiziksel durum, personel gözlemi]
- **Aynı belirtiyi üreten normal işletme durumları:** [planlı bakım, devreye alma, mevsimsel işletme, arıza, cihaz değişimi]
- **Mevcut kontroller ve kanıtları:** [kontrol → kanıt türü → doğrulama tarihi → güven düzeyi]
- **Artık risk:** [kontroller uygulandıktan sonra açık kalan kısım ve kabul eden rol]
- **Davranış etiketi (ATT&CK):** [alan ve teknik kimliği; kanıt desteklemiyorsa boş]
- **Bağlı algılama kartı:** [ALG-XX kimliği veya `yok`]
- **Sahibi:** [rol]
- **Gözden geçirme tarihi:** [YYYY-AA-GG]

"Beklenen hizmet etkisi" alanında gözlem ile çıkarım ayrılır. Ekrandaki olağandışı değer bir gözlemdir; bağımsız ölçüm yokken sürecin bozulduğunu söylemek çıkarımdır ve ayrıca kanıt ister. "Artık risk" alanı boş bırakılırsa kartın kontrol listesi gibi okunma olasılığı artar.

## 4. Önceliklendirme: en zayıf kanıtla ayakta duran varsayım

Yaygın yöntem, etki ile uygulanabilirliği çarpıp bir sayı üretmektir. Bu şablon farklı bir sıralama önerir: **hangi varsayım en zayıf kanıtla ayakta duruyor?** Bu sorunun yanıtı hem bir iyileştirme işi hem de bir kanıt toplama işi üretir; ikisi de doğrulanabilir. Bu, bu deponun özgün önerisidir.

| Varsayım | Varsayımı taşıyan kontrol | Kanıtın kaynağı | Kanıt yaşı | Güven düzeyi | Varsayım yanlışsa ilk etkilenen işlev | Kanıt üretecek iş ve sahibi |
|---|---|---|---|---|---|---|
| [yazılı varsayım] | [kontrol] | [belge/kayıt/gözlem/test] | [gün veya ay] | [doğrulandı / belgeye dayanıyor / tahmin] | [ISL-XX] | [iş, rol, hedef tarih] |

Sıralama kuralı olarak şu üçlü kullanılabilir: önce **kritik işlevi taşıyan ve kanıtı `tahmin` olan** varsayımlar, sonra **kanıtı eski olanlar**, sonra **kanıtı tek kaynaktan gelenler**. Bu bir puan değil, bir çalışma sırasıdır.

Puanlama kullanılacaksa sahte kesinlik riski kayda yazılır. Beş kademeli iki eksenin çarpımı, girdilerin kendisi tahmine dayanıyorken sonuca kesinlik görüntüsü verir. Aynı senaryoyu iki ekip puanlayınca farklı sonuç çıkması olağandır. Puan kullanılıyorsa ölçek, girdiler ve puanlayan rol yazılır; puan bir karar gerekçesi değil, tartışmayı başlatan bir sıralama aracı olarak tutulur. Risk değerlendirmesinin ayrı girdiler gerektirdiği [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) çerçevesinde de ele alınır.

## 5. Kurgusal doldurulmuş örnek: su tesisi

Aşağıdaki kart **tamamen kurgusaldır**. Yeşilova terfi merkezi, hesaplar ve iş emri numaraları uydurmadır; [çevrimdışı kayıt analizi laboratuvarındaki](../labs/01-kayit-analizi.md) sentetik ortamla aynı adları kullanır.

- **Senaryo kimliği:** TM-SU-01
- **Korunan işlev:** ISL-01 — Kurgusal TERFI-02 noktasında pompa işletmesinin onaylı kontrol mantığıyla sürmesi
- **Saldırganın amacı:** Bakım için verilmiş yetkiyi, onaylı kapsamın dışında bir yapılandırma değişikliği için kullanmak
- **Gereken ön koşullar**
  - Erişim: Erişim geçidi üzerinden açılabilen, tedarikçiye ait geçerli bir oturum
  - Bilgi: Hangi kontrolörün hangi terfi noktasına hizmet ettiği ve onaylı proje sürümünün adı
  - Zaman: Onaylı bakım penceresinin bitişine yakın ya da sonrasındaki düşük gözetim aralığı
  - Fiziksel: Gerekmiyor; senaryo uzak oturum üzerinden kurgulanmıştır
- **Geçilen güven sınırları:** GS-02 (tedarikçi ortamı → erişim geçidi) → GS-04 (geçit → mühendislik bölgesi) → GS-06 (mühendislik yetkisi → kontrolör)
- **Beklenen hizmet etkisi:** İlk sırada kontrol güvenilirliğinin kaybı ve işletim kısıtı. Hizmet kesintisi bu kartta bir çıkarımdır; pompa koordinasyonu ve depo kapasitesi bilinmeden kesinleştirilemez
- **Emniyet sisteminin rolü:** Kuru çalışma ve aşırı basınç için bağımsız koruma devrede sayılmıştır; kapsamı ekipman korumasıdır, hizmet sürekliliği veya veri güvenilirliği değildir. Son işlev testi tarihi `doğrulanacak`
- **Gözlenebilir belirtiler**
  - Süreç: Pompa çalışma biçiminin onaylı işletme niyetiyle uyuşmaması
  - Ağ: Mühendislik bölgesinden kontrolöre, bakım penceresi dışında oluşan trafik
  - Kimlik: İş emrine bağlanmayan oturum; onaylı pencere sonrasında süren oturum
  - Saha: Yerel gösterge ile merkez ekranının farklı davranması
- **Aynı belirtiyi üreten normal işletme durumları:** Onaylı acil bakım, pencere uzatma onayı, devreye alma sonrası ayar düzeltmesi, tedarikçinin ikinci bir iş emriyle çalışması
- **Mevcut kontroller ve kanıtları:** Kişisel hesap ve çok faktörlü doğrulama → geçit yapılandırma incelemesi → 2026-02-18 → doğrulandı. Oturumun iş emrine bağlanması → süreç belgesi → 2026-01-30 → belgeye dayanıyor. Proje değişikliğinde ikinci kişi incelemesi → görüşme → 2026-03-02 → tahmin
- **Artık risk:** İkinci kişi incelemesinin uygulandığı kanıtlanamıyor; pencere sonrası süren oturumlar için otomatik sonlandırma yok. Kabul eden rol: OT işletme sorumlusu, gözden geçirme ile
- **Davranış etiketi (ATT&CK):** ICS — [T0822 External Remote Services](https://attack.mitre.org/techniques/T0822/), [T0859 Valid Accounts](https://attack.mitre.org/techniques/T0859/); okundu: 2026-09-13. Program aktarımı kanıtı bulunursa [T0843 Program Download](https://attack.mitre.org/techniques/T0843/) ayrıca değerlendirilir
- **Bağlı algılama kartı:** ALG-01
- **Sahibi:** OT güvenlik sorumlusu (süreç mühendisiyle birlikte)
- **Gözden geçirme tarihi:** 2026-09-30

Sektör bağlamı için [su ve atıksu bölümü](../docs/02-sektorler/01-su-ve-atiksu.md) okunabilir.

## 6. Kurgusal doldurulmuş örnek: telekom saha desteği

Aşağıdaki kart **tamamen kurgusaldır**. Kavakdere sahası ve kurgusal operatör uydurmadır; gerçek bir saha, koordinat veya yönetim topolojisi anlatmaz.

- **Senaryo kimliği:** TM-TLK-01
- **Korunan işlev:** ISL-07 — Kurgusal Kavakdere sahasında enerji ve soğutma durumunun merkezden güvenilir biçimde izlenmesi
- **Saldırganın amacı:** Sahanın gerçek fiziksel durumunu merkezden gizlemek; arızanın geç fark edilmesini sağlamak
- **Gereken ön koşullar**
  - Erişim: Saha destek sistemlerinin izleme verisine etki edebilecek bir yönetim yolu
  - Bilgi: Hangi ölçümün merkez kararını beslediği ve hangi eşiğin bildirim ürettiği
  - Zaman: Saha ziyaretinin seyrek olduğu dönem; tek başına yeterli değildir
  - Fiziksel: Gerekmiyor; senaryo yönetim düzlemi üzerinden kurgulanmıştır
- **Geçilen güven sınırları:** GS-11 (yönetim ağı → saha OT denetleyicisi) → GS-12 (yerel sensör → merkez izleme kararı)
- **Beklenen hizmet etkisi:** Doğrudan kullanıcı hizmeti etkisi beklenmez. Etki, gerçek bir enerji veya soğutma sorunu oluştuğunda müdahalenin gecikmesidir. Bu bir koşullu etkidir ve tek başına gözlenmez
- **Emniyet sisteminin rolü:** Yerel aşırı sıcaklık ve batarya koruması bağımsız kabul edilmiştir; ekipmanı korur, merkez görünürlüğünü geri getirmez. Yerel korumanın merkeze ayrı bir yoldan bildirim yapıp yapmadığı `doğrulanacak`
- **Gözlenebilir belirtiler**
  - Süreç: Sıcaklık veya batarya değerinin uzun süre hiç değişmemesi; zaman damgasının ilerlememesi
  - Ağ: Saha denetleyicisinden merkeze akan izleme verisinin kesilmesi veya beklenmeyen kaynaktan gelmesi
  - Kimlik: Saha izleme ile şebeke yönetimi yetkilerinin aynı kimlikte birleşmesi
  - Saha: Yerinde okunan değerin merkez değerinden farklı olması
- **Aynı belirtiyi üreten normal işletme durumları:** Toplayıcı arızası, taşıma kesintisi, sensör arızası, yazılım güncellemesi sonrası donmuş değer, ölçüm çözünürlüğünün düşük olması
- **Mevcut kontroller ve kanıtları:** Veri tazeliği alarmı → izleme yapılandırması → 2026-04-11 → belgeye dayanıyor. Saha ziyaretlerinde bağımsız okuma → bakım kaydı → 2026-05-20 → doğrulandı. Şebeke ve saha OT yetkilerinin ayrılması → erişim incelemesi → tarih yok → `doğrulanacak`
- **Artık risk:** Ortak kimlik varsayımı kanıtlanmamış durumda; kanıt üretilene kadar iki alanın ayrı olduğu kabul edilmiyor. Kabul eden rol: saha operasyon sorumlusu
- **Davranış etiketi (ATT&CK):** ICS — [T0832 Manipulation of View](https://attack.mitre.org/techniques/T0832/); okundu: 2026-09-13
- **Bağlı algılama kartı:** ALG-02
- **Sahibi:** Saha OT sorumlusu (NOC temsilcisiyle birlikte)
- **Gözden geçirme tarihi:** 2026-10-15

Sektör bağlamı için [telekom ve baz istasyonları bölümü](../docs/02-sektorler/04-telekom-ve-baz-istasyonlari.md) okunabilir.

## 7. ATT&CK kimliği nereye yazılır?

Teknik kimliği, senaryo kartının **davranış etiketi** alanına yazılır; ayrı bir bölüm gerektirmez. Alan doldurulurken üç bilgi birlikte verilir: hangi alan (Enterprise veya ICS), teknik kimliği ve adı, kimliğin okunduğu tarih. Eşleştirme tablosu [MITRE ATT&CK for ICS bölümündedir](../docs/03-tehdit-modelleme/02-mitre-attack-ics.md).

Sınırlar:

- **Teknik kimliği risk önceliği belirlemez.** Kimlik bir davranışı adlandırır; hizmetin önemini, senaryonun olasılığını, kontrollerin gücünü veya iyileştirme sırasını hesaplamaz. Öncelik, bölüm 4'teki kanıt değerlendirmesinden çıkar.
- Bir kartta birden çok kimlik bulunabilir; kimlik sayısı ciddiyet göstergesi değildir.
- Alt teknik yalnızca eldeki kanıt bu ayrımı destekliyorsa yazılır.
- Kanıt yoksa alan boş bırakılır. Eşleştirme zorlanırsa kart, gerçekte incelenmemiş bir davranışı incelenmiş gibi gösterir.
- Kimlikten aktör veya kampanya çıkarımı yapılmaz.

## 8. Gözden geçirme kontrol listesi

- [ ] Her kart bir korunan işleve bağlı; işlev kaybı ile bozulması ayrı yazılmış.
- [ ] Güven sınırı envanterindeki her satırın kanıtı ve doğrulama tarihi var.
- [ ] Ön koşullar erişim, bilgi, zaman ve fiziksel başlıklarıyla ayrı ayrı doldurulmuş.
- [ ] Hizmet etkisinde gözlem ile çıkarım ayrılmış.
- [ ] Emniyet işlevinin kapsamadığı durumlar da yazılmış.
- [ ] Her belirtinin en az bir normal işletme açıklaması listelenmiş.
- [ ] Kontrollerin yanında kanıt türü, tarihi ve güven düzeyi bulunuyor.
- [ ] Artık riskin kabul eden rolü belli.
- [ ] Kanıtı `tahmin` olan varsayımlar için kanıt üretecek iş ve hedef tarih tanımlı.
- [ ] Kartlarda araç adı, komut veya istismar ayrıntısı yok.
- [ ] Hassas bilgi yerine kurum içi kayıt kimliği kullanılmış.
- [ ] Sahibi ve gözden geçirme tarihi güncel.

## Kaynaklar ve kapsam

Bu şablonun yapısı, alanları, önceliklendirme yaklaşımı ve iki kurgusal örneği bu deponun **özgün eğitim sentezidir**; belirli bir standardın resmî formu veya çevirisi değildir. Aşağıdaki kaynaklar yalnızca belirtilen kavramsal dayanaklar için kullanılmıştır. Erişim: **13.09.2026**.

| Yayıncı ve kaynak | Tarih | Desteklediği içerik |
|---|---|---|
| NIST, [SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Eylül 2012 | Tehdit, zafiyet, ön koşul ve etkinin ayrı değerlendirilmesi; risk değerlendirmesinin ayrı girdiler istemesi |
| NIST, [SP 800-82 Rev. 3: Guide to Operational Technology Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Eylül 2023 | OT güvenliğinin performans, güvenilirlik ve emniyet gereksinimleriyle birlikte ele alınması |
| MITRE, [ATT&CK for ICS Matrix](https://attack.mitre.org/matrices/ics/) | Yaşayan sayfa | Davranış etiketi alanında kullanılan teknik kimlikleri ve adları |

Örneklerde geçen tesis, saha, hesap, iş emri ve varlık adları kurgusaldır. Kartlar bir tesisin gerçek tasarımını, koruma ayarını veya erişim yapısını temsil etmez ve bir güvenlik değerlendirmesinin yerine geçmez.

**İlgili şablonlar:** [Envanter ve akış](01-envanter-ve-akis.md) · [Algılama kartı](03-algilama-karti.md) · [Olay ve kurtarma](04-olay-ve-kurtarma.md)
