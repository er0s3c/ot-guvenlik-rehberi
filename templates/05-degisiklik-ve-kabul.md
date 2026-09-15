# Değişiklik ve kabul şablonu

[Ana sayfa](../README.md) · [Şablon dizini](README.md) · [Zafiyet ve değişiklik yönetimi](../docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md)

Bu şablon bir OT değişikliğinin gerekçesini, onayını, kabul kanıtını ve geri dönüş yolunu tek kayıtta tutmak içindir. Yama, proje/ayar değişikliği, cihaz değişimi, ağ kuralı güncellemesi ve devreye alma için aynı form kullanılır; kapsam alanı hangisi olduğunu belirtir. Dosya boş formdur; doldurma kurumun kontrollü değişiklik kayıt sisteminde yapılır. Buradaki bütün örnek değerler **kurgusaldır**.

Şablon, [zafiyet ve değişiklik yönetimi](../docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) bölümündeki yedi kontrol kapısını kapsar: uygunluk, yedek, test, işletme, geri alma, gözlem ve kapanış. Eşleşme birebir değildir; bir kapı birden çok bölümde kaydedilir. Şablon bir onay yetkisi vermez; kimin neyi onaylayacağı kurumun kendi süreciyle belirlenir.

| Kontrol kapısı | Şablonda nerede kaydedilir? |
|---|---|
| Uygunluk | 1.1–1.2 alanları (etkilenen varlık, sürüm, risk sınıfı) ve 4. bölümdeki karar ağacının 1–3. adımları |
| Yedek | 1.2'deki ilgili yedek kaydı ve 2.1 tablosundaki yedek tazeliği satırı |
| Test | 2.3 doğrulama testleri |
| İşletme | 1.2'deki bakım penceresi, süreç koşulu ve iletişim planı ile 2.2 adım özeti |
| Geri alma | 3. geri alma planı |
| Gözlem | 2.4 kabul ölçütleri ve gözlem süresi |
| Kapanış | 5. kapanış listesi ve kapanış onayı tablosu |

## 1. Değişiklik kaydı

### 1.1 Alan tanımları

