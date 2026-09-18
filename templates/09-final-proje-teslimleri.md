# Final OT güvenlik projesi: 23 teslimin kabul şablonu

[Ana sayfa](../README.md) · [Şablonlar](README.md) · [Ders değerlendirmesi](07-ders-ve-degerlendirme.md) · [Risk ve değerlendirme kaydı](08-degerlendirme-ve-risk-kaydi.md)

Bu şablon, 50 konulu kapsamın finalindeki **23 çıktının tamamını** tek kurgusal danışmanlık dosyasına bağlar. **Özgün eğitim sentezidir**; standart uygunluğu, saha testi veya devreye alma onayı değildir. Çıktılar ayrı Markdown dosyaları veya tek belgenin bölümleri olabilir; ayrı kimlik ve kabul kaydı taşımaları yeterlidir.

Altı başlangıç şablonu bu teslimleri besler; altı boş formun bulunması 23 tamamlanmış rapor demek değildir. Öğrenci mevcut formları doldurur, eksik mimari/rapor/maliyet alanlarını aşağıdaki sözleşmeyle tamamlar. Yazılım veya sanal makine kurulumu gerekmez; gerçek kontrolün çalıştığına ilişkin kanıt yoksa sonuç belge/tasarım düzeyinde tutulur.

## 1. Proje kartı ve ortak kapsam

| Alan | Doldurulacak değer |
|---|---|
| Proje kimliği ve sürüm | [PRJ-001], [sürüm], [YYYY-AA-GG] |
| Kurgusal hizmet | [su, enerji veya seçilen hizmet], kritik süreç: [tanım] |
| Amaç ve karar | [değerlendirme sorusu ve yönetimden istenen karar] |
| Varlık kapsamı | [PLC, RTU, HMI, SCADA, historian, EWS, switch, firewall ve destek işlevleri] |
| Bölge ve dış bağımlılıklar | [bölge kimlikleri], [uzak saha/vendor/kimlik/zaman/güç/bulut] |
| Girdi paketi | [kurgusal belgeler, sentetik kayıtlar, kaynaklar ve sürümler] |
| Hazırlayan / inceleyen | [roller], değerlendirme: [eğitmen / öz değerlendirme] |
| Kapsam dışı | [varlık, yöntem ve doğrulanamayacak iddialar] |
| Bütçe ortak varsayımları | [tesis, varlık, kullanıcı, gözlem noktası, log hacmi, saklama ve süre] |
| Sonuç düzeyi | [belge tasarımı / verilen kayıt üzerinde inceleme]; gerçek sistem testi: [yapılmadı] |

Örnek ortak senaryo seçimi için [su ve atıksu](../docs/02-sektorler/01-su-ve-atiksu.md), [elektrik ve enerji](../docs/02-sektorler/02-elektrik-ve-enerji.md) veya [mimari inceleme laboratuvarı](../labs/02-mimari-inceleme.md) kullanılabilir. Farklı örnekler birleştiriliyorsa varlık adları ve verilen varsayımlar önce tutarlı hale getirilir.

## 2. Ortak kimlikler ve kanıt zinciri

| Kimlik türü | Kurgusal biçim | Kullanım |
|---|---|---|
| Varlık | `SU-PLC-001` | Envanter, çizim, protokol, bulgu, yedek ve maliyet kapsamı |
| Akış | `AK-001` | Kaynak/hedef, amaç, oturum yönü, kural ve gözlem |
| Bölge / geçiş | `ZN-001` / `CD-001` | Zone/conduit çizimi ve bağlı akışlar |
| Firewall kuralı | `FW-001` | Gerekçe, akış, izin/ret ve kabul planı |
| Bulgu | `BUL-001` | Gözlenen sapma veya kanıt boşluğu |
| Risk | `RSK-001` | İşletme etkisi, risk sahibi, karar ve kalan risk |
| Test / belge kontrolü | `TST-001` | Sınanan iddia, beklenen sonuç, gerçek gözlem veya yürütülmedi |
| Kanıt | `KNT-001` | Girdi/çıktı kaynağı, sürüm/tarih, tür ve desteklediği iddia |
| Değişiklik / iş | `DEG-001` | Düzeltme sahibi, termin, geri dönüş ve kabul |
| Final teslim | `TES-01` … `TES-23` | Aşağıdaki 23 çıktı ve bunların kabul durumu |

