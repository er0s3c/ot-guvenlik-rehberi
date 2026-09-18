# OT güvenlik değerlendirmesi ve test planı

[Ana sayfa](../../README.md) · [Değerlendirme şablonu](../../templates/08-degerlendirme-ve-risk-kaydi.md) · [Konu haritası](../11-konu-haritasi.md)

Güvenlik değerlendirmesi, bir hizmetin hangi koşullarda bozulabileceğini ve mevcut kontrollerin hangi kanıtlarla desteklendiğini araştırır. Penetrasyon testi bunun belirli saldırı varsayımlarını sınayan, daha dar kapsamlı bir parçasıdır. Bir yapılandırma incelemesi de değerli değerlendirme üretir; istismar yapılmaması bulguyu geçersiz kılmaz. NIST SP 800-115 testlerin planlanması, bulguların analizi ve iyileştirmeyi birlikte ele alır; aşağıdaki OT iş akışı bu deponun özgün uyarlamasıdır. [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)

## 1. Değerlendirme türünü seçmek

| Tür | Yanıtlanan soru | Beklenen kanıt | Sınırı |
|---|---|---|---|
| Mimari değerlendirme | İstenmeyen bir güven geçişi var mı? | Akış matrisi, bölge sınırı, rol ve bağımlılık | Kuralın cihazda uygulandığını ispatlamaz |
| Yapılandırma incelemesi | Onaylı gereksinim mevcut ayarda karşılanıyor mu? | Tarihli, kapsamı bilinen yapılandırma kopyası | Çalışma anındaki davranış farklı olabilir |
| Zafiyet değerlendirmesi | Duyurudaki ürün/işlev gerçekten bu varlıkta mı? | Model, sürüm, üretici duyurusu, erişim koşulu | CVE eşleşmesi başarılı saldırı demek değildir |
| Penetrasyon testi | Açıkça izin verilen saldırı varsayımı gerçekleşebilir mi? | Önceden kararlaştırılmış test ve gözlem | Tesisin bütün risklerini kapsamaz |
| Red team / emülasyon | Belirlenmiş bir hedefe karşı ekipler ve kontroller nasıl yanıt verir? | Senaryo, görünürlük, karar ve zaman çizelgesi | ATT&CK işaretlemek veya gizli test yapmak tek başına yeterli değildir |
| Masa başı tatbikatı | Ekip mevcut kanıtla hangi kararı verir? | Rol, karar gerekçesi ve dönüş kapısı | Teknik kontrolün çalıştığını doğrulamaz |

IT testindeki bir yeniden başlatmanın OT'deki karşılığı operatör görünürlüğünün, haberleşmenin veya bir fiziksel işlevin kaybı olabilir. Kimlik doğrulamalı bir sorgu da işlem yükü yaratabilir. Bu yüzden "read-only" veya "authenticated" etiketleri etki değerlendirmesinin yerine geçmez. OT'nin performans, güvenilirlik ve emniyet bağlamı için [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final).

## 2. On beş aşamalı çalışma

Bu sıra özgün eğitim yöntemidir. Belge alıştırmasında bütün girdiler kurgusaldır; gerçek varlığa işlem gönderilmez. Bir önceki aşamanın kanıtı eksikse sonraki aşamaya "doğrulandı" etiketi verilmez.

| Aşama | Yapılacak inceleme | Çıktı ve kabul koşulu |
|---|---|---|
| 1. Yetki | Hizmet sahibi, kapsam ve değerlendiren taraf | İmzalı kapsam; dışarıda bırakılan varlıklar belli |
| 2. Çalışma kuralları (RoE) | Yöntem, pencere, sorumlu, durdurma ve geri dönüş | Her yöntemin ayrı izni; acil irtibat ve tek durdurma yetkilisi |
| 3. Envanter | Bakım listesi, proje kaydı ve varlık sahipliği | Varlık kimliği, işlev, sürüm ve bilginin kaynağı |
| 4. Pasif inceleme | Yetkili mevcut kayıtların kapsamı ve zaman kalitesi | Görülenler ile gözlem dışı kalanların ayrılması |
| 5. Mimari | Kontrol, telemetri, yönetim ve destek akışları | Her sınırı geçen akışın sahibi ve amacı |
| 6. Protokol tanıma | Belge, sürüm ve eldeki trafik kaydı | Porttan çıkarım ile doğrulanmış protokolün ayrılması |
| 7. Zafiyet | Üretici koşulları ve işletme etkisi | Etkilenen/etkilenmeyen/belirsiz kararı ve kanıt |
| 8. Yapılandırma | Onaylı gereksinim ve mevcut ayar | Sapmanın varlık, sürüm ve kanıtla kaydı |
| 9. Kimlik doğrulama | Hesap yaşam döngüsü, kapı ve hedef kimliği | Sahipsiz/geçici/paylaşılan hesap bulguları |
| 10. Yetkilendirme | Rol × sistem × işlem matrisi | Gözlem ve değişiklik yetkisinin ayrı değerlendirilmesi |
| 11. Segmentasyon | Akış matrisi, kural sırası, alternatif yollar | İzin ve ret için beklenen davranış; henüz denenmemiş olanların işareti |
| 12. Uzak erişim | Kişi, hedef, süre, onay ve oturum | İptalin açık oturuma etkisi dahil uçtan uca kayıt |
| 13. İzleme | Kaynak → toplayıcı → depolama zinciri | Eksik alan, gecikme ve kayıp için sağlık kanıtı |
| 14. Algılama | Normal bakım ve inceleme gerektiren sentetik olay | Pozitif/negatif örnekler ve yanlış pozitif gerekçesi |
| 15. Raporlama | Bulgu, risk, sahip, işlem ve yeniden değerlendirme | Yönetici özeti ile teknik ekin aynı bulgu kimliklerini kullanması |