| Alan | Ne yazılır? | Kurgusal örnek | Doldurma notu |
|---|---|---|---|
| Değişiklik kimliği | Kurum içinde tekil kod | `DEG-2026-041` | Kod envanter, yedek ve kabul kayıtlarında aynı kullanılır |
| Değişiklik türü | Yama, proje/ayar, donanım, ağ kuralı, devreye alma, hizmetten çıkarma | `Donanım yazılımı güncellemesi` | Birden çok tür varsa her biri ayrı satırda listelenir |
| Talep gerekçesi | Çözülen sorun ve yapılmazsa beklenen sonuç | `Üretici duyurusundaki uzaktan erişilebilir bileşen; mevcut telafi kontrolü süreli` | "Güncel olsun" tek başına gerekçe sayılmaz |
| Tetikleyen kayıt | Zafiyet duyurusu, arıza, iyileştirme maddesi veya olay | `ZAF-2026-118` | Olay sonrası maddeler için [olay şablonundaki](04-olay-ve-kurtarma.md) iş listesi kimliği |
| Etkilenen varlıklar | Envanterdeki varlık kodları | `SU-PLC-014, SU-SRV-003` | [Envanter ve akış şablonundaki](01-envanter-ve-akis.md) kodlar kullanılır |
| Etkilenen işlev ve hizmet | İşin çıktısı düzeyinde etki | `2 nolu terfi noktasının otomatik seviye kontrolü` | Cihaz adı yerine hizmet yazılır |
| Etkilenen akışlar | Akış matrisi kimlikleri | `AK-012` | Ağ kuralı değişikliklerinde zorunlu alandır |
| Risk sınıfı ve gerekçesi | Kurumun ölçeğine göre sınıf ve dayanağı | `Orta — tek noktada kesinti, geri alınabilir` | Sınıf ölçeği şablonun başında tanımlanır |
| Emniyet değerlendirmesi gerekli mi? | Evet/hayır ve kararı veren rol | `Evet — emniyet sorumlusu (rol), 2026-09-02` | "Hayır" cevabı da gerekçesiyle yazılır |
| Emniyet değerlendirme kaydı | Değerlendirmenin kayıt kimliği | `EMN-2026-07` | Emniyetle ilgili işlevlerde ayrı süreç geçerli olabilir |
| Bakım penceresi | Tarih, saat aralığı ve süreç koşulu | `2026-09-20 02:00–05:00, depo seviyesi yüksek` | Sürecin hangi durumda olması gerektiği de yazılır |
| Kesinti beklentisi | Beklenen kesinti ve kimin etkileneceği | `İzlemede 20 dakika; yerel kontrol sürüyor` | Beklenen ile tolere edilebilir kesinti ayrı yazılır |
| Tedarikçi katılımı | Katılan kurum, rol, erişim yöntemi ve erişim kaydı | `Yüklenici T; refakatli uzak erişim, ERS-2026-233` | Erişim ayrıntısı [tedarikçi ve uzak erişim şablonuna](06-tedarikci-ve-uzak-erisim.md) bağlanır |
| İletişim planı | Kim, ne zaman, hangi kanaldan bilgilendirilir | `Vardiya devri; SOC nöbeti; saha ekibi` | Değişiklik sırasında alarm bekleyen ekipler de listelenir |
| Değişiklik sahibi | İşi yürüten rol | `Otomasyon sorumlusu (rol)` | Kişi adı değil rol yazılır |
| Onaylayan roller | Onay veren roller ve tarih | `İşletme sorumlusu, güvenlik ekibi` | Talep eden ile onaylayan aynı rol olmamalıdır |
| Uygulayan | İşlemi yapan rol/kurum | `Yüklenici T teknisyeni, refakat: otomasyon ekibi` | Refakat gerekliyse refakat eden rol yazılır |

### 1.2 Kopyalanabilir değişiklik kartı

| Alan | Değer |
|---|---|
| Değişiklik kimliği | [değişiklik kodu] |
| Değişiklik türü | [yama/proje-ayar/donanım/ağ kuralı/devreye alma/hizmetten çıkarma] |
| Talep gerekçesi | [çözülen sorun]; yapılmazsa: [beklenen sonuç] |
| Tetikleyen kayıt | [zafiyet/arıza/olay/iyileştirme kimliği] |
| Etkilenen varlıklar | [varlık kodları] |
| Etkilenen işlev ve hizmet | [hizmet tanımı] |
| Etkilenen akışlar | [akış kimlikleri] |
| Risk sınıfı ve gerekçesi | [sınıf] — [gerekçe] |
| Emniyet değerlendirmesi gerekli mi? | [evet/hayır] — karar veren: [rol], [YYYY-AA-GG] |
| Emniyet değerlendirme kaydı | [kayıt kimliği veya "uygulanmaz"] |
| Bakım penceresi ve süreç koşulu | [tarih, saat aralığı] — [süreç koşulu] |
| Kesinti beklentisi | Beklenen: [süre] / Tolere edilebilir: [süre] |
| Tedarikçi katılımı | [kurum], [rol], erişim kaydı: [erişim kimliği] |
| İletişim planı | Önce: [rol/kanal] / Sırasında: [rol/kanal] / Sonra: [rol/kanal] |
| Değişiklik sahibi | [rol] |
| Onaylayan roller ve tarih | [rol], [YYYY-AA-GG]; [rol], [YYYY-AA-GG] |
| Uygulayan ve refakat | [rol/kurum]; refakat: [rol veya "gerekmiyor" + gerekçe] |
| İlgili yedek kaydı | [yedek kimliği] |
| Kaydın sürümü ve değiştiren | [sürüm], [rol], [YYYY-AA-GG] |

Kurgusal doldurulmuş örnek (kısaltılmış):

