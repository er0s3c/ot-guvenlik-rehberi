# Laboratuvar 3 değerlendirmesi: masa başı tatbikatı

[Laboratuvarlar](../README.md) · [Tatbikat metni](../03-masa-basi-tatbikati.md) · [Ana sayfa](../../README.md)

Bu dosya kurgusal Denizkent HRS tatbikatında her enjekte için beklenen yanıtı, sık görülen hataları, gözlemci puanlama ölçeğini ve tatbikat raporu iskeletini içerir. Kolaylaştırıcı ve gözlemci içindir; katılımcılara tatbikattan önce dağıtılmaz.

Burada da saldırı prosedürü, araç adı veya komut bulunmaz. “İyi yanıt” ifadesi tek doğru cevap anlamına gelmez. Değerlendirmede aranan şey, yargının bir kanıta bağlanması, belirsizliğin açıkça yazılması ve kararın doğru rolde kalmasıdır. Gerekçeli farklı bir karar da geçerli sayılır.

## 1. Enjekte başına beklenen yanıt

### E1 — belirsiz başlangıç

**İyi bir yanıt neye benzer:** Ekip ilk beş dakikada bir olay lideri belirler ve bunu kaydeder. Tahtadaki üç sütun doldurulur: doğrulanmış olan, bir kesiklik ve ekranların boş olmasıdır; varsayım, ikisinin aynı nedenden geldiğidir; bilinmeyen, kesikliğin nerede oluştuğudur. Sefer kararı işletme ve trafik kontrol amirine bırakılır; SOC bu kararı vermez, girdisini verir. Kayıt koruma isteği daha ilk dakikalarda dile getirilir ve kapsamı yazılır. Yolcuya verilen ilk mesaj “aksaklık var, süre belirsiz” düzeyinde kalır ve neden bildirilmez.

**Eksik yanıt:** Nedene erken kilitlenmek, olay liderini atamadan teknik tartışmaya girmek, sefer kararını siber ekipten beklemek, kayıt korumayı sonraya bırakmak.

**Savunulabilir alternatif:** Olayı önce arıza olarak yürütmek ve siber hipotezi açık bırakmak. Bu tercih, kayıt koruma isteği aynı anda yapıldığı sürece puan düşürmez.

**Kolaylaştırıcı notu:** Bu enjektenin işi sonuç üretmek değil, belirsizliği görünür kılmaktır. Ekip “bilmiyoruz” diyebiliyorsa enjekte amacına ulaşmıştır.

### E2 — kanıt eklenir, hipotez kayar

**İyi bir yanıt neye benzer:** Ekip donmuş telemetriyi “normal” saymaz, “bilinmiyor” sütununa taşır ve etkilenen iki istasyon için saha doğrulaması ister. Enerji ve telekom bildirimleri ortak bir köken ihtimali olarak değerlendirilir, ancak siber hipotez kapatılmaz. Kısıtlı işletme kararı burada verilir: sefer aralığının uzatılması veya belirli bir bölümün kısıtlı sürdürülmesi, işletme yetkilisinin kararı olarak kaydedilir ve gözden geçirme saati yazılır. Yedek taşıma yolunun gerçekten bağımsız olup olmadığı sorulur; cevap bilinmiyorsa doğrulanacaklar listesine eklenir.

**Eksik yanıt:** Enerji açıklamasını bulup olayı kapatmak; donmuş ölçüme bakarak “tesis normal” demek; kısıtlı işletmeyi kimin kararlaştırdığını yazmadan uygulamak.

**Savunulabilir alternatif:** Kısıtlı işletmeye geçmeyip mevcut düzeni sürdürmek. Bunun için peron doluluğu, saha doğrulaması ve gözden geçirme saatinin yazılı olması beklenir.

**Kolaylaştırıcı notu:** Bu enjektede ölçülen şey, yeni bilgi geldiğinde hipotezin güncellenip güncellenmediğidir. Tahtadaki sütunlar değişmiyorsa ekip yeni bilgiyi kullanmıyor demektir.

### E3 — kanıt siber yöne kayar

