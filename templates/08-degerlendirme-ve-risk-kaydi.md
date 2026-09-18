# OT değerlendirme, çalışma kuralları ve risk kaydı şablonu

[Ana sayfa](../README.md) · [Şablonlar](README.md) · [Değerlendirme metodolojisi](../docs/09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) · [Final proje](09-final-proje-teslimleri.md)

Bu dosya kapsam, yöntem izni, bulgu, risk ve yönetici kararını aynı kimliklerle bağlayan **özgün eğitim şablonudur**. Kopyası kurgusal fabrika veya hizmet senaryosuyla doldurulur. Buradaki eğitim RoE kaydı gerçek bir tesise erişim yetkisi vermez; şablonu doldurmak test yürütmek değildir. Belge/sentetik kayıt incelemesi yeterli çalışma biçimidir.

## 1. Değerlendirme kapsamı

| Alan | Doldurulacak değer |
|---|---|
| Değerlendirme kimliği ve sürüm | [DGR-001], [sürüm], [YYYY-AA-GG] |
| Hizmet ve süreç | [kurgusal hizmet], kritik işlev: [işlev] |
| Amaç | [hangi güvenlik sorusuna cevap aranıyor?] |
| Tür | [mimari / yapılandırma / zafiyet değerlendirmesi / masa başı / belge üzerinde test planı] |
| Hizmet sahibi | [işletme rolü] |
| Teknik ve emniyet sorumluları | [roller ve sorumluluk sınırı] |
| Değerlendiren | [öğrenci veya ekip rolü] |
| Kapsamdaki varlıklar | [varlık kimlikleri], envanter: [belge bağlantısı] |
| Kapsamdaki akış ve bölgeler | [AK-...], [bölge kimlikleri], çizim: [bağlantı] |
| Destek bağımlılıkları | [kimlik, zaman, güç, yedek, lisans, uzak erişim] |
| Hariç tutulan varlık/işlev | [kimlik ve gerekçe]; sınırın kanıtı: [belge] |
| Kullanılan veri | [yalnız kurgusal/sentetik girdi listesi ve kaynak] |
| Varsayımlar ve bilinmeyenler | [madde], sahibi: [rol], kapanış hedefi: [tarih] |
| Sonuçların sınırı | [hangi iddialar bu yöntemle doğrulanamayacak?] |

Varlık ve akış ayrıntıları [envanter formundan](01-envanter-ve-akis.md) gelir. Gerçek tesis için kullanılan kopya kontrollü kayıt sisteminde kalır; kamuya açık depoya saha adresi, hesap, sır veya gerçek topoloji taşınmaz.

## 2. Rules of Engagement — çalışma kuralları

| Alan | Belge alıştırmasında doldurulacak karar |
|---|---|
| Yetki kaydı | [kurgusal kapsam/onay kimliği]; gerçek erişim yetkisi değildir |
| İzinli yöntemler | [aşağıdaki yöntem kimlikleri]; izin kapsamı: [girdi ve inceleme sınırı] |
| Yasak / kapsam dışı yöntemler | [sisteme bağlantı, yeni tarama, proses/konfigürasyon değişikliği ve diğer hariçler] |
| Çalışma penceresi | [tarih/saat/dilim]; belge çalışmasında planlama amaçlı |
| İrtibat ve yedek irtibat | [kurgusal işletme/teknik roller]; gerçek kişi bilgisi yazılmaz |
| Durdurma yetkilisi | [sorumlu rol]; diğer ekip üyeleri de kaygı bildirebilir |
| Durdurma koşulları | [kapsam dışı veri, beklenmeyen bağlantı ihtiyacı, kanıt bütünlüğü sorunu veya senaryoda tanımlanan işletme etkisi] |
| Bildirim yolu | [bulgu veya durdurma kararının hangi role, hangi kayıtla iletileceği] |
| Yeniden başlama kararı | [neden kapandı, kim onayladı, kapsam değişti mi?] |
| Yedek / geri alma referansı | [DEG-... / yedek kimliği / belge çalışmasında uygulanamaz gerekçesi] |
| Veri işleme | [saklama, erişim, paylaşım, silme veya arşiv sınırı] |
| Kanıt yöntemi | [dosya/bölüm/satır referansı, tarih, bütünlük kaydı gerekiyorsa yöntem] |
| Kapsam değişikliği | [yeni sürüm, gerekçe ve onay kaydı]; sessizce genişletilmez |

