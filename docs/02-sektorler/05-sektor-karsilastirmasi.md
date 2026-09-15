# Sektör karşılaştırması

Bu tablo sektör bölümlerinin özgün karşılaştırmasıdır; evrensel tasarım veya tehlike sınıflandırması değildir. Kaynaklı teknik ayrıntılar ilgili sektör belgelerindedir.

| Boyut | [Su / atıksu](01-su-ve-atiksu.md) | [Elektrik](02-elektrik-ve-enerji.md) | [Raylı](03-rayli-sistemler.md) | [Telekom sahası](04-telekom-ve-baz-istasyonlari.md) |
|---|---|---|---|---|
| Temel hizmet | Suyun sağlanması ve atıksuyun işlenmesi | Gücün üretilmesi, iletilmesi ve dağıtılması | Trenlerin emniyetli ve düzenli hareketi | Haberleşme ve saha altyapısının sürekliliği |
| Fiziksel değişken | Seviye, debi, basınç, kalite | Gerilim, akım, frekans, kesici durumu | Konum, hız, hat doluluğu, makas durumu | Güç, sıcaklık, akü ve saha çevresi |
| OT odağı | Pompalar, vanalar, süreç kontrolü | Koruma ve kontrol, saha telemetrisi | Sinyalizasyon, cer gücü, tünel/istasyon sistemleri | Güç, soğutma ve çevre izleme; RAN/core ayrıca telekom mimarisidir |
| Kritik güven sorusu | Ölçüm doğru ve güncel mi? | Komut ve koruma ayarı yetkili mi? | Hareket yetkisi ve emniyet varsayımları korunuyor mu? | Yönetim ve saha destek altyapısı birlikte güvenilir mi? |
| Yanlış çıkarım | HMI erişimi her zaman su kalitesinin bozulduğunu gösterir | IT kesintisi doğrudan koruma rölesi ihlalidir | Trenlerin durması emniyet kontrolünün aşıldığını gösterir | Bütün baz istasyonu klasik PLC/SCADA sistemidir |
| Doğrulama ihtiyacı | Bağımsız ölçüm, süreç kayıtları, saha teyidi | Koruma kayıtları, saha durumu, onaylı ayarlar | İşletme kayıtları, yetki durumu, mühendislik doğrulaması | Ağ yönetim kayıtları ile güç/çevre olaylarının birlikte incelenmesi |

## Aynı kontrol neden farklı uygulanır?

**Uzak erişim:** Dört sektörde de kimlik, kapsam ve kayıt önemlidir. Ancak saha sayısı, bağlantı kalitesi, çalışma vardiyası ve müdahale yetkisi farklıdır. Sürekli bağlantı kurulamayan sahada tasarım yerel işlev ve kontrollü yeniden bağlanmayı da kapsar.

**İzolasyon:** Kurumsal sunucuyu ağdan çıkarmakla saha kontrol ağını ayırmak aynı operasyon kararı değildir. Kontrol ve emniyet işlevlerinin yeni durumda nasıl davranacağı kanıtlanmadan ortak “bütün bağlantıları kapat” kuralı oluşturulmaz.

**Kurtarma:** Sunucunun açılması tek başına hizmetin doğru çalıştığını göstermez. Su sisteminde ölçüm ve saha durumu; elektrikte koruma/ayar ve sistem işletmesi; raylı sistemlerde emniyet ve hareket yetkisi; telekomda ağ işlevi ile saha güç/soğutması birlikte doğrulanır.

## Karşılaştırmalı alıştırma

Kurgusal olarak bir bakım sağlayıcısının hesabında şüpheli oturum bildirildiğini düşünün. Her sektör için aynı soruları yanıtlayın: Hangi hedefe gerçekten erişilmiş, hangi yetki verilmiş, değişiklik kanıtı var mı, hizmette gözlenen belirti ne, hangi normal bakım bunu açıklayabilir, erişimi sınırlama kararı kimde? Sonuçları [tehdit modeli şablonuna](../../templates/02-tehdit-modeli.md) yazın.
