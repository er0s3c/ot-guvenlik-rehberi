# Tehdit modelleme yöntemleri ve OT zararlı yazılım incelemeleri

[Saldırgan bakışı](../03-tehdit-modelleme/01-saldirgan-bakis-acisi.md) · [Teknik eşlemeleri](../03-tehdit-modelleme/02-mitre-attack-ics.md) · [Vaka kaynakları](../03-tehdit-modelleme/03-gercek-vakalar.md)

Tehdit modeli bir saldırı talimatı değildir. Bir hizmeti, güven varsayımını, o varsayımın bozulma koşulunu ve savunmanın görebileceği kanıtı birlikte tarif eder. Burada kullanılan PLC-01 ve bütün tasarım örnekleri kurgusaldır.

## 1. Dört yöntemin farklı soruları

| Yöntem | Sorduğu soru | Üreteceği çıktı | Bu bölümdeki kullanım |
|---|---|---|---|
| STRIDE | Kimlik, veri, izlenebilirlik, gizlilik, hizmet veya yetkide ne bozulabilir? | Veri akışı başına tehdit hipotezi | PLC mühendislik yolunu altı açıdan incelemek |
| ATT&CK for ICS | Gözlenen davranışı hangi ortak terimle anlatıyoruz? | Kanıta bağlı taktik/teknik eşlemesi | Proje aktarımı ile mantık değişikliğini ayırmak |
| Attack tree | Bir olumsuz sonucun alternatif veya birlikte gereken koşulları neler? | AND/OR koşullarından oluşan ağaç | Kontrol bütünlüğü için gerekli güven varsayımları |
| Cyber Kill Chain | İncelenen olayın aşamaları nerede gözlenebilir? | Aşama–gözlem–kontrol anlatımı | Geçmiş olayları karşılaştırmak |

