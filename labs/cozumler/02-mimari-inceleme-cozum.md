# Laboratuvar 2 çözümü: mimari inceleme

[Laboratuvarlar](../README.md) · [Laboratuvar metni](../02-mimari-inceleme.md) · [Ana sayfa](../../README.md)

Bu dosya, kurgusal Karaova Elektrik Dağıtım mimarisine bilerek yerleştirilen kusurların beklenen tespitlerini, öncelik gerekçelerini ve değerlendirme ölçeğini içerir. Kendi cevabınızı yazmadan önce okumayın.

Burada da saldırı prosedürü, araç adı veya komut bulunmaz. İncelenen şey tasarım kararlarıdır. “Mümkün hale gelir” ifadeleri olasılık değerlendirmesidir; kurgusal tasarımda başka korumaların bulunmadığı varsayımıyla yazılmıştır ve gerçek bir tesis için kesin sonuç olarak okunmamalıdır.

## 1. Beklenen tespitler

Kusur kodları bu çözüm dosyasına aittir; laboratuvar metninde verilmemiştir. Öğrencinin aynı kodları kullanması beklenmez, aynı olguyu bulması beklenir.

| Kod | Kusur | Bozulan güven varsayımı | Beklenen tespit ve hizmet etkisi | Gözlenebilir belirti |
|---|---|---|---|---|
| K1 | MI-01 mühendislik istasyonunun iki ağ arayüzü var | “Kontrol bölgesine yalnızca denetimli bir geçişten girilir” | İstasyonun kendisi bir geçiş haline gelir; kurumsal ağdan gelen bir etki, denetim noktalarını kullanmadan kontrol bölgesindeki yapılandırma yetkisine ulaşabilir. Etki, RTU yapılandırmasının güvenilirliğinin kaybı | İstasyonda iki arayüzün eşzamanlı etkin olması; kurumsal kaynaklara erişim kaydıyla kontrol bölgesi oturumlarının aynı makinede örtüşmesi |
| K2 | AD-KARAOVA tek dizin; OT hesapları kurumsal yapıda ve IT yönetiminde | “Kurumsal kimlik olayı proses gözetimini etkilemez” | Kimlik altyapısındaki bir sorun hem kurumsal hizmeti hem operatör oturumlarını aynı anda etkiler. Etki, vardiyanın ekrana erişememesi ve yetki kararlarının tek noktadan yönetilmesi | Kimlik hizmeti kesildiğinde HMI oturum açma hatalarının toplu görülmesi; OT yetki değişikliklerinin IT değişiklik kayıtlarında yer alması |
| K3 | Aksu Otomasyon için YON-01'de sonlanan kalıcı tünel; kullanımı için ayrı onay istenmiyor | “Tedarikçi erişimi bir iş emrine ve süreye bağlıdır” | Erişim, bakım ihtiyacı olmadığı zamanlarda da açık kalır ve GEC-01'in doğrulama, onay ve kayıt kapısını kullanmaz. Etki, sahadaki değişikliklerin kime ait olduğunun gösterilememesi | Tedarikçi kaynaklı trafiğin GEC-01 oturum kayıtlarında karşılığının bulunmaması; iş emri olmayan zaman aralıklarında saha bağlantısı |
| K4 | HIS-DMZ, HIS-01'e kendisi bağlanıp veri çekiyor | “DMZ'deki bir bileşen kontrol bölgesinde oturum başlatamaz” | Daha düşük güvenli bölgeden yüksek güvenli bölgeye doğru kalıcı bir izin oluşur; DMZ bileşeni bozulursa bu izin devralınır. Etki, historian verisinin ve kontrol bölgesi erişiminin bütünlüğü | Güvenlik duvarında DMZ kaynaklı ve kontrol bölgesi hedefli kalıcı izin satırı; HIS-01 tarafında dışarıdan başlatılan oturumlar |
| K5 | YON-01'in web yönetim arayüzü genel internetten erişilebilir | “Saha haberleşmesinin yönetimi yalnızca iç ağdan yapılır” | Sahaların toplandığı tek noktanın yönetimi, kurumun bütün erişim kapılarının dışında bir yüzeye sahip olur. Etki, telekontrol ve telemetrinin sürekliliği | Bilinmeyen kaynaklardan yönetim arayüzüne erişim denemeleri; yapılandırma değişikliği kaydının iç değişiklik kayıtlarıyla eşleşmemesi |
| K6 | YED-01 yedekleri yalnızca kontrol merkezinde tutuluyor | “Kurtarma kaynağı, kurtarılacak ortamdan bağımsızdır” | Kontrol merkezini etkileyen bir olay yedekleri de kapsayabilir. Etki, geri dönüşün uzaması; röle ayar dosyalarının tek kopya olması nedeniyle saha onarımının da gecikmesi | Yedek kopyanın ikinci bir konumda bulunmaması; geri yükleme denemesinin kayıtlarda görünmemesi |
| K7 | ZAM-01 tek zaman kaynağı; merkez ve bütün RTU'lar buradan besleniyor | “Olay sırası bağımsız olarak doğrulanabilir” | Zaman kaynağı bozulur veya kayarsa bütün kayıtlar aynı yönde hatalı olur ve hata fark edilmez. Etki, arıza ve olay analizinin yanlış yorumlanması, geri dönüş kararının gecikmesi | Cihazlar arası sapmanın izlenmemesi; olay sıralarının bağımsız bir ölçümle çelişmesi |
| K8 | Kuzey saha segmenti ve YON-01 kayıt toplama kapsamında değil | “Elimizdeki kayıtlar tesisin tamamını temsil eder” | Kırk sahanın yarısı için kanıt üretilmez; kuzeydeki bir olay merkezî analizde görünmez. Etki, olay kapsamının belirlenememesi ve diğer bulguların doğrulanamaması | KAY-01 kaynak listesinde eksik segment; kuzey sahalarda yalnızca yerel kayıt bulunması |
| K9 | Yedek haberleşme yolu aynı YON-01'de sonlanıyor ve aynı yönetim hesabıyla yönetiliyor | “Yedek yol ana yoldan bağımsızdır” | Yedeklilik cihaz ve yönetim düzeyinde ortadan kalkar; tek bir yapılandırma hatası iki yolu birden etkiler. Etki, saha görünürlüğünün topluca kaybı | Yol değiştirme testinin yapılmamış olması; iki yolun aynı yapılandırma kaydında yönetilmesi |

