# IEC 62443-3-3 Öz Değerlendirme ve Güvenlik Seviyesi (SL) Matrisi

[Şablonlar Ana Sayfası](README.md) · [Standartlar ve Türkiye Rehberi](../docs/05-standartlar-ve-turkiye.md) · [BİGR EKS Denetim Matrisi](10-bigr-eks-denetim-matrisi.md)

Bu çalışma şablonu; endüstriyel otomasyon ve kontrol sistemlerinde (IACS) **IEC 62443-3-3** standardında tanımlanan 7 Temel Gereksinim (Fundamental Requirements - FR) çerçevesinde sistemin **Hedeflenen Güvenlik Seviyesi (SL-T)** ile **Ulaşılan Güvenlik Seviyesi (SL-A)** arasındaki farkı (Gap Analysis) ölçmek ve puanlamak için hazırlanmıştır.

---

## 1. Değerlendirme Kapsamı ve Bölge (Zone) Bilgileri

| Değerlendirme Parametresi | Değer / Açıklama |
|---|---|
| **Değerlendirilen Güvenlik Bölgesi (Zone)** | Örn: Zone 1 - Arıtma PLC & Saha Hücresi / Zone 2 - SCADA Yönetim |
| **Bölge Kritiklik Derecesi** | Yüksek / Orta / Düşük |
| **Hedeflenen Güvenlik Seviyesi (SL-T)** | `SL-1` / `SL-2` / `SL-3` / `SL-4` |
| **Değerlendirme Tarihi ve Sorumlusu** | |

### Güvenlik Seviyeleri (Security Levels - SL) Özeti:
- **SL-1:** Kazara veya tesadüfi kural ihlallerine karşı koruma.
- **SL-2:** Düşük kaynaklı, basit araçlar kullanan kasıtlı saldırılara karşı koruma.
- **SL-3:** Orta kaynaklı, OT/ICS bilgisine sahip yetkin saldırganlara karşı koruma.
- **SL-4:** Yüksek kaynaklı, gelişmiş kalıcı tehdit (APT / Devlet destekli) aktörlerine karşı koruma.

---

## 2. IEC 62443-3-3 Temel Gereksinimler (FR 1 - FR 7) Matrisi

| Temel Gereksinim (FR) | Sistem Gereksinimi (SR) | SL-1 Gereği | SL-2 Gereği | SL-3 Gereği | SL-4 Gereği | Mevcut SL-A | Karşılanma Durumu & Açıklama |
|---|---|---|---|---|---|---|---|
| **FR 1: Kimlik & Doğrulama (IAC)** | SR 1.1: Benzersiz Kullanıcı Kimliği | Tüm insan kullanıcılar | Rol bazlı kullanıcılar | Merkezi kimlik doğrulama | Kriptografik donanımsal token | `[ ]` | |
| | SR 1.3: Çok Faktörlü Doğrulama (MFA) | Uzak erişimde tavsiye | Tüm uzaktan erişimlerde | L2/L3 tüm yönetim erişimlerinde | Tüm insan ve servis erişimlerinde | `[ ]` | |
| **FR 2: Kullanım Denetimi (UC)** | SR 2.1: Yetkilendirme (RBAC) | Temel kullanıcı/yönetici | Rol tabanlı yetki matrisi | En az yetki (Least Privilege) | Dinamik bağlamsal yetki (ABAC) | `[ ]` | |
| | SR 2.8: Eşzamanlı Oturum Kısıtı | Tanımsız | 3 oturum sınırı | Tek oturum ve otomatik kilit | Donanımsal kilit ve zorunlu log-off | `[ ]` | |
| **FR 3: Sistem Bütünlüğü (SI)** | SR 3.1: İletişim Bütünlüğü | CRC / Parite | TLS / Temel HMAC | IEC 62351 kriptografik imza | Donanımsal HSM tabanlı doğrulama | `[ ]` | |
| | SR 3.4: Yazılım/Firmware Bütünlüğü | Üretici hash kontrolü | Yükleme öncesi imza teyidi | Güvenli önyükleme (Secure Boot) | Donanımsal kök güven (Hardware RoT) | `[ ]` | |
| **FR 4: Veri Gizliliği (DC)** | SR 4.1: İletişim Gizliliği | Gerekli değil | Ağ sınırlarında şifreleme | Tüm Purdue L2/L3 şifreleme | L1/L0 dahil tüm kanallarda şifreleme | `[ ]` | |
| **FR 5: Sınırlı Veri Akışı (RDF)** | SR 5.1: Ağ Segmentasyonu | Temel alt ağ ayrımı | VLAN ve L3 Güvenlik Duvarı | Durum denetimli (Stateful) OT FW | Veri Diyodu / Donanımsal İzolasyon | `[ ]` | |
| | SR 5.2: Bölge Geçişleri (Conduits) | Tanımlı akışlar | Port bazlı izin listesi | Uygulama katmanı (DPI) filtreleme | Çift yönlü protokol doğrulama | `[ ]` | |
| **FR 6: Olaylara Zamanında Yanıt (TRE)** | SR 6.1: Denetim Günlükleri | Yerel hata kayıtları | Merkezi Syslog aktarımı | Kurcalanamaz merkezi SIEM | Gerçek zamanlı OT SOC analitiği | `[ ]` | |
| | SR 6.2: Sürekli İzleme & Algılama | Temel ağ izleme | İmza tabanlı OT IDS | Davranışsal anomali tespiti | Fiziksel süreç modeli korelasyonu | `[ ]` | |
| **FR 7: Kaynak Sürekliliği (RA)** | SR 7.1: DoS Koruması | Temel ağ filtreleme | Hız sınırlama (Rate-Limiting) | Donanımsal fırtına kontrolü | Tam yedekli bağımsız iletişim | `[ ]` | |
| | SR 7.3: Yedekleme ve Kurtarma | Manuel periyodik yedek | Doğrulanmış tam yedek | Otomatik çevrimdışı yedekleme | Hızlı felaket kurtarma (RTO < 2 sa) | `[ ]` | |

---

## 3. Güvenlik Seviyesi Vektör Özeti ve Fark Analizi

Her temel gereksinim için ulaşılan seviye bir vektör olarak ifade edilir:

$$\text{SL-A} = \{\text{IAC: SL-x, UC: SL-x, SI: SL-x, DC: SL-x, RDF: SL-x, TRE: SL-x, RA: SL-x}\}$$

```text
Hedeflenen Seviye (SL-T) : [ SL-3 ]
Ulaşılan Seviye  (SL-A) : [      ]
Fark (Gap) Alanları      :
1.
2.
3.
```

---

## 4. İyileştirme Yol Haritası ve Eylem Planı

| İyileştirme Eylemi | İlgili Gereksinim | Öncelik (Yüksek/Orta) | Sorumlu Mühendis | Hedef Tarih | Bütçe / Kaynak |
|---|---|---|---|---|---|
| IEC 62351 GOOSE İmzalamaya Geçiş | FR 3 - SR 3.1 | Yüksek | Koruma Mühendisi | | |
| OT IDS Anomali Sensörü Kurulumu | FR 6 - SR 6.2 | Yüksek | OT Siber Güvenlik Uzmanı | | |
| Çevrimdışı Yedekleme Kasası Tesisi | FR 7 - SR 7.3 | Orta | Tesis Bakım Amiri | | |
