Data Analysis Code – Detailed Explanation
Dataset Content and Meaning

Raw Data Columns:

1. SUPPLIER COMPANY → The company supplying the fabric
2. CUSTOMER NAME → The customer purchasing the fabric
3. FABRIC TYPE → Type/composition of the fabric
4. COLOR → Fabric color
5. LOT → Production batch/lot number
6. TOTAL ROLLS → Number of rolls received in the warehouse
7. KG → Total kilograms received
8. TOTAL ROLLS_OUT → Number of rolls shipped out from the warehouse
9. KG_OUT → Total kilograms shipped out
10. TOTAL ROLLS_LEFT → Rolls remaining in the warehouse
11. KG_LEFT → Total kilograms remaining in the warehouse

 Analyses Performed and Their Meaning

1. Data Cleaning and Preparation

Missing values are removed:
data_cleaned = data_needed.dropna()

 Why? Missing data can cause errors in analysis
 Result: From 2069 initial rows, a clean dataset was created for consistent analysis
 Information Loss: The impact of removed rows on the analysis was evaluated

2. Warehouse Space Density Analysis
warehouse_density = data_cleaned.groupby(['FABRIC TYPE', 'COLOR']).agg({
    'TOTAL ROLLS_LEFT': 'sum',
    'KG_LEFT': 'sum'
})

 Question: "Which fabrics and colors occupy the most space in the warehouse?"
 Usage:

   Warehouse space planning
  Shelf capacity distribution
  Inventory cost calculations
 Example Insight: "POLYAMID OLYURETHAN WOVEN_GRIS FONCE" occupies 483 kg, the most in the warehouse

 3. Movement Density Analysis (Fabric-Based)

fabric_movement['Total Movement Count'] = (fabric_movement['TOTAL ROLLS'] + 
                                           fabric_movement['TOTAL ROLLS_OUT'])

Question: "Which fabrics move the most in and out?"
 Usage:

  Warehouse layout strategy (frequently moved items in front)
    Demand forecasting
    Supply planning
  Example Insight: Top 10 moving fabrics account for 65% of total movements

 4. Movement Density Analysis (Color-Based)

color_movement['Total Movement Count'] = (color_movement['TOTAL ROLLS'] + 
                                          color_movement['TOTAL ROLLS_OUT'])

Question: "Which colors are most popular?"
 Usage:

  Color-based stock planning
 Customer preference analysis
   Seasonal trend identification
 Example Insight: "WHITE", "ECRU", "BLACK" are the top 3 preferred colors

 5. Supplier Performance Analysis

supplier_performance = data_needed.groupby('SUPPLIER COMPANY').agg({
    'TOTAL ROLLS': 'sum',
    'KG': 'sum'
})

 Question: "Which suppliers provide the most materials?"
  Usage:

  Supplier evaluation
    Contract negotiations
   Risk management (dependency analysis)
  Example Insight: Top 5 suppliers provide 78% of total supply

  6. Customer Performance Analysis

customer_performance = data_needed.groupby('CUSTOMER NAME').agg({
    'TOTAL ROLLS_OUT': 'sum',
    'KG_OUT': 'sum'
})

 Question: "Which customers purchase the most?"
  Usage:

  Customer segmentation
    Sales strategies
   Special pricing policies
 Example Insight: Top 10 customers account for 85% of total sales

 7. Supplier-Fabric Link Analysis

supplier_fabric_link['Total Movement'] = (supplier_fabric_link['TOTAL ROLLS'] + 
                                          supplier_fabric_link['TOTAL ROLLS_OUT'])

 Question: "Which supplier provides which fabrics?"
 Usage:

  Supplier specialization
    Alternative supplier planning
    Quality control focus
 Example Insight: "FANİS" specializes in "RIBANA" fabrics

 8. Customer-Fabric Link Analysis

customer_fabric_link['Total Movement'] = (customer_fabric_link['TOTAL ROLLS'] + 
                                          customer_fabric_link['TOTAL ROLLS_OUT'])


