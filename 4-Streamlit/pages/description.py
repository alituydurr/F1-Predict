import streamlit as st
import matplotlib.pyplot as plt

# Sayfa başlığı ve açıklama
st.title("Formula 1 Tahmin ve Analiz Aracı")
st.subheader("F1 Strateji Analizi ve Pit Stop Optimizasyonu")
st.markdown("""
Bu uygulama, Formula 1 yarış verilerini analiz etmek ve yarış sonucunu tahmin etmek amacıyla geliştirilmiştir. 
Makine öğrenimi modelleri ve görselleştirme için kullanılan verileri sayfa sonundaki bağlantılarda bulabilirsiniz.

### Projenin Amacı:
- Takımların strateji analizine destek olmak.
- Pit stop sürelerini optimize etmek.
- Yarış performansını modellemek.
""")


st.markdown("""
## Veri Hakkında

Bu veri seti, Formula 1 yarışlarıyla ilgili ayrıntılı bilgileri içermektedir. Yarışa özgü detaylar, sürücü performansları ve pit stop verilerini kapsamaktadır. Veri setindeki sütunların açıklamaları aşağıda verilmiştir:

| Sütun Adı         | Açıklama                                                                  |
|-------------------|---------------------------------------------------------------------------|
| `raceId`          | Her bir yarış için benzersiz bir kimlik numarası.                         |
| `year`            | Yarışın gerçekleştiği yıl.                                               |
| `round`           | Sezon içindeki yarışın tur numarası.                                     |
| `circuitId`       | Yarışın yapıldığı pistin benzersiz kimlik numarası.                      |
| `driverId`        | Yarışa katılan sürücünün benzersiz kimlik numarası.                      |
| `constructorId`   | Sürücünün takımı (konstrüktör) için benzersiz kimlik numarası.           |
| `pit_stop_time`   | Sürücünün yarıştaki toplam pit stop süresi (milisaniye cinsinden).       |
| `positionOrder`   | Sürücünün yarıştaki bitiş sırasındaki pozisyonu.                         |
| `grid`            | Sürücünün yarışa başladığı grid pozisyonu.                               |
| `points`          | Sürücünün yarış performansı için aldığı puanlar.                         |
| `laps`            | Sürücünün yarışta tamamladığı toplam tur sayısı.                         |
| `statusId`        | Sürücünün yarış durumunu temsil eden benzersiz kimlik numarası (ör. bitirdi, yarış dışı kaldı). |

### Temel İstatistikler
- **Satır Sayısı**: 7.979  
- **Sütun Sayısı**: 12  

Bu veri seti, Formula 1 yarışlarının farklı yönlerini kapsamlı bir şekilde analiz etmek için kullanılabilir. Strateji değerlendirme, performans trendleri ve pit stop optimizasyonu gibi çalışmalar için oldukça uygundur.


""")

st.subheader("Veri dosyalarının linkleri")
st.markdown("""
- github repo csv linki
- www.google.com
""")

st.subheader("Daha fazla uygulama incelemek için takip linkleri")
st.markdown(""" 
-medium linki
""")