| Alan | Değer |
|---|---|
| Değişiklik kimliği | DEG-2026-041 |
| Değişiklik türü | Ağ kuralı güncellemesi |
| Talep gerekçesi | Uzak saha telemetrisi için tanımsız kalan geçişin akış matrisine uygun hâle getirilmesi |
| Risk sınıfı ve gerekçesi | Orta — telemetri kesilirse uzak nokta izlenemez; kural geri alınabilir |
| Emniyet değerlendirmesi gerekli mi? | Hayır — emniyet işlevleriyle ilişkisiz; karar veren: emniyet sorumlusu (rol) |

Risk sınıfı ölçeği bu şablonda tanımlanmaz; kurum kendi ölçeğini kullanır. Ölçek seçilirken süreç etkisi, emniyetle ilişki, geri alınabilirlik ve kapsanan varlık sayısı ayrı ayrı sorulur. Tek bir "kritik/kritik değil" etiketi bu dört soruyu birleştirdiğinde bilgi kaybeder.

## 2. Kabul planı

### 2.1 Değişiklik öncesi çalışan durumun kanıtlanması

Değişiklikten sonra "eskisi gibi çalışıyor" diyebilmek için öncesinin yazılı olması gerekir. Bu kayıt, işin başlamasından önce alınır.

| Ölçüt | Değişiklik öncesi değer/durum | Ölçüm zamanı | Kanıt kimliği | Alan rol |
|---|---|---|---|---|
| Sürüm bilgisi (donanım yazılımı, proje, yapılandırma) | [sürümler] | [zaman] | [kanıt] | [rol] |
| Süreç davranışı (ilgili ölçüm ve kontrol) | [tipik değer aralığı] | [zaman] | [kanıt] | [rol] |
| Haberleşme durumu (ilgili akışlar) | [durum, kalite bayrağı] | [zaman] | [kanıt] | [rol] |
| Aktif alarm listesi | [açık alarmlar] | [zaman] | [kanıt] | [rol] |
| Kayıt akışı (hangi kayıt nereye gidiyor) | [durum] | [zaman] | [kanıt] | [rol] |
| Yedek tazeliği ve geri yüklenebilirliği | [yedek kimliği ve tarihi] | [zaman] | [kanıt] | [rol] |

- [ ] Değişiklik öncesi yedek alındı ve geri yüklenebilirliği daha önce denendi.
- [ ] Mevcut açık alarm ve arızalar listelendi; değişikliğe bağlanmayacakları belli.
- [ ] Ölçümler değişiklikten sonra aynı yöntemle tekrarlanabilir biçimde kaydedildi.
- [ ] Test ortamının üretimi temsil etmediği noktalar yazıldı.

### 2.2 Uygulanacak adımların özeti

| Sıra | Adım | Sorumlu rol | Beklenen süre | Bu adımdan sonra kontrol edilecek | Geri alma noktası mı? |
|---|---|---|---|---|---|
| 1 | [adım] | [rol] | [süre] | [kontrol] | [evet/hayır] |
| 2 | [adım] | [rol] | [süre] | [kontrol] | [evet/hayır] |
| 3 | [adım] | [rol] | [süre] | [kontrol] | [evet/hayır] |

Adım özeti bir ürün prosedürünün yerine geçmez; üreticinin talimatı ve kurumun iş izni süreci ayrıca geçerlidir. "Geri alma noktası" sütunu, hangi adımdan sonra geri dönmenin hâlâ mümkün olduğunu gösterir.

### 2.3 Doğrulama testleri

