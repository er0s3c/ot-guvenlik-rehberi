# Playbook 04: Olay Sonrası Güvenli Hizmete Dönüş ve Devreye Alma

[Playbook Dizini](README.md) · [Olay Müdahalesi ve Kurtarma](../05-olay-mudahalesi-ve-kurtarma.md) · [Kurtarma Doğrulama Laboratuvarı](../../../labs/04-kurtarma-dogrulama.md)

Bu operasyonel kılavuz; bir siber güvenlik olayının kontrol altına alınmasının ardından, endüstriyel tesisin veya kritik altyapının yeniden enerjilendirilmesi, vanaların açılması ve tam üretime geçilmesi sürecinde uygulanacak **5 Aşamalı Kabul Kapısı (5-Gate Re-commissioning)** prosedürünü tanımlar.

---

## 1. 5 Aşamalı Kabul Kapısı Mimarisi

Hiçbir tesis tek bir ekibin onayıyla veya sadece antivirüs temizleme raporuyla devreye alınamaz.

```mermaid
flowchart LR
    G1["Kapı 1: Siber & Yazılım Doğrulama"] --> G2["Kapı 2: Sinyal & I/O Eşleme"]
    G2 --> G3["Kapı 3: Mekanik & Emniyet Testi"]
    G3 --> G4["Kapı 4: Proses & Kalite Doğrulama"]
    G4 --> G5["Kapı 5: Islak İmzalı Vardiya Kabulü"]
```

---

## 2. Kabul Kapıları ve Gerekli Kanıtlar

### 🚪 Kapı 1: Siber Güvenlik ve Yazılım Bütünlüğü
- **Sorumlu:** OT SOC Analisti ve Ağ Güvenliği Uzmanı
- **Gerekli Kanıtlar:**
  - Olayın gerçekleştiği giriş vektörünün (zafiyet, açık port, sızdırılmış kimlik) tamamen kapatıldığının doğrulanması.
  - PLC/RTU/HMI/SCADA cihazlarına yüklenen firmware ve proje dosyalarının SHA-256 hash değerlerinin orijinal temel sürümlerle (baseline) %100 uyuşması.
  - Ağ segmentasyon kurallarının ve erişim izinlerinin yeniden tesis edilmesi.

### 🚪 Kapı 2: Saha Sinyal ve I/O Doğrulaması (Loop Check)
- **Sorumlu:** Otomasyon Mühendisi ve Enstrüman Teknisyeni
- **Gerekli Kanıtlar:**
  - PLC analog ve dijital girişlerinin (4-20mA, kuru kontak) saha fiziksel durumuyla birebir örtüştüğünün yerinde ölçümle (multimetre/kalibratör) teyit edilmesi.
  - SCADA ekranındaki göstergelerin ve renklerin sahadaki aktüatör konumlarıyla senkronize olduğunun doğrulanması.
  - Hiçbir PLC registerında `FORCE` veya `BYPASS` bayrağının kalmadığının tespiti.

### 🚪 Kapı 3: Mekanik ve Emniyet Sistemleri Testi (Cold Commissioning)
- **Sorumlu:** Mekanik Bakım Mühendisi ve İş Güvenliği Uzmanı
- **Gerekli Kanıtlar:**
  - Mekanik basınç emniyet ventilleri (PSV), patlama diskleri ve yangın damperlerinin fiziksel muayenesi.
  - Acil Duruş (ESD) butonlarının ve hardwired çekiş kilitlerinin (Interlock) enerjisiz ortamda fonksiyon testi.
  - Pompa/motor yağlama, soğutma ve ters dönüş mandallarının kontrolü.

### 🚪 Kapı 4: Proses ve Kalite Doğrulaması (Hot Commissioning)
- **Sorumlu:** Proses Kimyageri / Elektrik Şebeke İşletme Mühendisi
- **Gerekli Kanıtlar:**
  - Düşük debi/yükte kademeli başlatma testleri.
  - Su kalitesi (pH, klor, bulanıklık), şebeke senkronizasyon faz açısı veya reaktör sıcaklık gradyanlarının bağımsız laboratuvar/ölçümle teyidi.
  - 2 saatlik kararlı çalışma gözlemi.

### 🚪 Kapı 5: Islak İmzalı Nihai Devir ve Hizmete Dönüş
- **Sorumlu:** Tesis Müdürü / Vardiya Amiri
- **Gerekli Kanıtlar:**
  - Önceki 4 kapının yazılı ve imzalı tutanaklarının toplanması.
  - Merkezi yönetim sistemine resmî "Hizmete Dönüş" bildiriminin yapılması.

---

## 3. Hizmete Dönüş İmza Tutanağı Şablonu

| Kabul Kapısı | Doğrulama Durumu | Onaylayan Mühendis | Unvan / Sicil No | Tarih & Saat | İmza |
|---|---|---|---|---|---|
| **Kapı 1: Siber & Yazılım** | `[ ] UYGUN` | | OT Siber Güvenlik Uzmanı | | |
| **Kapı 2: Sinyal & I/O** | `[ ] UYGUN` | | Otomasyon Mühendisi | | |
| **Kapı 3: Mekanik & Emniyet** | `[ ] UYGUN` | | Bakım Mühendisi | | |
| **Kapı 4: Proses & Kalite** | `[ ] UYGUN` | | Proses / Kalite Sorumlusu | | |
| **Kapı 5: Nihai Kabul** | `[ ] ONAYLANDI` | | Tesis Müdürü / Vardiya Amiri | | |
