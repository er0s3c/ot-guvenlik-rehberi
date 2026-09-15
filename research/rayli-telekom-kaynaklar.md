# Araştırma kaydı: raylı sistemler ve telekom

**Araştırma / erişim tarihi:** 2026-09-13

**İlgili bölümler:** [Raylı sistemler](../docs/02-sektorler/03-rayli-sistemler.md), [Telekom ve baz istasyonları](../docs/02-sektorler/04-telekom-ve-baz-istasyonlari.md)

Bu kayıt, kullanılan birincil kaynakların hangi iddiayı desteklediğini ve erişim sınırını gösterir. Tehdit matrisleri, mimariler, masa başı senaryoları ve ölçüm hedefleri depo için üretilmiş eğitim analizleridir. Standartlardan alınmış zorunlu kontrol listeleri, gerçek olay raporları veya belirli işletmelerin topolojileri değildir. Kaynaklardaki grafikler kopyalanmamıştır.

## Raylı sistemler

| Kimlik | Başlık ve doğrudan bağlantı | Yayıncı | Tarih / sürüm | Destek ve erişim notu |
|---|---|---|---|---|
| RAY-01 | [Signals explained](https://www.networkrail.co.uk/stories/signals-explained/) | Network Rail | 2018-09-05 | Sinyalizasyonun birden fazla işlev içermesi; bilgi kaybının kısıtlayıcı işletme ve gecikmeyle ilişkisi. Resmî işletmeci açıklaması; istatistikler bugünkü şebekeye genellenmedi. |
| RAY-02 | [Jargon Buster](https://safety.networkrail.co.uk/jargon-buster/) | Network Rail Safety Central | Yayın tarihi belirtilmiyor | Interlocking terimi. İngiltere terim sözlüğü; tüm projelerin emniyet tasarımı olarak kullanılmadı. |
| RAY-03 | [ERTMS](https://www.era.europa.eu/sk/node/558) | European Union Agency for Railways | Güncel sayfa, sabit yayın tarihi belirtilmiyor | ETCS ve ERTMS ayrımı; demiryolu radyo haberleşmesinin rolü. Güncel sayfa düzenlemeleri içerse de Türkiye için mevzuat sonucu çıkarılmadı. |
| RAY-04 | [CBTC açıklaması](https://www.mta.info/projects/culver-line-signal-modernization) | Metropolitan Transportation Authority | Güncelleme 2025-03-11 | İşletmecinin CBTC uygulamasında sürekli haberleşmenin rolü. MTA projesi diğer CBTC ürünlerine bire bir genellenmedi. |
| RAY-05 | [Bölgeleme rehberi yayın sayfası](https://www.enisa.europa.eu/publications/zoning-and-conduits-for-railways) ve [PDF](https://www.enisa.europa.eu/sites/default/files/publications/Zoning%20and%20Conduits%20for%20Railways%20-%20Security%20Architecture.pdf) | ENISA | 2022-02-28 | İşlev bazlı bölgeler ve fiziksel/mantıksal sınırlar. PDF'de bölüm 3 incelendi. Dayanağı CLC/TS 50701:2021; 2023 tam metin özeti değildir. |
| RAY-06 | [Almanya demiryolu siber güvenlik sunumu](https://www.era.europa.eu/sites/default/files/2025-12/session%206-2%20-%20eba%20-%20cybersecurity%20in%20german%20nsa.pdf) | EBA; ERA konferansında yayımlanmış | 2025-12-02 | Araç, RBC, anklaşman ve anahtar yönetimi ilişkisine resmî örnek. Konferans sunumu normatif standart yerine konmadı. |
| RAY-07 | [Raylı sistemlerde siber risk yönetimi iyi uygulamaları](https://www.enisa.europa.eu/publications/railway-cybersecurity-good-practices-in-cyber-risk-management) | ENISA | 2021-11-25 | Kuruluş bağlamına uyarlanmış risk yöntemi seçimi; kamuya açık yayın özeti incelendi. |
| RAY-08 | [NVN-CLC/TS 50701:2023](https://www.nen.nl/en/nvn-clc-ts-50701-2023-en-314480) | NEN; köken CENELEC | 2023-09-01 | Katalogda güncel sürüm ve 2021'i ikame kaydı; RAMS ilişkisi, fonksiyonel emniyet gereksinimleriyle kapsam ayrımı. Ücretli tam metin satın alınmadı veya incelenmedi. |
| RAY-09 | [PD CLC/TS 50701:2023](https://knowledge.bsigroup.com/products/railway-applications-cybersecurity-1) | BSI | 2023-08-31 | Ulusal yayımlama tarihinin NEN tarihinden farklı olduğu teyit edildi. Katalog kapsamı; ek tam metin incelemesi yapılmadı. |
| RAY-10 | [TC 9 organizasyon kaydı](https://assets.iec.ch/further_informations/1248/Organizational%20chart%202026-02-16.pdf) | IEC | 2026-02-16 | PT 63452 projesi. Bu organizasyon kaydı yayımlanmış IEC standardı veya CLC/TS 50701'in ikamesi kanıtı sayılmadı. |

## Telekom ve saha destek OT'si

| Kimlik | Başlık ve doğrudan bağlantı | Yayıncı | Tarih / sürüm | Destek ve erişim notu |
|---|---|---|---|---|
| TEL-01 | [5GS sistem mimarisi](https://www.etsi.org/deliver/etsi_ts/123500_123599/123501/18.11.00_60/ts_123501v181100p.pdf) | 3GPP / ETSI | TS 23.501; ETSI V18.11.0, 2025-09 | İşlevler, kontrol/kullanıcı düzlemleri ve temel arayüzler. Bölüm 4 ve 8 referans alındı; referans sürümü en yeni sürüm diye sunulmadı. |
| TEL-02 | [Güç, soğutma ve çevresel yönetim arayüzü](https://www.etsi.org/deliver/etsi_es/202300_202399/20233601/01.03.01_60/es_20233601v010301p.pdf) | ETSI | ES 202 336-1 V1.3.1, 2025-04 | Telekom ekipmanı ile fiziksel destek denetiminin ayrımı; farklı üreticili saha bileşenleri, yönetim arayüzleri. Nihai yayımlanmış sürüm kullanıldı, Şubat 2025 taslağı kullanılmadı. |
| TEL-03 | [OSS/BSS](https://www.ericsson.com/en/oss-bss) | Ericsson | Yayın tarihi belirtilmiyor | Üreticinin OSS/BSS kavram tanımı. Pazarlama sayfasından ürün üstünlüğü veya performans iddiası alınmadı. |
| TEL-04 | [5GS güvenlik mimarisi](https://www.etsi.org/deliver/etsi_ts/133500_133599/133501/18.10.00_60/ts_133501v181000p.pdf) | 3GPP / ETSI | TS 33.501; ETSI V18.10.0, 2025-07 | Bölüm 4'teki güvenlik alanları ve SBA ayrımı. Bir alandaki koruma bütün şebekenin güvenliği olarak yorumlanmadı. |
| TEL-05 | [TS 33.501 sürüm kaydı](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3169) | 3GPP | Canlı sürüm kaydı | Birden fazla release/sürüm dalı bulunduğu doğrulandı; taslak, ürün desteği ve dağıtım durumu eşitlenmedi. |
| TEL-06 | [5G güvenlik eki](https://www.enisa.europa.eu/publications/5g-supplement-security-measures-under-eecc) | ENISA | İkinci baskı, 2021-07-07 | Sanallaştırma, dilimleme ve uç bilişim güvenlik kapsamı. AB rehberi; Türkiye'de otomatik yükümlülük olarak kullanılmadı. |
| TEL-07 | [5G Security Controls Matrix](https://www.enisa.europa.eu/publications/5g-security-controls-matrix) | ENISA | 2023-05-24 | Kontrol ve kanıt yaklaşımı. Yayın sayfası ve arka plan belgesi incelendi; kontrol tablosunun tamamı kopyalanmadı. |
| TEL-08 | [NESAS](https://www.gsma.com/solutions-and-impact/technologies/security/network-equipment%20-security-assurance-scheme/) | GSMA | Yayın tarihi belirtilmiyor | Üretici süreç denetimi, ürün değerlendirmesi ve sertifikasyon/akreditasyon ayrımı. Resmî sayfanın arama dizinindeki metni alındı; doğrudan sayfa isteği bu oturumda 403 döndü. |
| TEL-09 | [FS.16 geliştirme ve yaşam döngüsü gereksinimleri](https://www.gsma.com/solutions-and-impact/technologies/security/gsma_resources/fs-16-network-equipment-security-assurance-scheme-development-and-lifecycle-security-requirements-2/) | GSMA | V3.0, 2025-02-20 | Resmî yayın kaydıyla sürüm, tarih ve konu doğrulandı; tam doküman madde analizi yapılmadı. Doğrudan sayfa erişimi bu oturumda başarısız olduğundan arama dizini kaydı kullanıldı. |

## Araştırmada uygulanan yorum sınırları

- “Emniyetli duruma geçiş hedefi”, her siber saldırıda aynı sonucun garanti edildiği iddiasına dönüştürülmedi.
- ETCS, ERTMS ve CBTC eş anlamlı sunulmadı; ürün, baseline ve uygulama farklılıkları korundu.
- Raylı sistemlere ait CLC/TS 50701:2023, tamamlanmış IEC 63452 standardı diye adlandırılmadı. Bu araştırmanın IEC kaydı proje düzeyindedir.
- NESAS sonuçları “üretici/ürün sertifikası” veya bütün dağıtım için güvenlik garantisi diye sunulmadı.
- Seçili ETSI sürümleri sabit referanstır. Farklı release dallarının güncelliği, operatörün kurulu sürümünü veya uygulanabilir bütün gereksinimleri tek başına göstermez.
- Ücretli standardın tam metnine erişilmiş izlenimi verilmedi; kamuya açık katalog kapsamından madde bazında uygunluk çıkarılmadı.
- Kurgusal tehditlerde önkoşul, güven sınırı, hizmet etkisi ve savunma ayrıldı. Gerçek hedef bulma, erişim sağlama, RF müdahalesi veya hizmet kesintisi üretme talimatı hazırlanmadı.