Örnek bağ: `SU-PLC-001 → AK-001 → FW-001 → BUL-001 → RSK-001 → DEG-001 → TST-001 → KNT-001`. Bu zincir her kaydın birebir tek kayda bağlanmasını zorunlu kılmaz; bir bulgu birden çok varlık ve riski etkileyebilir. Çapraz referanslar tekil ve tutarlı olmalıdır.

| Referans veren teslim | Kullandığı varlık / akış | Bulgu / risk | Test / kanıt | Açık tutarsızlık |
|---|---|---|---|---|
| [TES-...] | [kimlikler] | [BUL/RSK] | [TST/KNT] | [soru ve sahibi / yok] |

## 3. Yirmi üç teslimin sözleşmesi

Her satırdaki alanları doldurun veya ilgili belgede bulunduğu yere bağlantı verin. **Kabul**, belgenin kendi kapsamını karşılamasıdır; gerçek sistemin güvenli olduğunun kabulü değildir.

| No / teslim | Doldurulacak asgari alanlar | Kabul ölçütü | Mevcut temel |
|---|---|---|---|
| 1 — Executive Summary | [hizmet/kapsam], [ana bulgular], [iş etkisi], [istenen karar], [sahip/termin], [belirsizlik] | Teknik ekte olmayan iddia yok; öncelikli kararlar BUL/RSK kimliklerine bağlı | [Yönetici özeti formu](08-degerlendirme-ve-risk-kaydi.md) |
| 2 — OT Architecture | [kontrol/gözetim/işletme işlevleri], [bileşenler], [destek bağımlılıkları], [hata davranışı], [veri/kontrol ilişkileri] | Bileşenlerin işi ve birbirine bağımlılığı anlaşılır; IT/kimlik kaybı sınırı belirtilmiş | [Mimari](../docs/08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) |
| 3 — Purdue Mapping | [varlık/işlev], [seviye gösterimi], [yerleşim gerekçesi], [istisna], [bulut/uzak saha bağı] | Seviye erişim yetkisi sayılmamış; 3.5/5 gösteriminin sınırı açıklanmış | [Purdue ve bölgeler](../docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) |
| 4 — Asset Inventory | [varlık kimliği], [üretici/model/sürüm], [işlev/kritiklik], [sahip], [bölge], [kaynak/tarih], [belirsizlik] | Çizimdeki her kapsam içi varlık envanterde; bilinmeyen sürüm tahmin edilmemiş | [Envanter ve akış](01-envanter-ve-akis.md) |
| 5 — Network Diagram | [zone/conduit], [cihaz/işlev], [bağlantılar], [yeni oturum yönü], [yönetim/izleme yolu], [şema açıklaması] | Çizimdeki ilişkiler AK kimlikleriyle eşleşir; kavramsal çizim kablolama veya çalışır kural diye sunulmaz | [Mimari labı](../labs/02-mimari-inceleme.md), [akış formu](01-envanter-ve-akis.md) |
| 6 — Protocol Inventory | [AK/varlık], [protokol/profil/sürüm], [taşıma/port veya uygulanamaz], [işlem amacı], [kimlik/şifreleme durumu], [kaynak] | Porttan çıkarım ile doğrulanmış protokol ayrılmış; bütün protokollere TCP portu atanmamış | [Protokol rehberi](../docs/07-protokoller/00-secim-ve-karsilastirma.md) |
| 7 — RBAC Matrix | [sekiz rol], [sistem], [okuma/işletme/değişiklik işlemi], [süre/koşul], [onay sahibi], [kanıt] | Operator, Engineer, Maintenance, Supervisor, Administrator, Vendor, Security Analyst ve Read-only Auditor kapsanır; rol/hesap/işlem ayrımı açık | [RBAC ve PAM](../docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md), [uzak erişim](06-tedarikci-ve-uzak-erisim.md) |
| 8 — Firewall Matrix | [FW/AK], [kaynak/hedef], [başlatan uç], [taşıma/hedef port], [izin/ret], [gerekçe], [log], [kabul] | Her iznin sahibi ve işi var; varsayılan ret açık; sembolik port bilinmeyen olarak korunmuş | [Sembolik firewall matrisi](../docs/08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) |
| 9 — Zone/Conduit Architecture | [ZN/CD kimlikleri], [gruplama gerekçesi], [güven sınırları], [AK ilişkileri], [kontrol], [risk bağlantısı] | VLAN, Purdue seviyesi ve zone birbirine eşit sayılmamış; geçişlerin amacı ve denetimi belli | [Tehdit modeli](02-tehdit-modeli.md), [mimari](../docs/08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) |
| 10 — Vulnerability Assessment | [duyuru/CVE], [ürün/sürüm/işlev], [önkoşul], [kaynak/tarih], [etkilenen/belirsiz kararı], [telafi ve test sınırı] | Sürüm eşleşmesi başarıyla istismar diye raporlanmamış; öncelik işletme bağlamıyla gerekçeli | [Bulgu ve risk formu](08-degerlendirme-ve-risk-kaydi.md) |
| 11 — Security Assessment | [kapsam/RoE], [15 aşama durumu], [yöntem], [bulgular], [kanıt sınırları], [dokuz assessment çıktısı] | İzinli/yürütülen/yürütülmeyen yöntemler ayrılmış; yönetici sonucu kanıtla bağlı | [Değerlendirme formu](08-degerlendirme-ve-risk-kaydi.md) |
| 12 — MITRE ATT&CK Mapping | [senaryo/BUL], [alan ve teknik ID/adı], [kaynak/sürüm/erişim tarihi], [gözlenen davranış], [kontrol], [kör nokta] | Teknik kimliği gözlenmemiş davranışı gerçekmiş gibi göstermiyor; savunma ve kanıt aynı satırda | [Tehdit modeli](02-tehdit-modeli.md), [ATT&CK bölümü](../docs/03-tehdit-modelleme/02-mitre-attack-ics.md) |
| 13 — Risk Register | [RSK/BUL], [hizmet/emniyet etkisi], [öncelik gerekçesi], [kontrol/kanıt], [risk sahibi], [işlem/termin], [kalan risk/kabul] | Kalan risk ve kabul yetkisi görünür; belirsiz risk düşük diye kapatılmamış | [Risk kaydı](08-degerlendirme-ve-risk-kaydi.md) |
| 14 — SIEM Architecture | [kayıt kaynakları], [alan/zaman], [toplayıcı/iletim/saklama], [kapasite varsayımı], [roller], [sağlık], [algılama] | Kaynak → analist yolu izlenebilir; veri kaybı ve gecikme görünür; ürün bağlantısı tek başına doğrulama sayılmaz | [İzleme ve SOC](../docs/09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md), [algılama kartı](03-algilama-karti.md) |
| 15 — IDS Architecture | [gözlem noktası], [trafik kopyalama ilişkisi], [görülen protokol/yön], [kör nokta], [sensör sağlığı], [alarm aktarımı] | Pasif gözlem ile aktif engelleme ayrılmış; şifreli/görülmeyen trafik kapsamda gösterilmemiş | [İzleme](../docs/04-savunma/03-izleme-ve-algilama.md), [algılama kartı](03-algilama-karti.md) |
| 16 — Incident Response Plan | [roller], [doğrulama], [emniyet/işletme kararı], [sınırlama seçenekleri], [kanıt koruma], [iletişim], [dönüş kapıları] | PLC'yi kapatma otomatik ilk adım değil; karar yetkisi ve kanıt/emniyet çatışması kayıtlı | [Olay ve kurtarma](04-olay-ve-kurtarma.md) |
| 17 — Backup/DR Plan | [varlık/yedek/proje sürümü], [yedek sıklığı], [saklama/erişim], [uyum/lisans], [RTO/RPO], [geri yükleme sırası], [doğrulama] | Yedeğin varlığı, uyumu ve geri yükleme kanıtı ayrı; yedek sunucu temiz kopya sayılmamış | [Kurtarma formu](04-olay-ve-kurtarma.md), [kurtarma bölümü](../docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md) |
| 18 — Hardening Checklist | [yedi varlık sınıfı], [kontrol], [durum], [kanıt], [istisna], [sahip], [değişiklik/geri alma] | PLC/HMI/SCADA/Windows Server/EWS/firewall/switch ayrı ele alınmış; uygulanamaz alan gerekçeli | [Sıkılaştırma listeleri](../docs/08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md), [değişiklik formu](05-degisiklik-ve-kabul.md) |
| 19 — Security Testing Plan | [yetki/RoE], [TST/yöntem/hedef], [olumlu/olumsuz beklenti], [etki], [durdurma/geri alma], [gerekli kanıt] | Test planı yürütülmüş sonuç diye sunulmamış; kapsam dışı yöntemler açık | [Değerlendirme formu](08-degerlendirme-ve-risk-kaydi.md), [kabul planı](05-degisiklik-ve-kabul.md) |
| 20 — Remediation Roadmap | [BUL/RSK], [iş], [bağımlılık/öncelik], [sahip], [termin], [kaynak], [kabul], [kalan risk] | Takvim gerçek düzeltme ve kabul kanıtına bağlı; bütün işler aynı anda başlayacak varsayılmamış | [90 günlük yol haritası](../docs/04-savunma/06-90-gunluk-yol-haritasi.md), [değişiklik formu](05-degisiklik-ve-kabul.md) |
| 21 — Budget Architecture | [açık kaynak güvenlik bileşenleri], [karşılanan gereksinimler], [kör noktalar], [donanım/emek], [TCO], [varsayım/kaynak] | Lisans bedelinin sıfır olması toplam maliyeti sıfır yapmıyor; ortak kapsam korunmuş | [Maliyet ve seçim modeli](../docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md) |
| 22 — Professional Architecture | [açık kaynak/ticari görev dağılımı], [entegrasyon], [destek], [TCO], [fiyat kanıtı], [kalan gereksinimler] | Aynı işlev iki kez ücretlendirilmemiş; paket/sürüm ve teklif eksikleri görünür | [Maliyet modeli](../docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md), [ürün karşılaştırması](../docs/10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md) |
| 23 — Enterprise Architecture | [ticari lisans/destek kapsamı], [yedeklilik], [sensör/yönetim], [veri/çıkış koşulları], [TCO], [kabul kanıtı] | Ticari kapsam güvenlik garantisi sayılmamış; ortak ölçek ve destek farkları açık | [Maliyet modeli](../docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md), [tedarikçi formu](06-tedarikci-ve-uzak-erisim.md) |