| Test alanı | Ne doğrulanır? | Kabul ölçütü | Kanıt | Sorumlu rol |
|---|---|---|---|---|
| İşlev | İlgili kontrol/koruma işlevinin beklenen davranışı | [ölçüt] | [test kaydı] | [rol] |
| Haberleşme | İzinli akışların çalışması ve kapsam dışı geçişin reddedilmesi | [ölçüt] | [test kaydı] | [rol] |
| Alarm | Alarmın üretilmesi, operatöre ulaşması ve doğru bağlamı taşıması | [ölçüt] | [test kaydı] | [rol] |
| Kayıt | Denetim ve olay kayıtlarının üretilip toplandığı | [ölçüt] | [test kaydı] | [rol] |
| Yedek | Yeni sürümün yedek kapsamına alınması ve bütünlüğünün doğrulanması | [ölçüt] | [yedek kaydı] | [rol] |
| Süreç doğrulaması | Saha ölçümü ile göstergenin tutarlılığı | [ölçüt] | [saha kaydı] | [rol] |

Kabul ölçütü sayısal veya gözlemlenebilir yazılır: "sorunsuz çalıştı" ifadesi ölçüt değildir. Testin kapsamadığı durumlar da yazılır; örneğin gerçek saha haberleşmesi veya yedeklilik davranışı denenmediyse "test geçti" ifadesi bunları kapsamaz.

### 2.4 Kabul ölçütleri ve gözlem süresi

| Alan | Değer |
|---|---|
| Kabul için tamamlanması gereken testler | [test listesi] |
| Kabul kararını veren roller | [roller] |
| Gözlem süresi | [süre] — gerekçe: [neden bu süre?] |
| Gözlem süresinde izlenecek belirtiler | [belirti listesi] |
| Gözlem sırasında kimin nöbetçi olduğu | [rol/vardiya] |
| Gözlem süresi boyunca geri alma hazır mı? | [evet/hayır] — [koşul] |
| Gözlem sonucu ve kanıt | [sonuç], [kanıt kimliği] |

Gözlem süresi, değişikliğin etkisinin ortaya çıkması beklenen süreç döngüsüne göre seçilir. Bir vardiya boyunca sorun görülmemesi, farklı yük veya hava koşullarında da sorun olmayacağını göstermez; bu sınır yazılır.

## 3. Geri alma planı

Geri alma planı değişiklikten önce hazır olur. Plan yoksa değişiklik başlatılmaz; bu, kabul kapılarından biridir.

| Alan | Ne yazılır? | Kurgusal örnek |
|---|---|---|
| Tetik koşulları | Hangi gözlem geri almayı başlatır? | `Telemetri 15 dakika boyunca gelmiyorsa` |
| Karar veren rol | Geri alma kararını kim verir? | `Vardiya amiri (rol); saat dışı: nöbetçi otomasyon sorumlusu` |
| Karar süresi | Ne kadar içinde karar verilir? | `Tetik gözleminden sonra 10 dakika` |
| Gereken yedek ve parça | Hangi sürüm, dosya, donanım, lisans ve araç gerekir? | `Önceki proje sürümü; yedek kart; mühendislik dizüstüsü` |
| Geri almanın kendi riski | Geri alma işleminin yaratabileceği etki | `İkinci kesinti; ayar kaybı; yarım kalmış işlem` |
| Geri alınamayan kısımlar | Hangi adım geri alınamaz? | `Donanım yazılımı sürüm düşürme üretici tarafından desteklenmiyor` |
| Geri alma sonrası doğrulama | Hangi testler tekrarlanır? | `2.3'teki işlev, haberleşme ve alarm testleri` |
| Geri alma sonrası kayıt | Nereye yazılır? | `Aynı değişiklik kaydına; olay açılması gerekiyorsa olay kimliği` |

- [ ] Tetik koşulları gözlemlenebilir biçimde tanımlandı.
- [ ] Karar yetkisi bakım penceresindeki saatler için de belirlendi.
- [ ] Geri alma için gereken dosya, parça ve araç pencereden önce hazır.
- [ ] Geri almanın kendi riski değerlendirildi ve kabul edildi.
- [ ] Geri alınamayan adımlar işaretlendi; bunlar için ek onay alındı.
- [ ] Geri alma sonrası doğrulama testleri belirlendi.