**İyi bir yanıt neye benzer:** Kayıt boşluğu ve iş emri bulunmayan oturum ayrı ayrı yazılır; ikisi tek bir sonuca birleştirilmez. Kanıt koruma kararı verilir: hangi kayıtların dondurulacağı, kimin erişeceği ve ne kadar saklanacağı yazılır. Erişim kısıtlaması ölçülü kurulur; tek hesabın askıya alınması ile tedarikçinin bütün erişiminin kapatılması arasındaki fark, arıza desteği üzerindeki etkisiyle birlikte tartışılır. Hukuk ve uyum rolü devreye alınır ve sözleşmedeki kayıt, bildirim ve destek yükümlülükleri çıkarılır. Aynı hesabın ANK ve CER-SCADA yetkisi olup olmadığı sorulur; cevap bilinmiyorsa bu, olayın kapsamını genişleten bir belirsizlik olarak yazılır.

**Eksik yanıt:** Oturumu doğrudan saldırı ilan etmek; tedarikçiyi kanıt olmadan suçlamak; kayıt boşluğunu tek başına kötü niyet kanıtı saymak; hızlanmak için sunucuyu yeniden başlatmak.

**Savunulabilir alternatif:** Tedarikçinin bütün erişimini geçici olarak askıya almak. Bunun için yerine geçecek destek düzeninin ve süre sınırının yazılması beklenir.

**Kolaylaştırıcı notu:** Bu enjektede iki ayrı olgunun bir arada bulunması, nedenselliği kanıtlamaz. Ekibin “zaman yakınlığı” ile “neden” arasındaki farkı söylemesi beklenir.

### E4 — emniyet kararı siber karardan önce gelir

**İyi bir yanıt neye benzer:** Peron doluluğu ve açık kabin bulgusu karşısında karar sırası açıkça kurulur. Emniyet değerlendirmesi ve gerekiyorsa ilgili bölümde seferin durdurulması, işletme ve emniyet yetkilisinin kararıdır; siber ekibin kanıt talebi bu kararı geciktirmez. Kabine yaklaşacak kişi, amacı ve yapılacak kaydı önceden belirlenir; fotoğraf, saat ve gözlem notu emniyet işleminin önüne geçmeden alınır. El ile güzergâh verme yoğunluğunun artırılması önerisi, operatör iş yükü ve hata olasılığıyla birlikte değerlendirilir. Kısıtlı işletmenin süresi ve gözden geçirme koşulu yazılır.

**Eksik yanıt:** Kanıt korumak için emniyet doğrulamasını bekletmek; kabin bulgusunu doğrudan olayın nedeni ilan etmek; turnike kısıtlamasını sahipsiz bırakmak; kısıtlı işletmeye süre ve gözden geçirme koşulu yazmamak.

**Savunulabilir alternatif:** Seferi durdurmayıp kısıtlı sürdürmek. Bunun için peron doluluğunun nasıl yönetileceği, ek personel ve gözden geçirme saati yazılmalıdır.

**Kolaylaştırıcı notu:** Bu enjektenin hedefi, iki ayrı kaygının yarıştığı bir anda sıralamanın kurulmasıdır. Kanıtın bir bölümünün kaybedilmesi emniyet gereğiyle kabul edilebilir; kabul edilmeyen şey, bunun kayda geçirilmemesidir.

### E5 — dış baskı, bildirim ve dönüş

**İyi bir yanıt neye benzer:** Dışa verilecek mesaj üç bölüme ayrılır: doğrulanmış olan, doğrulanmamış olan ve şu an paylaşılmayacak olan. “Siber saldırı yoktur” gibi kanıtın ötesine geçen bir cümle kurulmaz; belirsizliğin açıkça söylenmesi tercih edilir. Yolcuya verilen mesaj ile basına verilen mesaj ayrı hazırlanır ve zamanlaması yazılır. Düzenleyici bildirim tartışması, salonda bir yükümlülük yorumu üretmeye dönüşmez: kurumun kendi güncel yükümlülük listesinin açılacağı, listeyi kimin açıp kimin onaylayacağı ve hangi bilgilerin hazır tutulacağı kaydedilir. Tedarikçinin “temiz sürüm” önerisi kabul kapılarıyla karşılanır: sürümün kaynağı, tarihi, bütünlük bilgisi, sahadaki yapılandırmayla uyumu, kabul testi, onay sahibi ve geri alma planı istenir.