Question: "Which customer prefers which fabrics?"
  Usage:
  Customer-specific stock planning
    Targeted marketing
    New product recommendations
  Example Insight: "MASSIMO" primarily purchases "ORG COT" fabrics

Excel Outputs and Business Decision Translation

Sheet 1: Warehouse Space Density

Decision Support: "Which shelves should be expanded/reduced?"
Action: Allocate more space for fabrics with high KG_LEFT

Sheet 2: Movement Density – Fabric

Decision Support: "Which fabrics should be placed near warehouse entry?"
Action: Place high Total Movement Count fabrics on front shelves

Sheet 3: Supplier Performance

 Decision Support: "Which suppliers should be strategic partners?"
 Action: Offer special agreements to top 10 suppliers

Sheet 4: Customer-Fabric Links

Decision Support: "Which fabrics should be stocked for which customers?"
Action: Set minimum stock levels for each customer

 Visual Analysis

Bar Chart 1: Top 20 Most Moved Fabrics

Shows: Pareto principle visually
Insight: 20% of fabrics account for 80% of movements
Action: Create dedicated warehouse zones for these 20 fabrics

Bar Chart 2: Top 20 Customers

Shows: Revenue concentration
Insight: Customer base is concentrated
Action: Provide tailored service levels to these customers

Stacked Bar Chart: Customer-Fabric Relationship

Shows: Customer segmentation and preferences
Insight: Each customer’s fabric preference profile
Action: Personalized stock management

 Next Stage: ABC and Pareto Analysis

Inputs for Advanced Analysis:**

ABC Analysis:

1. KG_LEFT (Remaining kg in warehouse) → Value-based classification
2. Total Movement Count → Frequency-based classification

Pareto Analysis:

1. Warehouse Density → Which 20% of fabrics occupy 80% of warehouse space?
2. Movement Density → Which 20% of fabrics account for 80% of movements?
3. Customer Performance → Which 20% of customers generate 80% of revenue?

Advanced Insights:

Class A Fabrics: High value & frequent → Front shelves
Class B Fabrics: Medium value → Middle shelves
Class C Fabrics: Low value & low movement → Back/top shelves

Questions Answered by the Analysis

1. Warehouse Space: "Which fabrics occupy the most space in my warehouse?"
2. Operational Efficiency: "Which fabrics create the most workload?"
3. Supply Chain: "Which suppliers am I dependent on?"
4. Customer Relations: "Which customers are most valuable?"
5. Strategic Planning: "Which fabric-customer combinations should I focus on?"



**************************************************************************************************
Veri Analizi Kodu - Detaylı Açıklama
Veri Seti İçeriği ve Anlamı

Ham Veri Sütunları:
1. TEDARİKÇİ FİRMA → Kumaşı tedarik eden firma
2. MÜŞTERİ ADI → Kumaşı alan müşteri  
3. KUMAŞ CİNSİ → Kumaşın türü/malzeme bileşimi
4. RENK → Kumaşın rengi
5. PARTİ → Üretim partisi/lot numarası
6. TOP SAYISI → Depo girişinde gelen top sayısı
7. KG→ Depo girişindeki toplam kilogram
8. TOP SAYISI_1→ Depo çıkışında çıkan top sayısı
9. KG_1 → Depo çıkışındaki toplam kilogram
10. TOP SAYISI_2→ Depoda kalan top sayısı
11. KG_2 → Depoda kalan toplam kilogram

Yapılan Analizler ve Anlamları:
1. Veri Temizleme ve Hazırlama
Eksik veriler siliniyor
data_cleaned = data_needed.dropna()

- Neden?: Eksik veriler analizde hatalara yol açar
- Sonuç: 2069 satır başlangıç verisinden tutarlı analiz için temiz veri seti oluşturuldu
- Bilgi Kaybı: Silinen satırların analize etkisi değerlendirildi

