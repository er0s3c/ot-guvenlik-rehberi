# Varlık envanteri ve görünürlük

OT envanteri bir cihaz listesiyle sınırlı kalmamalıdır: cihazın yaptığı iş, sorumlusu, süreç açısından önemi ve bağımlılıkları görünür olmalıdır. CISA ve ortaklarının 2025 rehberi, envanteri işlev ve kritiklik açısından sınıflandıran bir OT taksonomisiyle birlikte ele alır. [Foundations for OT Cybersecurity](https://www.cyber.gov.au/business-government/secure-design/operational-technology-environments/foundations-for-ot-cybersecurity-asset-inventory-guidance-for-owners-and-operators)

## Envanteri oluşturma

Aşağıdaki sıra bu deponun uygulama önerisidir. Önce işletme çizimleri, bakım kayıtları, onaylı proje dosyaları ve cihaz sahipleriyle görüşmeler incelenir. Mevcut ağ kayıtları ve uygun noktadan pasif gözlem bu bilgiyi zenginleştirir. Sahada doğrulama güvenli çalışma koşullarıyla planlanır. Ürünlerin davranışı bilinmeden aktif sorgulama varsayılan keşif yöntemi yapılmaz.

Pasif gözlem de eksiksiz değildir: kapalı veya sessiz varlıklar görünmeyebilir, seri ağlar gözlem noktasına ulaşmayabilir, şifreli içerik okunamayabilir. Ağ aynalama yapılandırması bir değişikliktir; kapasite ve hata davranışı değerlendirilmelidir. Trafik görülmemesi varlığın bulunmadığını kanıtlamaz.

## Asgari alanlar

| Alan grubu | Örnek bilgi | Neden gerekli? |
|---|---|---|
| Kimlik | Varlık kodu, model, donanım revizyonu | Ürünü doğru eşleştirmek |
| Yazılım | Firmware, işletim sistemi, proje sürümü | Zafiyet ve uyumluluk değerlendirmesi |
| İşlev | Sağlanan hizmet, ölçüm/kontrol/koruma rolü | Önceliği iş etkisine bağlamak |
| Bağımlılık | Güç, zaman, ağ, kimlik, lisans, başka cihaz | Ortak arıza ve kurtarma sırası |
| Erişim | Bölge, yönetim yolu, roller, tedarikçi | Yetki yüzeyini görmek |
| Yaşam döngüsü | Destek sonu, değişiklik sahibi, yedek konumu | Sürdürülebilir işletme |
| Kanıt | Bilginin kaynağı, doğrulayan, tarih, güven düzeyi | Tahmin ile doğrulamayı ayırmak |

[Envanter ve akış şablonu](../../templates/01-envanter-ve-akis.md) bu alanları doldurmak içindir. Gerçek tesis koordinatları, adresleri, projeleri ve hesap bilgileri herkese açık depoya konulmaz; kurumun kontrollü kayıt sisteminde tutulur.

## Envanterin bakımını yapma

Bir varlık değiştiğinde yalnızca seri numarası güncellenmez. Uzak erişim kapsamı, yedek uyumluluğu, güvenlik duvarı akışı, alarm eşiği ve destek sorumlusu da değişmiş olabilir. Devreye alma ve hizmetten çıkarma kontrol listesi bu ilişkileri aynı değişiklik kaydında bağlamalıdır.

Örnek kalite ölçütleri: kritik işlevlere atanmış sahip oranı, son doğrulama tarihi bilinen varlık oranı, kurtarma bağımlılıkları tanımlı kritik varlık oranı. Payda açıklanmalıdır: “görülen 50 cihazın 50'si kayıtlı” ifadesi görünmeyen cihazlar nedeniyle tüm tesis kapsamını ispatlamaz.

## İlk inceleme kontrol listesi

- [ ] Kontrol ve koruma varlıkları işlevleriyle tanımlandı.
- [ ] Geçici bakım cihazları ve tedarikçi bağlantıları kaydedildi.
- [ ] Ağda görünmeyen varlıklar için ayrı doğrulama yolu var.
- [ ] Envanter bilgilerinin sahibi ve gözden geçirme tarihi mevcut.
- [ ] Süreç, ağ ve bakım kayıtlarındaki çelişkiler bir iş listesine alındı.
- [ ] Envanterin kendisi erişim kontrollü ve kurtarılabilir durumda.

## Kaynak

- CISA, EPA, NSA, FBI ve uluslararası ortaklar, *Foundations for OT Cybersecurity: Asset Inventory Guidance for Owners and Operators*, Ağustos 2025, [ACSC tam metin yayını](https://www.cyber.gov.au/business-government/secure-design/operational-technology-environments/foundations-for-ot-cybersecurity-asset-inventory-guidance-for-owners-and-operators), erişim: 13.09.2026. Girişteki envanter/taksonomi ilkesi bu kaynaktan; uygulama tablosu ve ölçütler özgün öneridir.
