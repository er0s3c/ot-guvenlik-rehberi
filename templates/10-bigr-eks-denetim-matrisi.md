# T.C. Cumhurbaşkanlığı DDO BİGR - EKS Güvenlik Tedbirleri Denetim Matrisi

[Şablonlar Ana Sayfası](README.md) · [Standartlar ve Türkiye Rehberi](../docs/05-standartlar-ve-turkiye.md) · [IEC 62443 Öz Değerlendirme](11-iec-62443-oz-degerlendirme.md)

Bu çalışma şablonu; **T.C. Cumhurbaşkanlığı Dijital Dönüşüm Ofisi Bilgi ve İletişim Güvenliği Rehberi (BİGR)** kapsamında yer alan **Endüstriyel Kontrol Sistemleri (EKS)** güvenlik tedbirlerine uyum durumunu denetlemek, kanıtları toplamak ve kurumsal boşluk analizi (Gap Analysis) yapmak için hazırlanmıştır.

---

## 1. Denetim Bilgileri

| Denetlenen Kurum / Tesis | |
|---|---|
| **Tesis / Sektör Türü** | Su / Enerji / Ulaşım / Proses / Telekom |
| **Denetim Tarihi** | |
| **Denetçi / Ekip Üyeleri** | |
| **Tesis Sorumlusu / Katılımcılar** | |
| **Kapsamdaki EKS Sistemleri** | SCADA / DCS / PLC / RTU / HMI / Historian |

---

## 2. BİGR EKS Tedbirleri Değerlendirme Tablosu

*Uyum Durumu Kısaltmaları:* **U** (Tam Uyumlu - 2 Puan), **KU** (Kısmen Uyumlu - 1 Puan), **UM** (Uyumsuz - 0 Puan), **UD** (Uygulanamaz).

| Tedbir No | BİGR EKS Güvenlik Tedbiri | Beklenen Kanıt ve Uygulama | Uyum | Mevcut Durum / Açıklama | Telafi Edici Kontrol & Eylem Planı |
|---|---|---|---|---|---|
| **EKS-01** | EKS ağları ile kurumsal IT ağları arasında fiziksel/mantıksal ayrım ve OT DMZ tesis edilmelidir. | Güvenlik duvarı kural seti, DMZ mimari çizimi, VLAN yapılandırma dökümü | `[ ]` | | |
| **EKS-02** | EKS bileşenlerine doğrudan internet erişimi engellenmeli; hiçbir kontrolör veya HMI internete açık olmamalıdır. | Shodan/Censys tarama raporu, dış IP NAT tablosu, güvenlik duvarı kuralları | `[ ]` | | |
| **EKS-03** | EKS uzaktan erişimleri çok faktörlü kimlik doğrulama (MFA) ve kontrollü erişim geçidi (PAM) üzerinden sağlanmalıdır. | PAM erişim logları, MFA yapılandırma kanıtı, süreli onay kayıtları | `[ ]` | | |
| **EKS-04** | EKS varlık envanteri (donanım, yazılım, firmware, port ve protokoller) eksiksiz çıkarılmalı ve güncel tutulmalıdır. | Varlık envanter tablosu, pasif ağ dinleme varlık keşif raporu | `[ ]` | | |
| **EKS-05** | Varsayılan üretici parolaları ve zayıf kimlik bilgileri devreye alma öncesinde değiştirilmelidir. | Cihaz sıkılaştırma kontrol listeleri, yetkili kullanıcı listesi | `[ ]` | | |
| **EKS-06** | EKS bakımında kullanılan geçici cihazlar (dizüstü, USB) güvenlik taramasından geçirilmeli ve kayıt altına alınmalıdır. | Taşınabilir ortam kabul formu, uç nokta EDR tarama raporu | `[ ]` | | |
| **EKS-07** | PLC/RTU lojik ve konfigürasyon değişiklikleri iş emrine bağlanmalı, onay mekanizması işletilmelidir. | Değişiklik yönetim formu, mühendislik istasyonu proje sürüm geçmişi | `[ ]` | | |
| **EKS-08** | EKS bileşenlerinin ve mühendislik projelerinin çevrimdışı (hava boşluklu) yedekleri düzenli alınmalı ve test edilmelidir. | Çevrimdışı yedekleme kasası kayıtları, test geri yükleme tutanağı | `[ ]` | | |
| **EKS-09** | Kritik güvenlik olay kayıtları (syslog, güvenlik duvarı, SCADA alarmları) merkezi izleme sistemine aktarılmalı ve zaman senkronizasyonu sağlanmalıdır. | NTP/PTP yapılandırma kaydı, SIEM/SOC log akış ekran görüntüleri | `[ ]` | | |
| **EKS-10** | EKS'ye özel Olay Müdahale Planı hazırlanmalı ve yılda en az bir kez masa başı tatbikatı yapılmalıdır. | Kurumsal Olay Müdahale Planı, tatbikat tutanağı ve iyileştirme raporu | `[ ]` | | |
| **EKS-11** | Emniyet Enstrümanlı Sistemler (SIS/ESD) ile temel proses kontrol sistemleri (BPCS/DCS) fiziksel/mantıksal olarak ayrılmalıdır. | Emniyet mimarisi çizimi, Safety PLC bağımsız ağ konfigürasyonu | `[ ]` | | |
| **EKS-12** | EKS ağlarında sadece gerekli endüstriyel protokol ve servislere izin verilmeli, gereksiz portlar kapatılmalıdır. | Ağ anahtarı port güvenlik ayarları, güvenlik duvarı beyaz liste kuralları | `[ ]` | | |

---

## 3. Uyum Skoru ve Olgunluk Özeti

- **Toplam Tedbir Sayısı:** 12
- **Maksimum Puan:** 24 Puan
- **Alınan Puan:** `[    ] / 24`
- **Uyum Oranı (%):** `[    % ]`

### Olgunluk Seviyesi Değerlendirmesi:
- `%0 - %49`: **Kritik Risk (Acil Eylem Gerekli)**
- `%50 - %74`: **Gelişmekte Olan (Temel kontroller var, operasyonel eksikler mevcut)**
- `%75 - %89`: **Yetkin (Yüksek uyum, sürekli izleme ve iyileştirme aşaması)**
- `%90 - %100`: **İleri Düzey / Olgun (Tam uyumlu, denetlenebilir ve dayanıklı EKS)**

---

## 4. Denetim Onay ve İmza

| Rol | Ad Soyad | Unvan | Tarih | İmza |
|---|---|---|---|---|
| **Baş Denetçi** | | Bilgi Güvenliği / EKS Denetçisi | | |
| **Tesis Temsilcisi** | | Otomasyon / Tesis Müdürü | | |
| **Kurum Onayı** | | CISO / Bilgi İşlem Daire Başkanı | | |
