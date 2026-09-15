# Laboratuvar 1: çevrimdışı kayıt analizi

[Laboratuvarlar](README.md) · [Ana sayfa](../README.md) · [Çözüm anahtarı](cozumler/01-kayit-analizi-cozum.md)

Bu alıştırmada kurgusal “Yeşilova” içme suyu terfi merkezine ait iki günlük kayıtları inceler, ortak bir zaman çizelgesi kurar ve gözlemleri açıklamalarıyla eşleştirirsiniz. Çıktı bir hüküm değil, kanıta bağlı bir ilk değerlendirmedir.

**Veriler tamamen sentetiktir.** Dört CSV dosyası bu depo için elle üretilmiştir. Tesis, kurum, hesap, iş emri ve varlık adları kurgusaldır. Adresler RFC 5737 belgeleme aralıklarından seçilmiştir (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) ve hiçbir gerçek sisteme karşılık gelmez. Dosyalarda çalıştırılabilir komut, araç adı, ürün zafiyeti veya protokol içeriği yoktur.

## 1. Amaç ve kapsam

| Başlık | İçerik |
|---|---|
| Amaç | Farklı kayıt kaynaklarını ortak bir zamana taşımak, kimlik ile yetkiyi eşleştirmek, normal işletme açıklamalarını ayırmak |
| Süre tahmini | Tek kişiyle 60–90 dakika; algılama kartları ayrıntılı doldurulursa 120 dakikaya çıkabilir |
| Ön okuma | [İzleme, algılama ve SOC iş akışı](../docs/04-savunma/03-izleme-ve-algilama.md) |
| Gereken araç | Bir metin editörü veya elektronik tablo uygulaması. Ağ bağlantısı, laboratuvar ortamı, sanal makine veya araç kurulumu gerekmez |
| Girdi | `veri/` klasöründeki dört CSV dosyası |
| Çıktı | Zaman çizelgesi, iki algılama kartı, işletmeye aktarılacak bir cümle, açık sorular listesi |
| Kapsam dışı | Gerçek sisteme bağlanma, tarama, saldırı adımı, ürün önerisi ve kesin suçlama |

Kayıt dosyaları: [uzak erişim](veri/01-uzak-erisim.csv), [mühendislik istasyonu](veri/02-muhendislik-istasyonu.csv), [historian ve proses](veri/03-historian-proses.csv), [ağ gözlemi](veri/04-ag-gozlem.csv).

## 2. Kurgusal ortam özeti

Aşağıdaki bilgiler incelemenin başlangıç bağlamıdır. Kayıtlarla çelişen bir nokta bulursanız çelişkiyi de bulgularınıza yazın.

| Konu | Kurgusal bilgi |
|---|---|
| Saha | Yeşilova terfi merkezi; TERFI-01 ve TERFI-02 depo/terfi noktaları, ARITMA-01 dezenfeksiyon hattı |
| Kontrol varlıkları | SCADA-01, HISTORIAN-01, MUH-IST-01 (mühendislik istasyonu), PLC-TERFI-02, RTU-TERFI-01, RTU-TERFI-02, RTU-TERFI-03 |
| Erişim yolu | Uzak oturumlar ERISIM-GECIDI üzerinden açılır; geçit kaydı ve çok faktörlü kimlik doğrulama kullanılır |
| Tedarikçi hesabı | `tdk.ozmen`, onaylı kaynak aralığı 198.51.100.64/28 olarak kayıtlıdır |
| Diğer hesaplar | `a.duran`, `s.bulut`, `o.kaya`, `n.tekin`, `m.sezer`, `t.arslan` personel/kurumsal; `svc.yedek`, `svc.izleme` hizmet hesabı; `tdk.ercan` analizör tedarikçisi |
| Bakım iş emri | IE-2026-0412, PLC-TERFI-02 proje yükselmesi; onaylı pencere 2026-03-10T22:00+03:00 – 2026-03-11T01:00+03:00 |
| Diğer iş emirleri | IE-2026-0398 saha cihazı değişimi, IE-2026-0401 analizör bakımı, IE-2026-0421 sonradan açılan haberleşme arızası kaydı |
| Envanter durumu | Envanter listesi RTU-TERFI-03 için 192.0.2.53 adresini gösterir; son güncelleme bu kayıt penceresinden öncedir |

