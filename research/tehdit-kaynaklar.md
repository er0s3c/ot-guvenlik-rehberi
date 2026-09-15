# Tehdit modelleme ve vaka kaynakları

Bu katalog `docs/03-tehdit-modelleme/` belgelerinde kullanılan kaynakları bir araya getirir. Bütün erişim/kontrol tarihleri **2026-09-13**. Belgelerdeki senaryo matrisleri, algılama önerileri ve dersler özgün değerlendirmedir; tarihsel olgularla karıştırılmamalıdır.

## Yöntem ve kapsam

- Öncelik standart kuruluşlarının kendi yayınlarına, resmî teknik kayıtlarına, olay müdahalesi yapan araştırmacıların ilk analizlerine ve kamu kurumlarının doğrudan açıklamalarına verildi.
- Birinci el raporun başka bir kurum arşivindeki kopyası, yayıncı değiştirilmeden belirtildi. Arşiv kurumu olayın ilk araştırmacısı değildir.
- Bazı CISA sayfaları doğrudan erişimde **403** verdi. İlgili olgular erişilebilen indeks metni veya resmî metnin arşiv kopyası üzerinden kontrol edildi; tam güncel HTML içeriğinin incelendiği iddia edilmez. Sabit 2023 belgesi, kampanyanın sonraki tüm etkinliğini temsil etmez.
- Kaynaklardan uzun alıntı yapılmadı. Her sayfanın özet kullanım sınırı dikkate alınarak kısa olgular çıkarıldı; savunma tabloları özgün yazıldı.

## Temel yöntem kaynakları

