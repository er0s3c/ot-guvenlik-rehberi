# OT Rol Tabanlı Erişim Kontrolü (RBAC) ve Siemens UMC Tasarım Şablonu

[Şablonlar Ana Sayfası](README.md) · [Zero Trust, RBAC ve PAM](../docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md) · [Siemens ve Merkezi Kullanıcı Yönetimi](../docs/10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md) · [BİGR EKS Matrisi](10-bigr-eks-denetim-matrisi.md)

Bu mühendislik şablonu; endüstriyel otomasyon ortamlarında (OT/ICS) Rol Tabanlı Erişim Kontrolü (RBAC) mimarisinin tasarlanması, Active Directory (AD) $\to$ SIMATIC UMC $\to$ TIA Portal UMAC $\to$ WinCC Unified ve S7-1500 PLC yetki zincirinin yapılandırılması, çoklu üretici (Rockwell FTSEC, Schneider, OPC UA) hak eşlemelerinin yapılması ve acil durum (Break-Glass) hesaplarının denetimi için hazırlanmıştır.

---

## 1. Tesis Bilgileri ve Kimlik Altyapısı Özeti

| Parametre | Tesis Değeri / Yapılandırma |
|---|---|
| **Tesis / Bölge (Zone) Adı** | |
| **Merkezi Kimlik Kaynağı (IDP)** | Active Directory (AD) / LDAP / Yerel UMC |
| **UMC Dağıtım Modu** | `[ ]` Ring Server (HA) `[ ]` Tekil Sunucu `[ ]` Yerel UMAC |
| **AD - UMC Bağlantı Protokolü** | `[ ]` LDAPS (Port 636) `[ ]` Kerberos over TLS |
| **Referans Zaman Kaynağı (NTP/PTP)** | Stratum-1 / Stratum-2 NTP IP: `....................` |
| **Tasarım Tarihi ve Mühendis** | |

---

## 2. Kurumsal AD $\to$ Siemens UMC $\to$ Hedef Cihaz Rol Eşleme Matrisi

Aşağıdaki tablo, kurumsal IT/OT dizinindeki güvenlik gruplarının otomasyon katmanındaki somut izinlere nasıl dönüştürüleceğini belirler:

| AD Güvenlik Grubu (Level 3 / Corp) | SIMATIC UMC Rolü | TIA Portal Mühendislik Rolü | WinCC Unified HMI Yetkisi | S7-1500 CPU Fonksiyonel Hakkı | Hedef Bölge / Varlık Kapsamı |
|---|---|---|---|---|---|
| `GG_OT_Operators` | `UMC_Operator` | *Yok (Erişim Engelli)* | `Operate`, `Acknowledge_Alarms` | `HMI access` (Salt tag okuma/yazma) | Zone 1 & Zone 2 HMI Panelleri |
| `GG_OT_Shift_Supervisors` | `UMC_Supervisor` | `Project Read-Only` | `Recipe_Management`, `Operate`, `Acknowledge` | `Read access`, `HMI access` | Zone 1 & Zone 2 SCADA / HMI |
| `GG_OT_Process_Engineers` | `UMC_Engineer` | `Standard Engineering` | `Modify_Parameters`, `Recipe_Management` | `Write access / Modify process values` | Üretim Hattı PLC'leri (Safety hariç) |
| `GG_OT_Safety_Engineers` | `UMC_Safety_Eng` | `Safety Engineering` | `Modify_Safety_Parameters` | `Full access / Safety download` | Safety PLC'ler (F-CPU) |
| `GG_OT_Maintenance_Techs` | `UMC_Maintenance` | `Diagnostic Viewer` | `Read_Only_Monitoring` | `Diagnostics & Force` (Süreli onaylı) | Tüm Saha PLC'leri ve Sürücüler |
| `GG_OT_Security_Auditors` | `UMC_Auditor` | `Audit Viewer` | `Read_Only_Monitoring` | `Diagnostics buffer read` | Tüm OT Varlıkları (Salt Okunur) |
| `GG_OT_UMC_Admins` | `UMC_Administrator` | *Yok (Proses yetkisi yok)* | *Yok (Operasyon yetkisi yok)* | *Yok (PLC programlama yetkisi yok)* | Yalnızca SIMATIC UMC Sunucuları |
| `GG_OT_Remote_Vendors` | `UMC_Vendor_Temp` | `Restricted Engineering` | *Geçici ekran izleme* | `Online monitoring` (PAM üzerinden 2 sa) | Belirli Tekil PLC / Hücre |

