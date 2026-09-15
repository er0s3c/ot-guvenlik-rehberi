# Güvenlik bildirimi

Bu depo bir yazılım ürünü değil, eğitim içeriğidir. Çalışan bir servis, ağ hizmeti veya tesis bileşeni barındırmaz. Bu nedenle "güvenlik açığı bildirimi" burada iki ayrı anlama gelir ve iki ayrı şekilde ele alınır.

## Bildirim kapsamı

| Tür | Örnek | Neden önemli? |
|---|---|---|
| Depo altyapısı ve betik sorunu | `scripts/check_docs.py` içinde güvensiz dosya işleme, bir iş akışı yapılandırmasının gereğinden geniş yetkisi, bağımlılık kaynaklı risk | Depoyu yerelde çalıştıran kişiyi etkileyebilir |
| İçerikte yanlış veya zararlı olabilecek yönlendirme | Emniyeti azaltan bir öneri, yanlış anlaşılan kurtarma adımı, kaynağın desteklemediği kesin ifade, sınırları aşan saldırı ayrıntısı | Okur bunu bir tesiste uygularsa hizmet veya emniyet etkilenebilir |
| İçerik sınırının ihlali | Metne sızmış gerçek tesis verisi, adres, hesap bilgisi veya çalıştırılabilir saldırı adımı | Yayımlanmış olması zararı sürdürür; öncelikli olarak ele alınır |

Sıradan yazım hataları, kopuk bağlantılar ve kaynak güncellemeleri güvenlik bildirimi değildir; bunlar için [katkı rehberindeki](CONTRIBUTING.md) olağan akış kullanılır.

## Nasıl bildirilir?

- **Özel bildirim:** Deponun GitHub sayfasındaki **Security** sekmesinden özel güvenlik açığı bildirimi (private vulnerability reporting) yolunu kullanın. Bu yol, sorun giderilene kadar ayrıntının herkese açık olmamasını sağlar.
- **Özel yol görünmüyorsa:** Duyarlı ayrıntı içermeyen bir konu açın; yalnızca sorunun türünü ve etkilediği dosyayı yazın, ayrıntıyı paylaşmak için yönlendirme isteyin.
- **Yardımcı olan bilgiler:** Etkilenen dosya ve satır, sorunun nasıl ortaya çıktığı, beklenen ile gözlenen davranış farkı, içerik sorunlarında hangi cümlenin hangi nedenle yanıltıcı olduğu ve varsa doğru bilgiyi gösteren birincil kaynak.

Bu depo gönüllü katkıyla yürütülür. Bildirimler alındıkları sırayla ve etkilerine göre değerlendirilir. Kesin bir yanıt veya düzeltme süresi taahhüt edilmez; içerik sınırı ihlali niteliğindeki bildirimler öncelikli ele alınır. Düzeltme yapıldığında değişiklik [değişiklik kaydına](CHANGELOG.md) işlenir; isteyen bildirimci orada anılabilir.

## Bildirimde gönderilmemesi gerekenler

- Gerçek tesis, kurum veya saha verisi: ad, adres, koordinat, ağ şeması, IP adresi, kontrol projesi, koruma ayarı, alarm eşiği.
- Hesap bilgisi, parola, anahtar, sertifika, oturum kaydı veya kişisel veri.
- Canlı sistemlerden alınmış kayıt, yapılandırma dosyası veya ekran görüntüsü.
- İstismar kodu, yük veya çalıştırılabilir saldırı adımı.

Bir sorunu anlatmak için bu verilere gerek yoktur. Gerekliyse veriyi anonimleştirin veya yalnızca yapısal tarifle aktarın. Duyarlı veri içeren bir bildirim, içeriği kaydedilmeden geri çevrilebilir.

## Üçüncü taraf sistemlerdeki zafiyetler

Bir üründe, cihazda veya başka bir kurumun sisteminde zafiyet bulduysanız bu deponun bildirim yolu doğru adres değildir. Sıra şöyledir:

1. **Üreticinin kendi bildirim kanalı.** Çoğu üretici bir güvenlik bildirimi sayfası veya iletişim adresi yayımlar; ürünün resmî destek sayfasından doğrulayın.
2. **Ulusal koordinasyon.** Türkiye'de siber olay bildirimi ve koordinasyonu USOM (Ulusal Siber Olaylara Müdahale Merkezi) üzerinden yürütülür. Resmî sayfa: <https://www.usom.gov.tr/>. Erişim sırasında bu sayfa, ihbar ve CVE başvuru süreçlerinin Siber Güvenlik Başkanlığı'nın <https://www.siberguvenlik.gov.tr/> adresine taşındığını belirtiyordu (erişim: 13.09.2026). Güncel kanalı ve varsa ilgili SOME yapısını başvuru anında resmî sayfadan doğrulayın. Bu depoda e-posta adresi veya telefon numarası yayımlanmaz.
3. **Kendi kurumunuzun yükümlülükleri.** Bir işletmede çalışıyorsanız sözleşmeler, düzenleyici bildirim şartları ve kurum içi olay planı ayrıca geçerlidir; teknik bildirimden önce bunları değerlendirin.

Kritik altyapıda çalışan bir sistemde bulunan zafiyetin açıklanma takvimi, üretici ve işletmeciyle koordineli belirlenir. Bu deponun içeriği böyle bir açıklama için gerekçe veya yetki oluşturmaz.

## Kapsam dışı

- Bu depo üzerinden gerçek bir sistemin test edilmesi talebi veya böyle bir testin planlanması.
- İstismar kodu, saldırı aracı, tarama komutu veya belirli bir ürünü hedef alan prosedür isteği.
- Belirli bir tesisin mimarisi, ayarları veya zafiyet durumu hakkında değerlendirme isteği.
- Bir kuruma veya kişiye yönelik suçlama, atıf ya da kaynağı doğrulanmamış olay iddiası.

Bir tesiste yapılacak güvenlik değerlendirmesi yazılı kapsam, işletme sorumlusunun onayı ve emniyet değerlendirmesi gerektirir. Bu koşullar bu depo tarafından sağlanamaz.

## Kapsam notu

Bu dosya, deponun özgün bildirim politikasıdır; bir standardın veya zorunlu bildirim rejiminin çevirisi değildir. Kurum ve süreç adları, erişim tarihinde resmî sayfalarından doğrulanmıştır; kurumsal yapı ve kanallar değişebilir. Erişim: 13.09.2026.
