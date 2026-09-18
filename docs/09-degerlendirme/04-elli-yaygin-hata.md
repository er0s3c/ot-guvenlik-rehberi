# OT güvenliğinde elli hata ve inceleme sorusu

[Değerlendirme yöntemi](01-guvenlik-degerlendirmesi-ve-test-plani.md) · [Risk kaydı](../../templates/08-degerlendirme-ve-risk-kaydi.md)

Bu liste, sıklık araştırması veya en çok görülen olaylar sıralaması değildir. Rehberin konularını incelemek için hazırlanmış **özgün eğitim kataloğudur**. Etkiler olası sonuçlardır; belirli bir tesiste gerçekleştiği varsayılmaz. Her seçilen satıra varlık, kanıt, doğrulayan, tarih ve işlem sahibi eklenir.

## Kimlik ve uzak erişim

| No | Hata / risk | Olası etki | Nasıl fark edilir? | Düzeltme ve kabul |
|---|---|---|---|---|
| 01 | Varsayılan kimlik bilgileri | Yetkisiz erişim | Ürün kabul kaydı ve hesap politikası incelemesi | Devreye alma hesabı değişikliği; hedefte doğrulama |
| 02 | Paylaşılan yönetici hesabı | Kişi–işlem bağı kaybı | Hesap sahipliği ve oturum eşlemesi | Kişisel hesap; zorunlu istisnaya kayıtlı sorumluluk |
| 03 | Sahipsiz tedarikçi hesabı | Süresiz dış erişim | Sözleşme ve hesap listesinin karşılaştırılması | Sahip, bitiş ve iptal kanıtı |
| 04 | Destekleyen erişim kapısında MFA eksikliği | Tek kimlik bilgisiyle giriş | Kapı politikası ve giriş kayıtları | Desteklenen MFA; kurtarma ve acil erişim testi |
| 05 | Gözlemciye değişiklik yetkisi | Onaysız işlem | Rol × sistem × işlem matrisi | Hedefte yetki ayrımı ve ret kanıtı |
| 06 | Hesap iptalinin oturumu bitirdiğini varsaymak | Eski oturumun sürmesi | Kapı ile hedef oturumunun karşılaştırılması | İptal sonrası etkin oturum kabul ölçütü |
| 07 | Bakım süresini sınırlamamak | Görev dışı erişim | Onay penceresi ve gerçek oturum süresi | Süreli yetki; uzatma için yeni kayıt |
| 08 | Vendor için doğrudan kontrol ağı yolu | Denetimsiz güven geçişi | Akış/rota ve dış erişim kaydı | Kontrollü kapı, hedef kapsamı ve kayıt |
| 09 | Acil hesabı hiç gözden geçirmemek | Kalıcı ayrıcalık | Kullanım geçmişi ve sorumlu kaydı | Kullanım sonrası inceleme ve sır yenileme |
| 10 | Kimlik servisi kesintisini planlamamak | Bakım veya operatör erişim kaybı | Bağımlılık haritası, masa başı kesinti senaryosu | Kontrollü yerel erişim ve geri dönüş planı |

## Ağ ve protokoller

| No | Hata / risk | Olası etki | Nasıl fark edilir? | Düzeltme ve kabul |
|---|---|---|---|---|
| 11 | Bütün OT varlıklarını aynı güven bölgesine koymak | Gereksiz erişim yayılımı | İşlev ve güven gereksinimi karşılaştırması | Bölge/geçiş tasarımı ve gerekçeli akışlar |
| 12 | VLAN etiketini tek başına erişim kontrolü saymak | Yönlendirilmiş istenmeyen trafik | Katman 3 yolları ve kuralların incelemesi | Geçiş kontrolü ve izin/ret kanıtı |
| 13 | Geniş kaynak/hedef/servis kuralları | İş gerekçesi dışı iletişim | Firewall kuralı ile akış matrisinin karşılaştırılması | En dar gerekçeli kapsam; gerekli işlevi doğrulama |
| 14 | Kullanılmayan kuralları süresiz bırakmak | Eski erişimin devamı | Sahip, son kullanım ve gözden geçirme tarihi | Sahip onayıyla kaldırma ve geri dönüş kaydı |
| 15 | IDMZ üzerinden gizli ikinci yol | Bölge sınırının atlanması | Çoklu ağ kartı, rota, proxy ve tünel incelemesi | Bütün alternatif yolların matrise alınması |
| 16 | İnternete doğrudan PLC erişimi | Yetkisiz dış erişim ihtimali | Kurumun onaylı dış bağlantı kayıtları | Erişimi kapı üzerinden sınırlama; sahip teyidi |
| 17 | Protokol adını güvenli profil sanmak | Korunmayan oturum | Uç profili, sürümü ve etkin ayarlar | İki uç ve ara geçitte profil kanıtı |
| 18 | Şifreli yolu uçtan uca şifreli sanmak | Ağ geçidi sonrası açık bölüm | Şifrelemenin sonlandığı noktaların çizimi | Her bölümün güven sınırını ayrı değerlendirme |
| 19 | Sertifika yenilemeyi plansız yapmak | Bağlantı ve işletme kaybı | Süre bitimi, güven listesi ve sahip kaydı | Yenileme/geri dönüş kabul planı |
| 20 | Kablosuz taşıyıcıyı envanter dışında bırakmak | Bilinmeyen dış bağımlılık | Modem, abonelik, anten ve saha kayıtları | Taşıyıcı sahibi ve kesinti davranışı |

