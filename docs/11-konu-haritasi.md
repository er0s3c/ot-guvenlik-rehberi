# İleri OT/ICS okuma ve çalışma haritası

[Ana sayfa](../README.md) · [Başlangıç programı](00-ogrenme-yolu.md) · [Ders formu](../templates/07-ders-ve-degerlendirme.md)

Bu harita, elli öğrenme başlığını deponun Markdown içeriklerine bağlar. Yakın konular aynı bölümde birlikte işlenir; her başlık için ayrı dosya veya kurulum gerekmez. Teknik örnekler, karar tabloları ve belge alıştırmaları eğitim kapsamındadır. Ürün belgelerinde tarif edilen özellik, burada kurulmuş ya da test edilmiş ürün anlamına gelmez.

## Nasıl çalışılır?

1. Başlangıçta [sekiz haftalık yolu](00-ogrenme-yolu.md) kullanın; ileri konulara önkoşullarınıza göre geçin.
2. Her konunun okumasını yaptıktan sonra [20 alanlı ders formunda](../templates/07-ders-ve-degerlendirme.md) ilgili alanları doldurun. Ortak maliyet, ürün ve vaka içeriklerini bağlantıyla kullanın; ilgisiz alana neden uygulanmadığını yazın.
3. **THEORY → LAB → TEST → DEFENSE → REPORT** döngüsünde bir belge çıktısı üretin. LAB bu depoda sentetik veri veya tasarım alıştırmasıdır; TEST ise iddianın hangi kanıtla kabul edileceğini inceler.
4. Düzeltme gereken alanları kabul edilmeden tamamlandı saymayın. Okur kendi kendini veya bir çalışma arkadaşını değerlendirebilir; repo otomatik eğitim/sertifika sistemi değildir.

## Elli başlığın dosya ve çıktı eşlemesi

