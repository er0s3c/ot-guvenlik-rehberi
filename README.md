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

Tam program: [sekiz haftalık öğrenme yolu](docs/00-ogrenme-yolu.md).

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
- [Sektörlerin karşılaştırılması](docs/02-sektorler/05-sektor-karsilastirmasi.md)

### 3. Saldırgan bakış açısı ve tehdit modelleme

- [Hedefler, ön koşullar ve güven sınırları](docs/03-tehdit-modelleme/01-saldirgan-bakis-acisi.md)
- [MITRE ATT&CK for ICS ve savunma eşleştirmeleri](docs/03-tehdit-modelleme/02-mitre-attack-ics.md)
- [Gerçek vakalar: olgular, belirsizlikler ve dersler](docs/03-tehdit-modelleme/03-gercek-vakalar.md)

### 4. Savunma ve işletme

- [Varlık envanteri ve pasif görünürlük](docs/04-savunma/01-envanter-ve-gorunurluk.md)
- [Segmentasyon, kimlik ve uzak erişim](docs/04-savunma/02-segmentasyon-ve-uzak-erisim.md)
- [İzleme, algılama ve SOC iş akışı](docs/04-savunma/03-izleme-ve-algilama.md)
- [Zafiyet, yama, tedarikçi ve değişiklik yönetimi](docs/04-savunma/04-zafiyet-ve-degisiklik-yonetimi.md)
- [Olay müdahalesi, yedekleme ve geri dönüş](docs/04-savunma/05-olay-mudahalesi-ve-kurtarma.md)
- [İlk 90 gün için savunma yol haritası](docs/04-savunma/06-90-gunluk-yol-haritasi.md)

### 5. Uygulama ve başvuru

- [Çevrimdışı laboratuvarlar](labs/README.md): kurgusal kayıt analizi, mimari inceleme ve masa başı tatbikatı
- [Kopyalanabilir çalışma şablonları](templates/README.md)
- [Standartlar ve Türkiye'de resmî başvuru noktaları](docs/05-standartlar-ve-turkiye.md)
- [Türkçe–İngilizce sözlük](docs/06-sozluk.md)
- [Kaynak kataloğu](KAYNAKLAR.md) ve [araştırma yöntemi](research/YONTEM.md)
- [Katkı rehberi](CONTRIBUTING.md), [güvenlik bildirimi](SECURITY.md) ve [değişiklik kaydı](CHANGELOG.md)

## İçeriğin sınırları ve kullanımı

Saldırı bölümleri, saldırganın amaçlarını, gerekli erişim koşullarını, olası etkileri ve savunma kanıtlarını inceler. Laboratuvarlar çevrimdışı ve tamamen kurgusaldır. Gerçek tesislere erişim, tarama veya işlem komutu içermez. Tesis üzerinde yapılacak değerlendirmeler yazılı kapsam, işletme sorumlusu ve emniyet değerlendirmesi gerektirir.

Mimari çizimler ve kontrol listeleri eğitim amaçlı özgün örneklerdir; belirli bir tesisin tasarımı veya devreye alma talimatı değildir. Her kurumun emniyet gerekleri, bakım penceresi, üretici desteği ve tabi olduğu düzenlemeler ayrıca değerlendirilir.

Araştırma kesim tarihi **13.09.2026**. Kaynaklarda yayın tarihi ile erişim tarihi ayrı tutulur. Örneğin [NIST yayın dizini](https://csrc.nist.gov/Projects/operational-technology-security/publications), SP 800-82 Rev. 3'ü final, Rev. 4 kaydını ise hazırlık amaçlı taslak olarak listeler. Bağlantılar ilgili bölümlerde iddiaların yanında yer alır; lisanslı standartların tam metinleri depoya eklenmez.

## Yerelde kullanma

Markdown dosyaları GitHub'da doğrudan okunur; Mermaid çizimleri destekleyen görüntüleyicilerde diyagram olarak görünür. Depoda ağ bağlantısı gerektirmeyen bir belge denetimi vardır:

```console
python3 scripts/check_docs.py
```

Denetim yerel dosya bağlantılarını ve başlık çapalarını, UTF-8 kodlamasını, kapatılmamış kod bloklarını, tek H1 kuralını, tablo sütun sayılarını ve satır sonu boşluklarını kontrol eder; güncel kapsam betiğin kendi açıklamasındadır. Aynı denetim, değişiklik önerilerinde [GitHub Actions iş akışıyla](.github/workflows/belge-denetimi.yml) da çalışır. Dış kaynakların erişilebilirliği ve bilimsel doğruluk için insan incelemesi gerekir.

## Lisans

Özgün metinler, diyagramlar, şablonlar ve sentetik eğitim verisi **CC BY 4.0**; `scripts/` içindeki yardımcı kod **MIT** lisanslıdır. Atıf koşulları ve üçüncü taraf materyal sınırları [LICENSE.md](LICENSE.md) dosyasındadır.