## 4. Mimari ve kontrolleri kopyalanabilir satırlara dönüştürme

### Varlık, seviye ve bölge

| Varlık kimliği | İşlev | Purdue gösterimi ve gerekçe | Zone | Bağımlılık | Kanıt / belirsizlik |
|---|---|---|---|---|---|
| [varlık] | [işlev] | [seviye], [gerekçe] | [ZN-...] | [varlık/hizmet kimliği] | [KNT-... / doğrulanacak] |

### Akış, protokol ve firewall

| Akış / kural | Kaynak → hedef | Yeni oturumu başlatan | Protokol / taşıma / hedef port | İzinli işlem ve karar | Gerekçe / sahip | Log / test |
|---|---|---|---|---|---|---|
| [AK-...] / [FW-...] | [varlık → varlık] | [uç] | [protokol/profil], [taşıma], [port veya uygulanamaz/doğrulanacak] | [işlem], [izin/ret] | [iş], [rol] | [KNT/TST veya gerekli kanıt] |

### Kontrol, bulgu ve kabul

| Kontrol | Varlık / akış | Bulgu / risk | Sahip ve değişiklik | Kabul ölçütü | Kanıt ve sonuç | Kalan risk |
|---|---|---|---|---|---|---|
| [kontrol] | [kimlikler] | [BUL/RSK] | [rol], [DEG] | [ölçüt] | [KNT/TST; yoksa yürütülmedi] | [açıklama/karar] |

