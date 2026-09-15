# Çevrimdışı laboratuvarlar

[Ana sayfa](../README.md) · [Öğrenme yolu](../docs/00-ogrenme-yolu.md) · [Şablonlar](../templates/README.md)

Bu dizindeki üç laboratuvar, rehberde okunan kavramları bir çıktı üretecek biçimde çalıştırmak içindir. Senaryolar, veriler, kurum adları ve mimariler **kurgusaldır**; belirli bir tesisin projesini, ağını veya olay kaydını temsil etmez. Amaç bir sistemi kırmak değil, bir tasarımı ve kanıt zincirini değerlendirmektir.

## Ortak kurallar

- Laboratuvarlar tamamen çevrimdışı yürütülür. Herhangi bir gerçek sisteme bağlanılmaz, tarama yapılmaz, adres veya cihaz aranmaz.
- Bütün girdiler bu depodaki sentetik dosyalardır. Dış veri getirilecekse kaynağı ve sentetik olduğu ayrıca belirtilir.
- Üretilen çıktılar gerçek bir tesise doğrudan uygulanmaz. Gerçek tesiste yapılacak değerlendirme yazılı kapsam, işletme sorumlusunun onayı ve emniyet değerlendirmesi ister.
- Alıştırmalar tehdit modelleme düzeyindedir: hedef, ön koşul, aşılan güven sınırı, hizmet etkisi, gözlenebilir belirti ve karşılık gelen kontrol incelenir. Araç adı, komut veya saldırı prosedürü yazılmaz, beklenmez.
- Bir cevabın “doğru” sayılması için gerekçesi ve dayandığı kanıt yazılmalıdır. Kanıtı olmayan yargı, belirsizlik olarak işaretlenir.
- Kurgusal veride bilerek boşluklar ve çelişkiler vardır. “Veri yetersiz” de kabul edilen bir sonuçtur; bunun hangi kararı bloke ettiği yazılır.

**Araç kurulumu gerekmez.** Metin düzenleyici ve Markdown okuyabilen bir görüntüleyici yeterlidir. Tablolar için bir hesap tablosu programı kullanılabilir, ancak zorunlu değildir. Ağ erişimi, sanal makine, simülatör veya güvenlik ürünü kurulumu istenmez.

## Laboratuvarlar

| Laboratuvar | Süre ve katılımcı | Ön okuma | Üretilen çıktı | İlgili bölüm |
|---|---|---|---|---|
| [1. Kayıt analizi](01-kayit-analizi.md) | 60–90 dakika, tek kişi | [İzleme ve algılama](../docs/04-savunma/03-izleme-ve-algilama.md) okundu | Zaman çizelgesi, iki algılama kartı, işletmeye aktarılacak bir cümle, açık sorular listesi | [İzleme ve algılama](../docs/04-savunma/03-izleme-ve-algilama.md) |
| [2. Mimari inceleme](02-mimari-inceleme.md) | 90–120 dakika, tek kişi veya ikili | [Mimari ve güven bölgeleri](../docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) ve [segmentasyon](../docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md) okundu | Bölge ve geçiş adlandırması, akış matrisi, sıralanmış kusur listesi, kabul kanıtları, emniyet değerlendirmesi gerekenlerin işareti, doğrulanacak varsayımlar listesi | [Mimari ve güven bölgeleri](../docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) |
| [3. Masa başı tatbikatı](03-masa-basi-tatbikati.md) | 90 dakika (kısa sürüm) veya yaklaşık 3,5 saat (tam sürüm), 4–8 katılımcı ve bir kolaylaştırıcı | [Olay müdahalesi](../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md) okundu; laboratuvar 1 ve 2 tamamlanmış olmalı | Karar günlüğü, yolcu/basın/kurum içi mesaj taslakları, bildirim listesini açacak ve onaylayacak rollerin belirlenmesi, hizmete dönüş kapıları, iyileştirme listesi | [Olay müdahalesi ve kurtarma](../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md) |

Süreler bu deponun tahminidir; grubun ön bilgisine ve tartışma derinliğine göre değişir. Tek kişilik çalışmada laboratuvar 3 bir tartışma yerine yazılı karar günlüğüne dönüşür.

