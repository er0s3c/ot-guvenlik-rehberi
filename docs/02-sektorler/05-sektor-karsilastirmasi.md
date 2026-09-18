# Sektör Karşılaştırması ve Savunma Matrisi

[Ana sayfa](../../README.md) · [Sektörel Senaryo Kataloğu](senaryolar/README.md)

Bu tablo; kritik altyapı sektörlerinin temel hizmetlerini, fiziksel süreç değişkenlerini, OT odaklarını, kritik güvenlik sorularını ve savunma mimarilerini karşılaştırmalı olarak sunar.

---

## Karşılaştırma Tablosu

| Boyut | [Su ve Atıksu](01-su-ve-atiksu.md) | [Elektrik ve Enerji](02-elektrik-ve-enerji.md) | [Raylı Sistemler](03-rayli-sistemler.md) | [Telekom Altyapısı](04-telekom-ve-baz-istasyonlari.md) | [Petrol, Gaz ve Kimya](05-petrol-gaz-ve-kimya.md) |
|---|---|---|---|---|---|
| **Temel Hizmet** | Temiz su sağlama, atıksu arıtma ve deşarj | Enerjinin üretimi, iletimi ve dağıtımı | Trenlerin emniyetli ve dakik hareketi | Haberleşme, hücresel veri ve transmisyon sürekliliği | Hidrokarbon iletimi, rafineri ve kimyasal üretim |
| **Fiziksel Değişkenler** | Seviye, debi, basınç, serbest klor, pH, bulanıklık | Gerilim, akım, frekans, faz açısı, kesici durumu | Konum, hız, hat doluluğu, makas kilidi, katener gerilimi | DC voltaj, kabinet sıcaklığı, akü SoC, yakıt, PTP zamanı | Basınç (MAOP), sıcaklık, debi, reaksiyon ısısı, LEL gazı |
| **Birincil OT Odağı** | Pompa terfileri, kimyasal dozajlama, filtreler, blowerlar | Koruma röleleri (IED), trafo merkezleri, RTU, EMS/SCADA | Anklaşman (Interlocking), ETCS/CBTC, cer gücü, makaslar | CRAC/HVAC, -48V DC doğrultucular, BMS, Grandmaster saat | DCS, SIL 3 SIS/ESD, HIPPS, gaz ve yangın (F&G), PSV |
| **Kritik Güven Sorusu** | Ölçüm doğru mu, su kalitesi güvende mi? | Komut ve koruma parametresi yetkili ve tutarlı mı? | Hareket izni (MA) ve kilit emniyeti bozuldu mu? | Güç, soğutma ve zamanlama senkronizasyonu sağlam mı? | Emniyet duruş (ESD) ve basınç tahliyesi çalışıyor mu? |
| **Yanlış Çıkarım** | HMI erişimi her zaman suyun zehirlendiğini gösterir | IT kesintisi doğrudan koruma rölesinin açmasıdır | Trenlerin acil durması emniyetin delindiğini gösterir | Baz istasyonları standart IT ağlarıyla aynıdır | DCS ekranı normalse tesiste patlama riski yoktur |
| **Birincil Fiziksel Koruma** | Mekanik akış anahtarları, yaylı darbe vanaları | Anti-pumping röleleri, mekanik senkroçek kilitleri | Mekanik sürgü kilidi, donanımsal cer kilitleme | Donanımsal OVP Crowbar, bağımsız mekanik termostat | Yaylı PSV, patlama diskleri, trapped-key kilitleri |
| **Ayrıntılı Senaryolar** | [15 Su Senaryosu](senaryolar/01-su-ve-atiksu-senaryolari.md) | [15 Enerji Senaryosu](senaryolar/02-elektrik-enerji-senaryolari.md) | [12 Raylı Senaryo](senaryolar/03-rayli-sistemler-senaryolari.md) | [10 Telekom Senaryosu](senaryolar/04-telekom-baz-istasyonu-senaryolari.md) | [10 Proses Senaryosu](senaryolar/05-petrol-kimya-proses-senaryolari.md) |

---

## Aynı Kontrol Neden Farklı Uygulanır?

### 1. Uzak Erişim ve Oturum Yönetimi
Beş sektörde de kimlik doğrulama, süre kısıtı ve kayıt esastır. Ancak sahaların coğrafi dağılımı farklı gereksinimler doğurur:
- **Su ve Telekom:** Yüzlerce insansız uzak terfi veya baz istasyonu hücresel (LTE/5G) veya uydu üzerinden bağlanır; yerel özerklik (Local Autonomy) ve iletişim kaybında güvenli çalışma hayati önem taşır.
- **Elektrik ve Proses:** Trafo merkezleri ve rafineriler genellikle özel fiber optik ağlar ve sabit hatlarla bağlıdır; gecikme toleransı çok düşüktür (GOOSE ve SV mesajları milisaniye seviyesindedir).

### 2. İzolasyon ve Acil Durdurma (Emergency Shutdown)
- **Raylı Sistemler ve Havacılık:** "Fail-Safe" prensibi genellikle sistemin enerjisini kesip trenleri durdurmayı (All Stop) emniyetli kabul eder.
- **Petrol, Rafineri ve Enerji:** Bir jeneratörü veya kimyasal reaktörü aniden kontrolsüz durdurmak aşırı basınç, rezonans veya reaksiyon kaçaklarına yol açabilir; bu nedenle kontrollü duruş (Controlled Trip / Safe Depressurization) uygulanır.

### 3. Kurtarma ve Yeniden Devreye Alma
- Sunucunun yeniden başlatılması tek başına prosesin toparlandığını kanıtlamaz.
- Su sektöründe biyolojik çamurun toparlanması ve su kalitesinin laboratuvarda doğrulanması gerekir.
- Enerji sektöründe şebeke kararlılığı ve faz senkronizasyonu test edilmelidir.
- Raylı sistemlerde hat boyu anklaşman ve makas son konum teyidi yapılmalıdır.
- Proses endüstrisinde boru hatlarının azotla süpürülmesi (purging) ve sızıntı testleri tamamlanmadan üretime geçilemez.

---

## Karşılaştırmalı Alıştırma

Kurgusal bir senaryoda yetkili bir bakım yüklenicisinin hesabının ele geçirildiğini varsayın. Her sektör için şu soruları yanıtlayın:
1. Saldırgan bu hesapla hangi fiziksel süreci doğrudan etkileyebilir?
2. Donanımsal mekanik koruma (PSV, bimetal röle, mekanik kilit) bu etkiyi nasıl sınırlar?
3. PLC/DCS mantığında hangi oran-değişim ve oylama kuralı saldırıyı yakalar?
4. OT SOC analisti ağda hangi protokol imzasını ilk 60 saniyede tespit etmelidir?

Bu alıştırmanın sonuçlarını [tehdit modeli şablonuna](../../templates/02-tehdit-modeli.md) kaydedin.