Geri alma bir başarısızlık işareti değil, planlanmış bir seçenektir. Geri alındıktan sonra değişiklik kapanmaz; neden çalışmadığı incelenerek yeni bir plan hazırlanır.

## 4. Yama kararı için karar ağacı

Aşağıdaki sıra bu deponun **özgün** karar yardımıdır; bir uygunluk kuralı değildir. Her adımın cevabı ve dayanağı değişiklik kaydına yazılır. Çıktı "yama yapıldı/yapılmadı" değil, gerekçeli bir işlem kararıdır.

- **1. Duyuru bu varlığı gerçekten kapsıyor mu?**
  - Model, donanım revizyonu ve sürüm envanterle eşleşiyor mu? Eşleşme belirsizse: `doğrulanacak` yazılır, sorumlu ve tarih atanır.
  - Etkilenen işlev bu kurulumda etkin mi? Etkin değilse gerekçe ve doğrulama kanıtı yazılır; karar "şimdilik kapsam dışı" olarak kaydedilir ve gözden geçirme tarihi konur.
- **2. Üretici bu sürüm için destek sağlıyor mu?**
  - Destekli güncelleme var → 3. adım.
  - Destek sonu geçmiş veya güncelleme yok → telafi edici kontrol ve yenileme planı yolu (6. adım). Destek durumu bilinmiyorsa üreticiye yazılı soru sorulur; cevap gelene kadar geçici önlem süreli olarak tanımlanır.
- **3. Güncelleme bu kurulumla uyumlu mu?**
  - Donanım revizyonu, proje sürümü, bağlı cihazlar ve lisanslar uyumlu mu?
  - Uyumluluk yalnız üretici belgesine mi dayanıyor, yoksa temsil kabiliyeti bilinen bir ortamda denendi mi? Denenmediyse bu sınır yazılır.
- **4. Geri dönüş mümkün mü?**
  - Önceki sürüme dönüş üretici tarafından destekleniyor mu? Gereken dosya, parça ve araç elde mi?
  - Geri dönüş desteklenmiyorsa risk sınıfı yükseltilir ve ek onay alınır.
- **5. Uygun bir bakım penceresi bulunabiliyor mu?**
  - Süreç koşulu, mevsim/talep yükü, personel ve tedarikçi katılımı uygun mu?
  - Yakın pencere yoksa: geçici kontrol + planlı pencere tarihi + geçici kontrolün sahibi ve bitiş tarihi yazılır.
- **6. Telafi edici kontrol seçenekleri neler?**
  - Gereksiz dış erişimi azaltmak, yönetim yolunu daraltmak, kişiye özel ve süreli erişim uygulamak, ilgili kayıtları daha sık incelemek, yenileme planını öne çekmek.
  - Her seçenek için: etkinliği nasıl doğrulanacak, yan etkisi ne, sahibi kim, ne zaman kaldırılacak?
  - Geçici kontroller kalıcı bakım borcunu görünmez yapmamalıdır; bitiş tarihi olmayan geçici kontrol yazılmaz.
- **7. Karar ve kayıt.**
  - Seçenek: yama, yapılandırma değişikliği, erişim azaltma, ürün yenileme veya gerekçeli erteleme.
  - Kararın dayandığı bilgi, kalan belirsizlik, gözden geçirme tarihi ve sahibi yazılır.

Bir zafiyetin istismar edildiğinin bilinmesi öncelik girdisidir; kataloglarda bulunmamak güvenli olmanın kanıtı değildir. Yabancı düzenleyicilerin kendi kurumlarına koyduğu süreler, Türkiye'deki bir işletme için kendiliğinden yükümlülük oluşturmaz. Bu şablonda güncel zafiyet listesi veya son tarih yeniden üretilmez.

## 5. Kapanış

Değişiklik, işlem tamamlandığında değil, etkilediği belgeler güncellendiğinde kapanır.