## Varlık, proje ve değişiklik

| No | Hata / risk | Olası etki | Nasıl fark edilir? | Düzeltme ve kabul |
|---|---|---|---|---|
| 21 | Yalnız IP listesine envanter demek | İşlev ve sorumluluk belirsizliği | Listeyi süreç/bakım kayıtlarıyla karşılaştırma | Sahip, işlev, sürüm ve bağımlılık ekleme |
| 22 | Sessiz cihazı yok saymak | Kapsam dışında kritik varlık | Çizim ve saha/bakım teyidi | Gözlenen ile toplam kapsamı ayrı raporlama |
| 23 | Firmware/proje sürümünü kaydetmemek | Yanlış zafiyet/yedek eşleşmesi | Sürüm kanıtı ve değişiklik geçmişi | Kaynaklı sürüm kaydı |
| 24 | Destek sonunu takip etmemek | Sürdürülemeyen bakım | Üretici yaşam döngüsü ve sözleşme | Telafi, yedek ve yenileme planı |
| 25 | CVSS'yi tek öncelik ölçütü yapmak | İşletme riskinin yanlış sıralanması | Bulgu gerekçeleri | Erişim, işlev, emniyet ve değişiklik etkisini ekleme |
| 26 | Ürün adına bakarak CVE eşlemek | Yanlış olumlu/olumsuz değerlendirme | Model, sürüm ve etkin işlev | Etkilenme kararının üretici koşuluyla kanıtlanması |
| 27 | SBOM'u kesin etkilenme listesi sanmak | Gereksiz veya eksik işlem | Bileşen ve ürün kapsamı incelemesi | Tedarikçi açıklaması ve etkin işlevle uzlaştırma |
| 28 | Onaysız proje değişikliği | Kontrol bütünlüğü kaybı | Proje farkı ve iş emri | Sürüm, onay, hedef ve kabul kaydı |
| 29 | Bakım dizüstü bilgisayarını kayıtsız bağlamak | Geçici cihazdan güven geçişi | Kabul/ziyaret ve bağlantı kaydı | Geçici varlık envanteri, yetki ve dosya aktarım kontrolü |
| 30 | USB ve mühendislik dosyalarının kaynağını bilmemek | Güvenilmeyen içerik aktarımı | Medya/dosya kabul kaydı | Kontrollü aktarım, bütünlük ve onay |

## İzleme ve analiz

| No | Hata / risk | Olası etki | Nasıl fark edilir? | Düzeltme ve kabul |
|---|---|---|---|---|
| 31 | Sensör kuruldu diye tam görünürlük ilan etmek | Görünmeyen segmentler | Gözlem noktası/varlık kapsamı matrisi | Kör noktaları ve doğrulama örneklerini raporlama |
| 32 | Sensör paket kaybını izlememek | Eksik olay analizi | Sensör sağlık/kayıp bilgisi | Kapasite ve kayıp alarmı |
| 33 | Şifreli içerikte işlem türünü bildiğini varsaymak | Yanlış algılama iddiası | Gerçek çözümlenmiş alanlar | Uç kayıtlarıyla tamamlayıp sınırı açıklama |
| 34 | Tek işletme modundan baseline çıkarmak | Bakımı saldırı veya saldırıyı normal saymak | Vardiya/mod/bakım dağılımı | Mod bazlı temel davranış ve inceleme |
| 35 | Kayıt gelmemesini olay olmaması saymak | Kanıt boşluğunun gizlenmesi | Son olay, kuyruk ve toplayıcı sağlığı | Ayrı kayıt sağlığı alarmı |
| 36 | Saat dilimini saat doğruluğuyla karıştırmak | Yanlış olay sırası | Sapma ve zaman kaynağı kaydı | Belirsizlik aralığı ve özgün zamanın korunması |
| 37 | Her Modbus yazmasını ihlal saymak | Gereksiz alarm yükü | Rol/iş emri ve süreç modu | Yetki bağlamıyla olumlu/olumsuz test |
| 38 | Eski ölçümü normal süreç saymak | Yanlış işletme kararı | Kalite ve veri yaşı | Tazelik kontrolü ve bağımsız gösterge |
| 39 | Bakım istisnasını süresiz susturmak | Kalıcı algılama körlüğü | İstisna bitişi ve sahibi | Süreli susturma, bitişte inceleme |
| 40 | Alarmdan otomatik PLC izolasyonu üretmek | Kontrol/görünürlük kaybı | Müdahale kuralı ve süreç bağımlılıkları | Varlık bazlı yetki, emniyet ve geri dönüş değerlendirmesi |