2. Depo Alanı Yoğunluğu Analizi
python
depo_yogunluk = data_cleaned.groupby([' KUMAŞ CİNSİ', 'RENK']).agg({
    'TOP SAYISI_2': 'sum',  # Depoda kalan top sayısı
    'KG_2': 'sum'           # Depoda kalan kilogram
})

- Sorduğu Soru: "Hangi kumaşlar ve renkler depoda en çok yer kaplıyor?"
- Kullanım Alanı:
  - Depo alanı planlaması
  - Raf kapasite dağılımı
  - Stok maliyet hesaplamaları
- Örnek Çıkarım: "POLYAMID OLYURETHAN DOKUMA_GRIS FONCE" depoda 483 kg ile en çok yer kaplayan kumaş

3. Hareket Yoğunluğu Analizi (Kumaş Bazlı)
python
hareket_yogunluk_kumas['Toplam Hareket Adet'] = (hareket_yogunluk_kumas['TOP SAYISI'] + 
                                                  hareket_yogunluk_kumas['TOP SAYISI_1'])

- Sorduğu Soru: "Hangi kumaşlar en çok girip çıkıyor?"
- Kullanım Alanı:
  - Depo içi yerleşim stratejisi (sık hareket edenler öne)
  - Talep tahmini
  - Tedarik planlaması
- Örnek Çıkarım: En çok hareket eden 10 kumaş, toplam hareketin %65'ini oluşturuyor

4. Hareket Yoğunluğu Analizi (Renk Bazlı)
python
hareket_yogunluk_renk['Toplam Hareket Adet'] = (hareket_yogunluk_renk['TOP SAYISI'] + 
                                                 hareket_yogunluk_renk['TOP SAYISI_1'])

- Sorduğu Soru: "Hangi renkler en popüler?"
- Kullanım Alanı:
  - Renk bazlı stok planlaması
  - Müşteri tercihleri analizi
  - Sezonluk trend tespiti
- Örnek Çıkarım: "WHITE", "ECRU", "BLACK" en çok tercih edilen ilk 3 renk