- [ ] Envanter kaydı güncellendi: sürüm, donanım revizyonu, destek durumu, son değişiklik kimliği.
- [ ] Akış matrisi güncellendi: yeni, değişen veya kaldırılan akışlar ve gerekçeleri.
- [ ] Ağ/güvenlik kuralları ile akış matrisi karşılaştırıldı; eşleşmeyen kalan kayıtlar iş listesine alındı.
- [ ] Alarm ve algılama kartları gözden geçirildi: eşik, beklenen davranış ve normal açıklama değişti mi?
- [ ] Yedek kapsamı güncellendi; yeni sürüm için yedek alındı ve bütünlüğü doğrulandı.
- [ ] Kurtarma sırası ve bağımlılık listesi güncellendi.
- [ ] Uzak erişim kaydı kapatıldı; geçici yetkilerin sona erdiği doğrulandı.
- [ ] İşletme ve saha dokümanları (prosedür, etiket, çizim) güncellendi.
- [ ] Gözlem süresi tamamlandı; sonucu ve kanıtı kayda yazıldı.
- [ ] Kapanış onayı alındı; kalan çekinceler iş listesinde sahibiyle birlikte açık.

| Kapanış onayı | Rol | Kanıt | Tarih |
|---|---|---|---|
| Teknik kabul | [rol] | [kanıt kimliği] | [YYYY-AA-GG] |
| İşletme kabulü | [rol] | [kanıt kimliği] | [YYYY-AA-GG] |
| Kayıt kapanışı | [rol] | [kanıt kimliği] | [YYYY-AA-GG] |

## İlgili belgeler

- [Zafiyet ve değişiklik yönetimi](../docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md): duyurudan iş kaydına giden akış ve kabul kapıları.
- [Envanter ve akış şablonu](01-envanter-ve-akis.md): etkilenen varlık, akış ve bağımlılık bilgisinin kaynağı.
- [Tedarikçi ve uzak erişim şablonu](06-tedarikci-ve-uzak-erisim.md): değişiklik sırasında açılan erişimin kaydı.
- [Olay ve kurtarma şablonu](04-olay-ve-kurtarma.md): olay sırasında yapılan değişikliklerin sonradan kayda bağlanması.
- [Segmentasyon, kimlik ve uzak erişim](../docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md): kural değişikliklerinin kabul testiyle doğrulanması.

## Kaynak ve kapsam

- CISA ve ortaklar, *Secure by Demand: Priority Considerations for OT Owners and Operators when Selecting Digital Products*, 13 Ocak 2025, [PDF](https://www.cisa.gov/sites/default/files/2025-01/joint-guide-secure-by-demand-priority-considerations-for-ot-owners-and-operators-508c.pdf), erişim: 13.09.2026. Güvenli güncelleme mekanizması ve üretici desteği sorularının bağlamı için.
- CISA, *Known Exploited Vulnerabilities Catalog*, [dinamik katalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), erişim denemesi: 13.09.2026. Bu depoda doğrudan sayfa erişimi 403 verdi; katalog işlevi CISA'nın [BOD 22-01 açıklamasından](https://www.cisa.gov/sites/default/files/publications/Reducing_the_Significant_Risk_of_Known_Exploited_Vulnerabilities_20211103.pdf) doğrulanmıştır. Güncel liste veya son tarihler burada yeniden üretilmez.
- NIST, *SP 1339: OT Backup Quick Start Guide*, 17 Haziran 2026, [yayın kaydı](https://csrc.nist.gov/pubs/sp/1339/final), erişim: 13.09.2026. Yedeklerin değişiklik yönetimiyle ilişkilendirilmesi bağlamı için.

Alan listeleri, kabul planı, geri alma formu, karar ağacı ve kapanış listesi bu deponun **özgün eğitim sentezidir**; kaynak belgelerin çevirisi veya bir standardın resmî formu değildir. Bütün örnek değerler kurgusaldır; gerçek bir tesisi, ürünü, zafiyeti veya yapılandırmayı temsil etmez. Lisans ve atıf koşulları [LICENSE.md](../LICENSE.md) dosyasındadır.
