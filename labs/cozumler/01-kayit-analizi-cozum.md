# Laboratuvar 1 çözüm anahtarı: kayıt analizi

[Alıştırmaya dön](../01-kayit-analizi.md) · [Laboratuvarlar](../README.md) · [Ana sayfa](../../README.md)

Bu dosya, [çevrimdışı kayıt analizi alıştırmasının](../01-kayit-analizi.md) beklenen çıktılarını, sık yapılan yorum hatalarını ve bir öz değerlendirme ölçeğini içerir. Kayıtlar sentetik olduğundan buradaki sonuçlar da kurgusaldır. Metin boyunca “kanıt şu kadarını destekler” dili kullanılır; kesin hüküm cümlesi kurulmaz.

Önce alıştırmayı kendi yorumunuzla tamamlayın. Çözümü okuduktan sonra farklı bir sonuca varmanız tek başına hata göstergesi değildir; farkın hangi kayıt satırından doğduğunu yazmak daha öğreticidir.

## 1. Beklenen zaman çizelgesi

Saatler yerel eksende (+03:00) verilmiştir. Uzak erişim dosyasındaki UTC değerleri parantez içinde gösterilir.

| Yerel saat | Kayıt | Gözlem |
|---|---|---|
| 2026-03-10 08:10 | AG-0005 | RTU-TERFI-03 adresiyle (192.0.2.53) telemetri kesildi |
| 2026-03-10 08:44–09:21 | MI-0004…MI-0007 | Saha ekibi IE-2026-0398 kapsamında cihaz değişimi yaptı; envanter güncellemesi iş listesine bırakıldı |
| 2026-03-10 09:12 | AG-0006 | 192.0.2.58 ile yeni iletişim çifti ilk kez görüldü; envanter kaydı yok |
| 2026-03-10 16:05 (13:05Z) | UE-0010 | Tedarikçi hesabı onaylı adresten kısa bir erişim ön testi yaptı; iş emri IE-2026-0412 |
| 2026-03-10 21:47 (18:47Z) | UE-0013 | Bakım penceresi onayı etkinleştirildi |
| 2026-03-10 22:14:05 (19:14:05Z) | UE-0014, UE-0015 | S-4471 oturumu 198.51.100.72 adresinden açıldı; mühendislik bölgesine geçiş kaydı var |
| 2026-03-10 22:15:40 | MI-0011 | Aynı oturum kimliği istasyon kaydında göründü |
| 2026-03-10 22:31–23:06 | MI-0012, MI-0013 | Proje dosyası açıldı ve v14 ile v15 adayı karşılaştırıldı |
| 2026-03-10 23:58:12 | MI-0014, AG-0013 | v15 yüklendi; aynı dakikada mühendislik trafiğinde artış gözlendi |
| 2026-03-10 23:59:30 (20:59:30Z) | UE-0016 | S-4471 oturumu ve IE-2026-0412 iş emri için süre uzatma onayı kaydedildi; kayıtta yeni bitiş saati yok |
| 2026-03-10 23:59:40 | HP-0013 | Kontrolör sürüm etiketi PRJ-TERFI-02-v15 olarak göründü |
| 2026-03-11 00:09–00:23 | MI-0015, MI-0016 | Çalışma modu ve yükleme sonrası okuma doğrulandı |
| 2026-03-11 00:51:30 / 00:52:10 (21:52:10Z) | MI-0018, UE-0017 | Oturum kapandı; istasyon 156 dk, geçit 158 dk süre gösteriyor |
| 2026-03-11 01:05 | AG-0016 | Kayıt toplayıcısı depolama doluluk uyarısı verdi |
| 2026-03-11 01:18 | AG-0017 | Toplayıcı servisi yanıt vermedi |
| 2026-03-11 01:26 | HP-0016 | TERFI-02 için son doğrulanmış telemetri güncellemesi |
| 2026-03-11 01:56 | HP-0017, HP-0018 | Değer sabit; kalite bayrağı “belirsiz”, güncelleme yaşı 1820 sn |
| 2026-03-11 01:58 | AG-0018 | Toplayıcı yeniden başladı; 01:18–01:58 arası kayıt yok |
| 2026-03-11 02:05 | AG-0019 | Boşluk sonrası ilk gözlemde RTU-TERFI-02 telemetri çifti kesik |
| 2026-03-11 02:26–03:30 | HP-0019, HP-0022, HP-0024 | Kalite bayrağı “eski”; değer 4.82 m'de sabit |
| 2026-03-11 02:34 | HP-0021 | HMI ekranı aynı değeri gösteriyor; ekranda kalite bayrağı alanı yok |
| 2026-03-11 03:02 | HP-0023 | Haberleşme kesintisi alarmı |
| 2026-03-11 03:37:12 (00:37:12Z) | UE-0019, UE-0020 | S-4489 oturumu 203.0.113.45 adresinden açıldı; iş emri alanı boş |
| 2026-03-11 03:41:05 | MI-0020 | Aynı oturum kimliği istasyonda göründü |
| 2026-03-11 03:52–04:29 | MI-0021…MI-0023 | Proje deposu, v12 arşiv dosyası ve cihaz listesi görüntülendi; kayıtlı değişiklik yok |
| 2026-03-11 04:41:50 / 04:42 | MI-0024, AG-0022 | v15 proje dosyası istasyon üzerindeki yerel dizine kopyalandı; dosya aktarımında artış |
| 2026-03-11 04:57:20 / 04:58:40 (01:58:40Z) | MI-0025, UE-0021 | Oturum kapandı; istasyon 76 dk, geçit 81 dk |
| 2026-03-11 05:05 | HP-0026 | Saha ekibi yerel göstergeden 4.16 m okudu |
| 2026-03-11 09:18–09:55 | MI-0029, MI-0030, AG-0027 | IE-2026-0421 açıldı; haberleşme modülü arızalı işaretlendi |
| 2026-03-11 11:10–11:12 | MI-0031, HP-0032, AG-0028 | Modül değişiminden sonra telemetri yeniden kuruldu; seviye 4.08 m |
| 2026-03-11 14:02 (11:02:44Z) | UE-0030 | Aynı kayıtlı olmayan adresten gelen yeni erişim isteği reddedildi |
| 2026-03-11 14:22 | MI-0033 | IE-2026-0412 değişiklik kaydı kapatıldı |