### Yöntem izin matrisi

Varsayılanlar bu Markdown alıştırmasının sınırıdır. Gerçek bir çalışma için gerekli yetki ve etki değerlendirmesinin yerine kullanılamaz.

| Yöntem ID | Yöntem | Bu alıştırmada durum | Gerekli girdi / önkoşul | Üretebileceği kanıt | Sınır |
|---|---|---|---|---|---|
| YNT-01 | Verilen mimari/envanter belgesini inceleme | İzinli | [dosya ve sürüm] | Belge tutarsızlığı, eksik sahip/akış | Cihazdaki gerçek durumu kanıtlamaz |
| YNT-02 | Verilen sentetik kayıt veya paket kaydını inceleme | İzinli | [dosya, veri sözlüğü, zaman bilgisi] | Girdideki olay/akış gözlemi | Gerçek tesis davranışına genellenmez |
| YNT-03 | Verilen yapılandırma kopyasını karşılaştırma | İzinli, yalnız kopyada | [kurgusal ayar, referans ve tarih] | Gereksinim–ayar farkı | Çalışma anı davranışını kanıtlamaz |
| YNT-04 | Rol ve olay masa başı tatbikatı | İzinli | [senaryo, roller, karar günlüğü] | Karar ve sorumluluk değerlendirmesi | Teknik kontrol testi değildir |
| YNT-05 | Yeni trafik yakalama veya cihazdan kimlikli bilgi alma | Yürütülmez | [yalnız gerek duyulursa kapsam/etki/onay için açık iş yazılır] | Bu alıştırmada yeni saha kanıtı yok | Salt okunur adı etkisizlik garantisi değildir |
| YNT-06 | Aktif tarama, istismar veya yapılandırma/proses değiştirme | Kapsam dışı | [hariç bırakma kaydı] | Test planı sınırı açıklanabilir | Komut veya uygulama adımı üretilmez |

### Test öncesi kontrol listesi

- [ ] Yazılı kapsamın kimliği, amacı ve sürümü var.
- [ ] Hizmet sahibi ve değerlendiren roller belli.
- [ ] Envanter ile ağ/bölge çizimi aynı varlıkları kullanıyor.
- [ ] Kritik süreç ve emniyet kararının sahibi belirlenmiş.
- [ ] Kapsam içi ve hariç varlıklar açıkça ayrılmış.
- [ ] Her yöntem ayrı satırda izinli, yasak veya yürütülmez olarak kayıtlı.
- [ ] Çalışma penceresi ve irtibat/yedek irtibat rolleri yazılmış.
- [ ] Durdurma, bildirim ve yeniden başlama kararı tanımlı.
- [ ] Yedek ve geri alma gereksinimi incelenmiş; belge çalışmasında uygulanamazsa gerekçe var.
- [ ] İzleme/gözlem kaynağı, saat dilimi ve veri sınırları biliniyor.
- [ ] Kimlikli veya salt okunur yöntemin otomatik olarak etkisiz sayılmadığı belirtilmiş.
- [ ] Kanıtların kaynağı, erişimi, saklanması ve paylaşım sınırı tanımlı.
- [ ] RoE onayı ile her testin yürütüldüğüne ilişkin kanıt birbirine karıştırılmamış.

## 3. On beş aşamanın kanıt ve durum kaydı