STRIDE adları [Microsoft'un modelinden](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats), saldırı ağacındaki AND/OR düşüncesi [Schneier'in açıklamasından](https://www.schneier.com/academic/archives/1999/12/attack_trees.html), Cyber Kill Chain'in yedi aşamalı çerçevesi [Lockheed Martin'den](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) gelir. Tablodaki kullanım ve aşağıdaki OT örnekleri özgün sentezdir. Yöntemlerden hiçbiri kendi başına olasılık veya uygunluk puanı vermez.

## 2. PLC-01 için STRIDE

Önce kapsam: PLC-01 bir kurgusal pompa döngüsünü yönetir; HMI-01 durum gösterir, ENG-01 yalnız onaylı bakımda proje yönetir. Bağımsız emniyet işlevinin ayrıntısı bu örnekte modellenmemiştir; mevcut olduğu varsayılarak siber etki azaltılmaz.

| Sınıf | Hedef / ön koşul / sınır | Olası etki | Gözlenebilir belirti | Savunma ve kanıt |
|---|---|---|---|---|
| Spoofing — kimliğe bürünme | Yetkili kaynak gibi görünmek; kaynak kimliğinin yeterince doğrulanmaması; mühendislik sınırı | Yetkisiz bakım oturumu | Kişi, cihaz ve iş emri uyumsuzluğu | Kişi/cihaz yetkisi, hedef kaydı, süreli onay |
| Tampering — değiştirme | Projeyi değiştirmek; yazma yetkisinin erişilmiş olması; proje kabul sınırı | Kontrol bütünlüğü kaybı | Onaylı proje ile fark | Sürüm kaydı, ikinci kişi incelemesi, kabul kanıtı |
| Repudiation — inkâr | İşlemi izsiz bırakmak; yetersiz kayıt; kişi–işlem bağı | Sorumluluk ve olay sırası belirsizliği | Eksik oturum/kayıt aralığı | Kişisel hesap, zaman kalitesi, kayıt sağlığı |
| Information disclosure — bilgi açığa çıkması | Projeyi okumak; fazla okuma yetkisi; mühendislik veri sınırı | Tasarım ve süreç bilgisinin ifşası | Beklenmeyen proje dışa aktarımı | En az yetki, aktarım onayı ve denetim |
| Denial of service — hizmet kaybı | İletişim/kaynak kaybı; korumasız ortak bağımlılık; kontrol yolu | Kontrol veya görünürlük kesintisi | Haberleşme/kalite alarmları | Bağımlılık analizi, kapasite, uygun yedeklilik |
| Elevation of privilege — yetki yükseltme | Gözlem yetkisiyle değişiklik yapmak; rol ayrımı eksikliği; yetki sınırı | Onaysız ayar değişimi | Rolün beklemediği işlem | Rol × işlem matrisi, hedefte olumsuz kabul testi |

Bu tablo davranışın nasıl gerçekleştirileceğini anlatmaz; bir kontrolün hangi kanıtla değerlendirilmesi gerektiğini gösterir. STRIDE sınıfı ile ATT&CK tekniği birebir eşdeğer değildir.

## 3. Basit koşul ağacı

```text
Amaç: PLC-01 üzerindeki onaylı kontrol bütünlüğünün kaybı
  OR
  ├─ Mühendislik yolunda yetkisiz değişiklik
  │    AND: hedefe erişim var + değişiklik yetkisi var + kabul denetimi yetersiz
  ├─ Güvenilmeyen proje kopyasından geri dönüş
  │    AND: kopya seçiliyor + güvenilir sürüm kanıtı yok
  └─ Yetkili değişikliğin yanlış hedefte uygulanması
       AND: hedef eşlemesi hatalı + bağımsız inceleme eksik
```

Kök sonuç her zaman saldırı demek değildir; son dal insan hatasıyla da oluşabilir. Bir AND dalında bir ön koşulu doğrulanmış kontrolle kesmek o dalı sınırlar; diğer OR dalları ayrıca incelenir. Ağaçta görünmeyen tehditlerin bulunmadığı sonucu çıkarılmaz.

## 4. ICS taktiklerinin kapsamı

16.09.2026 tarihinde MITRE'nin ICS listesinde aşağıdaki 12 taktik görülüyor. İsimler sürümle değişebileceğinden her proje kaynak tarihini saklar. Bunlar zorunlu kronolojik adımlar değildir. [Resmî ICS taktikleri](https://attack.mitre.org/tactics/ics/)

| Kimlik | Resmî ad | Özgün inceleme sorusu |
|---|---|---|
| TA0108 | Initial Access | Ortama girişin kanıtı nerede? |
| TA0104 | Execution | Yetkisiz çalıştırma gözlendi mi? |
| TA0110 | Persistence | Yetki kaldırıldıktan sonra kalıcılık göstergesi var mı? |
| TA0111 | Privilege Escalation | Başlangıç yetkisinden daha güçlü işlem doğrulandı mı? |
| TA0103 | Evasion | Görünürlük veya savunma kaybı açıklanabiliyor mu? |
| TA0102 | Discovery | Ortam bilgisinin toplanmasına ilişkin kanıt ne? |
| TA0109 | Lateral Movement | Hangi güven sınırı geçildi? |
| TA0100 | Collection | Hangi veri toplandı ve nasıl anlaşılıyor? |
| TA0101 | Command and Control | Yetkisiz yönetim iletişimi nasıl ayrılıyor? |
| TA0107 | Inhibit Response Function | Koruma veya operatör tepkisi etkilenmiş mi? |
| TA0106 | Impair Process Control | Kontrol işlevinin bütünlüğü etkilenmiş mi? |
| TA0105 | Impact | Gözlenen hizmet/fiziksel sonuç ne? |

"Recon → Initial Access → Discovery → Lateral Movement → Collection → Impact" bir senaryo özeti olarak kullanılabilir; ICS'nin tüm taktik listesi değildir. Reconnaissance, bu ICS listesinde ayrı taktik olarak yer almaz. OT'deki Windows sunucusu için Enterprise eşlemeleri de gerekebilir; alan adı açık yazılır.

Red team belgesinde hedef, başlangıçta varsayılan erişim, izinli kanıt üretimi, gözlem noktaları, durdurma koşulu ve işletme kararları birlikte tanımlanır. Doğru eşleme için saldırıyı gerçekleştirmek gerekmez: örneğin sentetik proje aktarımı kaydı, kayıt sağlığı ve analist kararını değerlendirmek için kullanılabilir. Bu, gerçek cihazdaki önleyici kontrolün sınandığı anlamına gelmez.

## 5. Beş zararlı yazılım örneği

Malware adı ile olayın bütün saldırı zinciri aynı şey değildir. Özellikle ilk erişim, kullanılan araçlar ve fiziksel sonuçlar yalnız ilgili araştırmanın doğruladığı kapsamda yazılır.

| Örnek | Hedef / teknik bağlam | İlk erişim ve protokol sınırı | Kaynak |
|---|---|---|---|
| Stuxnet | Windows mühendislik ortamı ve Siemens kontrol mantığı; proje/program bütünlüğü | Yayılma ve kontrol mantığı aşamaları ayrılır; tek bir protokole veya tek giriş yoluna indirgenmez | [MITRE S0603](https://attack.mitre.org/software/S0603/) davranış kaydı |
| BlackEnergy | Windows üzerinde modüler kötü amaçlı yazılım; Ukrayna 2015 olay bağlamıyla ilişkili | Kampanya erişimi ve sonraki işletme eylemleri ayrı incelenir; BlackEnergy tek başına PLC protokol istismarı diye tanımlanmaz | [MITRE S0089](https://attack.mitre.org/software/S0089/) ve [vaka bölümü](../03-tehdit-modelleme/03-gercek-vakalar.md) |
| Industroyer | Elektrik kontrol haberleşmesi; IEC 101/104, IEC 61850 ve OPC DA bileşenleri | Endüstriyel işlevlerin kötüye kullanımı, ilk girişin kendisini açıklamaz | [MITRE S0604](https://attack.mitre.org/software/S0604/) |
| Triton | Triconex emniyet kontrolörleri ve TriStation bağlamı | Emniyet sistemine erişim ile ilk tesis erişimi ayrılır; ilk giriş bilinmiyorsa açık kalır | [MITRE S1009](https://attack.mitre.org/software/S1009/) ve [Mandiant olay incelemesi](https://cloud.google.com/blog/topics/threat-intelligence/attackers-deploy-new-ics-attack-framework-triton) |
| PIPEDREAM | Modüler ICS araç takımı; Schneider/OMRON kontrolörleri ve OPC UA dahil farklı hedefler | 2022 ortak bildirim OT ağına ilk erişimi ön koşul kabul eder; açıklanan kabiliyet gerçekleşmiş saha etkisi değildir | [Dragos araştırma bağlamı](https://www.dragos.com/blog/potential-impact-of-pipedream-malware-module-mousehole), [DOE/CISA/NSA/FBI AA22-103A](https://media.defense.gov/2022/Apr/13/2002976115/-1/-1/0/JOINT_CSA_APT_CYBER_TOOLS_TARGETING_ICS_SCADA_20220413.PDF) |

Aşağıdaki savunma soruları kaynaklardaki yazılımların birebir imzası değildir; aynı davranış sınıfına yönelik özgün eğitim önerileridir.

| Örnek | Etkiyi okurken sınır | Algılama odağı | Savunma odağı |
|---|---|---|---|
| Stuxnet | Mantık değişikliğinden fiziksel sonuca giden kanıtı ayrı göster | Mühendislik iş istasyonu, proje farkı ve bağımsız süreç gözlemi | Bakım cihazı kabulü, proje bütünlüğü, yetki ve sürüm yönetimi |
| BlackEnergy | Yazılım, uzaktan işletme eylemi ve hizmet kesintisini aynı iddia sayma | Kimlik/uzak erişim, Windows ve operatör zaman çizelgesi | IT–OT sınırı, süreli erişim, geri yükleme hazırlığı |
| Industroyer | Tanıdık protokolün varlığı işlemin yetkili olduğunu göstermez | Kaynak–hedef–işlev, kontrol isteği ve cihaz yanıtı | İzinli kontrol kaynağı, bölge sınırı ve işletme teyidi |
| Triton | Olası fiziksel zarar ile raporlanan duruşu ayır | Emniyet mühendisliği erişimi, proje farkı ve teşhis olayları | Emniyet sistemi yaşam döngüsü, ayrı yetki ve bağımsız kabul |
| PIPEDREAM | Araç kabiliyeti ile sahada gözlenen olay aynı değildir | Mühendislik kaynağı, yönetim oturumu ve OPC UA güven ilişkisi | Desteklenen güvenli yapılandırma, açık güven listesi ve izlenebilir erişim |

## 6. Belge alıştırması

**THEORY:** Aynı PLC tehdidini STRIDE sınıfı ve ATT&CK tekniğiyle yazın; farkını açıklayın. **LAB:** Üç dallı ağaca bir kontrol ve kanıt kimliği ekleyin. **TEST:** "Proje aktarıldı" kaydının niçin "zararlı mantık çalıştı" sonucunu tek başına vermediğini gösterin. **DEFENSE:** Bir önleyici, bir algılayıcı ve bir kurtarıcı kontrol seçin. **REPORT:** Bir malware örneği için doğrulanmış olgu/belirsizlik/savunma dersi olarak üç ayrı paragraf yazın.

Kabul: her tehditte hedef, ön koşul, güven sınırı, etki, belirti ve kontrol bulunur; kaynakta olmayan ilk erişim veya fiziksel zarar uydurulmaz. İleri çalışma: sensör kapsamının ATT&CK eşlemesini nasıl sınırladığını [algılama bölümündeki](02-izleme-soc-ve-adli-inceleme.md) veri modeliyle açıklayın.

## Kaynak ve kapsam

- Microsoft, *Threat Modeling Tool threats*, 25 Ağustos 2022, [STRIDE açıklaması](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats).
- Bruce Schneier, *Attack Trees*, Aralık 1999, [yazarın yayını](https://www.schneier.com/academic/archives/1999/12/attack_trees.html).
- Lockheed Martin, *Cyber Kill Chain*, sayfada yayın tarihi belirtilmiyor, [çerçeve](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html).
- MITRE, [ICS taktikleri](https://attack.mitre.org/tactics/ics/) ve yukarıdaki dört yazılım kaydı; dinamik davranış sınıflandırmasıdır, ilk olay araştırması yerine kullanılmamıştır.
- DOE/CISA/NSA/FBI, AA22-103A, 13 Nisan 2022, yukarıdaki resmî arşiv PDF'si; hedef kapsamı ve başlangıç erişimi ön koşulu.
- Mandiant, 14 Aralık 2017, yukarıdaki TRITON incelemesi; ayrıntılı olgu/belirsizlik ayrımı mevcut vaka dosyasındadır.
- Dragos, *Measuring the Potential Impact of PIPEDREAM Malware OPC UA Module, MOUSEHOLE*, [araştırmacı yayını](https://www.dragos.com/blog/potential-impact-of-pipedream-malware-module-mousehole); PIPEDREAM adı ve OPC UA araştırma bağlamı. Kesin yayın günü bu incelemede doğrulanmadı.

Erişim: 16.09.2026. Kaynak tanımları kısa özetlenmiştir; tabloların OT inceleme soruları, koşul ağacı ve görevler özgün eğitim sentezidir.
