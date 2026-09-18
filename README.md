# OT Güvenliği Rehberi

**Operasyonel teknolojiyi sıfırdan öğrenmek, kritik altyapıları anlamak ve saldırgan bakış açısıyla savunma tasarlamak için Türkçe Markdown bilgi deposu.**

Bir pompanın çalışması, bir elektrik kesicisinin durumu, tren hareketine izin verilmesi veya baz istasyonunun soğutulması dijital kararlarla fiziksel dünya arasında bağ kurar. Bu depo o bağı açıklar: önce sistem nasıl çalışır, ardından hangi güven varsayımları bozulabilir, bunu nasıl fark ederiz ve hizmeti nasıl koruruz?

## Başlangıç

Ön bilgi gerektirmez. İlk okumada [OT nedir?](docs/01-temeller/01-ot-nedir.md) ile başlayın; ardından [kontrol döngüsünü](docs/01-temeller/02-kontrol-dongusu-ve-bilesenler.md), [ağ mimarisini](docs/01-temeller/03-mimari-ve-guven-bolgeleri.md) ve bir sektör bölümünü okuyun.

| Okur | Önerilen rota | Üreteceği çıktı |
|---|---|---|
| Yeni başlayan | Temeller → bir sektör → sözlük → laboratuvar | Bileşen ve veri akışı çizimi |
| IT / SOC uzmanı | Kontrol döngüsü → protokoller → ATT&CK → izleme | Süreç bağlamı taşıyan algılama kartı |
| Otomasyon / bakım mühendisi | Mimari → sektör → erişim → değişiklik ve kurtarma | Onaylı değişiklik ve geri dönüş planı |
| Yönetici / risk sorumlusu | Sektör karşılaştırması → risk → standartlar → yol haritası | Sorumlusu ve kanıtı tanımlı iyileştirme planı |

Başlangıç programı: [sekiz haftalık öğrenme yolu](docs/00-ogrenme-yolu.md). Teknik ayrıntılar ve belge çalışmaları: [elli başlıklı konu haritası](docs/11-konu-haritasi.md). Okuma ve alıştırmalar için Markdown görüntüleyici yeterlidir; ürün veya sanal makine kurulumu gerekmez.

## İçindekiler

### 1. Temeller

- [OT, IT, ICS, SCADA ve DCS](docs/01-temeller/01-ot-nedir.md)
- [Kontrol döngüsü, PLC, RTU, HMI ve emniyet](docs/01-temeller/02-kontrol-dongusu-ve-bilesenler.md)
- [Purdue modeli, bölgeler, geçişler ve veri akışları](docs/01-temeller/03-mimari-ve-guven-bolgeleri.md)
- [Endüstriyel protokoller ve güvenlik özellikleri](docs/01-temeller/04-endustriyel-protokoller.md)
- [Risk, fiziksel sonuçlar ve altyapı bağımlılıkları](docs/01-temeller/05-risk-emniyet-ve-bagimliliklar.md)

### 2. Kritik altyapılarda kullanım

- [Su ve atıksu](docs/02-sektorler/01-su-ve-atiksu.md)
- [Elektrik ve enerji](docs/02-sektorler/02-elektrik-ve-enerji.md)
- [Tren ve raylı sistemler](docs/02-sektorler/03-rayli-sistemler.md)
- [Telekom ve baz istasyonları](docs/02-sektorler/04-telekom-ve-baz-istasyonlari.md)
- [Petrol, doğal gaz ve kimya](docs/02-sektorler/05-petrol-gaz-ve-kimya.md)
- [Sektörlerin karşılaştırılması](docs/02-sektorler/05-sektor-karsilastirmasi.md)
- [Sektörel Tehdit ve Savunma Kataloğu (62 Senaryo)](docs/02-sektorler/senaryolar/README.md)
  - [Su ve Atıksu Senaryoları (15 Senaryo)](docs/02-sektorler/senaryolar/01-su-ve-atiksu-senaryolari.md)
  - [Elektrik ve Enerji Senaryoları (15 Senaryo)](docs/02-sektorler/senaryolar/02-elektrik-enerji-senaryolari.md)
  - [Raylı Sistemler Senaryoları (12 Senaryo)](docs/02-sektorler/senaryolar/03-rayli-sistemler-senaryolari.md)
  - [Telekom ve Baz İstasyonu Senaryoları (10 Senaryo)](docs/02-sektorler/senaryolar/04-telekom-baz-istasyonu-senaryolari.md)
  - [Petrol, Gaz ve Kimya Senaryoları (10 Senaryo)](docs/02-sektorler/senaryolar/05-petrol-kimya-proses-senaryolari.md)