**Eksik yanıt:** Doğrulanmamış bir yargıyı kamuya açıklamak; bildirim yükümlülüğünü salonda yorumlayıp karara bağlamak; tedarikçinin sürümünü kaynağı belgelenmeden yüklemek; dönüş sonrası izleme süresini yazmamak.

**Savunulabilir alternatif:** Basına bu aşamada içerik vermeyip yalnızca hizmet durumu açıklaması yapmak ve teknik değerlendirmeyi sonraya bırakmak.

**Kolaylaştırıcı notu:** Bu enjektede sık görülen eğilim, iletişim baskısının teknik kararı hızlandırmasıdır. Ekibin, dışa verilecek mesaj ile hizmete dönüş kararını ayrı tutması beklenir.

### E6 — isteğe bağlı kapanış

**İyi bir yanıt neye benzer:** Yedek ile sahadaki sürüm arasındaki farkın kaynağı araştırılmadan geri yükleme yapılmaz. Eksik lisans bilgisi ve tek kişiye bağlı erişim, kurtarma paketinin bir eksiği olarak yazılır. Kısıtlı işletmenin süresine ilişkin tahmin güncellenir ve yolcuya verilen bilgi buna göre düzeltilir. Eksikler iyileştirme listesine sahibiyle birlikte geçer.

**Eksik yanıt:** Farkı önemsiz sayıp geri yüklemek; eksikliği kişiye bağlamak; iyileştirme listesine sahip ve tarih yazmamak.

## 2. Sık görülen dört hata

Aşağıdaki dört hata bu tatbikatta yinelenen kalıplardır. Her biri için nasıl göründüğü, neden olduğu, kolaylaştırıcının müdahalesi ve yerine geçen davranış verilmiştir.

| Hata | Salonda nasıl görünür? | Neden olur? | Kolaylaştırıcının müdahalesi | Yerine geçen davranış |
|---|---|---|---|---|
| Erken kesinlik | İlk dakikalarda “saldırıya uğradık” veya “bu sadece arıza” denir; sonraki bilgiler bu yargıyı doğrulamak için okunur | Belirsizlik rahatsız edicidir; karar vermek için bir hikâye gerekir | “Bunu nereden biliyoruz?” sorusu; bilgiyi varsayım sütununa taşımak | Hipotezi yazılı tutmak, hangi kanıtın onu çürüteceğini önceden belirlemek |
| Kanıt yok etme | Hizmeti hızlandırmak için yeniden başlatma, önbellek temizleme, kaydın üzerine yazılması | Ekiplerin öncelikli refleksi hizmeti geri getirmektir | İşlemi durdurup “bu işlem hangi soruyu cevapsız bırakır?” diye sormak | Kanıt koruma kararını ilk enjektede vermek; emniyet gereği kaybedilen kanıtı kayda geçirmek |
| Tek kanaldan doğrulama | Bir ekrandan, bir kayıttan veya tek bir kişiden gelen bilginin doğrulanmış sayılması | Aynı sistemden gelen iki çıktı bağımsız kanıt sanılır | “İkinci ve bağımsız kaynak ne?” sorusu; kaynağın bağımlılığını göstermek | Saha doğrulaması, farklı sistemden kayıt, bağımsız ölçüm; aynı kaynağın iki görüntüsünü tek kanıt saymak |
| Emniyet ile güvenliği karıştırma | Siber ekibin emniyet kararını vermesi veya emniyet gerekçesiyle siber incelemenin tamamen durdurulması | İki alan da “güvenlik” sözcüğünü kullanır; karar sahipleri netleşmemiştir | Karar sahibini ve dayandığı belgeyi sormak; iki kararı ayrı satıra yazdırmak | Emniyet kararı işletme ve emniyet yetkilisinde, siber karar güvenlik sorumlusunda; ikisi arasındaki çatışmanın kayda geçmesi |

