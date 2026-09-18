# Çoklu üretici sistemlerde ve OPC UA'de RBAC

[Ana sayfa](../../../README.md) · [Seçim Rehberi](00-secim-ve-karsilastirma.md) · [Active Directory](01-active-directory-ve-ldap.md) · [Siemens UMC](03-siemens-simatic-umc.md) · [PAM ve Zero Trust](05-pam-ve-zero-trust.md)

Çok üreticili (heterojen) endüstriyel tesislerde her platform kendi yerel güvenlik ve yetkilendirme motorunu kullanır.

---

## 1. Üretici Bazında RBAC Karşılaştırması

| Platform / Üretici | Güvenlik Motoru | Kimlik Kaynağı | İzin Modeli ve Öncelik | Emniyet ve Kritik İşlem Denetimi |
|---|---|---|---|---|
| **Rockwell Automation** | FactoryTalk Security (FTSEC) | FactoryTalk Directory / Windows AD | **Action-Based:** `Tag Write`, `Online Edit`, `Logic Download`. *Deny-over-Allow* kuralı geçerlidir. | GuardLogix Safety PLC'lerde lojik indirme için zorunlu *Safety Engineer* rolü aranır. |
| **Schneider Electric** | Cybersecurity Admin Expert (CAE) & Security Editor | Merkezi LDAP veya Şifreli Yerel Profil | **Profil Bazlı:** `Full Control`, `Program Modification`, `Data Modification`, `Monitoring`. | Modicon M580/M340 PACSec ve EIFE ağ modüllerine şifreli güvenlik profili dağıtımı. |
| **ABB** | System 800xA Aspect Directory | Windows Domain Kullanıcı ve Grupları | **Hiyerarşik / Alan Bazlı:** Plant Structure ve Unit/Area seviyesinde kumanda kısıtlaması. | Operatörün yalnızca atandığı proses ünitesindeki butonlara basabilmesi. |
| **Emerson** | DeltaV Security Administration | Windows AD & DeltaV Kullanıcıları | **Fonksiyonel Haklar:** `Can Operate`, `Can Tune`, `Can Configure`, `Can Download`. | 21 CFR Part 11 uyumlu elektronik imza ve setpoint değişiminde Çift Onay (*Four-Eyes*). |
| **OPC UA (IEC 62541-18)** | Adres Uzayı (AddressSpace) Rol Yetkileri | X.509 Sertifikası, Kullanıcı/Parola veya JWT | **Bitmask İzinleri:** Her NodeId için `Read`, `Write`, `Browse`, `Call`, `WriteRolePermissions`. | Kritik metot çağırma (`Call`) ve değişken yazma (`Write`) haklarının rol bazında kilitlenmesi. |

---

## 2. OPC UA Part 18 Rol İzinleri (Bitmask Tablosu)

OPC UA Part 18 standardında her nesne ve değişken (NodeId) için roller ikili bit maskesiyle yetkilendirilir:

| İzin Bitmask Değeri | İzin Adı | Açıklama |
|---|---|---|
| `0x0001` | `Browse` | İstemcinin adres uzayında ilgili düğümü görebilmesi ve listeleyebilmesi. |
| `0x0004` | `Read` | Düğümün mevcut canlı proses değerini okuyabilmesi. |
| `0x0008` | `Write` | Düğümün değerini değiştirebilmesi (Setpoint veya komut yazma). |
| `0x0020` | `Call` | Düğüm üzerindeki metotları çalıştırabilmesi (ör. `StartPump()`, `CalibrateSensor()`). |
| `0x0080` | `WriteRolePermissions` | İlgili düğümün güvenlik izinlerini değiştirebilme (Yalnızca Güvenlik Yöneticisi). |

---

## 3. Heterojen Tesisler İçin Ortak Rol Haritalama

Farklı marka PLC ve SCADA'ların bulunduğu tesislerde ortak kurumsal roller şöyle haritalanır:

| Kurumsal Rol | Rockwell FTSEC | Schneider CAE | ABB 800xA | OPC UA Part 18 |
|---|---|---|---|---|
| **Operator** | `Operators` (Tag Write) | `Operator` | `Operator` | `Browse + Read + Limited Write` |
| **Process Engineer** | `Engineers` (Online Edit) | `Programmer` | `Application Engineer` | `Browse + Read + Write + Call` |
| **Safety Engineer** | `Safety Engineers` | `Safety Expert` | `System Engineer` | `Full Permissions (Safety Node)` |
| **Auditor** | `Auditors` (Read-Only) | `Monitoring` | `Observer` | `Browse + Read` |

---

## 4. Hızlı Konfigürasyon Kontrol Listesi

- [ ] Rockwell projelerinde *Deny-over-Allow* çakışmaları gözden geçirildi.
- [ ] Schneider M580 PACSec modüllerine güncel güvenlik profilleri yüklendi.
- [ ] OPC UA sunucularında `Anonymous` erişim kapatıldı; X.509 sertifika tabanlı roller atandı.
- [ ] Emerson DeltaV üzerinde 21 CFR Part 11 elektronik imza politikaları aktif edildi.
