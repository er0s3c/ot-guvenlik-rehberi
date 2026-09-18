# Güvenli PLC Kodlama Denetim Matrisi (Top 20 Secure PLC Coding)

[Şablonlar Ana Sayfası](README.md) · [Güvenli PLC Programlama](../docs/08-mimari-ve-erisim/04-guvenli-plc-programlama-top20.md) · [PLC ve HMI Sıkılaştırma](../docs/08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md) · [RBAC ve UMC Tasarımı](12-ot-rbac-ve-umc-tasarim-sablonu.md)

Bu mühendislik denetim şablonu; sahada çalışan veya devreye alınacak olan PLC/PAC/DCS kontrol lojiklerinin **Top 20 Secure PLC Coding Practices** kriterlerine göre incelenmesi, kod seviyesindeki zafiyetlerin tespit edilmesi, puanlanması ve iyileştirme aksiyonlarının belirlenmesi için hazırlanmıştır.

---

## 1. Denetlenen Kontrolör ve Varlık Bilgileri

| Denetim Parametresi | Varlık Değeri / Açıklama |
|---|---|
| **Kontrolör / Varlık Adı (Tag)** | Örn: `PLC-PUMP-01` (Terfi İstasyonu Ana Kontrolörü) |
| **Üretici / Model / Firmware** | Örn: Siemens S7-1516F-3 PN/DP (FW V3.1.2) / Rockwell ControlLogix 5580 |
| **Programlama Yazılımı & Dili** | TIA Portal V20 / Studio 5000 (SCL / Ladder / FBD) |
| **Bulunduğu Bölge (Purdue / Zone)** | Zone 1 - Saha Kontrol Hücresi (Level 1) |
| **Kritiklik Derecesi** | `[ ]` Kritik (Emniyet/Çevre) `[ ]` Yüksek `[ ]` Orta `[ ]` Standart |
| **Denetim Tarihi ve Denetçi** | |

---

## 2. Top 20 Güvenli PLC Kodlama Denetim Matrisi

| No | Pratik Adı | Denetim Sorusu | Uygunluk Durumu | Tespit Edilen Açık & Açıklama | Düzeltici Aksiyon & Sorumlu |
|---|---|---|---|---|---|
| **P1** | **Kodu Modülerleştirme** | Kod, her biri tekil işlev gören bağımsız test edilebilir Function Block (FB) yapılarına ayrılmış mı? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P2** | **Çalışma Modu Takibi** | PLC'nin donanımsal anahtar konumu (RUN/STOP) takip edilip RUN modu dışına çıkıldığında alarm üretiliyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P3** | **Lojiği PLC'de Tutma** | Kritik hesaplama, toplam debi hesabı ve emniyet kilitleri HMI script'i yerine doğrudan PLC'de mi çalışıyor? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P4** | **Sistem Hata Bayrakları** | Bölme sıfır (Divide-by-zero) ve matematik taşma bayrakları izlenip alarm sayacına bağlanmış mı? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P5** | **Kriptografik Bütünlük** | PLC program derleme imzası (Safety CRC / Code Checksum) kaydedilmiş ve dönemsel doğrulanıyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P6** | **Zamanlayıcı Doğrulama** | Operatör tarafından girilen tüm Timer ve Counter süreleri mantıksal minimum/maksimum sınırlarla korunuyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P7** | **Birbirini Dışlayan I/O** | Bir vananın aynı anda hem AÇ hem KAPA sinyali üretmesi veya çelişkili limit switch durumu engelleniyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P8** | **HMI Girdi Doğrulama** | HMI'dan girilen tüm proses set değerleri doğrudan PLC lojiği içinde Min/Max aralık kontrolünden geçiyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P9** | **Dizi / İşaretçi Sınırları** | Dizilerde indeks aşımını (Fence-post / Array out-of-bounds) engelleyecek sınır kontrolleri yapılmış mı? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P10** | **Veri Bloğu Ayrımı** | HMI'ın yazabildiği değişkenler ile PLC dahili proses parametreleri ayrı Data Block'larda (DB) mı tutuluyor? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P11** | **Proses Mantıksallığı** | Fiziksel olarak imkansız sensör değişim hızları ($\Delta \text{Value}/\Delta t$) mantıksallık filtresinden geçiyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P12** | **Güvenli Başlatma (OB100)** | PLC enerjilendiğinde veya yeniden başladığında tüm çıkışlar güvenli varsayılan duruma (Safe-State) çekiliyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P13** | **Gereksiz Portları Kapatma** | Web sunucu, SNMP, Telnet, FTP gibi kullanılmayan dahili protokol ve portlar CPU ayarlarından kapatılmış mı? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P14** | **Üçüncü Taraf Kısıtı** | ERP/MES veya dış entegrasyonlar yalnızca tanımlı, salt okunur DB alanlarına mı erişebiliyor? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P15** | **Çevrim Süresi İzleme** | PLC tarama süresi (Cycle time) izlenip aşırı artış veya sapmalarda anomali alarmı üretiliyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P16** | **Uptime ve Reset Takibi** | PLC'nin çalışma süresi ve beklenmeyen CPU yeniden başlama (restart) olayları loglanıyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P17** | **Donanımsal Arıza Kaydı** | Kritik I/O kart kopmaları ve emniyet açma (Trip) nedenleri silinmez (Retentive) hafızada saklanıyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P18** | **Hafıza Kullanım İzleme** | PLC yükleme ve çalışma hafızası doluluk oranları SCADA üzerinde trendleniyor mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P19** | **Alarm Doğrulama Mantığı** | Kritik bir alarm tekil sensör sinyali yerine proses teyidi ile birlikte mi tetikleniyor? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |
| **P20** | **Standart İsimlendirme** | Tüm tag, blok ve değişkenler standart IEC adlandırma kuralına ve güncel mühendislik dokümanına uygun mu? | `[ ]` Evet `[ ]` Kısmen `[ ]` Hayır | | |