### Ek olarak kabul edilen bulgular

Aşağıdakiler laboratuvarın hedeflediği dokuz kusurun dışındadır; bulunması cevabı güçlendirir.

- MI-01'den RTU-11..RTU-20'ye doğrudan yapılandırma yolu var; araya değişiklik onayı veya kabul kapısı yerleştirilmemiş.
- GEC-01 için çok faktörlü doğrulama ve oturum kaydı belirtilmiş, ancak oturumun bir iş emriyle eşleştirildiği yazılmamış. Kayıt tek başına yetkinin gerekçesini göstermez.
- Kuzey sahaların devralınmış olması, envanter ve sahiplik bilgisinin de farklı olabileceğine işaret eder; proje dosyası bu segmentin sahibini yazmıyor.
- Röle ayar dosyaları ile SCADA yedeği aynı depoda; kurtarma sırasında farklı onay sahipleri gerekmesine rağmen erişim ayrımı belirtilmemiş.
- Proje dosyasında kabul veya test ortamı görünmüyor; kabul kanıtlarının nerede üretileceği belirsiz.

## 2. Önceliklendirme gerekçesi

Aşağıdaki sıralama bu deponun önerisidir. Farklı ama gerekçeli bir sıralama da geçerli sayılır; değerlendirmede aranan şey gerekçenin kanıta bağlanmasıdır.

| Sıra | Kusur | Neden burada? |
|---|---|---|
| 1 | K8 kayıt kapsamı | Diğer bütün bulguların doğrulanması buna bağlı. Kapsam genişletilmeden “düzeldi” denemez. Düzeltme kontrol mantığına dokunmaz, bu nedenle erken yapılabilir |
| 2 | K5 internete açık yönetim arayüzü | Ön koşulu en geniş olan tasarım kararı; tek noktada bütün sahaları etkileyebiliyor. Erişimin kaynağa göre sınırlanması görece kısa sürede planlanabilir |
| 3 | K3 kalıcı tedarikçi tüneli | Sürekli açık ve kanıtsız bir yetki. Düzeltme sözleşme ve çalışma düzeni değişikliği gerektirdiği için erken başlatılmalı; tedarikçiyle birlikte planlanır |
| 4 | K1 çift bacaklı mühendislik istasyonu | Kontrol bölgesinin en yetkili istasyonu aynı zamanda bir geçiş. Düzeltme lisans ve dosya akışlarının yeniden tasarlanmasını gerektirir |
| 5 | K4 DMZ'den kontrol bölgesine başlatılan bağlantı | Yön değişikliği kalıcı bir izni ortadan kaldırır. Raporlama kesintisi riski nedeniyle planlı pencere ister |
| 6 | K2 ortak kimlik dizini | Etkisi geniş, ancak düzeltme uzun soluklu. Ara adım olarak OT yönetim hesaplarının ayrılması ve acil erişim yolunun tanımlanması önerilir |
| 7 | K6 yedeklerin tek konumda olması | Olayın başlangıcını değil süresini belirler. Düzeltme teknik olarak sade; sınama yapılmadan tamamlanmış sayılmaz |
| 8 | K7 tek zaman kaynağı | Analiz ve kurtarma kalitesini etkiler. Düzeltme koruma ve telekontrol açısından değerlendirme gerektirdiği için plana bağlanır |
| 9 | K9 yedek yolun ortak noktası | Yedekliliğin gerçek olup olmadığını gösterir. Düzeltme haberleşme tasarımı ve saha ziyareti ister |