## 3. Saat dilimi notu

`01-uzak-erisim.csv` dosyasındaki zaman damgaları **UTC (+00:00)**, diğer üç dosya **+03:00** ofseti kullanır. Karşılaştırmadan önce bütün kayıtları tek bir eksene taşıyın. Ofset yok sayılırsa aynı olay farklı bir güne veya farklı bir pencereye düşebilir. Saatin yanında tarihin de kaydığı satırlar vardır.

## 4. Veri sözlüğü

Sütun adları aksan içermeden yazılmıştır; serbest metin alanları kısaltmalı Türkçedir. Boş bırakılan alanlar `-` işaretiyle gösterilir.

### veri/01-uzak-erisim.csv

Erişim geçidinin oturum kaydı. Zaman damgaları UTC.

| Sütun | Anlamı |
|---|---|
| zaman_damgasi | Olayın geçit saatiyle kaydı; ofset +00:00 |
| kayit_no | Dosya içi sıra numarası (UE-nnnn) |
| oturum_kimligi | Oturumu izlemeye yarayan kimlik; diğer dosyalarda aynı değerle görünür |
| kullanici | Oturumu açan hesap |
| hesap_turu | personel, kurumsal, tedarikci, hizmet, sistem |
| kaynak_adres | Bağlantının geldiği adres |
| hedef_bolge | Erişilen bölge (OT-DMZ, OT-MUHENDISLIK, gecit) |
| hedef_varlik | Erişilen sistem |
| olay | oturum_acildi, oturum_kapandi, oturum_tamamlandi, bolge_gecisi, giris_reddedildi, talep_reddedildi, onay_kaydi, sure_uzatma_onayi, saglik_kaydi |
| sure_dk | Geçit tarafından ölçülen oturum süresi; yalnızca kapanış ve özet kayıtlarında dolu |
| is_emri | Oturumun bağlandığı iş emri; boşsa `-` |
| cok_faktorlu | Çok faktörlü doğrulamanın sonucu |
| sonuc | basarili veya reddedildi |

`oturum_tamamlandi`, kısa oturumlar için geçidin ürettiği tek satırlık özet kaydıdır; açılış ve kapanış ayrı satır olarak yazılmaz.

### veri/02-muhendislik-istasyonu.csv

MUH-IST-01 üzerindeki kullanıcı işlem kaydı. Zaman damgaları +03:00.

| Sütun | Anlamı |
|---|---|
| zaman_damgasi | İstasyon saatiyle kayıt |
| kayit_no | Dosya içi sıra numarası (MI-nnnn) |
| oturum_kimligi | Uzak oturumlarda geçit kimliği, yerel oturumlarda istasyon kimliği |
| kullanici | İşlemi yapan hesap |
| istasyon | Kayıt üreten iş istasyonu |
| islem | Yapılan işlem adı |
| hedef_varlik | İşlemin yöneldiği varlık |
| proje_surumu | Görüntülenen, karşılaştırılan veya yüklenen proje sürüm etiketi |
| is_emri | İşlemin bağlandığı iş emri |
| sonuc | İşlemin sonucu |
| aciklama | Kullanıcı veya sistem notu |

### veri/03-historian-proses.csv

Ölçüm, ekran gösterimi, saha okuması ve proses alarmı kayıtları. Zaman damgaları +03:00.

| Sütun | Anlamı |
|---|---|
| zaman_damgasi | Kaydın alındığı an |
| kayit_no | Dosya içi sıra numarası (HP-nnnn) |
| kaynak | historian, hmi_gosterim, saha_olcum, alarm |
| olcum_noktasi | Ölçümün ait olduğu nokta veya varlık |
| etiket | Ölçüm etiketi veya alarm adı |
| deger | Sayısal ölçüm ya da sürüm etiketi |
| birim | Ölçü birimi |
| kalite_bayragi | iyi, belirsiz, eski, gosterilmiyor |
| guncelleme_yasi_sn | Değerin kaç saniyedir yenilenmediği |
| aciklama | Kayıt notu |