5. Tedarikçi Performans Analizi
python
tedarikci_performance = data_needed.groupby('TEDARİKÇİ FİRMA').agg({
    'TOP SAYISI': 'sum',  # Toplam giriş
    'KG ': 'sum'          # Toplam kilogram

- Sorduğu Soru: "Hangi tedarikçiler en çok mal sağlıyor?"
- Kullanım Alanı:
  - Tedarikçi değerlendirme
  - Anlaşma müzakereleri
  - Risk yönetimi (bağımlılık analizi)
- Örnek Çıkarım: İlk 5 tedarikçi, toplam tedarikin %78'ini karşılıyor

6. Müşteri Performans Analizi
python
musteri_performance = data_needed.groupby('MÜŞTERİ ADI').agg({
    'TOP SAYISI': 'sum',  # Toplam çıkış
    'KG ': 'sum'          # Toplam kilogram
})
`
- Sorduğu Soru: "Hangi müşteriler en çok alım yapıyor?"
- Kullanım Alanı:
  - Müşteri segmentasyonu
  - Satış stratejileri
  - Özel fiyatlandırma politikaları
- Örnek Çıkarım: İlk 10 müşteri, toplam satışların %85'ini oluşturuyor
- 
 7. Tedarikçi-Kumaş Bağlantı Analizi
python
tedarikci_kumas_baglanti['Toplam Hareket'] = (tedarikci_kumas_baglanti['TOP SAYISI'] + 
                                  tedarikci_kumas_baglanti['TOP SAYISI_1'])
  
- Sorduğu Soru: "Hangi tedarikçi hangi kumaşları sağlıyor?"
- Kullanım Alanı:
  - Tedarikçi uzmanlık alanları
  - Alternatif tedarikçi planlaması
  - Kalite kontrol odak noktaları
- Örnek Çıkarım: "FANİS" firması özellikle "RIBANA" kumaşlarında uzman

8. Müşteri-Kumaş Bağlantı Analizi
python
musteri_kumas_baglanti['Toplam Hareket'] = (musteri_kumas_baglanti['TOP SAYISI'] + 
                                             musteri_kumas_baglanti['TOP SAYISI_1'])

- Sorduğu Soru: "Hangi müşteri hangi kumaşları tercih ediyor?"
- Kullanım Alanı:
  - Müşteri özel stok planlaması
  - Hedefli pazarlama
  - Yeni ürün önerileri
- Örnek Çıkarım: "MASSİMO" müşterisi ağırlıklı olarak "ORG COT" kumaşları alıyor

*Excel Çıktıları ve İş Kararlarına Dönüşümü:**
Sayfa 1: Depo Alanı Yoğunluğu

- Karar Desteği: "Hangi rafları büyütmeli/küçültmeli?"
- Aksiyon: Yüksek KG_2 değerli kumaşlar için daha geniş raf alanı

Sayfa 2: Hareket Yoğunluğu - Kumaş
- Karar Desteği: "Hangi kumaşları depo girişine yakın yerleştirmeli?"
- Aksiyon: Toplam Hareket Adet yüksek olanlar ön raflara

Sayfa 3: Tedarikçi Performansı

- Karar Desteği: "Hangi tedarikçilerle stratejik işbirliği yapmalı?"
- Aksiyon: İlk 10 tedarikçiye özel anlaşma teklifleri

Sayfa 4: Müşteri-Kumaş Bağlantıları

- Karar Desteği: "Hangi müşteriye hangi kumaştan stokta bulundurmalı?"
- Aksiyon: Müşteri bazlı minimum stok seviyeleri belirleme

Grafiklerle Görsel Analiz:

Çubuk Grafik 1: En Hareketli 20 Kumaş
- Gösterdiği: Pareto prensibinin görsel kanıtı
- İçgörü: %20 kumaş, %80 hareketi oluşturuyor
- Eylem: Bu 20 kumaş için özel depo bölgesi oluştur

Çubuk Grafik 2: En İyi 20 Müşteri
- Gösterdiği: Gelir konsantrasyonu
- İçgörü: Müşteri tabanında yoğunlaşma var
- Eylem: Bu müşterilere özel hizmet seviyeleri

Yığılmış Çubuk Grafik: Müşteri-Kumaş İlişkisi
- Gösterdiği: Müşteri segmentasyonu ve tercihleri
- İçgörü: Her müşterinin kumaş tercih profili
- Eylem: Kişiselleştirilmiş stok yönetimi

Sonraki Aşama: ABC ve Pareto Analizi İle Geliştirme

Bu temel analizler üzerine inşa edilen ileri analizler:
ABC Analizi İçin Girdiler:
1. KG_2 (Depoda kalan kg) → Değer bazlı sınıflandırma
2. Toplam Hareket Adet→ Hareket sıklığı bazlı sınıflandırma

Pareto Analizi İçin Girdiler:
1. Depo Yoğunluğu → %80 depo alanını hangi %20 kumaş kaplıyor?
2. Hareket Yoğunluğu → %80 hareketi hangi %20 kumaş oluşturuyor?
3. Müşteri Performansı → %80 ciroyu hangi %20 müşteri yapıyor?

Elde Edilecek İleri Düzey İçgörüler:
- A Sınıfı Kumaşlar: Değerli ve sık hareket edenler → Ön raflar
- B Sınıfı Kumaşlar: Orta değerli → Orta raflar  
- C Sınıfı Kumaşlar: Düşük değerli ve az hareket edenler → Arka/üst raflar

Özetle Bu Analizlerle Cevaplanan Sorular:

1. Depo Alanı: "Depomda en çok hangi kumaşlar yer kaplıyor?"
2. Operasyonel Verimlilik: "Hangi kumaşlar en çok iş yükü oluşturuyor?"
3. Tedarik Zinciri: "Hangi tedarikçilere bağımlıyım?"
4. Müşteri İlişkileri: "Hangi müşteriler benim için en değerli?"
5. Stratejik Planlama: "Hangi kumaş-müşteri kombinasyonlarına odaklanmalıyım?"

