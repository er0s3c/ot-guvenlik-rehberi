# Sekiz haftalık öğrenme yolu

Bu program başlangıç düzeyi için önerilen bir çalışma planıdır. Haftada yaklaşık 3–5 saat ayırmak örnek bir tempodur; süreler ölçülmüş öğrenme garantisi değildir. Bir hafta sonunda ortaya çıkan belge, sonraki haftanın girdisidir.

| Hafta | Konu | Okuma | Uygulama / tamamlanma ölçütü |
|---|---|---|---|
| 1 | Fiziksel dünya ve OT | [OT nedir?](01-temeller/01-ot-nedir.md), [bileşenler](01-temeller/02-kontrol-dongusu-ve-bilesenler.md); başvuru kaynağı: [sözlük](06-sozluk.md) | Bir pompa örneğinde sensör, karar, aktüatör ve operatörü ayır |
| 2 | Ağ ve haberleşme | [Mimari](01-temeller/03-mimari-ve-guven-bolgeleri.md), [protokoller](01-temeller/04-endustriyel-protokoller.md) | Beş veri akışını kaynak, hedef, amaç ve yetkiyle yaz |
| 3 | Süreç ve sektör | [Sektör karşılaştırması](02-sektorler/05-sektor-karsilastirmasi.md), [risk, emniyet ve bağımlılıklar](01-temeller/05-risk-emniyet-ve-bagimliliklar.md) ve seçilen sektör | Hizmeti kaybetmenin üç sonucunu ve bağımlılıklarını çiz |
| 4 | Tehdit modelleme | [Saldırgan bakışı](03-tehdit-modelleme/01-saldirgan-bakis-acisi.md), [vakalar](03-tehdit-modelleme/03-gercek-vakalar.md) | Bir olayda doğrulanmış bulgu ile olası sonucu ayır |
| 5 | Savunma mimarisi | [Envanter](04-savunma/01-envanter-ve-gorunurluk.md), [erişim](04-savunma/02-segmentasyon-ve-uzak-erisim.md) | Her erişim yoluna sahip, onay ve kayıt noktası ekle; [mimari inceleme laboratuvarını](../labs/02-mimari-inceleme.md) tamamla |
| 6 | Algılama | [ATT&CK](03-tehdit-modelleme/02-mitre-attack-ics.md), [izleme](04-savunma/03-izleme-ve-algilama.md) | [Sentetik kayıt laboratuvarını](../labs/01-kayit-analizi.md) tamamla |
| 7 | İşletme ve dayanıklılık | [Değişiklik](04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md), [kurtarma](04-savunma/05-olay-mudahalesi-ve-kurtarma.md) | Yedeğin varlığı ile geri yüklemenin doğrulanmasını ayrı kanıtla |
| 8 | Bütünleştirme | [Masa başı tatbikatı](../labs/03-masa-basi-tatbikati.md), [standartlar](05-standartlar-ve-turkiye.md); tatbikatın geçtiği iki sektör bölümü bu hafta okunur: [raylı sistemler](02-sektorler/03-rayli-sistemler.md) ve [telekom](02-sektorler/04-telekom-ve-baz-istasyonlari.md) | Senaryo, sorumlular, karar günlüğü ve iyileştirme listesi sun; çıkan iyileştirmeleri [90 günlük yol haritasına](04-savunma/06-90-gunluk-yol-haritasi.md) yerleştir |

## Kendini değerlendirme

Bir sektörü anladığınızı, marka veya port ezberlemekten çok şu soruları yanıtlayarak gösterirsiniz:

1. Sistem hangi fiziksel değişkenleri ölçüyor ve hangi ekipmanı etkiliyor?
2. Operatör ekranda gördüğü değerin güncel ve doğru olduğunu nasıl doğruluyor?
3. Uzaktan yönetim kesilirse yerel işlev ne kadar ve hangi koşullarda sürdürülebiliyor?
4. Bir bakım hesabı hangi güven sınırlarını geçebiliyor; yetkisinin sona erdiğini ne kanıtlıyor?
5. Siber alarmı açıklayan normal işletme davranışları hangileri?
6. Kimin onayıyla, hangi kanıtlara dayanarak normal işletmeye dönülüyor?

## Bitirme çalışması

Gerçek bir tesise ait ayrıntı kullanmadan kurgusal küçük bir hizmet işletmesi seçin. [Şablonlarla](../templates/README.md) bir envanter, akış matrisi, üç tehdit senaryosu, iki algılama kartı ve bir geri dönüş planı oluşturun. Başka bir kişi yalnızca bu belgelerle hangi rolün hangi kararı verdiğini anlayabiliyorsa çalışma amacına yaklaşmıştır. Eksik veri varsa tahmin eklemek yerine “doğrulanacak” olarak işaretleyin.