| No | Konu | Ana okuma | Belge çıktısı |
|---|---|---|---|
| 01 | OT/ICS temelleri | [OT](01-temeller/01-ot-nedir.md), [bileşenler](01-temeller/02-kontrol-dongusu-ve-bilesenler.md) | IT–OT farkı ve kontrol döngüsü |
| 02 | OT/ICS mimarisi | [Mimari ve akış](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) | MES/ERP dahil işlev ve veri/kontrol akışı |
| 03 | Purdue modeli | [Temel model](01-temeller/03-mimari-ve-guven-bolgeleri.md), [ileri mimari](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) | Seviye, bölge ve geçiş gerekçesi |
| 04 | Zero Trust OT | [Kimlik ve politika](08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md) | Kullanıcı/cihaz/politika kararları |
| 05 | RBAC | [Rol matrisi](08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md), [şablon](../templates/12-ot-rbac-ve-umc-tasarim-sablonu.md) | Sekiz rolün sistem/işlem yetkisi ve üretici eşlemeleri |
| 06 | PAM | [Ayrıcalıklı erişim](08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md) | Sır, onay, oturum ve iptal yaşam döngüsü |
| 07 | OT protokolleri | [On dört aile](07-protokoller/01-protokol-katalogu.md) | Taşıma, port, işlev ve güvenlik profili tablosu |
| 08 | Protokol seçimi | [Karar karşılaştırmaları](07-protokoller/03-trafik-analizi-ve-protokol-secimi.md) | Dört karşılaştırma için gerekçeli seçim |
| 09 | Modbus güvenliği | [Modbus ve OPC UA](07-protokoller/02-modbus-ve-opc-ua-guvenligi.md) | İşlem türü, yetki ve telafi kontrolü |
| 10 | OPC UA güvenliği | [Güvenli iletişim](07-protokoller/02-modbus-ve-opc-ua-guvenligi.md) | Uç, kullanıcı, sertifika ve politika kabulü |
| 11 | Industrial firewall | [Sınır kontrolü](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md), [ürünler](10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md) | L3/L7 ihtiyacı ve kabul soruları |
| 12 | Segmentasyon | [Bölge geçişleri](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) | VLAN, yönlendirme ve izin/ret ayrımı |
| 13 | Industrial DMZ | [Servis yerleşimi](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md) | Bakım, kopyalama ve güncelleme akışları |
| 14 | SIEM + OT | [Kayıt mimarisi](09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md) | Alan modeli, veri sağlığı ve bağlam |
| 15 | OT IDS/IPS | [Gözlem ve müdahale](09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md), [araçlar](10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md) | Sensör kapsamı ve inline etki incelemesi |
| 16 | Varlık keşfi | [Envanter](04-savunma/01-envanter-ve-gorunurluk.md), [form](../templates/01-envanter-ve-akis.md) | Kaynaklı varlık/iletişim envanteri |
| 17 | Zafiyet yönetimi | [Karar yöntemi](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md), [değişiklik](04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md) | Etkilenme, işletme riski ve işlem kaydı |
| 18 | Penetrasyon testi | [On beş aşama](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) | Yetki, RoE ve değerlendirme planı |
| 19 | Security assessment | [Yöntem](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md), [form](../templates/08-degerlendirme-ve-risk-kaydi.md) | Kapsam, bulgu, risk ve yönetici özeti |
| 20 | OT Red Team | [Senaryo ve emülasyon](09-degerlendirme/03-tehdit-modelleme-ve-vakalar.md) | Amaç, varsayım, gözlem ve durdurma sınırları |
| 21 | ATT&CK for ICS | [Teknikler](03-tehdit-modelleme/02-mitre-attack-ics.md), [taktikler](09-degerlendirme/03-tehdit-modelleme-ve-vakalar.md) | Davranış–kanıt–kontrol eşlemesi |
| 22 | OT malware | [Beş örnek](09-degerlendirme/03-tehdit-modelleme-ve-vakalar.md), [vaka ayrımları](03-tehdit-modelleme/03-gercek-vakalar.md) | Olgu, belirsizlik ve savunma dersi |
| 23 | PLC security | [Varlık kontrolleri](08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md), [Siemens](10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md) | Proje/CPU/firmware ve mühendislik kabulü |
| 24 | Siemens security | [Ürün ve sürüm kapsamı](10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md) | Model/sürüm/lisans/kanıt tablosu |
| 25 | SCADA security | [SCADA ilişkileri](08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md) | Alarm, DB, historian ve yedeklilik bağımlılığı |
| 26 | HMI security | [HMI kontrol listesi](08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md) | Kullanıcı, servis, medya ve kalite incelemesi |
| 27 | Remote access | [Tasarım](08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md), [form](../templates/06-tedarikci-ve-uzak-erisim.md) | Kişi/hedef/süre/onay/iptal kaydı |
| 28 | Backup/DR | [Kurtarma](04-savunma/05-olay-mudahalesi-ve-kurtarma.md), [alıştırma](../labs/04-kurtarma-dogrulama.md) | Paket, bağımlılık, RTO/RPO ve kabul |
| 29 | Incident response | [Karar akışı](04-savunma/05-olay-mudahalesi-ve-kurtarma.md), [tatbikat](../labs/03-masa-basi-tatbikati.md) | İşletme/emniyet ve müdahale karar günlüğü |
| 30 | OT forensics | [Kanıt incelemesi](09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md), [kayıt labı](../labs/01-kayit-analizi.md) | Zaman çizelgesi, bütünlük ve kanıt zinciri |
| 31 | Honeypot | [Araçların kapsamı](10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md), [tasarım](../labs/06-sanal-laboratuvar-tasarimi.md) | Ayrı tuzak bölgesi ve gözlem sınırı |
| 32 | Windows/VMware lab tasarımı | [Sanal laboratuvar belgesi](../labs/06-sanal-laboratuvar-tasarimi.md) | Kaynak/izolasyon/geri dönüş kabul planı |
| 33 | Trafik analizi | [Çevrimdışı filtreler](07-protokoller/03-trafik-analizi-ve-protokol-secimi.md) | Normal davranış ve veri boşluğu raporu |
| 34 | Zafiyet taraması | [Yöntem ve etki ayrımı](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) | Pasif/aktif yöntem kararı; hedef komutu yok |
| 35 | Hardening | [Yedi varlık sınıfı](08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md) | Kontrol, kanıt, doğrulayan ve tarih |
| 36 | Ticari ürün karşılaştırması | [Ürün tablosu](10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md) | İşlev, dağıtım, kısıt ve lisans karşılaştırması |
| 37 | Açık kaynak seçenekleri | [Araç/lisans ayrımları](10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md) | Karşılanan ve açık kalan işlevler |
| 38 | Siemens UMC | [Merkezi kullanıcı yönetimi](10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md), [şablon](../templates/12-ot-rbac-ve-umc-tasarim-sablonu.md) | UMC ring server, S7-1500 central logon ve break-glass |
| 39 | Maliyet | [Üç mimari ve hesap](10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md) | Teklif/varsayım ayrımı ve toplam maliyet |
| 40 | IEC 62443 | [Standartlar](05-standartlar-ve-turkiye.md), [kanıt eşlemesi](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) | Zone/conduit ve güvenlik seviyesi bağlamı |
| 41 | NIST SP 800-82 | [Değerlendirme eşlemesi](09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md) | Öneri, yerel kontrol ve kanıt matrisi |
| 42 | Test öncesi liste | [Değerlendirme formu](../templates/08-degerlendirme-ve-risk-kaydi.md) | Yetki, hariçler, geri dönüş ve durdurma |
| 43 | Elli hata | [Kontrol kataloğu](09-degerlendirme/04-elli-yaygin-hata.md) | Risk → etki → algılama → düzeltme |
| 44 | Bütünleşik su tesisi | [Doldurulmuş tasarım](../labs/05-butunlesik-su-tesisi.md) | On mimari bileşenin ortak akış ve rolleri |
| 45 | Elektrik şebekesi | [Elektrik ve enerji](02-sektorler/02-elektrik-ve-enerji.md), [15 senaryo](02-sektorler/senaryolar/02-elektrik-enerji-senaryolari.md) | RTU/IED/SCADA, telekontrol ve bağımlılık değerlendirmesi |
| 46 | Su yönetimi | [Sektör](02-sektorler/01-su-ve-atiksu.md), [15 senaryo](02-sektorler/senaryolar/01-su-ve-atiksu-senaryolari.md) | Fiziksel süreçten kontrol gereksinimine eşleme |
| 47 | OT SOC | [Rol ve vardiya modeli](09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md) | Tier rolleri, işletme teyidi ve devir kaydı |
| 48 | Detection engineering | [Altı mantık ve test girdileri](09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md) | Normal, şüpheli ve veri eksikliği ayrımı |
| 49 | Threat modeling | [Dört yöntem](09-degerlendirme/03-tehdit-modelleme-ve-vakalar.md), [62 senaryo kataloğu](02-sektorler/senaryolar/README.md) | Tek PLC için gerekçeli tehdit modeli |
| 50 | Final proje | [Yirmi üç teslim](../templates/09-final-proje-teslimleri.md), [örnek](../labs/05-butunlesik-su-tesisi.md) | İzlenebilir danışmanlık dosyası |