**Savunulabilir alternatif:** K6'yı ilk üçe almak da gerekçelendirilebilir. Kurtarma kaynağı kaybedilirse diğer düzeltmeler olayın süresini kısaltmakta sınırlı kalır. Bu tercih yazıldığı sürece düşük puan almaz.

**Savunulması güç tercih:** K7 ve K6'yı listenin dışında bırakmak. İkisi de olayın başlamasını değil, olaydan çıkışı belirler; “saldırıyı engellemiyor” gerekçesiyle elenmeleri kurtarma boyutunu görmezden gelir.

## 3. Düzeltmenin kendisi risk üretir

Bu bölüm, laboratuvarın altıncı adımının karşılığıdır. Her düzeltme bir değişikliktir ve kendi hata modunu taşır.

| Düzeltme | Düzeltmenin ürettiği risk | Beklenen telafi |
|---|---|---|
| ZAM-01 yerine çoklu zaman kaynağı (K7) | Kaynak değişimi sırasında saat sıçraması; zaman damgalı telemetri ve olay kayıtlarının tutarsızlaşması, bazı cihazlarda beklenmeyen davranış | Koruma ve telekontrol açısından ön değerlendirme; saha bazında kademeli geçiş; geçiş penceresinde sapma izleme ve geri alma eşiği |
| YON-01 yönetim arayüzünün erişimini daraltmak (K5) | Yanlış bir kural, kontrol merkezinin sahalarla bağlantısını kesebilir; uzaktan yapılan rutin müdahale saha ziyaretine döner | Değişiklik öncesi yedek yönetim yolu; kısa doğrulama listesi; kesinti halinde geri alma adımının önceden yazılması ve saha ekibinin hazır olması |
| Kalıcı tedarikçi tünelini kapatmak (K3) | Arıza anında uzman desteğinin gecikmesi; tedarikçinin sözleşme yükümlülüğünü yerine getirememesi | Kapatmadan önce GEC-01 üzerinden onaylı yolun sınanması; acil erişim istisnasının kayıtlı biçimde tanımlanması; sözleşmenin güncellenmesi |
| MI-01'in ikinci arayüzünü kaldırmak (K1) | Lisans doğrulaması ve proje dosyası akışı kesilirse mühendislik kabiliyeti durur; bakım penceresinde iş yapılamaz | Dosya ve lisans akışı için denetimli bir yol tasarlanması; geçiş öncesi bir bakım işinin uçtan uca denenmesi |
| HIS-DMZ akış yönünü çevirmek (K4) | Aktarım mimarisi değişir; raporlamada veri boşluğu, kuyruk birikmesi veya çift kayıt oluşabilir | Kabul ortamında yön değişikliğinin sınanması; geçiş sırasında veri bütünlüğü karşılaştırması; boşlukların olay kaydına yazılması |
| Kuzey segmentini kayıt kapsamına almak (K8) | Aynalama veya kayıt gönderimi bir yapılandırma değişikliğidir; bant genişliği ve cihaz yükü telemetriyi etkileyebilir | Önce tek sahada sınama; kapasite ölçümü; kayıt hacmi ve saklama süresinin önceden planlanması |
| OT kimliklerini ayırmak (K2) | Hesap taşıma sırasında operatörün oturum açamaması, yani vardiya körlüğü; acil erişim yolunun eksik kalması | Geçiş öncesi acil yerel erişim yolunun tanımlanması ve sınanması; vardiya devriyle uyumlu kademeli geçiş; geri alma planı |
| Yedekleri ikinci konuma çıkarmak (K6) | Kopyalama yolu yeni bir veri akışıdır; yanlış tasarlanırsa kontrol bölgesine yeni bir geçiş açar | Akışın yönü ve başlatan ucunun akış matrisine yazılması; kopyanın içeriğinin erişim kontrollü tutulması; geri yükleme denemesiyle doğrulama |

