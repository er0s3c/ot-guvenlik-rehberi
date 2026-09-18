# Laboratuvar 4 — Kurtarma doğrulama çözümü

[Senaryoya dön](../04-kurtarma-dogrulama.md). Aşağıdaki sonuçlar gerçek test çıktıları değil, senaryodaki bilgilerin yorumudur.

## Paket kararları

| Paket | Örnek karar | Gerekçe / sonraki kanıt |
|---|---|---|
| Y-01 | Aday; kullanım onayı bekliyor | D-17 ile izlenebilir. Hedef ürün/araç uyumu ve bağımsız saha kabulü tamamlanmalı |
| Y-02 | Mevcut kanıtla güvenilir başlangıç olarak seçilemez | Hash yalnız kopya bütünlüğünü destekler. Kaynağı açıklanamayan değişiklik kopyaya taşınmış olabilir |
| Y-03 | Aday; lisans bağımlılığı bloke | Proje kopyası var; uygulamanın lisansla açılacağı doğrulanmamış |
| Y-04 | Veri adayı; RPO karşılanmıyor | Bilinen son veri 08.30. 10.00'a göre kayıp aralığı 90 dakika; hedef 60 dakika |
| Y-05 | Uyumluluk doğrulaması bekliyor | Başka sürümdeki içe aktarım hedef yazılım sürümüne kanıt değil |
| Y-06 | Doğrulama bekliyor | Test planı, tamamlanmış test sonucu değildir |

Y-02 inceleme kanıtı olarak korunabilir; geri dönüş için seçilmemesi silinmesini gerektirmez. Y-04'te başka günlük bulunursa RPO hesabı yeniden yapılır; olmayan günlük var kabul edilmez.

## Hedefler ve bağımlılık

Saat 10.00 başlangıcına göre RTO hedef sonu 14.00'dır. Lisans, araç ve saha kabul süreleri bilinmediğinden bu hedefin karşılanacağı söylenemez. RTO bir hedef, ölçülen kurtarma süresi ayrı bir kayıttır.

Örnek karar sırası:

1. İşletme/emniyet durumu ve eldeki kanıt korunur; canlı süreç durumuna ilişkin belirsizlik açıklanır.
2. Envanter, güvenilir sürüm, zaman ve yetkili kurtarma erişimi teyit edilir.
3. Ağ/kimlik/araç/lisans bağımlılıkları hedef sürümleriyle çözümlenir.
4. Uygulama/proje adayları yetkili ekiplerin kabul planına bağlanır.
5. Fiziksel durum ve bağımsız kabul tamamlanmadan normal işletmeye dönüş onayı verilmez.

Bu sıra tüm tesislerde uygulanacak cihaz açma sırası değildir. Örneğin ağ cihazının kimlik hizmetine, kimlik hizmetinin aynı ağa bağımlı olması döngü yaratabilir; yerel kurtarma erişimi bu döngüyü çözmek için tasarlanır.

## Örnek yönetici özeti

SU-A için D-17 ile ilişkili kopyalar kurtarma adayıdır. En yeni PLC kopyasının güvenilirliği kanıtlanmamıştır. HMI lisans geri kazanımı ve ağ cihazı sürüm uyumluluğu açıktır. Historian için bilinen veri kaybı hedefi aşmaktadır. Normal işletmeye dönüş, otomasyon ve işletme rollerinin bağımsız saha kabulüne bağlıdır; 14.00 hedefinin karşılanabilirliği mevcut kanıtla doğrulanamamaktadır.

## Sık yapılan değerlendirme hataları

- Hash bulunduğu için Y-02'yi temiz ilan etmek.
- Planlanmış testi yapılmış saymak.
- RPO'yu dosyanın oluşturulma saatinden, verinin son kullanılabilir zamanını incelemeden hesaplamak.
- Simülatörü gerçek saha/emniyet kabulüne eşdeğer saymak.
- RTO hedefini gerekçesiz bir tamamlanma taahhüdüne çevirmek.

## Kapsam notu

Özgün çözüm örneği; 17.09.2026. Gerekçeli başka bağımlılık sıraları kabul edilebilir. [Senaryonun değerlendirme ölçütleri](../04-kurtarma-dogrulama.md) esas alınır.