Durum: `planlandı`, `belge incelemesi tamamlandı`, `kanıt eksik` veya `kapsam dışı — gerekçeli`. Aşağıdaki satırın tamamlanması gerçek bir sisteme karşı aynı aşamanın yürütüldüğü anlamına gelmez.

| Aşama | Doldurulacak çıktı | Kabul sorusu | Durum / kanıt |
|---|---|---|---|
| 1. Authorization | [yetki/kapsam kaydı] | Sorumlu ve hariç varlıklar belli mi? | [durum], [KNT-...] |
| 2. Rules of Engagement | [RoE sürümü] | Yöntem, sınır ve durdurma kararı açık mı? | [durum], [KNT-...] |
| 3. Asset discovery | [envanter ve belirsizlik listesi] | Sessiz/gözlem dışı varlıklar kayıp sayılmadan işaretli mi? | [durum], [KNT-...] |
| 4. Passive reconnaissance | [verilen kayıtların kapsamı] | Gözlem noktası ve zaman kalitesi biliniyor mu? | [durum], [KNT-...] |
| 5. Architecture mapping | [bölge ve akış çizimi] | Kontrol, veri, yönetim ve destek ayrılmış mı? | [durum], [KNT-...] |
| 6. Protocol identification | [protokol envanteri] | Belgeyle doğrulanan ile porttan tahmin ayrılmış mı? | [durum], [KNT-...] |
| 7. Vulnerability assessment | [ürün/sürüm/koşul eşlemesi] | Etkilenen, etkilenmeyen ve belirsiz kararları kaynaklı mı? | [durum], [KNT-...] |
| 8. Configuration review | [ayar–gereksinim farkları] | Ayarın sürümü ve referans gereksinimi belli mi? | [durum], [KNT-...] |
| 9. Authentication testing | [kimlik yaşam döngüsü incelemesi] | Kullanıcı, aracı ve hedef kimlikleri ayrılmış mı? | [durum], [KNT-...] |
| 10. Authorization testing | [rol × sistem × işlem matrisi] | Görüntüleme ve değiştirme ayrı mı? | [durum], [KNT-...] |
| 11. Segmentation testing | [izin/ret kabul planı] | Kural, alternatif yol ve henüz denenmeyen davranış görünür mü? | [durum], [KNT-...] |
| 12. Remote access testing | [erişim ve iptal kaydı] | Kişi, hedef, süre, onay ve açık oturum etkisi bağlı mı? | [durum], [KNT-...] |
| 13. Monitoring validation | [kaynak–toplayıcı–saklama kapsamı] | Kayıp/gecikme ve kaynak sağlığı değerlendirilmiş mi? | [durum], [KNT-...] |
| 14. Detection validation | [normal/anormal sentetik örnek karşılaştırması] | Pozitif/negatif örnek ve yanlış pozitif açıklaması var mı? | [durum], [KNT-...] |
| 15. Reporting | [bulgu, risk ve yönetici özeti] | Her karar aynı bulgu/risk kimliğine dayanıyor mu? | [durum], [KNT-...] |

## 4. Bulgu formu

| Alan | Doldurulacak değer |
|---|---|
| Bulgu kimliği / başlığı | [BUL-001], [somut eksik veya sapma] |
| Tür ve durum | [mimari / yapılandırma / zafiyet / süreç / kanıt eksiği], [açık / düzeltmede / yeniden incelemede / kapalı] |
| İlgili varlık / akış / bölge | [kimlikler] |
| Beklenen durum | [kaynaklı gereksinim veya açıkça özgün kabul ölçütü] |
| Gözlenen durum | [verilen kanıttaki durum; yer, bölüm veya satır] |
| Kanıt | [KNT-...], kaynak/sürüm/tarih: [bilgi] |
| Doğrulama yöntemi | [YNT-...], [TST-...], durum: [yürütülmüş belge kontrolü / yalnız plan] |
| Eksik / çelişen bilgi | [soru], sahibi: [rol], hedef: [tarih] |
| Saldırı / arıza ön koşulu | [mevcut kabul edilen erişim veya bağımlılık] |
| Olası etki | Hizmet: [etki]; emniyet: [etki/belirsiz]; veri/kayıt: [etki] |
| Mevcut ve telafi kontrolleri | [kontrol], kanıt: [kimlik], sınırı: [açıklama] |
| Önerilen düzeltme | [iş], sahibi: [rol], değişiklik: [DEG-...] |
| Kabul / yeniden inceleme | [beklenen ölçüt], kanıt: [gerekli KNT/TST], gözden geçiren: [rol] |
| Risk bağlantısı | [RSK-...] |