Fabrika örneğinde PLC/HMI/SCADA/historian mühendislik işlevleri; firewall ve switch geçişleri; kimlik, zaman ve yedekleme destek hizmetleri birlikte kapsanır. Yalnızca kontrolör listesini incelemek değerlendirme sınırını eksik tarif eder.

## 3. Tarama ve keşif için karar tablosu

| Yöntem | Avantaj | Kör nokta / maliyet | Ön koşul |
|---|---|---|---|
| Belge ve sahip görüşmesi | Cihaza trafik üretmez, sessiz varlıkları kapsayabilir | Eski çizim ve yanlış sürüm bilgisi | Kaynak ve tarih, ikinci doğrulama |
| Mevcut pasif kayıt | İletişim ortakları ve kullanılan işlevler | Sessiz cihaz, şifreli içerik, gözlem dışı ağ; depolama/analist zamanı | Kayıt alma yetkisi ve gözlem noktası bilgisi |
| Üreticinin desteklediği durum bilgisi | Ürün kimliği ve ayar bağlamı | Kimlikli olması etkisiz olduğu anlamına gelmez | Üretici desteği, işletme onayı ve sınırlı yöntem |
| Aktif tarama | Belirli hizmet varsayımlarını sınayabilir | Trafik yükü, hassas yığınlar, yanıltıcı tanıma | Temsil eden test ortamı, varlık bazlı yöntem onayı ve durdurma ölçütü |

Bu depoda aktif tarama komutları yer almaz. Bir tarayıcının "safe" profili tesis için güvence kabul edilmez. Canlı sistemde kaynak tüketimi, bağlantı sayısı, süreç alarmı veya operatör görünürlüğü değişirse kimin hangi kararla testi durduracağı kapsam belgesinde önceden yazılır. Hız sınırı için evrensel paket/saniye değeri verilmez.

## 4. CVSS'den işletme kararına