### 3. Saldırgan bakış açısı ve tehdit modelleme

- [Hedefler, ön koşullar ve güven sınırları](docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md)
- [MITRE ATT&CK for ICS ve savunma eşleştirmeleri](docs/03-tehdit-modelleme/02-mitre-attack-ics.md)
- [Gerçek vakalar: olgular, belirsizlikler ve dersler](docs/03-tehdit-modelleme/03-gercek-vakalar.md)
- [MITRE ATT&CK for ICS Navigator Rehberi ve Isı Haritası](docs/03-tehdit-modelleme/04-mitre-navigator-rehberi.md) ([JSON Katmanı](research/mitre_attack_ics_layer.json))

### 4. Savunma ve işletme

- [Varlık envanteri ve pasif görünürlük](docs/04-savunma/01-envanter-ve-gorunurluk.md)
- [Segmentasyon, kimlik ve uzak erişim](docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md)
- [İzleme, algılama ve SOC iş akışı](docs/04-savunma/03-izleme-ve-algilama.md)
- [Zafiyet, yama, tedarikçi ve değişiklik yönetimi](docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md)
- [Olay müdahalesi, yedekleme ve geri dönüş](docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md)
  - [OT Olay Müdahale Playbook Koleksiyonu (5 Runbook)](docs/04-savunma/playbooks/README.md)
- [İlk 90 gün için savunma yol haritası](docs/04-savunma/06-90-gunluk-yol-haritasi.md)

### 5. Uygulama ve başvuru