## 2. Gözlem ve açıklama eşlemesi

| Gözlem | Destekleyen kayıt | Kanıtın desteklediği açıklama | Kanıtın sınırı |
|---|---|---|---|
| S-4471 oturumu | UE-0013…UE-0017, MI-0011…MI-0018 | Onaylı bakım: iş emri var, kaynak adres kayıtlı aralıkta, yükleme onayı ve doğrulama adımları kayıtlı | Yüklenen projenin içeriği bu kayıtlardan görülmez; kabul kontrolü ayrı kanıt ister |
| S-4489 oturumu | UE-0019…UE-0021, MI-0020…MI-0025 | Aynı hesabın, hiçbir iş emrine bağlanmamış ve kayıtlı olmayan bir adresten açtığı ikinci oturum | Uzatılan bakım penceresinin yeni bitişi kayıtlarda yoktur; oturumun onaylı kapsamın dışında olduğu sonucu iş emrinin yokluğuna ve kaynak adrese dayanır. Kayıtlar oturumun kim tarafından ve neden açıldığını göstermez; kötü niyet veya hesap ele geçirilmesi bu satırlarla kanıtlanmaz |
| Arşiv v12 dosyasının açılması | MI-0022 | Yalnızca dosyanın açıldığı; kayıtlı bir değişiklik veya yükleme yok | Sürüm düşürme girişimi olduğunu gösteren yükleme kaydı yok |
| Proje dosyasının yerel dizine kopyalanması | MI-0024, AG-0022 | Dosyanın istasyon üzerindeki bir dizine kopyalandığı | Dosyanın tesis dışına çıktığına dair kayıt yok; geçit tarafında karşılık gelen bir aktarım satırı bulunmuyor |
| 192.0.2.58 iletişim çifti | AG-0005, AG-0006, MI-0004…MI-0007 | Değiştirilen saha cihazının yeni adresi; envanter kaydı güncellenmemiş | Ağ gözlemi bu uç için varlık adı vermez (`hedef_varlik` alanı `-`); eşleme yalnızca adres ile cihaz değişimi kayıtları üzerinden kurulur. Cihazın doğru yapılandırıldığı ve yetkili olduğu saha doğrulamasıyla teyit edilmelidir |
| Sabit ölçüm ve eskiyen kalite bayrağı | HP-0016…HP-0029, AG-0019, MI-0029…MI-0031 | Haberleşme/donanım arızası; modül değişimiyle düzeldi | Donmanın tam başlangıç anı bilinmiyor; 01:26 ile 01:56 arasında bir yerdedir |
| 40 dakikalık kayıt kesintisi | AG-0016, AG-0017, AG-0018 | Toplayıcının depolama sorunu nedeniyle kayıt üretememesi | Kesinti süresince ağda ne olduğu bilinmiyor; bu aralık için “bir şey olmadı” denemez |
| AG-0010 yönetim oturumu (16:08) | AG-0010; karşılaştırma: UE-0010, MI-0009 ve MI-0010 | Geçit kaydında ve istasyon kaydında karşılığı bulunmayan kısa bir yönetim oturumu; kanıt, kayıt kapsamının veya kayıtlar arası eşlemenin eksik olduğunu destekler | Yetkisiz erişimin kanıtı değildir; hangi kaydın eksik kaldığı bu dört dosyadan anlaşılmaz, geçit ve istasyon kayıt yapılandırması sorulmalıdır |
| `svc.yedek` oturumlarında çok faktörlü doğrulama alanı | UE-0007, UE-0012, UE-0027, UE-0033 | Hizmet hesabının dört oturumunda `cok_faktorlu` alanı `yok`; bu, ortam özetindeki “geçit kaydı ve çok faktörlü kimlik doğrulama kullanılır” ifadesiyle çelişir | Çelişkinin tanımlı bir istisnadan mı, yapılandırma eksiğinden mi geldiği kayıtlardan anlaşılmaz; iş listesine alınacak bir bulgudur |
| Reddedilen erişim isteği | UE-0030 | Aynı kayıtlı olmayan adresten ertesi gün yeni bir istek geldiği ve reddedildiği | İsteği kimin yaptığı kayıttan anlaşılmaz |

