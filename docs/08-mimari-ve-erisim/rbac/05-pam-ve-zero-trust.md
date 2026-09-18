# OT ortamında PAM ve Zero Trust mimarisi

[Ana sayfa](../../../README.md) · [Seçim Rehberi](00-secim-ve-karsilastirma.md) · [Active Directory](01-active-directory-ve-ldap.md) · [Siemens UMC](03-siemens-simatic-umc.md) · [Tasarım Şablonu](../../../templates/12-ot-rbac-ve-umc-tasarim-sablonu.md)

**Ayrıcalıklı Erişim Yönetimi (PAM)** ve **Zero Trust**, endüstriyel ağlarda harici tedarikçilerin, bakım mühendislerinin ve kritik yönetici oturumlarının kontrol altına alınmasını sağlar.

---

## 1. OT Zero Trust Mimarisi ve İlkeleri

Geleneksel "çevre güvenliği" (perimeter security) yaklaşımında güvenli bölgeye giren her kullanıcı güvenilir kabul edilirdi. Zero Trust yaklaşımında ise ağ konumu önemsizdir:

```mermaid
flowchart LR
    Vendor["Dış Tedarikçi / Mühendis"] --> MFA["1. MFA & Kimlik Doğrulama"]
    MFA --> PAM["2. PAM Proxy (Oturum İzolasyonu & Video Kayıt)"]
    PAM --> Approver["3. Vardiya Amiri Onayı (Four-Eyes)"]
    Approver --> Vault["4. Parola Kasasından Tek Seferlik Sır Alma"]
    Vault --> EWS["5. Mühendislik İstasyonu / SCADA"]
    EWS --> PLC["6. Hedef PLC (En Az Yetki / Kısıtlı Süre)"]
```

### Zero Trust 5 Temel İlkesi:
1. **Asla Güvenme, Her Zaman Doğrula:** Ağın içindeki cihazlar da potansiyel tehdit kabul edilir.
2. **En Az Yetki (Least Privilege):** Kullanıcıya yalnızca o an yapacağı iş için gereken asgari hak verilir.
3. **Zaman Kısıtlı Erişim (Just-In-Time - JIT):** Yetkiler süresiz verilmez; işlem bitince (ör. 2 saat sonra) otomatik geri alınır.
4. **Mikro-Segmentasyon:** Her hücre ve proses alanı bağımsız güvenlik duvarları ile yalıtılır.
5. **Varsayılan İhlal (Assume Breach):** Sistemin halihazırda sızılmış olduğu varsayılarak tüm eylemler denetim günlüğüne kaydedilir.

---

## 2. PAM Bileşenleri ve İşleyişi

| PAM Bileşeni | Görevi ve OT Faydası | Örnek Uygulama |
|---|---|---|
| **Parola Kasası (Safe/Vault)** | PLC, SCADA ve switch yönetici şifrelerini şifrelenmiş olarak saklar. Kullanıcı şifreyi görmeden oturum açar. | CyberArk Enterprise Vault, HashiCorp Vault |
| **Oturum İzolasyonu (Proxy/Gateway)** | Kullanıcının kendi bilgisayarı ile saha cihazları arasında doğrudan TCP bağlantısını keser; oturumu HTML5/RDP üzerinden taşır. | BeyondTrust PRA, JumpServer |
| **Oturum Video Kaydı** | Mühendisin ekranda yaptığı tüm fare hareketlerini ve komutları video formatında kaydeder. | Olay sonrası adli analiz (forensics) |
| **Dinamik Şifre Rotasyonu** | Oturum kapandığı anda cihazın yerel şifresini otomatik olarak rastgele yeni bir şifreyle değiştirir. | Şifrenin kopyalanmasını önler |
| **Çift Onay (Four-Eyes Principle)** | Kritik bir PLC'ye bağlanmadan önce sistemin Vardiya Amirine onay bildirimi göndermesi. | Yetkisiz bakım müdahalelerini engeller |

---

## 3. Artılar ve Eksiler

| Artıları | Eksileri |
|---|---|
| Tedarikçilere asla kalıcı şifre verilmez; oturum süresi dolunca erişim anında kesilir. | Yüksek lisans maliyeti ve sunucu altyapısı gerektirir. |
| Tüm mühendislik müdahaleleri video ve log olarak kanıtlanır (Denetim uyumluluğu). | PAM sunucusu arızalanırsa acil durum kasalama prosedürü (Break-Glass) olmadan sahaya ulaşılamaz. |
| RDP/SSH tünelleme ile hedef cihaza zararlı yazılım transferi zorlaştırılır. | TIA Portal veya RSLogix gibi ağır mühendislik yazılımlarında RDP gecikmesi yaşanabilir. |

---

## 4. Acil Durum (Break-Glass) Prosedürü

PAM sunucusunun veya ağın çökmesi durumunda tesiste üretimin durmaması için:
1. Her kritik PLC ve HMI için tek bir yerel `Local_Emergency_Admin` hesabı tanımlanır.
2. 24+ karakterli karmaşık parola, mühürlü fiziksel kasada veya çevrimdışı donanımsal kasada tutulur.
3. Parola yalnızca Tesis Müdürü ve Vardiya Amirinin ortak kararıyla açılır.
4. Müdahale bittiğinde CPU Diagnostic Buffer incelenir ve parola derhal değiştirilir.

---

## 5. Hızlı Konfigürasyon Kontrol Listesi

- [ ] Dış tedarikçilerin doğrudan VPN ile sahaya erişimi kapatıldı; PAM zorunlu kılındı.
- [ ] PAM üzerinde 2 saatlik oturum zaman aşımı ve video kayıt profili aktif edildi.
- [ ] Kritik PLC'ler için çift onay (Four-Eyes) kuralı devreye alındı.
- [ ] Break-Glass acil durum şifreleri mühürlü kasaya alındı.