Bu satırlar mevcut envanter, algılama, olay ve değişiklik formlarının yerine geçmez; final rapordaki bağlantılarını görünür kılar. Aynı alan iki yerde tutuluyorsa ana kayıt hangisi olduğu belirtilir.

## 5. Üç maliyet mimarisini aynı kapsamla karşılaştırma

Budget, Professional ve Enterprise bu eğitimdeki seçenek adlarıdır. Her birinin aynı gereksinimi aynı düzeyde karşıladığı varsayılmaz; farklar aşağıda açıkça yazılır. Kurgusal hesap için [maliyet bölümünün](../docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md) verileri kullanılabilir; oradaki varsayımsal tutarlar güncel piyasa fiyatı olarak aktarılmaz.

| Gereksinim / ortak ölçek | Budget | Professional | Enterprise | Farkın karar üzerindeki etkisi |
|---|---|---|---|---|
| Tesis / varlık / gözlem noktası | [ortak kapsam] | [ortak kapsam] | [ortak kapsam] | [kapsam değiştiyse gerekçe] |
| Kullanıcı / erişim oturumu | [sayı ve kabul varsayımı] | [aynı] | [aynı] | [kapasite/destek farkı] |
| Log hacmi / saklama / kopya | [birim ve süre] | [aynı] | [aynı] | [lisans/saklama farkı] |
| Protokol görünürlüğü | [kanıtlanan ve eksik] | [kanıtlanan ve eksik] | [kanıtlanan ve eksik] | [kalan risk] |
| Destek / yedeklilik / çıkış | [kapsam] | [kapsam] | [kapsam] | [işletme/tedarik bağımlılığı] |