## 3. Siber olmayan bulgu

Ölçüm tazeliği sorunu bu senaryoda **siber bir olay değildir**. Kanıt zinciri şöyledir: TERFI-02 değeri 01:26'dan sonra yenilenmiyor, kalite bayrağı sırayla “belirsiz” ve “eski” oluyor, güncelleme yaşı düzenli artıyor (HP-0016…HP-0029). Aynı dönemde TERFI-01 ve ARITMA-01 ölçümleri güncel kalıyor (HP-0020, HP-0025, HP-0030); yani sorun tek bir uzak noktayla sınırlı. Ağ gözlemi aynı çiftin kesildiğini gösteriyor (AG-0019). Saha ekibi yerel göstergeden farklı bir değer okuyor (HP-0026). Tanılama haberleşme modülünü arızalı buluyor ve modül değişiminden sonra telemetri geri geliyor (MI-0029…MI-0031, HP-0032, AG-0028).

Bu bulgunun eğitimdeki asıl dersi, verinin **güvenilir görünmesi ile güncel olması** arasındaki farktır. Operatör ekranında kalite bayrağı gösterilmediği için (HP-0021) ekran, saatlerce eski bir değeri güncelmiş gibi sunmuştur. Siber bir olay olmasa da bu, karar kalitesini etkileyen gerçek bir görünürlük bulgusudur ve ekran tasarımı ile alarm eşiği tarafında düzeltme gerektirir.

## 4. Kanıt boşluğu

Boşluk 2026-03-11 01:18 ile 01:58 arasındadır ve 40 dakikadır. Nedenine ilişkin kanıt depolama doluluk uyarısıdır (AG-0016); bu, kapasite kaynaklı bir kayıp açıklamasını destekler ancak tek başına kasıtlı bir müdahale olmadığını kanıtlamaz. Boşluğun etkileri:

- Telemetri kesintisinin tam başlangıç anı ağ tarafından doğrulanamaz; yalnızca 01:26–01:56 aralığına yerleştirilebilir.
- Bu 40 dakikada mühendislik bölgesinde yeni bir iletişim çifti oluşup oluşmadığı bilinmiyor.
- Boşluk, olay kaydına “kanıt boşluğu” olarak yazılmalı ve ilgili bulguların güven düzeyi buna göre işaretlenmelidir.