Bu dört hata ahlaki bir eksiklik değildir; baskı altındaki ekiplerde beklenen davranışlardır. Tatbikatın işi onları salonda görünür kılmak, iyileştirmeyi prosedüre taşımaktır.

## 3. Gözlemci puanlama tablosu

Sekiz ölçüt, her biri 0–3 puan; toplam 24. Ölçek bu deponun özgün önerisidir ve kurum içi eğitimde uyarlanabilir. Puan ekibin çıktısına verilir, kişilere değil.

| Ölçüt | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Durum resmi ve belirsizlik yönetimi | Doğrulanmış ile varsayım ayrılmadı | Ayrım sözlü yapıldı, yazıya geçmedi | Üç sütun dolduruldu ve güncellendi | Sütun değişiklikleri gerekçeleriyle kayıtlı; çürütücü kanıt önceden adlandırıldı |
| Rol ve karar yetkisi | Olay lideri belirsiz | Lider var, karar sahipleri karışık | Her karar bir role bağlandı | Yedek karar sahibi, ulaşma süresi ve anlaşmazlık çözümü de tanımlı |
| Emniyet önceliği | Emniyet kararı siber talebe bağlandı | Sıra sözlü kuruldu, kaydedilmedi | Emniyet kararı ayrı satırda ve doğru sahipte | Kanıt ile emniyet çatışması açıkça çözüldü ve gerekçesiyle kaydedildi |
| Kısıtlı işletme kararı | Karar verilmedi veya sahipsiz | Karar var, gerekçe yok | Gerekçe ve kapsam yazıldı | Süre, gözden geçirme koşulu ve geri dönüş eşiği de yazıldı |
| Kanıt koruma ve kayıt kalitesi | Kanıt koruma gündeme gelmedi | Sözlü istendi, kapsamı yok | Kapsam, sorumlu ve saklama yazıldı | Kaybedilen kanıt ve nedeni de kayda geçti; karar günlüğü enjekte başına dolu |
| İç ve dış iletişim | Mesaj hazırlanmadı | Tek bir genel mesaj hazırlandı | Yolcu, basın ve kurum içi mesajlar ayrıldı | Doğrulanmış, doğrulanmamış ve paylaşılmayan bilgi ayrımı yazılı; zamanlama ve kanal belirli |
| Bildirim yükümlülüğünün ele alınışı | Hiç gündeme gelmedi | Salonda yorum üretildi | Kurumun kendi listesine yönlendirildi | Listeyi açacak ve onaylayacak roller, hazır tutulacak bilgiler ve listenin güncelliği sorusu kayıtlı |
| Hizmete dönüş ve öğrenme | Dönüş koşulu tanımlanmadı | Dönüş “çalışıyor” ölçütüne bağlandı | Kabul kapıları listelendi | Kabul kanıtı, onay sahibi, izleme süresi ve iyileştirme listesi sahipleriyle tamam |

Yorum önerisi, bu tatbikatta gözlenen kanıt ve kayıt diline ilişkindir: 0–8 arası temel rollerin ve karar sırasının yeniden çalışılması; 9–16 arası kavramlar oturmuş, kanıt ve kayıt dili gelişmeli; 17–24 arası kararların role, kanıta ve geri dönüş koşuluna bağlandığı düzey. Eşikler eğitimi verenin hedefine göre değiştirilebilir.

Buradaki puanlama bir yetkinlik belgesi değildir. Kurgusal ve tek oturumluk bir çalışmanın çıktısıdır; gerçek bir olayda sonuç, saha doğrulaması ve işletme teyidi olmadan kesinleşmez.

**Puan düşürmeyen durumlar:** gerekçeli biçimde farklı bir işletme kararı; olayı arıza olarak yürütüp siber hipotezi açık bırakmak; “bu bilgi bizde yok, şu soruyu tesise sormak gerekir” sonucu; bir kararın süre alması, gerekçesi yazılmışsa.