CVSS bir zafiyetin teknik ciddiyetini ifade eder. V4.0, çevresel ve tehdit metriklerinin yanı sıra Safety gibi tamamlayıcı metrikler içerir; tamamlayıcı metrikler nihai CVSS sayısını değiştirmez. Dolayısıyla "CVSS emniyeti hiç ele almaz" da "yüksek CVSS otomatik ilk yama demektir" de yeterli açıklama değildir. [FIRST CVSS v4.0 belirtimi](https://www.first.org/cvss/v4.0/specification-document)

Özgün karar kaydı şu girdileri ayrı tutar:

1. Ürün, sürüm, işlev ve duyuru eşleşmesi.
2. Saldırının ön koşulu; ilgili yolu hangi kontrol sınırlar?
3. İşlevin hizmet/emniyet etkisi ve alternatif işletme imkânı.
4. İstismar kanıtının kaynağı ve tarihi; yokluğu güvence değildir.
5. Değişikliğin uyumluluk, duruş ve geri alma etkisi.
6. Yapılacak işlem, sorumlu, kabul tarihi ve o zamana kadarki telafi kontrolü.

Kurgusal örnek: yönetim ağına kapalı test sunucusundaki yüksek teknik skor ile uzak bakımdan erişilen kritik HMI'daki daha düşük skor birlikte değerlendirilir. İkinci varlığın önce ele alınması için yolun varlığı ve etkisi belgelenir; yalnız varlık adına bakılarak otomatik öncelik verilmez.

SBOM (yazılım bileşen envanteri), ürünün içerdiği bileşenleri anlamaya yardımcı girdidir. Bileşen adının eşleşmesi, etkilenen kodun çalıştırılabilir olduğunu tek başına göstermez. Tedarikçiden alınan listenin ürün/sürüm kapsamı, tarihi ve zafiyet açıklaması envanter kaydına bağlanır. Bu uygulama önerisi [değişiklik yönetimindeki](../04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) tedarik sorularını ayrıntılandırır.

## 5. NIST ve IEC 62443'ü kanıta bağlamak

NIST SP 800-82, OT güvenlik rehberidir; IEC 62443 birden fazla parçadan oluşan endüstriyel otomasyon güvenliği standart ailesidir. Seri, sistem risk değerlendirmesi ve sistem gereksinimleriyle bileşen/geliştirme kapsamlarını ayırır. Ayrıntılı künye ve kapsamlar [standartlar bölümündedir](../05-standartlar-ve-turkiye.md). Aşağıdaki tablo resmî uygunluk eşlemesi değildir.

| Değerlendirme konusu | NIST rehberini okuma amacı | IEC 62443 bağlamı | Bu depoda istenecek kanıt |
|---|---|---|---|
| Kapsam ve işlev | OT bağımlılıklarını tanımak | Sistem sınırı ve risk değerlendirmesi | Envanter, bağımlılık ve sahip |
| Mimari | Segmentasyon ve kontrollü iletişim | Bölgeler ve geçişler | Gerekçeli zone/conduit ve akış matrisi |
| Kimlik ve erişim | Gereken işi yetkili kişiyle sınırlamak | Sistem güvenlik gereksinimleri | Rol matrisi, hedef yetkisi, iptal kaydı |
| Ürün seçimi | Ürün ve işletme sınırlamalarını değerlendirmek | Bileşen gereksinimleri, güvenli geliştirme | Model/sürüm/lisans ve kabul planı |
| Yaşam döngüsü | Değişiklik, izleme ve kurtarma | İşletmeci ve hizmet sağlayıcı süreçleri | Değişiklik, bulgu ve geri yükleme kayıtları |

Security Level (SL) tek bir tesis pazarlama puanı olarak kullanılmaz. Hedeflenen (SL-T), tasarımın/kontrolün sağlayabildiği kabiliyet (SL-C) ve elde edilen durum (SL-A) ayrımı için seçilen IEC parçası, kapsam ve değerlendirme kanıtı kaydedilir. Lisanslı gereksinimler doğrulanmadan bir kontrol listesinden "SL2 uyumlu" sonucu çıkarılmaz. SIL ile SL ayrı kavramlardır; [mevcut açıklamayı](../05-standartlar-ve-turkiye.md) kullanın.

## 6. Belge alıştırması

Kurgusal bir tesiste tedarikçi erişiminin süresi dolmuş, kapı kaydı başarılı çıkış gösteriyor, hedef istasyonun oturum kaydı ise eksik. Yedek listesinde son HMI projesi var, geri yükleme kanıtı yok.

- **THEORY:** Kimlik doğrulama, yetki iptali ve hedef oturumunun farkını açıklayın.
- **LAB:** [Değerlendirme şablonunda](../../templates/08-degerlendirme-ve-risk-kaydi.md) iki bulgu, bir risk ve üç açık soru oluşturun.
- **TEST:** "Çıkış kaydı var" sonucunun hangi iddiayı doğrulamadığını yazın; ek kanıtı belirtin.
- **DEFENSE:** Geçici erişim sınırı ve geri yükleme kabul kapısı önerin.
- **REPORT:** Beş cümlelik yönetici özeti; karar sahibi ve kalan belirsizlikleri ekleyin.

Kabul: yetkisiz işlem yaşandığı kanıtsız ilan edilmemiş; kapı ile hedef ayrılmış; kurtarma testi yapılmış gibi gösterilmemiş; her öneri bir bulguya ve doğrulama yöntemine bağlanmış olmalıdır. Bu çalışma CV'de "kurgusal OT değerlendirme dosyası" diye gösterilebilir; tesis testi olarak sunulmaz.

## Kaynak ve kapsam

- NIST, SP 800-115, Eylül 2008, [yayın kaydı](https://csrc.nist.gov/pubs/sp/800/115/final); test planlama ve bulgu analizi amacı.
- NIST, SP 800-82 Rev. 3, Eylül 2023, [yayın kaydı](https://csrc.nist.gov/pubs/sp/800/82/r3/final); OT bağlamı.
- FIRST, CVSS v4.0, [belirtim](https://www.first.org/cvss/v4.0/specification-document); teknik ciddiyet, metrik grupları ve tamamlayıcı Safety alanı.
- IEC seri kaynakları [standartlar bölümünde](../05-standartlar-ve-turkiye.md); ücretli tam metin veya normatif madde aktarılmamıştır.

Yeni kaynak erişimi: 16.09.2026. Aşamalar, karar tablosu ve alıştırma özgün eğitim sentezidir; gerçek test sonucu veya uygunluk beyanı değildir.