## 5. Düşülmesi olası üç yanlış yorum

1. **“İkinci tedarikçi oturumu bakım penceresinin içindedir.”** UE-0019 satırı 00:37 görünür, ancak bu değer UTC'dir ve yerel karşılığı 03:37'dir. Ofset yok sayıldığında oturum, onaylı 22:00–01:00 aralığına düşüyormuş gibi okunur. Süre uzatma onayı (UE-0016) S-4471 oturumuna ve IE-2026-0412 iş emrine bağlıdır; kayıtta uzatılmış pencerenin yeni bitiş saati yoktur, bu nedenle yeni bitiş verilerden belirlenemez. İkinci oturum (S-4489) hiçbir iş emrine bağlı değildir ve ilk oturum 00:51'de kapandıktan sonra açılmıştır; bu yüzden uzatmanın kapsamına girmez ve ayrı değerlendirilir. Aynı dosyada ters yönde bir tuzak daha vardır: ilk oturumun kapanış kaydı UTC'de 2026-03-10, yerel eksende 2026-03-11 tarihine düşer (UE-0017).
2. **“Ekrandaki sabit değer, operatörü yanıltmak için verinin değiştirildiğini gösterir.”** Zamanların yakınlığı bu yorumu çekici kılar, fakat kanıt haberleşme arızasını destekler: donma ikinci oturumdan yaklaşık iki saat önce başlamıştır, tek noktayla sınırlıdır, kalite bayrağı zaten bozulmayı bildirmektedir ve donanım değişimiyle düzelmiştir. Veriye müdahale edildiğini gösteren bir kayıt yoktur.
3. **“Envanterde olmayan iletişim çifti yetkisiz bir cihazın işaretidir.”** Aynı pencerede IE-2026-0398 kapsamında bir cihaz değişimi kayıtlıdır (MI-0004…MI-0007) ve eski adres tam da o sırada susmuştur (AG-0005). Kanıt, envanter ve değişiklik yönetimi eksiğini destekler. Cihazın kimliği yine de saha doğrulamasıyla teyit edilmelidir; “açıklandı” ile “doğrulandı” aynı şey değildir.

## 6. Beklenen algılama kartı içerikleri

Alan adları [algılama kartı şablonundaki](../../templates/03-algilama-karti.md) adlarla verilmiştir. Alıştırma şablonun tamamını değil, aşağıdaki alt kümesini ister.

Birinci kart, erişim ve yetki gözlemi içindir. **Hipotez:** tedarikçi hesabının, iş emrine bağlanmamış ve kayıtlı olmayan bir kaynak adresten açılan oturumu inceleme gerektirir. **Veri kaynağı ve kapsamı:** geçit oturum kaydı ve mühendislik istasyonu kaydı; kapsam iki günlük pencere, zaman ekseni geçit tarafında UTC, istasyon tarafında +03:00. **Birleştirilecek bağlam:** iş emri, onay ve uzatma kayıtları, kaynak adres aralığı, oturum kimliğinin istasyon kaydındaki karşılığı. **Beklenen normal açıklamalar:** onaylı acil bakım veya kaydı geç açılmış bir iş emri. **İlk üç doğrulama adımı:** oturum kimliğinin iki kayıtta da izlenmesi, kaynak adresin onaylı aralıkla karşılaştırılması, oturumun bir iş emrine bağlanıp bağlanmadığının görülmesi. **İşletmeye aktarım kuralı ve karar sahibi:** tedarikçi sözleşme sahibinden ve vardiya amirinden oturumun sahibinin teyidi istenir; hesabın kapsamını gözden geçirme kararı erişim sahibine aittir.

İkinci kart, ölçüm güvenilirliği içindir. **Hipotez:** HMI değeri sabitken historian kalite bayrağının eskimesi, operatörün güncel sanılan bir değerle karar vermesine yol açabilir. **Veri kaynağı ve kapsamı:** historian ve HMI gösterim kayıtları, saha okuması, ağ gözlemi; kapsam TERFI-02 ölçüm noktası, kör nokta HMI ekranında kalite bayrağının bulunmaması. **Birleştirilecek bağlam:** güncelleme yaşı, aynı sahadaki diğer noktalar, ağ gözlemindeki çift durumu, saha okuması, açık iş emri. **Beklenen normal açıklamalar:** haberleşme veya sensör arızası. **İlk üç doğrulama adımı:** güncelleme yaşının seyri, aynı sahadaki diğer noktaların tazeliği, ağ gözleminde çiftin durumu. **İşletmeye aktarım kuralı ve karar sahibi:** operatörün güvenilir veriyle karar verip veremediği vardiya amirine teyit ettirilir; ekranda tazelik göstergesi eksiği iş listesine alınır ve sahibi ekran tasarımından sorumlu roldür.