---

## 3. Donanım ve Yazılım Seviyesinde Detaylı İşlev Hakları (Function Rights)

| Rol Adı | TIA Portal Hakları | S7-1500 CPU Hakları | WinCC Unified Hakları | SCALANCE / Ağ Cihazı Hakları |
|---|---|---|---|---|
| **Operator** | Giriş Yetkisi Yok | Tag Read/Write (HMI üzerinden) | Buton kontrolü, alarm onayı | Giriş Yetkisi Yok |
| **Shift Supervisor** | Proje Salt Okunur Açma | Alarm/Teşhis okuma | Reçete oluşturma/yükleme, limit ayarı | Giriş Yetkisi Yok |
| **Process Engineer** | DB/FB/FC düzenleme, PLC Download | Program yazma, online debug, tag force | Ekran geliştirme, parametre yükleme | Konfigürasyon Salt Okunur |
| **Safety Engineer** | Safety F-Block düzenleme, Safety Compile | F-Signature güncelleme, Safety Download | Safety bypass parametresi onaylama | Giriş Yetkisi Yok |
| **Maintenance Tech** | Hardware Diagnostics, Online & Diagnostic | Hata tamponu okuma, geçici force | Bakım ekranı trend izleme | Port durumu okuma (LLDP/SNMP) |
| **UMC Administrator** | Proje Kullanıcı Yönetimi | Yok (PLC programına erişemez) | Kullanıcı veritabanı senkronizasyonu | Radius/TACACS+ Kullanıcı Yönetimi |

---

## 4. Çoklu Üretici ve Protokol Yetki Uyarlama Kataloğu

| Platform / Standart | Merkezi Kimlik Kaynağı | Rol / Profil Tanımı | İzin Düzeyi ve Öncelik | Denetim İzi Kaynağı |
|---|---|---|---|---|
| **Siemens (UMC & TIA UMAC)** | Active Directory / SADS | UMC Grupları $\to$ UMAC Function Rights | CPU yerel eşleme tablosu | UMC Event Log (`UM_VIEWELG`) & CPU Diag Buffer |
| **Rockwell Automation (FTSEC)** | FactoryTalk Directory / Windows AD | FTSEC Windows-Linked Groups | Action-based (Deny-over-Allow kuralı) | FactoryTalk Audit Log (FTAE) |
| **Schneider Electric (Control Expert)** | EIFE / PACSec / Central LDAP | Security Editor Profilleri (Operate/Eng/Admin) | Cihaz güvenlik profili eşleşmesi | PAC Controller Syslog & Event Log |
| **ABB (System 800xA)** | Windows Domain Controller | Aspect Directory $\to$ Functional & Area Perms | Hiyerarşik nesne bazlı yetki | 800xA Audit Trail & Windows Security Log |
| **Emerson (DeltaV)** | DeltaV User Manager / Windows DC | Area & Workstation Security Groups | 21 CFR Part 11 Four-Eyes elektronik imza | DeltaV Event Chronicle & Verify Log |
| **OPC UA (IEC 62541-18)** | GDS (Global Discovery Server) / X.509 | OPC UA Roles (`Anonymous`, `Operator`, `Engineer`) | NodeId Bitmask (`Read`, `Write`, `Call`, `WritePerm`) | OPC UA Audit Events & Session Logs |

---

## 5. Acil Durum (Break-Glass) ve Çevrimdışı Kasa Yönetimi

