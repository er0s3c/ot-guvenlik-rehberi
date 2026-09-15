# Gerçek vakalar: olgu, atıf ve belirsizlik

Bir olayın güvenilir incelenmesi dört ayrı kayıt gerektirir: **ne zaman olduğu**, **hangi etkinin gözlendiği**, **sorumluluğun kim tarafından kime atfedildiği** ve **hangi ayrıntıların bilinmediği**. Aşağıdaki vakalar saldırıların uygulanmasını öğretmek için değil, farklı savunma ihtiyaçlarını karşılaştırmak için seçilmiştir. “Ders” başlıkları kaynaklardan hareketle yapılan özgün değerlendirmelerdir.

## 1. Ukrayna elektrik dağıtımı — 23 Aralık 2015

**Olgu:** ICS-CERT'in 25 Şubat 2016 tarihli raporu, üç bölgesel dağıtım şirketindeki uzaktan siber müdahaleler sonrasında yaklaşık 225.000 müşterinin kesintiden etkilendiğini bildirir. Rapor, işletme personeliyle görüşmelere dayanır; araştırmacıların teknik delilleri bağımsız olarak inceleyemediğini açıkça belirtir. Kesintiyle birlikte bazı sistemlerde tahrip edici işlemler ve toparlanma güçlüğü raporlanmıştır. [ICS-CERT raporunun National Security Archive kopyası](https://nsarchive.gwu.edu/media/21941/ocr)

**Atıf:** ABD Adalet Bakanlığının 19 Ekim 2020 açıklaması, 2015–2016 Ukrayna saldırılarına ilişkin suçlamaları GRU Birim 74455 mensubu altı kişiyle ilişkilendirir. Bu, açıklamayı yapan kurumun adli iddiasıdır; iddianameyi kesinleşmiş mahkûmiyet gibi sunmamak gerekir. [DOJ açıklaması](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and)

**Belirsizlik:** İlk ICS-CERT raporu BlackEnergy'nin ağlarda bulunduğunu, ancak kesintideki özel rolünün o tarihte kesinleşmediğini söyler. Dolayısıyla “BlackEnergy kendi başına elektriği kesti” ifadesi bu ilk kaynağın desteklediğinden daha güçlüdür. Müşteri sayısını nüfus sayısıyla değiştirmek de kapsamı bozar. [ICS-CERT, 2016](https://nsarchive.gwu.edu/media/21941/ocr)

**Ders:** Uzaktan erişim yetkisi, operatör işlemlerinin izlenmesi ve kurtarma araçlarının korunması birlikte düşünülmelidir. Yalnızca zararlı yazılımın adını engellemeye dayanan bir çalışma, meşru araçlarla yapılan yetkisiz işletme işlemlerini kaçırabilir. Tatbikatta kontrol merkezi görünürlüğü azaldığında kimin hangi bağımsız bilgiye ulaşacağı ve sahaya yönlendirme kararının nasıl verileceği değerlendirilmelidir.

## 2. Ukrayna elektrik iletimi — Aralık 2016

