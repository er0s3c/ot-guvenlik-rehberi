# OT nedir?

**OT (Operational Technology, operasyonel teknoloji)** fiziksel ortamı izleyen veya değiştiren programlanabilir sistemler ve cihazlardır. Su seviyesini ölçen sistem, vanayı yöneten kontrolör, bina havalandırma otomasyonu ve ulaştırma kontrolü bu çerçevede ele alınabilir. NIST, OT güvenliğinin performans, güvenilirlik ve emniyet gereksinimleriyle birlikte düşünülmesini ister. [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

## Bir günlük hayat örneği

Kurgusal bir binada depodaki su seviyesini sensör ölçsün. Kontrolör bu ölçümü değerlendirip pompayı yönetsin. Görevli ekrandan seviyeyi ve arızaları görsün. Burada sensör, kontrolör, pompa sürücüsü ve operatör arayüzü birlikte OT işlevi oluşturur. Faturaların tutulduğu uygulama ise bir IT işlevi görür. Aynı bilgisayarın veya ağın iki işlevi birden desteklemesi aradaki risk ayrımını ortadan kaldırmaz.

Bu örnekte bir bilgi güvenliği olayını yalnızca “veri sızdı mı?” diye incelemek eksiktir. Gösterilen seviye eskiyse görevli yanlış karar verebilir. Kontrolör haberleşmeyi kaybettiğinde pompanın davranışı cihazın tasarımına bağlıdır. Elektrik kesildiğinde doğru yazılım bile hizmet veremez. Olayı anlamak için veri, fiziksel süreç ve insan kararını beraber incelemek gerekir.

## Terimleri yerli yerine koymak

| Terim | Ne anlatır? | Kurgusal örnekte karşılığı |
|---|---|---|
| IT | Bilginin işlenmesi ve kurumsal hizmetler | Faturalama, e-posta, insan kaynakları |
| OT | Fiziksel süreçle etkileşen teknoloji | Pompa ve seviye kontrolü |
| ICS | Endüstriyel kontrol sistemleri; OT içinde kullanılan yaygın şemsiye terim | Kontrolör, arayüz ve kontrol ağı bütünü |
| SCADA | Dağıtık süreçleri merkezi gözetleme ve veri toplama düzeni | Farklı depoların merkezden izlenmesi |
| DCS | Bir proses tesisindeki dağıtılmış kontrol işlevlerinin bütünleşik düzeni | Birden fazla proses ünitesinin ortak işletilmesi |
| IIoT | Endüstriyel sensör ve hizmetlerin bağlantılı veri ekosistemi | Bakım tahmini için ayrı ağ geçidine aktarılan ölçümler |

ICS, SCADA ve DCS kelimeleri birbirinin birebir yerine kullanılmaz; gerçek kurulumlar işlevleri birleştirebilir. Tablodaki örnekler öğretim amaçlıdır; ürün sınıflandırması değildir.

## IT bilgisini OT'ye taşırken ne değişir?

Aşağıdaki tablo bir değerlendirme çerçevesidir; bütün IT veya OT sistemleri için değişmez kural değildir.

| Soru | OT açısından araştırılacak konu |
|---|---|
| Yeniden başlatabilir miyiz? | Çalışan ekipmanın ve operatörün bu kesintideki davranışı |
| Güncelleme var mı? | Üretici desteği, proje uyumluluğu, yedek ve geri alma imkânı |
| Ağ bağlantısını kesebilir miyiz? | Yerel kontrol, emniyet işlevi, gözlem ve koordinasyon üzerindeki etki |
| Başka sunucuya taşıyabilir miyiz? | Zamanlama, lisans, sürücü, donanım ve saha arayüzü bağımlılığı |
| Şifreleme açabilir miyiz? | İki ucun desteği, sertifika yaşam döngüsü, gecikme ve izleme etkisi |
| Alarm kesin saldırı mı? | Bakım, arıza, vardiya değişimi ve süreç geçişiyle ilişkisi |

Gizlilik, bütünlük ve erişilebilirlik OT'de birlikte önemlidir. “OT'de gizlilik önemsizdir” veya “her zaman erişilebilirlik ilk sıradadır” kestirmeleri doğru tasarım üretmez. Emniyetli duruş gereken bir durumda sürekli çalışmayı sürdürmek daha kötü sonuç verebilir; hizmetin emniyet içinde sürmesi gereken başka bir durumda gereksiz duruş da risk yaratabilir.

## İnsanlar ve sorumluluklar

Operatör sürecin o anki durumunu, otomasyon mühendisi kontrol tasarımını, bakım ekibi fiziksel ekipmanı, güvenlik ekibi dijital belirtileri bilir. Yönetim kabul edilen riske ve kaynağa karar verir. Tedarikçi ürün davranışını açıklayabilir; işletme sorumluluğunu otomatik olarak devralmaz.

Başlangıç çalışması olarak bu rollerin aynı örnek olayı farklı nasıl yorumlayacağını yazın: “Ekrandaki değer on dakikadır değişmedi.” Olası açıklamalar sabit süreç, eski veri, bağlantı arızası, sensör sorunu veya yetkisiz değişiklik olabilir. İlk iş, tek açıklamaya bağlanmadan kanıt toplamaktır.

## Devam et

[Kontrol döngüsü ve bileşenler](02-kontrol-dongusu-ve-bilesenler.md) → [mimari](03-mimari-ve-guven-bolgeleri.md).

## Kaynak

- NIST, *Guide to Operational Technology (OT) Security*, SP 800-82 Rev. 3, Eylül 2023. [Yayın kaydı](https://csrc.nist.gov/pubs/sp/800/82/r3/final). OT kapsamı ve temel güvenlik bağlamı; erişim: 13.09.2026. Diğer örnek ve değerlendirme soruları bu deponun özgün öğretim içeriğidir.