- [Çevrimdışı laboratuvarlar](labs/README.md): kayıt analizi, mimari inceleme, masa başı tatbikatı, kurtarma doğrulama, bütünleşik su tesisi ve sanal laboratuvar tasarımı
- [Kopyalanabilir çalışma şablonları](templates/README.md) (11 Şablon: BİGR EKS ve IEC 62443 dahil)
- [Standartlar ve Türkiye'de resmî başvuru noktaları](docs/05-standartlar-ve-turkiye.md)
- [Türkçe–İngilizce sözlük](docs/06-sozluk.md)
- [Kaynak kataloğu](KAYNAKLAR.md) ve [araştırma yöntemi](research/YONTEM.md)
- [Katkı rehberi](CONTRIBUTING.md), [güvenlik bildirimi](SECURITY.md) ve [değişiklik kaydı](CHANGELOG.md)

### 6. Protokoller ve teknik inceleme

- [On dört protokol ailesi: taşıma, işlev ve güvenlik profilleri](docs/07-protokoller/01-protokol-katalogu.md)
- [Modbus ve OPC UA güvenliği](docs/07-protokoller/02-modbus-ve-opc-ua-guvenligi.md)
- [Çevrimdışı trafik analizi ve protokol seçimi](docs/07-protokoller/03-trafik-analizi-ve-protokol-secimi.md)

### 7. Mimari, kimlik ve varlık güvenliği

- [Zero Trust, RBAC, ABAC ve PAM](docs/08-mimari-ve-erisim/01-zero-trust-rbac-ve-pam.md)
- [Firewall, IDMZ ve uzak erişim tasarımı](docs/08-mimari-ve-erisim/02-firewall-dmz-ve-uzak-erisim.md)
- [PLC, HMI, SCADA ve destek varlıklarını sıkılaştırma](docs/08-mimari-ve-erisim/03-plc-hmi-ve-scada-sikilastirma.md)

### 8. Değerlendirme ve savunma çalışmaları

- [Güvenlik değerlendirmesi, test planı ve zafiyet önceliklendirme](docs/09-degerlendirme/01-guvenlik-degerlendirmesi-ve-test-plani.md)
- [OT SOC, altı algılama tasarımı ve adli inceleme](docs/09-degerlendirme/02-izleme-soc-ve-adli-inceleme.md)
- [STRIDE, ATT&CK, saldırı ağaçları ve beş malware örneği](docs/09-degerlendirme/03-tehdit-modelleme-ve-vakalar.md)
- [Elli hata: risk, etki, algılama ve düzeltme](docs/09-degerlendirme/04-elli-yaygin-hata.md)

### 9. Araçlar, ürünler ve maliyet

- [Ticari ve açık kaynak araçların işlev/lisans karşılaştırması](docs/10-araclar-ve-maliyet/01-arac-ve-urun-karsilastirmasi.md)
- [Siemens güvenliği ve UMC merkezi kullanıcı yönetimi](docs/10-araclar-ve-maliyet/02-siemens-ve-merkezi-kullanici-yonetimi.md)
- [Budget, Professional ve Enterprise maliyet modelleri](docs/10-araclar-ve-maliyet/03-maliyet-ve-secim-modeli.md)
- [Ders ve değerlendirme formu](templates/07-ders-ve-degerlendirme.md), [risk/değerlendirme kaydı](templates/08-degerlendirme-ve-risk-kaydi.md), [23 final teslimi](templates/09-final-proje-teslimleri.md)

## İçeriğin sınırları ve kullanımı

Saldırı bölümleri, saldırganın amaçlarını, gerekli erişim koşullarını, olası etkileri ve savunma kanıtlarını inceler. Laboratuvarlar çevrimdışı ve tamamen kurgusaldır. Gerçek tesislere erişim, tarama veya işlem komutu içermez. Tesis üzerinde yapılacak değerlendirmeler yazılı kapsam, işletme sorumlusu ve emniyet değerlendirmesi gerektirir.

Mimari çizimler ve kontrol listeleri eğitim amaçlı özgün örneklerdir; belirli bir tesisin tasarımı veya devreye alma talimatı değildir. Her kurumun emniyet gerekleri, bakım penceresi, üretici desteği ve tabi olduğu düzenlemeler ayrıca değerlendirilir.

İlk araştırma kesimi **13.09.2026**; teknik genişletmenin kaynak erişimleri **16–17.09.2026** tarihlerindedir. Her kaydın yayın/sürüm ve erişim tarihi ayrı tutulur; eski kayıtlar yeniden okunmuş gibi tarihlenmez. [NIST yayın dizini](https://csrc.nist.gov/Projects/operational-technology-security/publications), incelenen tarihte SP 800-82 Rev. 3'ü nihai, Rev. 4 kaydını taslak öncesi görüş çağrısı olarak listeler. Bağlantılar iddiaların yanındadır; lisanslı standartların tam metinleri depoya eklenmez.

## Yerelde kullanma

Markdown dosyaları GitHub'da doğrudan okunur; Mermaid çizimleri destekleyen görüntüleyicilerde diyagram olarak görünür. Depoda ağ bağlantısı gerektirmeyen bir belge denetimi vardır:

```console
python3 scripts/check_docs.py
```

Denetim yerel dosya bağlantılarını ve başlık çapalarını, UTF-8 kodlamasını, kapatılmamış kod bloklarını, tek H1 kuralını, tablo sütun sayılarını ve satır sonu boşluklarını kontrol eder; güncel kapsam betiğin kendi açıklamasındadır. Aynı denetim, değişiklik önerilerinde [GitHub Actions iş akışıyla](.github/workflows/belge-denetimi.yml) da çalışır. Dış kaynakların erişilebilirliği ve bilimsel doğruluk için insan incelemesi gerekir.

## Lisans

Özgün metinler, diyagramlar, şablonlar ve sentetik eğitim verisi **CC BY 4.0**; `scripts/` içindeki yardımcı kod **MIT** lisanslıdır. Atıf koşulları ve üçüncü taraf materyal sınırları [LICENSE.md](LICENSE.md) dosyasındadır.