| Maliyet kalemi | Budget | Professional | Enterprise | Birim, süre ve kaynak |
|---|---|---|---|---|
| Hardware | [ilk yatırım] | [ilk yatırım] | [ilk yatırım] | [para birimi, kapsam, kaynak] |
| Firewall | [cihaz/entegrasyon] | [cihaz/entegrasyon] | [cihaz/entegrasyon] | [lisansın ayrı/dahil durumu] |
| IDS | [sensör/entegrasyon] | [sensör/entegrasyon] | [sensör/entegrasyon] | [gözlem kapsamı] |
| SIEM | [entegrasyon/kapasite] | [entegrasyon/kapasite] | [entegrasyon/kapasite] | [lisans ölçütü ve dahil kalemler] |
| PAM | [entegrasyon] | [entegrasyon] | [entegrasyon] | [kasa/oturum kapsamı] |
| Monitoring | [sağlık izleme] | [sağlık izleme] | [sağlık izleme] | [bileşen kapsamı] |
| Licensing | [yıllık] | [yıllık] | [yıllık] | [satıcı/SKU/tarih/bölge; teklif veya kurgusal] |
| Support | [yıllık] | [yıllık] | [yıllık] | [lisansa dahil değilse ayrı] |
| Maintenance | [saat × ücret] | [saat × ücret] | [saat × ücret] | [emek varsayımı ve sorumlu] |
| Diğer / çıkış | [enerji, depolama, yenileme, geçiş] | [aynı sınıflar] | [aynı sınıflar] | [çifte sayım sınırı] |
| Toplam | [ilk yıl ve N yıl] | [ilk yıl ve N yıl] | [ilk yıl ve N yıl] | [denklem ve süre] |

Fiyat kanıtı: `[ürün/SKU] [sürüm/paket] [tarih] [ülke/bölge] [para birimi] [birim] [vergi] [destek dahil mi?] [yenileme] [resmî URL/teklif kimliği]`. Kanıt yoksa `teklif gerekli` veya `kurgusal varsayım` yazılır; bilinmeyen kalem sıfır sayılmaz. Seçim gerekçesi maliyet yanında kontrol kapsamını ve kalan riski de karşılaştırır.

## 6. Teslim ve kabul kaydı