## Kurtarma, kanıt ve yönetim

| No | Hata / risk | Olası etki | Nasıl fark edilir? | Düzeltme ve kabul |
|---|---|---|---|---|
| 41 | Yedek dosyası var diye kurtarma hazır saymak | Geri dönememe | Uyumluluk ve geri yükleme kanıtı | Bileşen/proje/araç bazlı doğrulama |
| 42 | Yedeği yalnız aynı kimlik/ağ alanında tutmak | Ortak olayda yedek kaybı | Saklama ve erişim bağımlılığı | Bağımsız korunan kopya ve erişim testi |
| 43 | Lisans/anahtar/araç bağımlılığını unutarak yedeklemek | İşlevsel geri yüklemenin engellenmesi | Kurtarma paketinin incelemesi | Güvenli sır erişimi ve uyumlu araç kaydı |
| 44 | Temiz olduğu bilinmeyen sürüme dönmek | Olayın tekrar etmesi | Değişiklik tarihi ve güvenilir sürüm kanıtı | Bilinen iyi durumun gerekçelendirilmesi |
| 45 | RTO/RPO'yu bütün varlıklara aynı vermek | Yanlış kurtarma sırası | Hizmet ve veri kaybı hedefleri | İşlev bazlı hedef, bağımlılık ve saha kabulü |
| 46 | Kanıtın aslı üzerinde çalışmak | Delil bütünlüğü kaybı | Kopyalama ve erişim kaydı | Özgün kayıt, çalışma kopyası ve bütünlük kontrolü |
| 47 | Aynı kaynaktan iki ekranı bağımsız kanıt saymak | Yanlış süreç doğrulaması | Veri soy ağacı | Bağımsız ölçüm/yol veya açık belirsizlik |
| 48 | Emniyet değerlendirmesini izolasyondan sonraya bırakmak | Müdahalenin yeni tehlike yaratması | Olay karar sırası | İlk karardan itibaren işletme/emniyet rolü |
| 49 | Bulgulara sahip ve tarih atamamak | Süresiz açık risk | Risk/iyileştirme kaydı | Sorumlu, hedef tarih ve yeniden değerlendirme |
| 50 | Ürün sertifikasını tüm tesis uygunluğu saymak | Yanlış güvence | Belge model/sürüm/kapsamı | Kurulu sistem, entegrasyon ve işletme kanıtlarını ayrı inceleme |

## Belge alıştırması

Bir kurgusal tesis için beş satır seçin. **THEORY:** risk ve sonucu ayırın. **LAB:** her satıra iki kanıt kaynağı ekleyin. **TEST:** mevcut bilgiyle karar verilemeyen bir alan gösterin. **DEFENSE:** öncelikli düzeltmeyi ve kabul ölçütünü yazın. **REPORT:** bulguları [risk kaydına](../../templates/08-degerlendirme-ve-risk-kaydi.md) bağlayın.

Kabul: beş farklı kök neden seçilmiş; sıklık veya gerçekleşmiş zarar iddiası üretilmemiş; her düzeltmenin sorumlusu, kanıtı ve tarihi tanımlanmış olmalıdır.

## Kaynak ve kapsam

Katalog, [temeller](../01-temeller/01-ot-nedir.md), [envanter](../04-savunma/01-envanter-ve-gorunurluk.md), [erişim](../04-savunma/02-segmentasyon-ve-uzak-erisim.md), [izleme](02-izleme-soc-ve-adli-inceleme.md), [değerlendirme](01-guvenlik-degerlendirmesi-ve-test-plani.md) ve [kurtarma](../04-savunma/05-olay-mudahalesi-ve-kurtarma.md) bölümlerindeki kaynaklı çerçevenin özgün soru setidir. Bir standardın resmî kontrol listesi değildir. Oluşturma: 16.09.2026.