Zafiyet bulgusuysa ayrıca `[duyuru/CVE] [üretici/model] [sürüm] [etkilenen işlev] [önkoşul] [duyuru tarihi] [erişim tarihi]` doldurulur. CVSS yazılacaksa sürüm, vektör, kaynak ve tarih korunur. Duyuruyla eşleşme başarılı istismar veya öncelik sırasını tek başına kanıtlamaz; [değerlendirme bölümündeki](../docs/09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) işletme bağlamı kullanılır.

### Kurgusal örnek

`BUL-001`: Vendor erişiminin bitişinde kapı çıkış kaydı var, hedef EWS oturum kaydı yok. Bu, hedefte açık oturum kaldığını kanıtlamaz; iptal davranışının eldeki kayıtla doğrulanamadığını gösterir. Düzeltme önerisi: erişim iptali ile hedef oturum davranışını ilişkilendiren kabul ölçütü ve gerekli kayıt alanları. İlgili risk `RSK-001`; kapanış kanıtı hedef/kapi eşlemesi bulunan kabul raporudur. Bu rapor henüz yoksa bulgu kapatılmaz.

## 5. Risk kaydı

Öncelik ölçeği çalışma başında tanımlanır. Bu form otomatik bir olasılık × etki sayısı istemez. Gerekçe; kritik işlev, emniyet/hizmet etkisi, maruz kalma, ön koşul, mevcut kontrol ve değişiklik riskini görünür kılar. Belirsizlik düşük risk diye kaydedilmez.

| Alan | Çalışmanın tanımı |
|---|---|
| Öncelik sınıfları | [örn. acil karar / planlı iyileştirme / izleme]; her sınıfın ölçütü: [açıklama] |
| Değerlendiren roller | [işletme, otomasyon, emniyet ve güvenlik rollerinin girdisi] |
| Kabul yetkisi | [hangi rol hangi risk ve süreyi kabul edebilir?] |
| Gözden geçirme tetikleyicisi | [yeni kanıt, değişiklik, süre sonu, olay veya kontrol kaybı] |

| Risk ID | Varlık / akış ve bulgu | Risk senaryosu / etki | Öncelik ve gerekçe | Mevcut kontrol / kanıt | Risk sahibi | İşlem ve termin | Kalan risk / kabul | Durum / yeniden inceleme |
|---|---|---|---|---|---|---|---|---|
| [RSK-001] | [varlık], [AK-...], [BUL-...] | [önkoşul → olay → hizmet/emniyet etkisi] | [sınıf], [gerekçe ve belirsizlik] | [kontrol], [KNT-...] | [hesap verecek rol] | [azalt/kabul/kaçın/paylaş kararı], [iş sahibi], [YYYY-AA-GG] | [işlemden sonra kalan], [kabul yetkilisi ve süre / kabul yok] | [açık/izleniyor/kapalı], [tarih/koşul] |

Önerilen kontrolün riski azaltacağı öngörüsü ile kontrol uygulandıktan sonra kanıtlanan durum ayrı yazılır. `Kalan risk` alanına "yok" yazmak için gerekçe gerekir. Termin geçmişse kayıt sessizce kapanmaz; gecikme nedeni, geçici kontrol ve yeni karar görünür olur.

## 6. Dokuz assessment çıktısını bağlama

