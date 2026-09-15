# MITRE ATT&CK for ICS ile savunma eşleştirmesi

## 1. Modelin amacı ve sınırı

MITRE ATT&CK®, gözlenmiş saldırgan davranışlarını ortak adlarla tartışmaya yarayan bir bilgi tabanıdır. Taktik amaçla, teknik davranışla ilgilidir. Teknik numarasının bulunması, o davranışın belirli bir tesiste mümkün olduğunu veya gerçekleştiğini göstermez. [MITRE SSS](https://attack.mitre.org/resources/faq/)

**Enterprise** alanı kurumsal bilgisayarlar, sunucular, kimlik ve bulut ortamlarındaki davranışları; **ICS** alanı endüstriyel kontrol bağlamındaki davranışları sınıflandırır. OT içindeki bir Windows mühendislik bilgisayarı için Enterprise davranışları da anlamlı olabilir. Aynı olay kaydında iki alan kullanılabilir; alan ve teknik kimliği açık yazılmalıdır. [Enterprise teknikleri](https://attack.mitre.org/techniques/enterprise/), [ICS teknikleri](https://attack.mitre.org/techniques/ics/)

ATT&CK **risk skoru değildir**. Bir matriste kaç hücrenin işaretlendiği; hizmetin önemini, saldırının olasılığını, sensörlerin kapsadığı alanı veya iyileştirme önceliğini kendiliğinden hesaplamaz. Bu sonuç, modelin davranış sınıflandırma amacı ile risk değerlendirmesinin ayrı girdiler gerektirmesinin birlikte okunmasına dayanır. MITRE ayrıca bütün teknikleri kapatılması gereken bir kontrol listesi gibi kullanmamayı ve yalnızca teknik benzerliğinden aktör atfı yapmamayı açıklar. [MITRE Design and Philosophy](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf), [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

## 2. Doğrulanmış on teknik

Kimlikler ve İngilizce adlar resmî sayfalardan **13.09.2026** tarihinde kontrol edildi. Türkçe karşılıklar açıklama amacı taşır. Aşağıdaki algılama, yanlış pozitif ve kontrol önerileri bu rehberin savunma tasarımı örnekleridir; MITRE tarafından onaylanmış hazır kurallar veya tüm ürünlerde çalışan garantiler değildir.

| Resmî teknik ve Türkçe açıklama | Davranışın anlamı | Gerekli veri ve algılama fikri | Olası yanlış pozitif | Kontrol ve inceleme odağı |
|---|---|---|---|---|
| [T0822 — External Remote Services](https://attack.mitre.org/techniques/T0822/) — Dış uzaktan erişim | Dış bağlantı hizmetinin ilk erişim amacıyla kullanılması | VPN ve erişim sunucusu kayıtlarını iş emriyle eşleştir; onaysız zaman veya hedef değişimini incele | Acil tedarikçi desteği, vardiya değişimi | Çok faktörlü doğrulama, kişisel hesap, süreli erişim, oturum sahibinin doğrulanması |
| [T0859 — Valid Accounts](https://attack.mitre.org/techniques/T0859/) — Geçerli hesaplar | Meşru kimlik bilgilerinin kötüye kullanılması | Kimlik kayıtları, hedef cihaz ve görev listesi; hesabın alışılmış görev alanı dışındaki erişimini ara | Geçici görev devri, yetkili yedek personel | Ayrı OT kimlikleri, asgari yetki, kullanılmayan hesapların kapatılması |
| [T0864 — Transient Cyber Asset](https://attack.mitre.org/techniques/T0864/) — Ortamlar arasında dolaşan cihaz | Bakım bilgisayarı gibi geçici varlıkların güvenilen bağlantısından yararlanılması | Cihaz kabul ve bağlantı kayıtları; kayıtlı bakım olmadan yeni cihaz görünmesini değerlendir | Donanım değişimi, yeni servis bilgisayarı | Ayrılmış bakım cihazı, kabul kontrolü, dosya aktarımının izlenebilirliği |
| [T0886 — Remote Services](https://attack.mitre.org/techniques/T0886/) — Uzak hizmetler | Sistemler veya ağ bölümleri arasında uzaktan yönetim hizmetlerinin kullanılması | Oturum ve ağ akışlarını birleştir; beklenmeyen kaynak–hedef çiftlerini incele | Planlı uzaktan bakım, yönetim aracı yenilemesi | Rol ve kaynak bazlı izin; operatörün yerel oturumunu koruma |
| [T0843 — Program Download](https://attack.mitre.org/techniques/T0843/) — Kontrolöre program aktarımı | Bir kullanıcı programının kontrol cihazına aktarılması | Cihaz olayı, mühendislik kaydı ve varsa pasif protokol görünürlüğü; aktarımı onaylı değişiklikle eşleştir | Devreye alma, doğrulanmış kurtarma, planlı bakım | Yetkili mühendislik kaynağı, sürüm kaydı, aktarımın ardından kabul incelemesi |
| [T0889 — Modify Program](https://attack.mitre.org/techniques/T0889/) — Program değiştirme | Kontrol cihazındaki programın değiştirilmesi veya eklenmesi | Onaylı proje ile cihaz programının uygun araçlarla karşılaştırılması; açıklanmamış mantık farkını incele | Üretici güncellemesi, belgelenmiş hata düzeltmesi | Program değişikliğinde ikinci kişi incelemesi ve güvenilir başlangıç kopyası |
| [T0836 — Modify Parameter](https://attack.mitre.org/techniques/T0836/) — Parametre değiştirme | Kontrol davranışını etkileyen parametrelerin değiştirilmesi | Eski/yeni değer, kullanıcı, zaman ve işletme modu; iş emriyle uyuşmayan değişikliği incele | Reçete değişimi, kalibrasyon, mevsimsel işletme | Rol bazlı yazma yetkisi; süreç sahibinin belirlediği sınırlar ve değişiklik takibi |
| [T0878 — Alarm Suppression](https://attack.mitre.org/techniques/T0878/) — Alarm bastırma | Alarmın oluşması veya iletilmesinin engellenmesi | Alarm yapılandırması, devre dışı bırakma kayıtları ve iletişim sağlığı; süreç sapmasına karşın beklenen alarm yokluğunu araştır | Onaylı bakım susturması, iletişim arızası | Süreli alarm susturma, ayrı onay, alarm yolunun sağlık izlemesi |
| [T0832 — Manipulation of View](https://attack.mitre.org/techniques/T0832/) — Görüntünün/verinin çarpıtılması | Operatöre veya kontrolöre bildirilen durumun yanıltılması | HMI, historian ve bağımsız saha bilgisi; zaman ve kalite bilgisiyle tutarsızlık ara | Sensör sürüklenmesi, örnekleme farkı, eski veri | Bağımsız doğrulama, veri eskimesi uyarısı, gösterim değişiklik kontrolü |
| [T0831 — Manipulation of Control](https://attack.mitre.org/techniques/T0831/) — Kontrolün manipülasyonu | Fiziksel süreç kontrolünün yetkisiz biçimde etkilenmesi | Komut kaydı, cihaz yanıtı ve bağımsız süreç ölçümü; onaylı işletme niyetiyle uyuşmazlığı incele | Otomatik koruma müdahalesi, yerel operatör işlemi | Kontrol yetkisinin sınırlandırılması, bağımsız koruma, olayın operasyon ekibiyle birlikte değerlendirilmesi |

T0843 ve T0889 aynı şeyi söylemez: biri **aktarımı**, diğeri **program değişikliğini** adlandırır. Her aktarım kötü niyetli değişiklik değildir; her program farkının nasıl oluştuğu yalnızca ağ kaydından anlaşılmaz. T0843 sayfası, güncel sürümde Download All, Online Edit ve Program Append alt tekniklerini listeler. Alt teknik, yalnızca eldeki kanıt bu ayrımı destekliyorsa seçilmelidir. [T0843](https://attack.mitre.org/techniques/T0843/), [T0889](https://attack.mitre.org/techniques/T0889/)

## 3. Bir tekniği algılama gereksinimine dönüştürmek

Aşağıdaki örnek özgün bir savunma tasarımıdır: “T0843'ü görüyoruz” demek yerine, “kapsamdaki A laboratuvar kontrolöründe program aktarımı kaydı oluşuyor; kayıt merkezi sisteme ulaşıyor; onaysız aktarım örneği görev kaydı oluşturuyor” denir. Böylece başarı, teknik adına değil gözlenebilir davranışa bağlanır. Aynı ürünün başka sürümünde veya başka saha bağlantısında sonuç yeniden doğrulanır.

Bir algılama kaydında en az şu bilgiler bulunmalıdır:

1. **Kapsam:** Hangi varlıklar, sahalar ve yazılım sürümleri gözleniyor?
2. **Veri:** Kaynağın adı, zaman doğruluğu, saklama süresi ve kayıp durumundaki bildirim yöntemi nedir?
3. **Hipotez:** Hangi davranış neden inceleme gerektiriyor; normal işletmeden hangi bağlamla ayrılıyor?
4. **Kanıt:** Alarmı doğrulamak için hangi ikinci kaynak kullanılacak?
5. **Sorumluluk:** Güvenlik analisti neyi inceleyecek, süreç mühendisi neyi doğrulayacak?
6. **Kısıt:** Şifreli trafik, eski cihaz, eksik günlük veya uzaktaki saha hangi kör noktayı yaratıyor?

Kontrolöre ait olay kaydı yoksa ağda da görünürlük bulunmayabilir. Bu durumda teknik “kapsanıyor” sayılmaz; elde edilemeyen veri açıkça kaydedilir. Güvenilir proje sürümüyle karşılaştırma gibi telafi edici yöntemler seçilebilir, fakat bunların olayın anında yakalandığı anlamına gelmediği belirtilir. Savunma durumu “tasarlandı”, “veri geliyor”, “örnekle doğrulandı” ve “işletmede izleniyor” gibi ayrı aşamalarla ifade edilebilir.

## 4. Yanlış pozitif ve emniyet ilişkisi

OT'de bakım, devreye alma ve işletme modu değişimi normal davranışı ciddi biçimde değiştirebilir. Bu rehberin önerisi, istisnaların yalnızca bir IP adresini sessize almak biçiminde değil, sorumlu kişi, süre ve iş emriyle kaydedilmesidir. Alarm susturması kendi süresini aştığında ayrıca incelenmelidir; istisna, görünürlüğü kalıcı olarak ortadan kaldırmamalıdır.

Bir güvenlik alarmından otomatik süreç durdurma kararı çıkarılmaz. Örneğin bir parametre değişikliği önce kaynağı ve yetkisiyle, sonra süreçteki anlamıyla değerlendirilir. Müdahale tasarımı yerel kontrol, iletişim kaybı ve emniyet prosedürleriyle uyumlu olmalıdır. Tablo bu nedenle saldırı komutları veya otomatik kesme kuralları içermez; süreç sahibiyle geliştirilecek gözlem gereksinimleri sunar.

## Kaynaklar

Erişim tarihi bütün kaynaklar için **2026-09-13**. Aşağıdaki tarih, teknik sayfasındaki **Last Modified** alanıdır; bir ürün açıklığının yayın tarihi değildir.

| Yayıncı | Kaynak | Sayfa tarihi | Desteklediği bilgi |
|---|---|---|---|
| MITRE | [T0822](https://attack.mitre.org/techniques/T0822/), [T0859](https://attack.mitre.org/techniques/T0859/), [T0886](https://attack.mitre.org/techniques/T0886/), [T0843](https://attack.mitre.org/techniques/T0843/) | 2026-05-12 | Resmî teknik kimliği, adı, davranış kapsamı |
| MITRE | [T0864](https://attack.mitre.org/techniques/T0864/), [T0889](https://attack.mitre.org/techniques/T0889/), [T0832](https://attack.mitre.org/techniques/T0832/) | 2025-04-15 | Resmî teknik kimliği, adı, davranış kapsamı |
| MITRE | [T0836](https://attack.mitre.org/techniques/T0836/), [T0878](https://attack.mitre.org/techniques/T0878/), [T0831](https://attack.mitre.org/techniques/T0831/) | 2025-04-16 | Resmî teknik kimliği, adı, davranış kapsamı |
| MITRE | [Enterprise](https://attack.mitre.org/techniques/enterprise/), [ICS](https://attack.mitre.org/techniques/ics/), [SSS](https://attack.mitre.org/resources/faq/) | Yaşayan sayfalar | Alanların ve taktik/teknik kavramlarının ayrımı |
| MITRE | [ATT&CK: Design and Philosophy](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf) | Mart 2020 revizyonu | Kontrol listesi yaklaşımının ve tekniğe dayalı atfın sınırları |
| NIST | [SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Eylül 2012 | Risk değerlendirmesinin ayrı bağlam ve girdilere ihtiyaç duyması |

**Önceki:** [Saldırgan bakış açısıyla tehdit modelleme](01-saldirgan-bakis-acisi.md) · **Sonraki:** [Gerçek vakalar](03-gercek-vakalar.md)