### Emniyet değerlendirmesi olmadan yapılmayacaklar

Beklenen işaretleme: **K7** ve **K5**. Zaman kaynağı değişikliği koruma ve olay kaydı davranışını etkileyebilir; YON-01 üzerindeki değişiklik sahaların uzaktan izlenme ve kumanda edilme kabiliyetini geçici olarak kaldırabilir. **K9**'un sınanması da yol değiştirme testi gerektirdiği için aynı gruba alınabilir.

Röle ayar dosyalarına dokunan herhangi bir adım koruma mühendisinin onayına tabidir. Bu laboratuvarda ayar değişikliği önerilmesi beklenmez; yalnızca dosyaların korunması ve kurtarılabilirliği değerlendirilir.

K3'ün kapatılması bir emniyet konusu değil, işletme sürekliliği konusudur. İkisinin ayrı gerekçelerle yazılması beklenir.

## 4. Değerlendirme ölçeği

Altı ölçüt, her biri 0–3 puan; toplam 18. Ölçek bu deponun özgün önerisidir ve kurum içi eğitimde uyarlanabilir.

| Ölçüt | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Bölge ve geçiş adlandırması | Yapılmadı | Bölgeler adlandırıldı, geçişler eksik | Geçişler ve başlatan uçlar yazıldı | Çok bölgeli bileşenler ayrıca işaretlendi ve gerekçelendirildi |
| Akış matrisi | Doldurulmadı | Kaynak ve hedef var, kimlik ve kayıt boş | Alanların çoğu dolu, eksikler işaretli | Eksikler “verilmedi” olarak ayrıldı, “Hata davranışı” ve sahibi alanları yazıldı |
| Kusurların bulunması | Dörtten az kusur | 4–6 kusur | 7–8 kusur | Dokuz kusur veya daha fazlası, ek bulgularla |
| Güven varsayımı dili | Kusurlar liste halinde yazıldı | Varsayım yazıldı, güven sınırı belirsiz | Varsayım, sınır ve etki yazıldı | Belirti de yazıldı ve kanıt kaynağına bağlandı |
| Önceliklendirme | Sıralama yok | Sıralama var, gerekçe yok | Etki gerekçesi var | Etki ve uygulanabilirlik ayrı ayrı gerekçelendirildi |
| Kabul kanıtı ve emniyet | Tanımlanmadı | Kontrol adı yazıldı, kanıt belirsiz | Üç kontrol için kanıt tanımlandı | Geri dönüş planı, onay sahibi ve emniyet değerlendirmesi gereken düzeltmeler işaretlendi |

Yorum önerisi, bu çalışmada gözlenen kanıt diline ilişkindir: 0–6 arası temel okumaların tekrarı; 7–12 arası kavramlar oturmuş, kanıt dili gelişmeli; 13–18 arası kusurların güven varsayımı diliyle ve kanıta bağlı biçimde yazıldığı düzey. Eşikler eğitimi verenin hedefine göre değiştirilebilir.

Buradaki puanlama bir yetkinlik belgesi değildir. Kurgusal ve tek oturumluk bir çalışmanın çıktısıdır; gerçek bir incelemede sonuç, saha doğrulaması ve işletme teyidi olmadan kesinleşmez.

**Puan düşürmeyen durumlar:** farklı ama gerekçeli sıralama; bir kusurun iki ayrı madde olarak yazılması; “veri yetersiz, şu soruyu tesise sormak gerekir” biçimindeki sonuçlar.

**Puan düşüren durumlar:** proje dosyasında bulunmayan bilgiyi olgu gibi yazmak; kusuru ürün kusuru olarak sunmak; düzeltme önerisini kesinti, onay ve geri dönüş boyutu olmadan vermek; mimari incelemeyi saldırı senaryosuna çevirmek.

## Kapsam notu

Bu çözüm dosyası kurgusal bir mimariye ilişkin **özgün eğitim değerlendirmesidir**. Belirli bir standardın uygunluk yorumu, bir tesis için tasarım onayı veya ürün değerlendirmesi değildir. Arkasındaki savunma ilkeleri ve kaynaklar [mimari ve güven bölgeleri](../../docs/01-temeller/03-mimari-ve-guven-bolgeleri.md), [segmentasyon, kimlik ve uzak erişim](../../docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md), [zafiyet ve değişiklik yönetimi](../../docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) ve [elektrik ve enerji](../../docs/02-sektorler/02-elektrik-ve-enerji.md) bölümlerindedir. Erişim tarihi: 13.09.2026.