`hmi_gosterim` satırları operatör ekranında görünen değeri anlatır. Bu ekranda kalite bayrağı alanı bulunmaz.

### veri/04-ag-gozlem.csv

Pasif ağ gözleminin özet kayıtları ve toplayıcının kendi sağlık satırları. Zaman damgaları +03:00.

| Sütun | Anlamı |
|---|---|
| zaman_damgasi | Gözlem penceresinin başlangıcı |
| kayit_no | Dosya içi sıra numarası (AG-nnnn) |
| gozlem_dk | Özetlenen pencerenin uzunluğu |
| kaynak_varlik, kaynak_adres | Konuşan uçlardan biri |
| hedef_varlik, hedef_adres | Konuşan uçlardan diğeri |
| trafik_turu | telemetri, izleme_verisi, dosya_aktarimi, yonetim_oturumu, muhendislik_trafigi, tanilama_trafigi, zaman_senkronizasyonu, kayit_aktarimi, saglik_kaydi |
| cift_durumu | bilinen, yeni, artis, azalis, kesildi, yeniden_kuruldu |
| envanter_kaydi | Çiftin envanterde karşılığı var mı? |
| aciklama | Gözlem notu |

Paket içeriği, port ve protokol ayrıntısı bu dosyada yoktur. Kayıt yalnızca hangi uçların konuştuğunu ve akışın durumunu gösterir.

## 5. Görev adımları

### Adım 1 — ortak eksende zaman çizelgesi

Dört dosyadaki kayıtları tek bir tabloda birleştirin. Sütunlar: yerel saat (+03:00), kaynak dosya, kayıt numarası, gözlem. Önce bütün zaman damgalarını aynı ofsete çevirin; çevirdiğiniz satırların yanına özgün değeri de yazın.

**Tamamlanma ölçütü:** Her satır tek bir zaman eksenine taşınmış; UTC kayıtlarının yerel karşılığı ve gerekiyorsa değişen tarih açıkça yazılmıştır.

### Adım 2 — kimlik ve yetki eşleştirme

Uzak oturumları hesap, kaynak adres, hedef bölge ve iş emrine göre gruplayın. Her oturum için şu soruları yanıtlayın: hesap hangi türde, kaynak adres kayıtlı aralıkta mı, iş emri var mı, oturum onaylı pencerede mi?

**Tamamlanma ölçütü:** Tedarikçi hesabına ait oturumların tamamı listelenmiş; her biri için onaylı kapsam içinde mi (iş emri, kaynak adres ve bakım penceresi) kararı ve bu kararın dayandığı satır numarası yazılmıştır. Bir kaydın tek başına yetmediği yerde hangi bilginin eksik olduğu yazılır.

### Adım 3 — normal işletme açıklamalarını ayırma

Kayıtların bir bölümü rutin işletmeyle açıklanır: vardiya oturumları, planlı yedekleme, zaman senkronizasyonu, onaylı bakım ve saha işleri. Dikkat çeken her gözlem için “en olası normal açıklama” ve “bu açıklamayı destekleyen kayıt” sütunlarını doldurun. Normal açıklaması olan bir gözlemi kapatmadan önce hangi kaydın bunu desteklediğini gösterin.

**Tamamlanma ölçütü:** En az bir gözlem, siber olmayan bir açıklamayla ve o açıklamayı destekleyen en az iki bağımsız kayıt satırıyla eşleştirilmiştir.

### Adım 4 — kanıt boşluğunu işaretleme

Kayıt akışının kesildiği aralığı bulun. Kesintinin başlangıcını, bitişini ve etkilediği soruları yazın. Bu aralıkta olup bitenler hakkında hangi ifadeleri kuramayacağınızı da belirtin.

**Tamamlanma ölçütü:** Boşluğun süresi ve nedeni hakkındaki kanıt ayrı ayrı yazılmış; boşluk nedeniyle belirsiz kalan en az bir soru listelenmiştir.

### Adım 5 — iki algılama kartı yazma

