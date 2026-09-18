# Ders, teslim ve değerlendirme şablonu

[Ana sayfa](../README.md) · [Şablonlar](README.md) · [Öğrenme yolu](../docs/00-ogrenme-yolu.md) · [Final proje teslimleri](09-final-proje-teslimleri.md)

Bu şablon, bir OT konusunu kaynaklı açıklamadan gerekçeli bir belge teslimine dönüştürür. **Bu deponun özgün eğitim önerisidir**; bir standardın sınavı, sertifika ölçütü veya canlı test yetkisi değildir. Depodaki boş form kopyalanarak doldurulur. Alıştırma, kurgusal mimari ve sentetik kayıtlarla Markdown üzerinde tamamlanabilir; yazılım, sanal makine veya cihaz kurulumu zorunlu değildir.

## 1. Ders kimliği ve çalışma sınırı

| Alan | Doldurulacak değer |
|---|---|
| Ders / konu kimliği | [DERS-001], ana kapsam numarası: [1–50], konu: [ad] |
| Hazırlayan ve değerlendiren | [öğrenci kaydı veya rol], [değerlendiren rol / öz değerlendirme] |
| Sürüm ve tarih | [sürüm], [YYYY-AA-GG], saat dilimi: [dilim] |
| Önkoşul | [önceki ders / gerekli kavram], kanıtı: [teslim kimliği] |
| Öğrenme çıktısı | [bu çalışmanın sonunda açıklanacak, karşılaştırılacak veya üretilecek somut çıktı] |
| Senaryo ve varsayımlar | [kurgusal hizmet, varlıklar, verilen bilgiler ve bilinmeyenler] |
| Çalışma biçimi | [belge incelemesi / sentetik kayıt analizi / masa başı tasarım] |
| Girdi dosyaları | [depo bağlantıları veya kurgusal kanıt kimlikleri] |
| Kapsam dışı | [bu çalışmada incelenmeyen işlev ve yöntemler] |
| Hedef teslim tarihi | [YYYY-AA-GG]; zaman tahmini: [öğrencinin planlama varsayımı] |
| Sonuç durumu | [taslak / teslim edildi / düzeltme gerekiyor / kabul edildi] |

Öğrenme çıktısını "OPC UA'yı öğrenmek" yerine "sertifika güveni ile kullanıcı yetkisini ayıran bir kontrol tablosu hazırlamak" gibi doğrulanabilir yazın. Verilmemiş bir ürün sürümü, fiyat veya test sonucu tahminle tamamlanmaz; ilgili alan `doğrulanacak` olarak işaretlenir.

## 2. Yirmi alanlı ders sözleşmesi

Her alanın cevabı bu hücreye veya bağlantı verilen ders bölümüne yazılır. Alan konuya uygulanmıyorsa `uygulanamaz — [neden]` kullanılır; boş hücre bırakılmaz. Böylece bütün derslerde yirmi uzun başlık tekrar etmek gerekmez.

| No | Alan | Doldurulacak açıklama / çıktı | Kanıt veya kapsam notu |
|---|---|---|---|
| 1 | Tanım | [kavramın ne olduğu ve karıştırılan bir terimden farkı] | [birincil kaynak / özgün açıklama] |
| 2 | OT için önemi | [etkilenen hizmet, süreç veya karar] | [senaryodaki varlık/işlev kimliği] |
| 3 | IT'den farkı | [gecikme, süreklilik, emniyet, yaşam döngüsü veya erişim farkı] | [koşul ve kaynak] |
| 4 | Mimari | [bileşenler, güven sınırı, veri/kontrol akışı; diyagram bağlantısı] | [varlık ve akış kimlikleri] |
| 5 | Protokol / teknoloji | [protokol, profil, sürüm, taşıma ve gerekli teknoloji] | [belge sürümü; porttan çıkarım varsa işaretle] |
| 6 | Güvenlik riskleri | [tehdit, maruz kalma, mevcut kontrol, hizmet etkisi] | [risk kimliği; bilinmeyenler] |
| 7 | Saldırı senaryosu | [hedef, mevcut kabul edilen ön koşul ve aşılan güven sınırı] | [olası etki, gözlenebilir belirti ve kontrol] |
| 8 | Savunma | [kontrolün konumu, sahibi ve neyi sınırlandırdığı] | [kabul kanıtı ve kalan risk] |
| 9 | Artılar | [hangi gereksinimi hangi koşulda karşılar?] | [iddianın kaynağı veya özgün karar gerekçesi] |
| 10 | Eksiler | [uyumluluk, kör nokta, hata/bağımlılık veya bakım yükü] | [sınır ve telafi seçeneği] |
| 11 | Maliyet | [lisans, donanım, entegrasyon, emek, destek ve süre] | [fiyat kaynağı/tarihi veya açık kurgusal varsayım] |
| 12 | Açık kaynak / düşük maliyet | [alternatifin karşıladığı ve karşılamadığı işlevler] | [lisans/sürüm kaynağı; maliyetsiz işletim varsayma] |
| 13 | Ticari çözümler | [gereksinimle ilişkili ürün/paket ve seçim ölçütü] | [resmî belge; doğrulanmayan fiyat için teklif gerekli] |
| 14 | Üretici örneği | [üretici, model, firmware/yazılım, ilgili özellik] | [sürümle sınırlı kaynak; aileye genelleme yapma] |
| 15 | Lab / belge uygulaması | [kurgusal girdi, görev ve üretilecek belge] | [girdi bağlantısı; kurulum gerektirmeyen seçenek] |
| 16 | Test / doğrulama | [sınanacak iddia, beklenen olumlu/olumsuz sonuç] | [tasarım mı, yürütülmüş belge kontrolü mü?] |
| 17 | Sık hata | [hata, etkisi, fark edilme yolu ve düzeltme] | [senaryo veya kaynak] |
| 18 | Gerçek vaka | [kaynakta doğrulanan olay, belirsizlik ve çıkarılan ders] | [birincil olay kaynağı; yoksa uygulanamaz gerekçesi] |
| 19 | CV / portföy | [üretilen belgenin adı, kapsamı ve kişisel katkı] | [kurgusal çalışma etiketi; saha testi iddiası yok] |
| 20 | İleri çalışma | [açık soru, gerekli ek bilgi ve sonraki inceleme] | [önkoşul ve kaynak/teslim bağlantısı] |