## 7. İşletmeye aktarım cümlesi örneği

“Kurgusal Yeşilova sahasında bakım hesabının mühendislik istasyonundaki ikinci oturumu, onaylı pencerenin dışında ve kayıtlı olmayan bir adresten açılmış görünüyor; ayrıca TERFI-02 telemetrisi 01:26'dan itibaren yenilenmiyor. İkisi arasında bir bağlantı doğrulanmadı; oturumun sahibini ve sahadaki ölçümün güncel değerini teyit etmenizi rica ediyoruz.”

## 8. Öz değerlendirme ölçeği

Altı görev adımının her biri için bir ölçüt vardır; her madde 0, 1 veya 2 puanla değerlendirilir. Toplam 12 üzerindendir. Geçme eşiği verilmemiştir; eşik ve hedefler eğitimi düzenleyen kurumca belirlenir.

| Madde | 0 puan | 1 puan | 2 puan |
|---|---|---|---|
| Zaman ekseni | Ofsetler dikkate alınmadı | Çevrim yapıldı ama bazı satırlarda tarih kayması gözden kaçtı | Bütün kayıtlar tek eksende; çevrilen satırların özgün değeri de yazılı |
| Kimlik ve yetki | Oturumlar hesap bazında ayrılmadı | Oturumlar listelendi, iş emri karşılaştırması eksik | Her oturum için kaynak adres, iş emri ve onaylı kapsam kararı kayıt numarasıyla gerekçelendirildi; kaydın yetmediği yerde eksik bilgi yazıldı |
| Normal açıklamalar | Her dikkat çeken gözlem şüpheli sayıldı | Bazı gözlemler normal açıklamayla eşleşti, dayanak gösterilmedi | En az bir gözlem siber olmayan açıklamayla ve iki bağımsız kayıtla eşleşti |
| Belirsizlik ve kanıt boşluğu | Boşluk fark edilmedi | Boşluk yazıldı, etkisi değerlendirilmedi | Boşluğun süresi, nedeni ve belirsiz bıraktığı sorular ayrı ayrı yazıldı |
| Algılama kartları | Kart yazılmadı veya alanları boş kaldı | Kartlar yazıldı, şablonun alan adları kullanılmadı | İki kart da istenen alt kümeyle dolduruldu; aktarım kuralı kimin neyi teyit edeceğini söylüyor |
| Aktarım dili | Kanıtın ötesine geçen ifadeler kullanıldı | Doğru ama belirsizliği göstermeyen bir özet yazıldı | Bilinen, bilinmeyen ve istenen teyit tek bir kısa metinde ayrıldı |

Değerlendirmede hızlı sonuç kadar yanlış sonucun önlenmesi de dikkate alınır. Katılımcı doğru gözlemleri bulup açıklamaları karıştırdıysa, eksik olan veri okuma değil bağlam birleştirmedir.

## Kaynak ve kapsam notu

Bu çözüm anahtarı, beklenen çizelge, açıklama eşlemesi, yanlış yorum listesi ve öz değerlendirme ölçeği bu deponun **özgün eğitim sentezidir**. Dış bir kaynaktan alınmış olay verisi, gerçek bir tesis incelemesi veya resmî bir değerlendirme ölçütü içermez. Kayıt katmanlarının sınırlarına ilişkin çerçeve [izleme ve algılama bölümünde](../../docs/04-savunma/03-izleme-ve-algilama.md), davranışların ortak adlandırması [MITRE ATT&CK for ICS bölümünde](../../docs/03-tehdit-modelleme/02-mitre-attack-ics.md) kaynaklarıyla birlikte verilmiştir.

Buradaki puanlama bir yetkinlik belgesi değildir. Gerçek bir olayda sonuç, kayıtların bütünlüğü, saat senkronizasyonu ve işletme teyidi doğrulanmadan kesinleştirilmez.