| Teslim | Dosya / bölüm ve sürüm | Durum | Değerlendiren / tarih | Açık düzeltme ve kabul kanıtı |
|---|---|---|---|---|
| TES-01 | [Executive Summary] | [durum] | [rol/tarih] | [kayıt] |
| TES-02 | [OT Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-03 | [Purdue Mapping] | [durum] | [rol/tarih] | [kayıt] |
| TES-04 | [Asset Inventory] | [durum] | [rol/tarih] | [kayıt] |
| TES-05 | [Network Diagram] | [durum] | [rol/tarih] | [kayıt] |
| TES-06 | [Protocol Inventory] | [durum] | [rol/tarih] | [kayıt] |
| TES-07 | [RBAC Matrix] | [durum] | [rol/tarih] | [kayıt] |
| TES-08 | [Firewall Matrix] | [durum] | [rol/tarih] | [kayıt] |
| TES-09 | [Zone/Conduit Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-10 | [Vulnerability Assessment] | [durum] | [rol/tarih] | [kayıt] |
| TES-11 | [Security Assessment] | [durum] | [rol/tarih] | [kayıt] |
| TES-12 | [MITRE ATT&CK Mapping] | [durum] | [rol/tarih] | [kayıt] |
| TES-13 | [Risk Register] | [durum] | [rol/tarih] | [kayıt] |
| TES-14 | [SIEM Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-15 | [IDS Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-16 | [Incident Response Plan] | [durum] | [rol/tarih] | [kayıt] |
| TES-17 | [Backup/DR Plan] | [durum] | [rol/tarih] | [kayıt] |
| TES-18 | [Hardening Checklist] | [durum] | [rol/tarih] | [kayıt] |
| TES-19 | [Security Testing Plan] | [durum] | [rol/tarih] | [kayıt] |
| TES-20 | [Remediation Roadmap] | [durum] | [rol/tarih] | [kayıt] |
| TES-21 | [Budget Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-22 | [Professional Architecture] | [durum] | [rol/tarih] | [kayıt] |
| TES-23 | [Enterprise Architecture] | [durum] | [rol/tarih] | [kayıt] |

Durumlar: `başlanmadı`, `taslak`, `teslim edildi`, `düzeltme gerekli`, `belge kabul edildi`. Bir alan uygulanamazsa ilgili teslim içinde gerekçesi yazılır; bütün teslim sessizce listeden çıkarılmaz. Kurgusal senaryoda zafiyet doğrulanamamış olması, kaynakları ve kapsamı açıklanmış bir değerlendirme teslimine engel değildir; zafiyet uydurulmaz.

### Son tutarlılık kontrolü

- [ ] 23 teslimin tamamı referans ve durum taşıyor.
- [ ] Çizim, envanter, Purdue, zone/conduit ve protokol kimlikleri uyuşuyor.
- [ ] Rol matrisindeki izinler firewall ve hedef işlem yetkisiyle tutarlı.
- [ ] Her bulgunun kanıtı veya açık kanıt eksiği var; risk sahibi belirli.
- [ ] SIEM/IDS görünürlüğü gerçek girdi sınırlarını aşıyor gibi gösterilmemiş.
- [ ] Test planı, yürütülmüş belge kontrolü ve saha testi birbirine karıştırılmamış.
- [ ] Olay ve kurtarma kararları doğru işletme/teknik rollere bağlanmış.
- [ ] Üç maliyet seçeneği ortak kapsamda; bilinmeyen fiyat ve kurgusal sayı etiketli.
- [ ] İyileştirme takvimi kabul kanıtına ve kalan risk kararına bağlı.
- [ ] Kaynak, yayın/sürüm ve erişim tarihi güncel; lisanslı standart uygunluğu iddia edilmemiş.

Final portföy ifadesi: `[kurgusal hizmet] için kaynaklı OT güvenlik mimarisi, belge temelli değerlendirme ve 23 teslimden oluşan danışmanlık projesi`. Yapılmayan kurulum veya saha testi bu ifadeye eklenmez. Eksikler [ders değerlendirme formunun](07-ders-ve-degerlendirme.md) düzeltme kaydıyla geri bildirilir.

## Kaynak ve kapsam

Bu teslim sözleşmesi, tablolar ve kabul ölçütleri **özgün eğitim sentezidir**. Teknik dayanaklar satırlarda bağlanan depo bölümlerinde; maliyet kaynakları [maliyet modelinde](../docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md) bulunur. Şablon, standart denetim raporu, ürün tavsiyesi veya gerçek tesis tasarım onayı değildir. Son inceleme: **17.09.2026**.