---

## 3. Güvenli Kodlama Uyum Skoru ve Risk Değerlendirmesi

$$\text{Uyum Skoru (\%)} = \left( \frac{\text{Evet Sayısı} \times 1.0 + \text{Kısmen Sayısı} \times 0.5}{20 - \text{Kapsam Dışı Sayısı}} \right) \times 100$$

```text
Toplam Kriter Sayısı      : 20
Evet (Tam Uyumlu)         : [  ]
Kısmen Uyumlu             : [  ]
Hayır (Uyumsuz)           : [  ]
Hesaplanan Uyum Skoru     : [    %]

Risk Değerlendirmesi      : [ ] Kritik Risk (<%50)  [ ] Yüksek Risk (%50-70)  [ ] Kabul Edilebilir (%70-90)  [ ] İleri Güvenli (>%90)
```

---

## 4. İyileştirme Aksiyon Planı ve Takip

| Öncelik | Kural No | Yapılacak Mühendislik Değişikliği | Sorumlu Mühendis | Hedef Tarih | Tamamlanma Durumu |
|---|---|---|---|---|---|
| **Yüksek** | P8 | `FB_HMI_Input_Validator` bloğu tüm analog setpoint'lere bağlanacak. | | | `[ ]` |
| **Yüksek** | P7 | Vana aç/kapa komutlarına `FB_Paired_Signal_Monitor` eklenecek. | | | `[ ]` |
| **Orta** | P12 | OB100 içine tüm dijital çıkışları sıfırlayan lojik yazılacak. | | | `[ ]` |
| **Orta** | P15 | Cycle time sapma eşiği 40 ms olarak ayarlanacak. | | | `[ ]` |

---

## 5. Onay ve İmza

| Rol | İsim - Soyisim | Unvan | İmza | Tarih |
|---|---|---|---|---|
| **Denetimi Yapan (OT Mühendisi)** | | Otomasyon / Kontrol Mühendisi | | |
| **Güvenlik Gözden Geçiren** | | OT Siber Güvenlik Uzmanı | | |
| **Tesis / Üretim Müdürü** | | Tesis İşletme Müdürü | | |