Saldırı alanı çalıştırılabilir işlem tarifi istemez; [tehdit modeli şablonundaki](02-tehdit-modeli.md) altı bilgiyi kullanır. Ürün, lisans ve fiyat alanları güncel birincil belgeyle doldurulur; araştırma yapılamadıysa eksik açıkça görünür bırakılır.

## 3. THEORY → LAB → TEST → DEFENSE → REPORT teslimi

| Aşama | Görev | Doldurulacak teslim kaydı |
|---|---|---|
| THEORY | Kavramı, OT'deki önemini ve bir IT farkını senaryoyla açıkla | [açıklama bağlantısı], kaynak: [KNT-...] |
| LAB | Verilen girdilerle mimari, matris veya kayıt analizi üret | [belge/diyagram/tablo], kullanılan girdiler: [kimlikler] |
| TEST | İddiaları verilen kanıtla karşılaştır; karşı örnek veya eksik veriyi göster | [TST-...], yöntem: [belge kontrolü], gerçek sonuç: [sonuç / yürütülmedi] |
| DEFENSE | Bulgulara uygun kontrol seç; süreç etkisini ve kalan riski açıkla | [BUL-...] → [kontrol] → [kabul kanıtı], kalan: [RSK-...] |
| REPORT | Sonucu, sınırları, sahipleri ve açık işleri kısa raporla | [rapor bağlantısı], açık işler: [kimlikler] |

**TEST** aşaması bir cihazda teknik test yapılmasını zorunlu kılmaz. Örneğin CSV'deki oturum saatini iş emriyle karşılaştırmak yürütülebilir bir belge kontrolüdür. Bir firewall'ın engellediğini gösteren test planı hazırlamak ise planlamadır; ilgili cihaz testinin yapıldığı anlamına gelmez.

### Kanıt kaydı