**Olgu:** ESET'in araştırmacıları, Aralık 2016'daki Ukrayna kesintisi bağlamında Industroyer adını verdikleri yazılımı inceledi. 12 Haziran 2017 yayını, endüstriyel haberleşme protokolleriyle etkileşebilen, elektrik kontrol sistemlerine özgü işlevler içeren bir yapıyı anlatır. ESET'in sonraki tarihsel değerlendirmesi ikinci kesintiyi 17 Aralık 2016'ya tarihler. [ESET ilk analiz](https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/), [ESET tarihsel değerlendirme](https://www.welivesecurity.com/2022/03/21/sandworm-tale-disruption-told-anew/)

**Atıf:** 2020 DOJ açıklaması Industroyer'ı da kapsayan 2015–2016 saldırılarını aynı GRU birimine yönelik suçlamalar içinde sayar. Burada yazılım adı, kampanya adı ve devlet kurumu atfı farklı bilgi türleridir. Bir yazılım örneğini görmek tek başına belirli bir operatörün kimliğini kanıtlamaz. [DOJ, 2020](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and)

**Belirsizlik:** ESET'in ilk yayını, olay yerinde araştırma yapmadan kesin eşleştirmenin zor olduğunu ve Industroyer'ın bu olayda kullanılmış olmasını yüksek olasılıklı gördüğünü belirtir. Yazılımın sahip olduğu tüm işlevlerin o olayda başarıyla çalıştığını varsaymak doğru değildir. [ESET, 2017](https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/)

**Ders:** Ağda tanıdık bir protokolün görünmesi davranışın yetkili olduğunu göstermez. Savunma, iletişimi hangi sistemin hangi işlev için başlattığını değerlendirmelidir. Yetkili komut kaynağı, iş emri, işletme modu ve cihaz yanıtı birlikte anlamlıdır. Laboratuvar çalışmasında hedef, zararlı yazılımı yeniden üretmek yerine kayıtların bu bağlamı taşıyıp taşımadığını sınamaktır.

## 3. TRITON/TRISIS/HatMan — 2017

**Olgu:** Olay müdahalesini yapan Mandiant'ın 14 Aralık 2017 yayını, bir kritik altyapı kuruluşunun emniyet enstrümanlı sistemlerini hedefleyen TRITON'u açıklar. Bazı emniyet kontrolörlerinin güvenli hata durumuna geçmesiyle endüstriyel süreç durmuş ve inceleme başlamıştır. Rapor, fiziksel zarar oluşturma kabiliyetinin geliştirildiği ve duruşun istenmeden gerçekleştiği değerlendirmesine **orta güven** düzeyi verir. [Mandiant olay analizi](https://cloud.google.com/blog/topics/threat-intelligence/attackers-deploy-new-ics-attack-framework-triton)

**Atıf:** İlk Mandiant yayını belirli bir aktör atfı yapmaz. CISA, FBI ve ABD Enerji Bakanlığının 24 Mart 2022 ortak bildirimi ise 2017 olayını Rus TsNIIKhM bağlantılı aktörlerle ilişkilendirir. İki kaynak farklı tarihlerdeki bilgi düzeylerini temsil eder. [Mandiant, 2017](https://cloud.google.com/blog/topics/threat-intelligence/attackers-deploy-new-ics-attack-framework-triton), [AA22-083A](https://www.cisa.gov/sites/default/files/publications/AA22-083A_TTPs_of_Indicted_State-Sponsored_Russian_Cyber_Actors_Targeting_the_Energy_Sector.pdf)

**Belirsizlik:** Potansiyel fiziksel zarar ile raporlanan süreç duruşu ayrı sonuçlardır. Bu kaynaklar temelinde patlama, ölüm veya gerçekleşmiş büyük çevre zararı anlatısı kurulmaz. İlk araştırmacıların aktör niyetine ilişkin değerlendirmesi de doğrudan gözlemle eşdeğer değildir.

**Ders:** Emniyet sistemi üretim kontrolünden bağımsız düşünülmeli; ortak bakım bilgisayarı, kimlik ve yönetim bağlantıları bu bağımsızlığı zayıflatabilecek bağımlılıklar olarak incelenmelidir. Bir güvenli duruş yaşanması siber bütünlüğün sağlam olduğunu göstermez. Sonrasında yalnızca cihazın yeniden çalışması değil, programın güvenilirliği ve emniyet işlevinin yetkili ekipçe doğrulanması gerekir.

## 4. Unitronics kullanan su ve atıksu sistemleri — Kasım 2023

**Olgu:** CISA'nın 28 Kasım 2023 duyurusu, ABD'deki bir su tesisinde Unitronics PLC'ye yönelik yetkisiz erişimi ve su idaresinin sistemi çevrimdışına alarak elle işletmeye geçtiğini bildirir. Duyuru, o aşamada içme suyu veya su arzına ilişkin bilinen risk bulunmadığını açıklar. Bu, belirli olay ve duyuru zamanı için verilen bilgidir. [CISA ilk duyurusu](https://www.cisa.gov/news-events/alerts/2023/11/28/exploitation-unitronics-plcs-used-water-and-wastewater-systems)

**Atıf:** 1 Aralık 2023 tarihli ortak AA23-335A bildirimi, CyberAv3ngers adını kullanan aktörleri IRGC ile bağlantılı olarak niteler ve birden fazla sektörde Unitronics Vision serisi cihazların hedeflendiğini belirtir. Atıf, bildirimi yayımlayan kurumların değerlendirmesidir. [AA23-335A, 2023 PDF](https://www.cisa.gov/sites/default/files/2023-12/aa23-335a-irgc-affiliated-cyber-actors-exploit-plcs-in-multiple-sectors-1.pdf)

**Belirsizlik:** Bir cihazın ekranına erişim veya ekran içeriğinin değiştirilmesi, suyun kimyasal özelliklerinin değiştirildiğini kanıtlamaz. Ayrıca tek belediyeyle ilgili “bilinen risk yok” açıklaması, kampanyadaki tüm tesislerde aynı etki oluştuğu anlamına gelmez. 2023 tarihli sabit bildirimin kapsamı, sonraki yıllardaki olaylarla karıştırılmamalıdır.

**Ders:** Varlık envanteri, dış bağlantının gerekçesi, cihaz kimlikleri ve yerel işletme hazırlığı birlikte incelenmelidir. Bakım kolaylığı için kurulmuş erişimin bugün hâlâ gerekli olup olmadığı belirlenmelidir. Elle işletme seçeneğinin varlığı kadar personelin erişimi, güncel talimatı ve veri doğrulama imkânı da önemlidir; bu seçenek sınırsız süreyle yeterli kabul edilmez.

## 5. Colonial Pipeline — 7 Mayıs 2021

**Olgu:** Colonial yönetiminin 9 Haziran 2021 kongre ifadesi, fidye yazılımının IT sistemlerini şifrelediğini ve olayın kapsamı başlangıçta bilinmediği için OT'ye yayılma olasılığını sınırlamak amacıyla hat işletmesinin durdurulduğunu açıklar. Bu vaka, hizmet kesintisinin doğrudan PLC mantığının değiştirilmesinden kaynaklanmasının şart olmadığını gösterir. [Kongre tutanağı, basılı s. 12–13](https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/pdf/CHRG-117hhrg45085.pdf)

**Atıf:** ABD Enerji Bakanlığı olay sayfası, FBI'ın 10 Mayıs 2021'de olayı DarkSide fidye yazılımıyla ilişkilendirdiğini kaydeder. Yazılım/grup atfı, ayrıca kanıt bulunmadan devlet yönlendirmesi olarak genişletilmez. [DOE olay sayfası](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident)

**Belirsizlik:** Kamuya açık ifade, tüm kurum içi delillerin yayımlandığı anlamına gelmez. “OT cihazları fiziksel olarak tahrip edildi” iddiasını desteklemek için ayrı kanıt gerekir. Duruş kararını, saldırganın doğrudan saha komutu vermesiyle aynı olay gibi anlatmak savunma önceliklerini yanlış yönlendirebilir.

**Ders:** IT–OT ayrımı yalnızca ağdan oluşmaz. Kimlik, işletme verisi, iletişim ve kurtarma süreçleri de bağımlılık yaratabilir. Bir süreklilik çalışması, OT'ye doğrudan müdahale olmasa bile hangi destek hizmetlerinin kaybında işletmenin duracağını belirlemelidir. Yeniden başlama ölçütleri, teknik temizliğin yanında güvenilir görünürlük ve süreç kabulünü kapsamalıdır.

## Vakaları karşılaştırırken

Bu beş örnek farklı sonuç yollarını gösterir: yetkisiz uzaktan işletme, endüstriyel protokol odaklı davranış, emniyet sisteminin bütünlüğü, saha erişimi ve IT olayına bağlı işletme kararı. Bunları tek bir “SCADA ele geçirildi” cümlesine indirgemek, gerekli kontrollerin hangi noktada çalışacağını belirsizleştirir.

Bir vaka okuma çalışmasında katılımcılar üç çıktı üretmelidir: kaynakla desteklenen kısa olay çizelgesi, bilinmeyenleri içeren kanıt tablosu ve kendi tesisinde doğrulanabilecek üç savunma gereksinimi. Tarihsel bir saldırının başarı koşullarının başka ülkede, üreticide veya süreçte aynen bulunduğu varsayılmamalıdır.

## Kaynaklar

Erişim tarihi bütün kaynaklar için **2026-09-13**. Kaynak tarihi ile olay tarihi ayrı tutulmuştur.

| Yayıncı | Kaynak ve yayın tarihi | Desteklediği bilgi / erişim notu |
|---|---|---|
| DHS/ICS-CERT | [Cyber-Attack Against Ukrainian Critical Infrastructure](https://nsarchive.gwu.edu/media/21941/ocr), 2016-02-25 | 2015 olayının etki ve kanıt sınırları; George Washington University National Security Archive'da korunan resmî belgenin metni |
| ABD Adalet Bakanlığı | [Six Russian GRU Officers Charged](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and), 2020-10-19 | 2015–2016 Ukrayna olaylarıyla ilgili adli atıf; açıklama iddianameye ilişkindir |
| ESET, Anton Cherepanov ve Robert Lipovský | [Industroyer](https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/), 2017-06-12 | Zararlı yazılımın endüstriyel kapsamı ve ilk olay eşleştirmesinin güven sınırı |
| ESET | [Sandworm: A tale of disruption told anew](https://www.welivesecurity.com/2022/03/21/sandworm-tale-disruption-told-anew/), 2022-03-21 | İkinci elektrik kesintisinin tarihsel konumu |
| Mandiant, Blake Johnson ve diğerleri | [Attackers Deploy New ICS Attack Framework TRITON](https://cloud.google.com/blog/topics/threat-intelligence/attackers-deploy-new-ics-attack-framework-triton), 2017-12-14 | Olay müdahalesinden emniyet sistemi bulguları, duruş ve niyet değerlendirmesi |
| CISA, FBI, DOE | [AA22-083A](https://www.cisa.gov/sites/default/files/publications/AA22-083A_TTPs_of_Indicted_State-Sponsored_Russian_Cyber_Actors_Targeting_the_Energy_Sector.pdf), 2022-03-24 | TRITON olayına ilişkin sonraki kurum atfı |
| CISA | [Exploitation of Unitronics PLCs](https://www.cisa.gov/news-events/alerts/2023/11/28/exploitation-unitronics-plcs-used-water-and-wastewater-systems), 2023-11-28 | İlk su tesisi olayı, elle işletme ve o tarihte bilinen etki; doğrudan sayfa erişimi kısıtlandığında indekslenmiş resmî metin kontrol edildi |
| CISA, FBI, NSA, EPA, INCD | [AA23-335A — 2023 PDF](https://www.cisa.gov/sites/default/files/2023-12/aa23-335a-irgc-affiliated-cyber-actors-exploit-plcs-in-multiple-sectors-1.pdf), 2023-12-01 | Unitronics kampanyası ve kurumların IRGC bağlantısı değerlendirmesi; 2023 tarihli arşiv sürümü |
| ABD Temsilciler Meclisi | [Cyber Threats in the Pipeline](https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/pdf/CHRG-117hhrg45085.pdf), 2021-06-09 | Colonial yönetiminin IT etkisi ve işletmeyi durdurma kararına ilişkin doğrudan ifadesi |
| ABD Enerji Bakanlığı | [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident), Mayıs 2021 olay güncellemeleri | FBI'ın 10 Mayıs tarihli DarkSide atfı ve olay zaman çizelgesi |

**Önceki:** [MITRE ATT&CK for ICS](02-mitre-attack-ics.md) · [Tehdit modelleme](01-saldirgan-bakis-acisi.md)
