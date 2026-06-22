# Genetik Algoritma ile Depo Yerleşim Optimizasyonu

Bu modül, bir tekstil deposunda kumaş toplarının raflara optimal yerleştirilmesi için geliştirilmiştir.

## Amaç
Depo alanı verimliliğini artırmak, raf kapasitelerini optimize etmek, birlikte hareket eden kumaşları yakın konumlandırmak ve toplama sürelerini kısaltmak.

## Nasıl Uygulandı?
1. **Genetik Algoritma Tasarımı**: Biyolojik evrim prensiplerine dayalı optimizasyon
2. **Çok Kriterli Fitness Fonksiyonu**: Birden fazla kısıt ve hedefi aynı anda değerlendirme
3. **Kısıt Yönetimi**: Depo fiziksel sınırlarını ve operasyonel kuralları dikkate alma

## Gerekli Veriler
1. **Kumaş Özellikleri**
   - Kumaş cinsi, rengi, tedarikçisi
   - Top sayısı ve kilogram değerleri
   - ABC sınıflandırması (A, B, C kategorileri)
   - Hareket sıklığı ve devir hızı

2. **Depo Yapısı**
   - Raf sayısı ve kapasiteleri
   - Kat yükseklikleri ve erişilebilirlik seviyeleri
   - Alan bölümleri (ön/arka/orta)

3. **Operasyonel Kurallar**
   - Birliktelik analizi sonuçları
   - Tercih edilen raf puanları
   - Minimum/maksimum doluluk oranları

## İşleyiş Adımları
1. Rastgele başlangıç popülasyonu oluşturulur (farklı yerleşim senaryoları)
2. Her bireyin fitness değeri hesaplanır (uygunluk puanı)
3. En iyi bireyler seçilerek yeni nesil oluşturulur
4. Çaprazlama (crossover) ile yeni çözümler üretilir
5. Mutasyon ile çeşitlilik sağlanır
6. Belirlenen iterasyon sayısına veya uygun çözüme ulaşılana kadar devam edilir

## Fitness Fonksiyonu Bileşenleri
1. **Kapasite Kısıtı**: Raf kapasitesinin aşılmaması (500 kg sınır)
2. **Doluluk Dengesi**: Raf doluluk oranının %10-90 aralığında olması
3. **ABC Sınıfı Uyumu**: A sınıfı kumaşların alt kat-ön alana, C sınıfı kumaşların üst kat-arka alana yerleştirilmesi
4. **Birliktelik Puanı**: Birlikte işlem gören kumaşların yakın konumlandırılması
5. **Parçalanma Cezası**: Aynı kumaşın farklı raflara dağılmasının engellenmesi
6. **Erişilebilirlik Bonusu**: Yüksek devirli ürünlerin kolay erişilebilir raflara yerleştirilmesi

## Çıktılar
1. **Optimal Yerleşim Planı**
   - Hangi kumaşın hangi rafta olduğu
   - Raf doluluk oranları ve kapasite kullanımı
   - Yerleşim dengesi ve verimlilik metrikleri

2. **Performans İyileştirmeleri**
   - Raf sayısında azalma: 654 → 648 (%10.2 daha az raf)
   - Etkin kullanılan raf oranı: %68.8 → %62.3
   - Hiçbir rafta kapasite aşımı olmaması
   - Dengeli yük dağılımı

3. **Operasyonel Faydalar**
   - A sınıfı kumaşların öncelikli erişim alanlarına yerleştirilmesi
   - Toplama rotalarının kısalması
   - Stok takip kolaylığının artması
   - İş gücü verimliliğinde iyileşme

## Teknik Detaylar
- **Popülasyon Büyüklüğü**: 100-500 birey
- **Iterasyon Sayısı**: 1000-5000 nesil
- **Seçim Yöntemi**: Turnuva seçimi
- **Çaprazlama Oranı**: %70-80
- **Mutasyon Oranı**: %1-5
- **Durdurma Kriteri**: Belirli fitness değerine ulaşma veya maksimum iterasyon

---

# Genetic Algorithm for Warehouse Layout Optimization

This module was developed for optimal placement of fabric rolls on racks in a textile warehouse.

## Objective
To increase warehouse space efficiency, optimize rack capacities, position frequently co-moved fabrics close together, and reduce picking times.

## How It Was Implemented?
1. **Genetic Algorithm Design**: Optimization based on biological evolution principles
2. **Multi-Criteria Fitness Function**: Simultaneous evaluation of multiple constraints and objectives
3. **Constraint Management**: Consideration of warehouse physical limits and operational rules

## Required Data
1. **Fabric Properties**
   - Fabric type, color, supplier
   - Number of rolls and weight values
   - ABC classification (A, B, C categories)
   - Movement frequency and turnover rate

2. **Warehouse Structure**
   - Number of racks and their capacities
   - Level heights and accessibility levels
   - Area divisions (front/back/middle)

3. **Operational Rules**
   - Association analysis results
   - Preferred rack scores
   - Minimum/maximum occupancy rates

## Process Steps
1. Random initial population is created (different layout scenarios)
2. Fitness value of each individual is calculated (suitability score)
3. Best individuals are selected to create a new generation
4. New solutions are generated through crossover
5. Diversity is ensured through mutation
6. Process continues until predetermined iteration count or suitable solution is reached

## Fitness Function Components
1. **Capacity Constraint**: Not exceeding rack capacity (500 kg limit)
2. **Occupancy Balance**: Rack occupancy rate between 10-90%
3. **ABC Class Compliance**: Class A fabrics placed in lower level-front areas, Class C fabrics in upper level-back areas
4. **Association Score**: Positioning frequently co-processed fabrics close together
5. **Fragmentation Penalty**: Preventing the same fabric from being distributed across different racks
6. **Accessibility Bonus**: Placing high-turnover products in easily accessible racks

## Outputs
1. **Optimal Layout Plan**
   - Which fabric is in which rack
   - Rack occupancy rates and capacity utilization
   - Layout balance and efficiency metrics

2. **Performance Improvements**
   - Reduction in rack count: 654 → 648 (10.2% fewer racks)
   - Effectively used rack ratio: 68.8% → 62.3%
   - No capacity exceedance in any rack
   - Balanced load distribution

3. **Operational Benefits**
   - Placement of Class A fabrics in priority access areas
   - Reduction in picking route lengths
   - Increased stock tracking ease
   - Improvement in workforce efficiency

## Technical Details
- **Population Size**: 100-500 individuals
- **Iteration Count**: 1000-5000 generations
- **Selection Method**: Tournament selection
- **Crossover Rate**: 70-80%
- **Mutation Rate**: 1-5%
- **Stopping Criteria**: Reaching specific fitness value or maximum iteration