Bu liste güvenlik değerlendirmesinin çıktı paketidir; [23 parçalı final projenin](09-final-proje-teslimleri.md) tamamıyla eşdeğer değildir.

| Çıktı | Doldurulacak referans | Asgari kabul |
|---|---|---|
| Asset inventory | [envanter](01-envanter-ve-akis.md): [dosya/sürüm] | Varlık, işlev, sahip, sürüm ve bilginin kaynağı belli |
| Network diagram | [mimari/akış belgesi]: [dosya/sürüm] | Kapsam ve sınırlar envanterle tutarlı |
| Risk register | [bu formun risk kaydı]: [sürüm] | Her riskte sahip, işlem, termin ve kalan risk var |
| Vulnerability report | [zafiyet türündeki BUL kimlikleri]: [liste] | Ürün/koşul eşleşmesi ve belirsizlik kaynaklı |
| Configuration report | [ayar farkı BUL kimlikleri]: [liste] | Mevcut kopya ile kabul edilen referans ayrı |
| Segmentation report | [AK/FW/TST/BUL eşlemesi]: [liste] | Tasarlanan izin/ret ile yürütülmüş kanıt ayrı |
| RBAC report | [rol/işlem matrisi](../docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md): [dosya] | Rol, sistem, işlem ve süre; görev ayrımı açık |
| Incident response assessment | [olay ve kurtarma formu](04-olay-ve-kurtarma.md): [dosya] | Rol, karar, kanıt ve geri dönüş kapısı boşlukları belirli |
| Final executive report | [aşağıdaki özet]: [dosya/sürüm] | Teknik eklerle aynı bulgular ve kararlar kullanılıyor |

## 7. Yönetici özeti ve kapanış

| Yönetici özeti alanı | Doldurulacak metin |
|---|---|
| Amaç ve kapsam | [hangi hizmet, hangi belgeler ve hangi sınır] |
| En önemli sonuç | [kanıtın desteklediği sonuç; kesinlik derecesi] |
| Öncelikli kararlar | [BUL/RSK], [istenen karar], [sahip ve tarih] |
| Hizmete etkisi | [karar verilmezse / önerilen değişiklik yapılırsa beklenen etki] |
| Kaynak ihtiyacı | [emek, bakım penceresi, destek veya teklif ihtiyacı]; doğrulama: [kaynak] |
| Kalan belirsizlik | [eksik kanıt ve kapanış sorumlusu] |
| İnceleme sınırı | [saha testi yapılmadı, şu kontroller yalnız tasarım düzeyinde incelendi vb.] |
| Yeniden değerlendirme | [ölçüt, tarih/olay ve sahip] |

| Bulgu / risk | Düzeltme / değişiklik | Kabul ölçütü | Yeniden inceleme kanıtı | Karar ve rol |
|---|---|---|---|---|
| [BUL-... / RSK-...] | [DEG-... / iş kaydı] | [beklenen sonuç] | [KNT/TST veya henüz yok] | [kapalı / açık / kalan risk kabul edildi], [rol/tarih] |

- [ ] Yönetici özeti, risk kaydı ve teknik bulgular aynı kimlikleri kullanıyor.
- [ ] Gözlem, varsayım ve test planı birbirinden ayrılmış.
- [ ] Kanıtı olmayan kontrol çalışıyor diye işaretlenmemiş.
- [ ] Kapanan bulgunun kabul kanıtı ve kalan risk kararı var.
- [ ] Çalışılmayan varlık/yöntemler kapsam sınırında görünür.

## Kaynak ve kapsam

Form alanları, ölçek seçimi ve kabul soruları **bu deponun özgün eğitim sentezidir**. Teknik gerekçeler ve birincil kaynaklar [değerlendirme metodolojisinde](../docs/09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md), veri ve kaynak disiplini [katkı rehberinde](../CONTRIBUTING.md) bulunur. Bir standardın normatif formu, uygunluk beyanı veya gerçek test izni değildir. Son inceleme: **17.09.2026**.