## Önkoşul ve çalışma sırası

| Aşama | Konular | Çıkış ölçütü |
|---|---|---|
| Temel kavrayış | 1–3, 16, 40–41, 45–46 | İşlev, güven sınırı, bağımlılık ve kaynak ayrılabiliyor |
| Protokol ve veri | 7–10, 30, 33 | Protokol profilini ve kanıtın sınırını açıklayan rapor |
| Mimari ve erişim | 4–6, 11–13, 23–27, 35 | Rol ve akışların izin/ret gerekçeleri tutarlı |
| Değerlendirme | 17–22, 34, 42–43, 49 | Kapsam, bulgu, risk, kanıt ve karar sahibi bağlı |
| İzleme ve dayanıklılık | 14–15, 28–29, 47–48 | Alarmdan işletme kararına ve geri dönüşe izlenebilir yol |
| Araç ve kaynak planı | 31–32, 36–39 | Lisans, işletme emeği ve temsil sınırları açıklanmış |
| Bütünleştirme | 44, 50 | Yirmi üç teslimde ortak kimlikler ve açık belirsizlikler |

Süre, ön bilgi ve çalışma kapsamına göre değişir. Junior analist için kayıt yorumlama; mühendis için gerekçeli kontrol tasarımı; test uzmanı için kapsam ve kanıt; mimar için bağımlılık ve seçenek değerlendirmesi örnek gelişim hedefleridir. Unvanlar otomatik geçiş veya mesleki yetki olarak verilmez.

## Kaynak ve kapsam

17.09.2026 tarihli özgün gezinme ve öğrenme düzenidir. Teknik iddiaların kaynakları bağlantı verilen bölümlerdedir. Bu harita içeriklerin tamamını tek bir canlı laboratuvarda doğrulanmış gibi sunmaz; Markdown başvuru ve belge alıştırmaları için kullanılır.
