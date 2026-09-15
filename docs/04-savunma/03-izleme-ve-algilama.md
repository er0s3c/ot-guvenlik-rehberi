# İzleme ve algılama

Bir OT alarmının değeri, hangi fiziksel işlevle ilişkili olduğunun ve hangi kararı desteklediğinin bilinmesidir. “Şüpheli trafik bulundu” ifadesi operatör için yetersizdir. Varlık, kullanıcı, işlem, çalışma modu, beklenen davranış ve süreç belirtisi birlikte sunulmalıdır.

## Veri katmanları

| Veri | Ne gösterir? | Tek başına neyi göstermez? |
|---|---|---|
| Erişim kapısı / VPN | Giriş, kimlik, süre, kaynak ve hedef | Hedefte ne yapıldığını |
| Hedef denetim kaydı | Kullanıcı işlemi, yapılandırma veya rol değişimi | Fiziksel sonucu |
| Pasif ağ gözlemi | Konuşan uçlar, bağlantı yapısı, destek varsa protokol anlamı | Şifreli içeriği veya gözlem dışı segmenti |
| Historian ve süreç alarmları | Ölçüm, kalite, tazelik, süreç değişimi | Verinin bağımsız doğruluğunu |
| Değişiklik / iş emri | Beklenen bakım kapsamı ve onay | İşlemin gerçekten bu kapsamda kaldığını |
| Saha / koruma kaydı | Fiziksel duruma ilişkin ek kanıt | Bütün dijital erişim yollarını |

Bu sınırlamalar birleştirme ihtiyacını gösterir. Aynı sistemden türetilmiş iki kayıt bağımsız kanıt değildir. Zaman senkronizasyonu ve farklı saat dilimleri hesaba katılmadan olay sırası kesinleştirilmez.

## Örnek algılama kartları

Aşağıdakiler ürün bağımsız özgün analitik tasarımlarıdır. OT protokolüne gönderilecek komut veya gerçek tesiste çalıştırılacak kural değildir.

| Gözlem | Birleştirilecek bağlam | Normal açıklama | Sonraki karar |
|---|---|---|---|
| Bakım penceresi dışında mühendislik oturumu | Kullanıcı, hedef, vardiya ve iş emri | Onaylı acil bakım | Onayın kapsamını teyit et; yetkiyi işletmeyle değerlendir |
| Proje/ayar kimliği değişti | Önceki onaylı sürüm, yükleme kaydı, kullanıcı | Planlı sürüm geçişi | Yeni sürümün yetki ve doğrulama kaydını incele |
| Yeni iletişim çifti görüldü | Envanter, ağ değişikliği, tedarikçi yolu | Değiştirilen cihaz veya yeni toplayıcı | İşlev ve sahip belirlenene kadar inceleme aç |
| HMI değeri sabit, kalite eski | Sensör kalitesi, haberleşme, bağımsız gösterge | Bağlantı veya sensör arızası | Operatörün güvenilir veriyle karar verebildiğini teyit et |
| Oturum kaydı kesildi | Toplayıcı sağlığı, depolama, ağ, saat | Bakım veya kapasite sorunu | Kanıt boşluğunu olay kaydına ekle |
| Birçok sahada eşzamanlı güç/iletişim alarmı | Bölgesel olay, ortak taşıyıcı, güç bağımlılığı | Enerji veya operatör arızası | Ortak bağımlılık incelemesini başlat |

Teknik adlarla eşleştirme için [MITRE ATT&CK for ICS tablosu](../03-tehdit-modelleme/02-mitre-attack-ics.md) kullanılabilir. MITRE, davranışı adlandırır; kendi başına yerel alarm doğruluğunu veya risk önceliğini belirlemez. [Resmi ICS matrisi](https://attack.mitre.org/matrices/ics/)

## SOC'tan işletmeye aktarım

Alarmın ilk satırı şöyle olabilir: “Kurgusal A sahasında, bakım hesabının B hedefindeki oturumu onay süresinden sonra devam ediyor; süreç bozukluğu henüz doğrulanmadı.” Ardından bilinenler, bilinmeyenler, destekleyen kayıtlar ve karar sahibi belirtilir. “Sistem ele geçirildi” gibi kanıtın ötesine geçen özetler kullanılmaz.

İşletmeye bildirim kanalı ve nöbetçi roller önceden tanımlanır. Güvenlik ekibinin otomatik karantina yetkisi, süreç etkisi değerlendirilmiş belirli varlıklarla sınırlandırılmalıdır. İş istasyonu, kontrolör ve emniyet sistemine aynı müdahale kuralı uygulanmaz.

## Ölçmek

Alarm sayısını artırmak başarı ölçütü değildir. Örnek ölçütler: gerekli bağlamı tam olan alarm oranı, işletme teyidine ulaşma süresi, kanıt kaybı yaşanan olay oranı ve yanlış pozitiflerin neden dağılımı. Ortalama süre yanında geciken kritik olayları da inceleyin. Eşikler ve hedefler tesise özgü belirlenir.

[Algılama kartı şablonu](../../templates/03-algilama-karti.md) ve [çevrimdışı kayıt alıştırması](../../labs/01-kayit-analizi.md) bu iş akışını çalıştırmak içindir.

## Kaynak

- MITRE, *ATT&CK for ICS Matrix*, [canlı matris](https://attack.mitre.org/matrices/ics/), erişim: 13.09.2026. Teknik sözlüğü için; bu belgedeki algılama tasarımları özgün öneridir.