Merkezi UMC / AD altyapısının çökmesi, ağ izolasyonu veya siber saldırı durumunda acil bakım müdahalesi için yerel hesap prosedürü:

| Varlık / Cihaz Adı | Acil Durum Hesabı | Parola Saklama Konumu | Onay Verenler (Four-Eyes) | Maksimum Kullanım Süresi | Olay Sonrası Zorunlu Eylemler |
|---|---|---|---|---|---|
| **S7-1500 PLC Grubu 1** | `Local_Emergency_Admin` | PAM Kasası (Mühürlü Zarf / Vault) | Vardiya Amiri + OT Güvenlik Sor. | 4 Saat | 1. CPU Diag Buffer dökümü al<br>2. Parolayı PAM üzerinden yenile<br>3. Değişiklik raporu imzala |
| **WinCC Unified SCADA** | `Local_Recovery_Admin` | PAM Kasası (Safe-Deposit) | Tesis Müdürü + Vardiya Amiri | 2 Saat | 1. SCADA Audit Trail dışa aktar<br>2. Parola rotasyonu yap<br>3. UMC servisini kontrol et |
| **SCALANCE Firewall** | `scalance_local_admin` | Fiziksel Kasa (Anahtarlı Kasa) | Ağ Yöneticisi + OT Güvenlik Sor. | 2 Saat | 1. Firewall config hash karşılaştır<br>2. Parolayı yenile ve yedekle |

---

## 6. NTP, Sertifika ve Zaman Bağımlılıkları Doğrulama Kontrol Listesi

- [ ] **NTP Kaynağı:** Tüm PLC'ler, UMC sunucuları ve SCADA düğümleri aynı güvenilir OT NTP sunucusuna bağlıdır.
- [ ] **Saat Kayması (Clock Drift):** UMC ve CPU saat farkı $\le 60\text{ saniye}$ olarak doğrulanmıştır.
- [ ] **Sertifika Geçerliliği:** UMC Root CA ve sunucu X.509 sertifikalarının bitiş tarihine en az 180 gün vardır.
- [ ] **SADS / LDAPS Portu:** UMC $\leftrightarrow$ AD arasındaki TCP 636 (LDAPS) portu firewall üzerinde kısıtlı IP eşleşmesiyle açıktır.
- [ ] **Kilitlenme Testi (Lockout Verification):** UMC sunucusu ağdan izole edildiğinde yerel acil durum hesabıyla CPU'ya erişilebildiği masa başında test edilmiştir.

---

## 7. Periyodik RBAC ve Kimlik Denetim Formu (3 Aylık / Yıllık)

| Denetim Maddesi | Kontrol Sorusu | Tespit Edilen Uygunsuzluk / Durum | Düzeltici Faaliyet & Sorumlu |
|---|---|---|---|
| **Kullanıcı Yaşam Döngüsü** | Tesis veya görev değiştiren personelin AD/UMC hesabı kapatıldı mı? | | |
| **Yetki Şişmesi (Privilege Creep)** | Operatör veya bakımcı grubunda fazladan mühendislik hakkı bulunan hesap var mı? | | |
| **Geçici / Tedarikçi Hesapları** | Süresi dolmuş aktif `Vendor` veya `Temporary` hesabı mevcut mu? | | |
| **Break-Glass Parola Durumu** | Acil durum hesapları son 90 gün içinde kullanıldı mı? Parolaları güncel mi? | | |
| **UMC Event Log Analizi** | Başarısız oturum açma veya yetki aşımı denemeleri SIEM'e aktarıldı mı? | | |

---

## 8. Onay ve İmza

| Rol | İsim - Soyisim | Unvan | İmza | Tarih |
|---|---|---|---|---|
| **Hazırlayan (OT Mühendisi)** | | Otomasyon / E&I Mühendisi | | |
| **Kontrol Eden (OT Güvenlik)** | | Endüstriyel Siber Güvenlik Uzmanı | | |
| **Onaylayan (Tesis Müdürü)** | | Tesis İşletme Müdürü | | |