| Yayıncı | Başlık ve bağlantı | Yayın/güncelleme | Desteklediği içerik |
|---|---|---|---|
| NIST | [SP 800-82 Rev. 3 — Guide to Operational Technology Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Eylül 2023 | OT güvenliğinde performans, güvenilirlik ve emniyet bağlamı |
| NIST | [SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Eylül 2012 | Tehdit, zafiyet ve etki ayrımı; riskin bağlama bağlı girdileri |
| MITRE | [Frequently Asked Questions](https://attack.mitre.org/resources/faq/) | Yaşayan sayfa; yayın tarihi belirtilmemiş | Taktik ve teknik kavramları |
| MITRE | [ATT&CK: Design and Philosophy](https://www.mitre.org/sites/default/files/2021-11/prs-19-01075-28-mitre-attack-design-and-philosophy.pdf) | Mart 2020 revizyonu | ATT&CK kapsamını kontrol listesine dönüştürmeme; yalnızca teknik benzerliğinden atıf yapmama |
| MITRE | [Enterprise teknikleri](https://attack.mitre.org/techniques/enterprise/), [ICS teknikleri](https://attack.mitre.org/techniques/ics/) | Yaşayan sayfalar | Davranış alanlarının kapsamı |

## MITRE teknik doğrulama kaydı

Tarihler resmî teknik sayfalarındaki `Last Modified` alanıdır. Sürüm, ATT&CK'in tüm yayınının sürümü değil ilgili tekniğin sürümüdür.

| Kimlik ve resmî ad | Teknik sürümü | Son değişiklik |
|---|---|---|
| [T0822 — External Remote Services](https://attack.mitre.org/techniques/T0822/) | 1.1 | 2026-05-12 |
| [T0859 — Valid Accounts](https://attack.mitre.org/techniques/T0859/) | 1.1 | 2026-05-12 |
| [T0864 — Transient Cyber Asset](https://attack.mitre.org/techniques/T0864/) | 1.2 | 2025-04-15 |
| [T0886 — Remote Services](https://attack.mitre.org/techniques/T0886/) | 1.1 | 2026-05-12 |
| [T0843 — Program Download](https://attack.mitre.org/techniques/T0843/) | 1.1 | 2026-05-12 |
| [T0889 — Modify Program](https://attack.mitre.org/techniques/T0889/) | 1.2 | 2025-04-15 |
| [T0836 — Modify Parameter](https://attack.mitre.org/techniques/T0836/) | 1.3 | 2025-04-16 |
| [T0878 — Alarm Suppression](https://attack.mitre.org/techniques/T0878/) | 1.2 | 2025-04-16 |
| [T0832 — Manipulation of View](https://attack.mitre.org/techniques/T0832/) | 1.0 | 2025-04-15 |
| [T0831 — Manipulation of Control](https://attack.mitre.org/techniques/T0831/) | 1.0 | 2025-04-16 |

T0843 sayfasında `T0843.001 Download All`, `T0843.002 Online Edit`, `T0843.003 Program Append` alt teknikleri doğrulandı. Tarihsel üçüncü taraf matrisleri bu ayrımı içermeyebilir. Her tablodaki teknik adının ve kimliğinin kaynağı MITRE'dir; yanlış pozitif ve yerel süreç eşleştirmeleri bu deponun önerileridir.

## Vaka kaynakları ve kanıt sınırları

| Yayıncı | Başlık ve bağlantı | Yayın tarihi | Kullanılan olgu ve sınır |
|---|---|---|---|
| DHS/ICS-CERT | [Cyber-Attack Against Ukrainian Critical Infrastructure — National Security Archive kopyası](https://nsarchive.gwu.edu/media/21941/ocr) | 2016-02-25 | 23 Aralık 2015 olayı, yaklaşık 225.000 müşteri, görüşmeye dayalı inceleme; teknik delillerin bağımsız incelenemediği ve ilk raporda BlackEnergy rolünün belirsiz olduğu |
| ABD Adalet Bakanlığı | [Six Russian GRU Officers Charged](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and) | 2020-10-19 | 2015–2016 Ukrayna olayları ve GRU Birim 74455 hakkında adli iddialar; mahkûmiyet sonucu olarak kullanılmadı |
| ESET, Anton Cherepanov ve Robert Lipovský | [Industroyer: Biggest threat to industrial control systems since Stuxnet](https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/) | 2017-06-12 | Endüstriyel protokol odaklı yetenekler; olayla yüksek olasılıklı bağlantı; tüm yeteneklerin olayda kullanıldığı varsayılmadı |
| ESET | [Sandworm: A tale of disruption told anew](https://www.welivesecurity.com/2022/03/21/sandworm-tale-disruption-told-anew/) | 2022-03-21 | İkinci Ukrayna kesintisinin 17 Aralık 2016 tarihi |
| Mandiant, Blake Johnson ve diğerleri | [Attackers Deploy New ICS Attack Framework TRITON](https://cloud.google.com/blog/topics/threat-intelligence/attackers-deploy-new-ics-attack-framework-triton) | 2017-12-14 | Birinci el olay müdahalesi, emniyet kontrolörü ve güvenli duruş; niyet değerlendirmesinde orta güven, ilk yayında belirli aktöre atıf yok |
| CISA, FBI, DOE | [AA22-083A — TTPs of Indicted State-Sponsored Russian Cyber Actors Targeting the Energy Sector](https://www.cisa.gov/sites/default/files/publications/AA22-083A_TTPs_of_Indicted_State-Sponsored_Russian_Cyber_Actors_Targeting_the_Energy_Sector.pdf) | 2022-03-24 | TRITON için sonraki TsNIIKhM bağlantısı değerlendirmesi; doğrudan PDF erişimi 403, indekslenmiş resmî metin kullanıldı |
| CISA | [Exploitation of Unitronics PLCs used in Water and Wastewater Systems](https://www.cisa.gov/news-events/alerts/2023/11/28/exploitation-unitronics-plcs-used-water-and-wastewater-systems) | 2023-11-28 | Etkilenen su idaresinin elle işletmeye geçmesi; o tarihte su arzı/kalitesi için bilinen risk olmadığı; doğrudan erişim 403, [resmî metnin arşiv kopyası](https://www.dejavu.org/cgi-bin/get.cgi?url=https%3A%2F%2Fwww.cisa.gov%2Fnews-events%2Falerts%2F2023%2F11%2F28%2Fexploitation-unitronics-plcs-used-water-and-wastewater-systems&ver=93) incelendi |
| CISA, FBI, NSA, EPA, INCD | [AA23-335A — 2023 PDF](https://www.cisa.gov/sites/default/files/2023-12/aa23-335a-irgc-affiliated-cyber-actors-exploit-plcs-in-multiple-sectors-1.pdf) | 2023-12-01 | Unitronics Vision hedeflemesi ve kurumların CyberAv3ngers–IRGC bağlantısı değerlendirmesi; doğrudan erişim 403, indekslenmiş resmî metin kullanıldı |
| ABD Temsilciler Meclisi, Homeland Security Committee | [Cyber Threats in the Pipeline](https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/pdf/CHRG-117hhrg45085.pdf) | 2021-06-09 | Colonial yönetiminin IT şifrelenmesi ve belirsizlik nedeniyle OT işletmesini durdurma kararı; basılı s. 12–13, PDF s. 15–16 |
| ABD Enerji Bakanlığı | [Colonial Pipeline Cyber Incident](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident) | Mayıs 2021 olay güncellemeleri | FBI'ın 10 Mayıs 2021 tarihli DarkSide atfı |

## Editoryal denetim notları

- Vaka belgelerinde zaman, gözlenen etki, atıf ve belirsizlik ayrı tutuldu. Gerçekleşmemiş fiziksel zarar gerçekleşmiş gibi sunulmadı.
- Saha adresi, internette cihaz bulma sorgusu, kimlik bilgisi, kötü amaçlı yazılım kodu, çalıştırılabilir sabotaj sırası veya emniyet baypası prosedürü bulunmaz.
- Bu kaynak kümesi Türk hukukuna, sektör ruhsat yükümlülüklerine veya Türkiye'deki belirli kurumların güncel güvenlik durumuna ilişkin iddia içermez.