[Algılama kartı şablonunu](../templates/03-algilama-karti.md) kullanarak iki kart hazırlayın: biri erişim ve yetki gözlemi, diğeri ölçüm güvenilirliği gözlemi için. Bu alıştırmada şablonun bütün alanları değil, aşağıdaki kısaltılmış alt kümesi doldurulur ve alan adları şablondaki adlarla birebir yazılır: hipotez, veri kaynağı ve kapsamı, birleştirilecek bağlam, beklenen normal açıklamalar, ilk üç doğrulama adımı, işletmeye aktarım kuralı ve karar sahibi. Kartlar araç yapılandırması değil, analiz tasarımıdır.

**Tamamlanma ölçütü:** İki kartın da “beklenen normal açıklamalar” alanı doludur ve “işletmeye aktarım kuralı ve karar sahibi” alanı kimin neyi teyit edeceğini söyler.

### Adım 6 — işletmeye aktarılacak ilk cümle

SOC'un vardiya amirine söyleyeceği ilk cümleyi yazın. Cümle; sahayı, gözlemi, kanıtın sınırını ve istenen teyidi içersin. Kanıtın ötesine geçen ifadeler kullanmayın. [Olay ve kurtarma şablonunun](../templates/04-olay-ve-kurtarma.md) ilk bölümü bu cümleyi kaydetmek için kullanılabilir.

**Tamamlanma ölçütü:** Cümle iki satırı geçmiyor; doğrulanmış olan ile doğrulanmamış olanı ayırıyor ve bir teyit talebiyle bitiyor.

## 6. Çalışma kağıdı

Aşağıdaki liste ilerlemeyi izlemek içindir.

- [ ] Bütün kayıtlar [yerel saat] eksenine taşındı.
- [ ] Tedarikçi hesabının oturumları iş emriyle karşılaştırıldı.
- [ ] Envanterde karşılığı olmayan iletişim çifti işaretlendi.
- [ ] Ölçüm tazeliği sorunu için bağımsız bir kayıt arandı.
- [ ] Kanıt boşluğu süresi ve etkisi yazıldı.
- [ ] İki algılama kartı dolduruldu: [kart adı 1], [kart adı 2].
- [ ] İşletmeye aktarım cümlesi yazıldı ve ikinci bir kişiye okutuldu.
- [ ] Açık sorular listesi ve doğrulama sahibi belirlendi.

## 7. İlgili bölümler

- [İzleme, algılama ve SOC iş akışı](../docs/04-savunma/03-izleme-ve-algilama.md): veri katmanları ve algılama kartı yaklaşımı.
- [MITRE ATT&CK for ICS ve savunma eşleştirmeleri](../docs/03-tehdit-modelleme/02-mitre-attack-ics.md): gözlenen davranışı ortak sözlükle adlandırmak için.
- [Varlık envanteri ve pasif görünürlük](../docs/04-savunma/01-envanter-ve-gorunurluk.md): envanterde bulunmayan iletişim çiftini yorumlamak için.
- [Su ve atıksu sistemlerinde OT güvenliği](../docs/02-sektorler/01-su-ve-atiksu.md): terfi merkezinin süreç bağlamı.

## 8. Çözüm anahtarı

Çözümü açmadan önce altı adımı kendi yorumunuzla tamamlayın; alıştırmanın değeri sonucu bilmekte değil, kanıt ile yorumu ayırmayı denemektedir. Hazır olduğunuzda [çözüm anahtarı ve değerlendirme ölçütü](cozumler/01-kayit-analizi-cozum.md) dosyasını açın.

## Kaynak ve kapsam notu

Bu alıştırmanın senaryosu, dört CSV dosyası, veri sözlüğü, adım sırası ve çalışma kağıdı bu deponun **özgün eğitim sentezidir**. Dışarıdan alınmış bir olay kaydı, gerçek bir tesis verisi veya lisanslı bir eğitim materyali içermez. Kayıt katmanlarının ne gösterip ne göstermediğine ilişkin çerçeve [izleme ve algılama bölümünde](../docs/04-savunma/03-izleme-ve-algilama.md) kaynaklarıyla birlikte açıklanmıştır.

Alıştırma bir denetim yöntemi, adli inceleme prosedürü veya uygunluk kanıtı değildir. Gerçek bir olayda kayıt toplama, saklama ve inceleme sırası kurumun olay planına ve hukuki yükümlülüklerine göre belirlenir.