**Puan düşüren durumlar:** kanıtın ötesine geçen yargıları dışa açmak; emniyet kararını siber ekipten beklemek; kanıt üreten bir kaydı gerekçesiz ortadan kaldırmak; bildirim yükümlülüğünü salonda karara bağlamak; tatbikatı bir saldırı bulmaca yarışına çevirmek.

## 4. Tatbikat raporu iskeleti

Rapor tatbikattan sonraki bir hafta içinde yazılır ve kişi adı yerine rol adı kullanır. Köşeli parantezli alanlar doldurulacak yerlerdir.

1. **Kapak bilgisi:** tatbikat adı, tarih [gg.aa.yyyy], sürüm (90 dakikalık kısa sürüm veya yaklaşık 3,5 saatlik tam sürüm), kolaylaştırıcı rolü, katılan roller, gözlemci var mı.
2. **Amaç ve kapsam:** hangi yetenekler çalışıldı, hangileri kapsam dışı bırakıldı. Kısa sürüm uygulandıysa çalışılmayan konular burada adlandırılır.
3. **Senaryo özeti:** kurgunun kısa anlatımı ve uygulanan enjekteler [E1..E6]; uygulanan varyantlar ayrıca yazılır.
4. **Zaman çizelgesi:** karar günlüğünden türetilmiş sıralı liste; her satırda saat, karar, rol, kanıt ve belirsizlik.
5. **Gözlemler:** işleyen üç nokta, zorlayan üç nokta. Her biri bir enjekteye ve bir kanıta bağlanır.
6. **Hata kalıpları:** ikinci bölümdeki dört kalıptan hangilerinin görüldüğü ve hangi anda görüldüğü.
7. **Puanlama:** gözlemci varsa ölçüt bazında puanlar ve kısa gerekçeleri; gözlemci yoksa bu bölüm “uygulanmadı” yazılarak geçilir.
8. **İyileştirme listesi:** bulgu, önerilen iş, sahip, hedef tarih, kabul kanıtı ve ilgili şablon. Liste [olay ve kurtarma şablonuna](../../templates/04-olay-ve-kurtarma.md) bağlanır.
9. **Doğrulanacaklar:** tatbikatta cevabı bilinmeyen ve gerçek kurum verisiyle doğrulanması gereken sorular; her soru için cevaplayacak rol.
10. **Sınırlar notu:** senaryonun kurgusal olduğu, çıktıların gerçek bir tesise doğrudan uygulanamayacağı ve “kimse cezalandırılmaz” kuralının rapor için de geçerli olduğu.
11. **Dağıtım ve saklama:** raporu kimin okuyacağı, nerede saklanacağı ve erişim sınırı.

Rapor bir başarı belgesi değildir. İçinde hiç zorlayan nokta bulunmayan bir rapor, tatbikatın fazla kolay kurulduğuna işaret edebilir; bir sonraki tatbikatta enjekte sayısı veya belirsizlik düzeyi artırılır.

## Kapsam notu

Bu değerlendirme dosyası kurgusal bir senaryoya ilişkin **özgün eğitim değerlendirmesidir**. Belirli bir standardın uygunluk yorumu, bir kurum için olay planı onayı veya düzenleyici yükümlülük yorumu değildir. Bildirim yükümlülükleri bu depodan değil, kurumun kendi güncel listesinden ve yetkili kaynaklardan yürütülür.

Arkasındaki savunma ilkeleri ve kaynaklar [olay müdahalesi ve kurtarma](../../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md), [izleme ve algılama](../../docs/04-savunma/03-izleme-ve-algilama.md), [raylı sistemler](../../docs/02-sektorler/03-rayli-sistemler.md), [telekom ve baz istasyonları](../../docs/02-sektorler/04-telekom-ve-baz-istasyonlari.md) ve [risk, emniyet ve altyapı bağımlılıkları](../../docs/01-temeller/05-risk-emniyet-ve-bagimliliklar.md) bölümlerindedir. Erişim tarihi: 13.09.2026.
