# OT'ye saldırgan bakış açısıyla tehdit modelleme

> Amaç: Bir saldırganın hangi güven varsayımını bozabileceğini anlamak ve bunu gözlem, kontrol ve kurtarma gereksinimine çevirmek. Buradaki örnekler kurmaca mimari değerlendirmelerdir; gerçek tesislerde uygulanacak saldırı adımları değildir.

## 1. Önce korunacak işlevi tanımla

OT değerlendirmesinde başlangıç noktası bir IP adresi değil, sürdürülmesi gereken hizmettir. NIST, OT güvenliğinin performans, güvenilirlik ve emniyet gereksinimleriyle birlikte ele alınmasını ister. Bu nedenle bir güvenlik bulgusunun anlamı, bağlı olduğu fiziksel süreç ve işletme koşullarından ayrı değerlendirilemez. [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

Bu rehber için önerilen çalışma sırası şöyledir: hizmeti tanımla, hizmeti gerçekleştiren işlevleri çıkar, bağımlılıkları göster, güven sınırlarını işaretle ve her sınır için kötüye kullanım varsayımı yaz. Örneğin “su tesisinin ağı” çok geniştir; “depo seviyesinin güvenilir biçimde izlenmesi ve pompa işletmesinin sürekliliği” incelenebilir bir işlevdir. Operasyon ekibi bu işlevin kabul edilebilir kesintisini, bağımsız doğrulama olanağını ve geri dönüş koşullarını tanımlar.

Bir **tehdit**, zarar doğurabilecek olay veya kaynaktır; **zafiyet**, olayın gerçekleşmesine elverişli zayıflıktır. **Önkoşul**, belirli senaryonun başlayabilmesi için doğru olması gereken varsayımdır. **Etki**, olay gerçekleştiğinde ortaya çıkan sonuçtur. Bu ayrım risk değerlendirmesini sadece yazılım açıklıklarının listesine indirgememeyi sağlar. [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

## 2. Giriş yüzeyleri ve güven sınırları

Güven sınırı, farklı yetki veya güven varsayımlarının karşılaştığı yerdir. Şirket ağı ile OT bölgesi arasındaki geçiş kadar, aynı saha içinde operatör hesabından mühendislik yetkisine geçiş de önemlidir. Resmî MITRE tanımları dış uzaktan erişimi, geçerli hesapların kötüye kullanımını ve ortamlar arasında dolaşan bakım bilgisayarlarını ayrı davranış sınıfları olarak ele alır. [T0822](https://attack.mitre.org/techniques/T0822/), [T0859](https://attack.mitre.org/techniques/T0859/), [T0864](https://attack.mitre.org/techniques/T0864/)

Aşağıdaki matris özgün bir değerlendirme örneğidir. “Olası etki” sütunu gerçekleşmiş olay veya kaçınılmaz sonuç anlamına gelmez. Her satırın tesis sahibince doğrulanması gereken varsayımları vardır.

| Giriş yüzeyi ve önkoşul | Saldırganın hedefi | Aşılan güven sınırı | Olası etki | Gözlem ve doğrulama | Önleyici veya sınırlayıcı kontrol |
|---|---|---|---|---|---|
| Tedarikçi erişimi; kullanılabilir hesap ve gereğinden geniş erişim yolu | Yetkisiz bakım oturumu oluşturmak | Tedarikçi ortamı → OT erişim noktası | İşletme araçlarına yetkisiz erişim | Erişim kaydı, iş emri, operatör onayı ve oturum süresini birleştir | Kişisel hesap, çok faktörlü doğrulama, süreli onay, kontrollü erişim sunucusu |
| Bakım dizüstüsü; birden fazla ortamda kullanılması | Güvenilen bakım cihazının yetkisini devralmak | Harici ortam → saha mühendislik alanı | Proje dosyasının bütünlüğünün bozulması | Cihaz kabul kaydı, dosya bütünlüğü, bağlantı geçmişi | Ayrılmış bakım cihazı, giriş kontrolü, onaylı dosya aktarımı |
| IT–OT veri aktarımı; gereksiz çift yönlü izin | Raporlama bağlantısını yönetim yoluna dönüştürmek | İş ağı → endüstriyel ara bölge → kontrol ağı | Erişim alanının genişlemesi | Onaylı akış listesiyle gerçek bağlantıların karşılaştırılması | İşlev bazında izin, ayrı kimlikler, gereksiz geri bağlantıların kaldırılması |
| Mühendislik iş istasyonu; geniş değişiklik yetkisi | Yetkisiz yapılandırmayı meşru işlem gibi göstermek | Bakım yetkisi → kontrol cihazı | Kontrol davranışının değişmesi | Sürüm farkı, değişiklik kaydı, cihazın yapılandırma olayı | Rol ayrımı, ikinci kişi incelemesi, doğrulanmış geri dönüş kopyası |
| Saha haberleşmesi; mesaj kaynağının yeterince doğrulanmaması | Ölçüm veya komutun güvenilirliğini bozmak | Haberleşme ortamı → güvenilen süreç verisi | Görünürlük kaybı veya hatalı karar | Zaman damgası, kalite bilgisi, bağımsız ölçüm karşılaştırması | Uygun kimlik doğrulama, erişim kısıtı, iletişim kaybı prosedürü |
| Historian veya gösterge ekranı; tek bilgi kaynağına bağımlılık | Operatörün durumu yanlış değerlendirmesine yol açmak | Ham ölçüm → işletme kararı | Yanlış müdahale ya da gecikmiş tepki | Yerel gösterge, alternatif ölçüm ve olay kaydı arasında tutarlılık | Bağımsız doğrulama, veri eskimesi uyarısı, ekran değişiklik kontrolü |
| Paylaşılan kimlik veya yedekleme hizmeti; IT ile ortak bağımlılık | İşletmenin destek hizmetlerini kullanılamaz kılmak | Ortak hizmet → OT sürekliliği | Kontrol cihazı değişmeden hizmetin durması | Bağımlılık envanteri, kimlik ve yedek erişim kayıtları | Ayrı kurtarma kimlikleri, çevrimdışı kopyalar, bağımlılık kaybı tatbikatı |

Matrisin okunması bir bağlantının varlığını kanıtlamaz. Örneğin historian üzerinden kontrol ağına yönetim erişimi ancak gerçek izinler buna olanak tanıyorsa senaryoya dönüşür. Mimari çizimde bulunan bir güvenlik duvarı da tek başına etkili ayrım kanıtı değildir; izinlerin sahibi, gerekçesi ve gözlenen kullanım birlikte incelenir.

## 3. Kavramsal yaşam döngüsü

Bu bölüm doğrusal bir saldırı tarifi yerine inceleme mercekleri sunar. Bir olay bazı aşamaları atlayabilir; aynı anda birden çok hedef izleyebilir. MITRE, taktikleri saldırganın amacı, teknikleri bu amacı gerçekleştiren davranış sınıfları olarak tanımlar. [MITRE ATT&CK SSS](https://attack.mitre.org/resources/faq/)

1. **Erişim olanağı:** Hangi bağlantı, hesap veya bakım ilişkisi güvenilir kabul ediliyor? Savunma çıktısı, bağlantıların sahipliğini ve gerekli yetkileri gösteren listedir.
2. **Yetki ve bağlam:** Erişim elde edildiği varsayıldığında hangi varlıkların işlevi anlaşılabilir? Savunma çıktısı, proje belgeleri ve yönetim yetkilerinin erişim incelemesidir.
3. **Güven sınırı geçişi:** Bir kullanıcının yetkisi hangi başka sisteme taşınabiliyor? Savunma çıktısı, işlevle gerekçelendirilmiş akış ve kimlik ayrımıdır.
4. **İşletme durumuna müdahale:** Yazılım, parametre veya görüntü değişikliği hangi kararları etkileyebilir? Savunma çıktısı, onaylı başlangıç durumu ve değişiklik izidir.
5. **Etkinin sınırlandırılması:** Yerel kontrol, bağımsız koruma ve insan müdahalesi hangi koşullarda hizmeti koruyabilir? Savunma çıktısı, operasyon ekibince sınanmış geçiş prosedürüdür.
6. **Kurtarma:** Güvenilir duruma geri dönüldüğü nasıl anlaşılacak? Savunma çıktısı, dosyaların geri yüklenmesinin ötesinde işlevsel kabul ölçütleridir.

## 4. Siber etki neden fiziksel etkiye eşit değildir?

Bir mühendislik dosyasının değişmesi, değişikliğin cihazda etkinleştiğini göstermez. Etkinleşmesi de süreçte beklenen sonucu doğurduğunu kanıtlamaz. Kontrolün hangi çalışma modunda olduğu, yerel mantığın davranışı, fiziksel kapasite, bağımsız korumalar ve operatörün müdahalesi ayrıca değerlendirilir. Bu, süreç mühendisliğiyle birlikte sınanacak bir analiz çerçevesidir; herhangi bir korumanın her koşulda başarılı olacağı varsayılmaz.

Benzer biçimde hizmet kesintisi, saldırganın saha kontrolünü ele geçirdiğini tek başına göstermez. Colonial Pipeline yönetiminin 2021 kongre ifadesi, IT fidye yazılımı olayının kapsamı belirsizken yayılımı sınırlamak için işletmenin durdurulduğunu anlatır. [9 Haziran 2021 oturum tutanağı, basılı s. 13](https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/pdf/CHRG-117hhrg45085.pdf)

Bu nedenle değerlendirme dört ayrı sonuç kaydeder: **siber bütünlük kaybı**, **kontrol veya görünürlük etkisi**, **hizmet etkisi**, **fiziksel/emniyet etkisi**. Her sonuç için “gözlendi”, “mümkün olduğu değerlendiriliyor” veya “bilinmiyor” yazılır. Örneğin ekrandaki olağandışı değer gözlemdir; bağımsız ölçüm yokken gerçek su kalitesinin bozulduğunu söylemek bir çıkarımdır ve ayrıca kanıt ister.

## 5. İzinli değerlendirmenin kapsamı

Önerilen başlangıç, belge incelemesi ve mevcut kayıtların değerlendirilmesidir. Ardından laboratuvar veya dijital model üzerinde hipotezler ele alınır. Üretimde veri toplama yöntemi bile işletme sorumlusuyla belirlenir; “yalnızca okuma” ifadesi cihazın ek yükten etkilenmeyeceğinin kanıtı değildir. NIST, OT güvenlik önlemlerinin işletme ve emniyet gereksinimlerini gözetmesini vurgular. [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

Yazılı kapsamda varlık sahibi, incelenecek alan, çalışma zamanı, izinli veri kaynakları, sorumlu operatör, iletişim kanalı, durdurma ölçütü ve kurtarma sorumlusu bulunmalıdır. Bulut hizmeti veya tedarikçi bağlantısı, tesisin onayıyla otomatik olarak kapsam içine girmez. Yetki, bağlantılı sistemlerin sahipliğiyle birlikte değerlendirilir. Bu bir çalışma önerisidir; belirli bir ülkeye ilişkin hukuki görüş değildir.

Başarı ölçütü “tesisi durdurabildik” olmamalıdır. Daha yararlı çıktılar, izinsiz bakım oturumunun fark edilmesi, beklenmeyen proje farkının incelemeye düşmesi ve bağımsız işletme bilgisinin erişilebilir kalmasıdır. Rapor, her bulguyu bir varlığa, bir hizmete, bir kanıta, bir sorumluya ve doğrulanabilir düzeltme ölçütüne bağlamalıdır.

## Kaynaklar

Erişim tarihi bütün kaynaklar için **2026-09-13**.

- **NIST**, [SP 800-82 Rev. 3: Guide to Operational Technology Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final), Eylül 2023. OT güvenliği ile performans, güvenilirlik ve emniyet ilişkisini destekler.
- **NIST**, [SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Eylül 2012. Tehdit, zafiyet ve etkiyi ayrı değerlendirme yaklaşımını destekler.
- **MITRE**, [T0822](https://attack.mitre.org/techniques/T0822/) ve [T0859](https://attack.mitre.org/techniques/T0859/), son değişiklik 12 Mayıs 2026; [T0864](https://attack.mitre.org/techniques/T0864/), son değişiklik 15 Nisan 2025. Uzaktan erişim, hesap ve geçici bakım varlığı sınıflarını doğrular.
- **MITRE**, [Frequently Asked Questions](https://attack.mitre.org/resources/faq/), yaşayan sayfa; yayın tarihi belirtilmemiş. Taktik ve teknik ayrımını destekler.
- **ABD Temsilciler Meclisi, Homeland Security Committee**, [Cyber Threats in the Pipeline](https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/pdf/CHRG-117hhrg45085.pdf), 9 Haziran 2021. Colonial yönetiminin işletmeyi durdurma gerekçesine ilişkin birinci el ifadesini içerir.

**Devam:** [MITRE ATT&CK for ICS ile savunma eşleştirmesi](02-mitre-attack-ics.md) · [Gerçek vakalar](03-gercek-vakalar.md)
