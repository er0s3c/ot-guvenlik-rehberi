# Laboratuvar 4 — Yedeğin geri dönüşe yeterliliği

[Laboratuvarlar](README.md) · [Kurtarma rehberi](../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md) · [Kayıt şablonu](../templates/04-olay-ve-kurtarma.md)

Bu çalışma tamamen kurgusal bir **belge incelemesidir**. Yedek dosyası açılmaz, cihaz veya sanal makine kurulmaz. Öğrenme hedefi, en yeni kopya ile güvenilir ve kullanılabilir kurtarma paketini ayırmaktır. Ön okuma: kurtarma rehberi ve değişiklik/kabul şablonu. Önerilen süre 60–90 dakikadır; ölçülmüş bir başarı süresi değildir.

## Senaryo ve girdiler

Kurgusal SU-A tesisinde saat 10.00'da mühendislik kayıtlarında açıklanamayan proje farkı görülmüştür. Son onaylı değişiklik D-17, önceki gün 16.00'da kapanmıştır. Farkın ne zaman oluştuğu bilinmiyor. Operatör gözlem hizmeti için masa başı hedef RTO dört saat, historian verisi için RPO bir saat olarak belirlenmiştir; bunlar sektör önerisi değildir. Yerel kontrolün ve saha durumunun güvenilirliği henüz teyit edilmemiştir.

| Paket | Varlık | İçerik ve zaman | Bütünlük / sürüm kanıtı | Geri yükleme ve bağımlılık |
|---|---|---|---|---|
| Y-01 | PLC-01 | D-17 projesi, önceki gün 16.10 | Onaylı proje kaydıyla eşleşiyor | Yalnız simülatörde test kaydı; fiziksel giriş/çıkış doğrulanmamış |
| Y-02 | PLC-01 | Bugün 09.55 otomatik kopya | Hash var; hangi değişiklikten geldiği bilinmiyor | Geri yükleme kaydı yok |
| Y-03 | HMI-01 | Önceki gün 16.15 proje ve ayarlar | D-17 etiketi var | Aynı çalışma ortamında test kaydı var; lisans kurtarma yöntemi kayıp |
| Y-04 | HIS-01 | Bugün 08.30 veri yedeği | Kopya bütünlüğü kayıtlı | 09.00–10.00 işlem günlüğü yok; başka kopya bilinmiyor |
| Y-05 | FW-01 | Önceki gün 16.20 kural/nesne kopyası | Değişiklik D-17 ile eşleşiyor | Farklı yazılım sürümünde içe aktarım denenmiş; hedef sürüm uyumu belirsiz |
| Y-06 | SW-01 | Önceki gün 16.25 yapılandırma | Onaylı kayıtla eşleşiyor | Yönetim erişimi, VLAN ve kayıt yolu için masa başı test planı var; sonuç yok |

| Bağımlılık | Eldeki bilgi | Eksik |
|---|---|---|
| Envanter ve akış kaydı | Bağımsız korunan belge kopyası okunabiliyor | Son fiziksel saha teyidi |
| Zaman ve kimlik hizmetleri | Normal işletmede merkezi sunucuya bağlı | Kesinti sırasında yerel erişim ve doğru saat teyidi |
| Mühendislik araçları | Sürüm listesi var | Kurulum medyası ve lisansın erişilebilirlik kanıtı |
| Fiziksel durum | Son historian ölçümleri var | Bağımsız saha gözlemi |

## Görevler

1. **THEORY:** RTO, RPO, kopya bütünlüğü, güvenilir sürüm ve süreç kabulünü beş ayrı cümleyle açıklayın.
2. **LAB:** Her paketi `aday`, `doğrulama bekliyor` veya `mevcut kanıtla seçilemez` olarak sınıflandırın. Aynı paket için aday olma ve kullanımın hâlâ bloke olması birlikte yazılabilir.
3. **TEST:** Her aday için eksik kabul kanıtını belirtin. Belgedeki simülatör veya eski testin kapsamadığı işlevleri gösterin.
4. **DEFENSE:** Tek bir cihaz sırası ezberlemek yerine bağımlılık sırası çıkarın: erişim/kanıt → destek hizmetleri → haberleşme → uygulama/proje → saha kabulü. Varlıkların bu sıradaki yeri gerekçeli olsun.
5. **REPORT:** En fazla bir sayfada seçilen adaylar, açık engeller, karar sahipleri, RTO/RPO durumu ve normal hizmete dönüş koşullarını yazın.

RTO için en geç hangi saatin hedeflendiğini hesaplayın; hedef sürenin içinde işlemin gerçekten yapılabileceğinin kanıtlanıp kanıtlanmadığını ayrı belirtin. RPO hesabında son kullanılabilir veri zamanını esas alın.

## Değerlendirme

Her ölçüt `0: yok/kanıtsız`, `1: kısmi`, `2: gerekçeli ve izlenebilir` olarak değerlendirilir. Bu özgün ölçek diğer üç laboratuvarın puanlarına çevrilmez.

| Ölçüt | Tam kabul |
|---|---|
| Güvenilir kopya | Y-02'nin yeni olmasının yeterli olmadığı açıklanır |
| Bağımlılık | Lisans, araç, zaman, kimlik ve ağ engelleri görülür |
| RTO/RPO | Hedef ve mevcut kanıtın farkı doğru hesaplanır |
| Temsil sınırı | Simülatör testi fiziksel süreç kabulü sayılmaz |
| Karar | Dönüşü onaylayacak işletme/otomasyon rolleri ve açık işler bellidir |

Beş ölçütün tamamı en az 1 olmalı; kanıtlanmamış fiziksel kabul veya geri yükleme başarısı yazılmışsa çalışma düzeltilir. Puan mesleki yeterlilik belgesi değildir. Kendi raporunuzdan sonra [çözüm anahtarını](cozumler/04-kurtarma-dogrulama-cozum.md) okuyun.

## Kaynak ve kapsam

Senaryo, saatler, paketler ve değerlendirme özgün sentetik eğitim içeriğidir. NIST [SP 1339](https://csrc.nist.gov/pubs/sp/1339/final), 17 Haziran 2026, yedekleri değişiklik, düzenli oluşturma, test ve kurtarma alıştırmalarıyla birlikte ele alır; senaryo bu yayının resmî alıştırması değildir. Kaynak 16.09.2026'da incelendi; çalışma 17.09.2026'da oluşturuldu.