| Kanıt kimliği | İçerik ve kaynak | Üretilme / erişim tarihi | Tür | Desteklediği iddia | Sınırı |
|---|---|---|---|---|---|
| [KNT-001] | [dosya, bölüm, satır veya kaynak URL'si] | [tarih ve gerekiyorsa saat dilimi] | [sentetik girdi / öğrenci çıktısı / kaynak belge / plan] | [iddia] | [kanıtlamadığı nokta] |

### Doğrulama kaydı

| Test kimliği | Sınanan iddia ve yöntem | Beklenen sonuç | Gerçek gözlem | Kanıt | Durum |
|---|---|---|---|---|---|
| [TST-001] | [iddia], [yalnız belge/sentetik veri incelemesi] | [önceden belirlenmiş ölçüt] | [gözlem veya yürütülmedi] | [KNT-...] | [tasarlandı / yürütüldü / kanıt yetersiz] |

## 4. Ortak 0 / 1 / 2 rubriği

Bu beş ölçüt, yeni ders teslimlerinin ortak değerlendirmesi için özgün bir öneridir. [Mevcut üç laboratuvarın](../labs/README.md) 12, 18 ve 24 puanlık ölçekleri korunur; bu ölçeğe dönüştürülmez ve toplamları karşılaştırılmaz. Bir eski lab kullanıldıysa kendi sonucu ek belge olarak tutulur; aşağıdaki puan dersin beş teslimine ayrı verilir.

| Ölçüt | 0 — eksik | 1 — kısmen yeterli | 2 — gerekçeli ve tamam |
|---|---|---|---|
| THEORY | Temel kavram yanlış veya açıklama yok | Tanım doğru; OT/IT farkı veya kaynak eksik | Kavram, OT etkisi ve fark kaynaklı örnekle açıklanmış |
| LAB | Teslim yok veya verilen girdilerle ilgisiz | Çıktı var; kimlik, akış veya varsayım eksik | Çıktı girdilere bağlı; kimlikler tutarlı, bilinmeyenler açık |
| TEST | Sonuç uydurulmuş veya iddia sınanmamış | Beklenen sonuç var; kanıt/sınır ayrımı eksik | Olumlu/olumsuz durum ve kanıt sınırı açık; yürütülmeyen plan etiketli |
| DEFENSE | Kontrol önerisi yok veya etkisi açıklanmamış | Kontrol bulguya bağlı; işletme etkisi/kalan risk eksik | Kontrol, sahip, süreç etkisi, kabul kanıtı ve kalan risk bağlantılı |
| REPORT | Bulgular izlenemiyor veya rapor yok | Ana sonuç var; sahip/açık iş/kapsam eksik | Karar, kanıt, belirsizlik ve düzeltme işleri izlenebilir |

| Aşama | Puan | Gerekçe ve kanıt | Gerekli düzeltme |
|---|---|---|---|
| THEORY | [0/1/2] | [gerekçe, KNT-...] | [iş veya yok] |
| LAB | [0/1/2] | [gerekçe, KNT-...] | [iş veya yok] |
| TEST | [0/1/2] | [gerekçe, KNT-...] | [iş veya yok] |
| DEFENSE | [0/1/2] | [gerekçe, KNT-...] | [iş veya yok] |
| REPORT | [0/1/2] | [gerekçe, KNT-...] | [iş veya yok] |
| Toplam | [0–10] | [beş puanın toplamı] | [karar] |

Önerilen kabul: **en az 8/10, hiçbir aşamada 0 olmaması ve kritik düzeltmenin açık kalmaması**. Bu eşik bir yetkinlik standardı veya bilimsel başarı garantisi değildir. Kritik düzeltme örnekleri: yapılmamış testi yapılmış göstermek, kurgusal çalışmayı saha deneyimi diye sunmak, kaynaksız ürün/fiyat bilgisini doğrulanmış saymak veya verilen senaryonun emniyet kararını yetkisiz role atamak. Eşik kullanılacaksa değerlendirme başlamadan belirlenir; sonuç görüldükten sonra değiştirilmez.

## 5. Geri bildirim, düzeltme ve ilerleme

| Düzeltme kimliği | İlgili alan / kanıt | Sorun | Beklenen düzeltme | Öğrenci yanıtı | Yeniden inceleme sonucu |
|---|---|---|---|---|---|
| [DZL-001] | [alan no / aşama / KNT-...] | [somut hata veya boşluk] | [ölçülebilir kabul] | [düzeltilen belge ve sürüm] | [açık / kapandı; gerekçe] |

| Kayıt | Doldurulacak karar |
|---|---|
| Teslim alındı | [tarih, sürüm, dosya bağlantıları] |
| Değerlendirme tamamlandı | [rol / öz değerlendirme], [puan], [gerekçe] |
| İlerlemeyi engelleyen açık iş | [DZL-... / yok] |
| Son karar | [düzeltme gerekli / bölüm kabul edildi] |
| Sonraki bölüm | [ders kimliği ve önkoşul]; geçiş kaydı: [tarih veya bekliyor] |

Teslim ve değerlendirme kaydı olmadan bölüm "tamamlandı" sayılmaz. Düzeltme gerekiyorsa öğrenci aynı teslimin yeni sürümünü gönderir; önceki değerlendirme korunur. Öz değerlendirme yapıldıysa bağımsız eğitmen onayı varmış gibi yazılmaz. Final projeye taşınacak çıktı [teslim şablonundaki](09-final-proje-teslimleri.md) ilgili kimliğe bağlanır.

## Kaynak ve kapsam

Bu form, yirmi ders alanı ile beş teslim aşamasını bir araya getiren özgün eğitim sentezidir. Teknik iddiaların kaynakları doldurulan dersin içinde tutulur. Kaynak ve veri disiplini için [katkı rehberi](../CONTRIBUTING.md), kanıtlı çalışma için [mevcut laboratuvarlar](../labs/README.md) esas alınır. Formun son inceleme tarihi: **17.09.2026**.