Kolaylaştırıcı, laboratuvar 3'te tatbikatı yürüten, enjekteleri veren, süreyi tutan ve karar günlüğünün dolduğunu gören roldür; senaryodaki kararların sahibi değildir. Tatbikattaki “üst yönetim” rolüyle karıştırılmamalıdır.

## Önerilen sıra

1. **Kayıt analizi** ile başlayın. Kanıtın nasıl okunduğunu ve tek bir kaydın neyi göstermediğini görmek, sonraki iki laboratuvarın dilini kurar.
2. **Mimari inceleme** ile devam edin. Kayıtlarda görülen belirtilerin hangi tasarım kararlarından doğabileceği burada ele alınır.
3. **Masa başı tatbikatı** ile bitirin. Önceki iki çıktı senaryonun girdisidir: kusur listesi olayın ön koşullarını, algılama kartı ise ilk belirtiyi besler.

Sıra zorunlu değildir. Zamanı kısıtlı bir ekip yalnızca laboratuvar 2'yi de yapabilir; bu durumda kayıt ve olay yönü eksik kalır ve sonuç buna göre yorumlanır.

## Kullanılan şablonlar

Her laboratuvar çıktısını [şablonlar dizinindeki](../templates/README.md) bir dosyaya yazar. Şablonlar kopyalanır; bu depodaki asıl dosyalar doldurulmaz.

| Şablon | Hangi laboratuvarda |
|---|---|
| [Envanter ve akış](../templates/01-envanter-ve-akis.md) | Laboratuvar 2 |
| [Tehdit modeli](../templates/02-tehdit-modeli.md) | Laboratuvar 2 (isteğe bağlı genişletme) ve Laboratuvar 3 |
| [Algılama kartı](../templates/03-algilama-karti.md) | Laboratuvar 1 |
| [Olay ve kurtarma](../templates/04-olay-ve-kurtarma.md) | Laboratuvar 1 (yalnız ilk kayıt bölümü) ve Laboratuvar 3 |
| [Değişiklik ve kabul](../templates/05-degisiklik-ve-kabul.md) | Laboratuvar 2 ve 3 |
| [Tedarikçi ve uzak erişim](../templates/06-tedarikci-ve-uzak-erisim.md) | Laboratuvar 2 (isteğe bağlı genişletme) ve Laboratuvar 3 |

## Çözümler ve değerlendirme

Çözüm dosyaları `cozumler/` dizinindedir: [kayıt analizi](cozumler/01-kayit-analizi-cozum.md), [mimari inceleme](cozumler/02-mimari-inceleme-cozum.md) ve [masa başı değerlendirmesi](cozumler/03-masa-basi-degerlendirme.md). Kendi cevabınızı yazmadan açmayın; çözümler beklenen tespitleri ve değerlendirme ölçeğini içerir.

Üç çözüm dosyasının puanlama ölçekleri birbirinden farklıdır (laboratuvar 1'de 6 ölçüt, laboratuvar 2'de 6, laboratuvar 3'te 8; toplamlar sırasıyla 12, 18 ve 24). Fark, alıştırmaların ayrıntı düzeyinden gelir; ölçekler birbirine çevrilmez ve toplam puanları karşılaştırılmaz.

Çözümler tek doğru cevap listesi değildir. Gerekçesi kayıtla desteklenen farklı bir sıralama da geçerli olabilir. Değerlendirmede aranan şey, yargının kanıta bağlanması ve belirsizliğin açıkça yazılmasıdır.

Sentetik girdi dosyaları `veri/` dizinindedir. Bu dosyalar üretilmiş kayıtlardır; gerçek bir sistemin çıktısı değildir ve saha davranışı hakkında istatistik olarak kullanılamaz.

## Kapsam notu

Bu dizindeki senaryolar, mimariler, veri kümeleri, görev adımları ve değerlendirme ölçekleri **bu deponun özgün eğitim sentezidir**. Herhangi bir standardın, kılavuzun veya üretici belgesinin çevirisi ya da özeti değildir. Laboratuvarların dayandığı kaynaklı arka plan ilgili rehber bölümlerinde ve [kaynak kataloğunda](../KAYNAKLAR.md) verilmiştir. Erişim tarihi: 13.09.2026.
