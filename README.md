# Fabric-Warehouse-Optimization-System

# Integrated Fabric Warehouse Optimization & Analytics System 🏭📊

An end-to-end industrial software system developed to enhance operational efficiency, minimize material-picking times, and optimize space utilization in a textile fabric warehouse. The project combines **Exploratory Data Analysis (EDA)**, **Metaheuristics (Genetic Algorithms)**, and **Graph Theory (TSP + Dijkstra)** into a unified decision-support platform.

---

## 📈 System Architecture & Module Breakdown

The system is structured into three interconnected modules. Each module addresses a specific phase of the warehouse management cycle:

### 1. [Data Analysis & Business Intelligence](./Data-analysis-study-in-a-fabric-warehouse-main)
* **Objective:** Clean raw operational data (2,069 records) and extract actionable supply chain insights.
* **Core Analyses:**
  * **Warehouse Density Analysis:** Identifies space hogs (e.g., *POLYAMID OLYURETHAN WOVEN_GRIS FONCE* occupying the peak density of 483 kg).
  * **Movement Density (Fabric & Color):** Reveals velocity trends. (Top 10 moving fabrics generate **65%** of all warehouse workloads; *WHITE, ECRU, BLACK* are top colors).
  * **Performance & Network Links:** Evaluates supplier dominance (Top 5 suppliers cover **78%** of intake) and customer concentration (Top 10 customers trigger **85%** of shipments).
* **Strategic Value:** Feeds the exact data metrics required for the ABC/Pareto categorization of inventory.

### 2. [Genetic Algorithm Layout Optimization](./Application-of-Genetic-Algorithm-in-Fabric-Warehouse-Layout)
* **Objective:** Mathematically place fabric types onto physical warehouse racks based on complex constraints.
* **Algorithm Details:** Multi-criteria optimization using an evolutionary **Genetic Algorithm** with tournament selection, 70-80% crossover, and 1-5% mutation over 1000–5000 generations.
* **Fitness Function Components:**
  * Hard capacity limits ($500 \text{ kg}$ threshold per rack) and stable occupancy balancing ($10\% - 90\%$).
  * **ABC Compliance:** Automatic positioning of high-velocity Class A items on ground-level/front zones and Class C items on higher/back shelves.
  * Penalties for material fragmentation across different racks and bonuses for high affinity/co-moved items.
* **Measured Improvements:** * Reduced required physical rack count from **654 to 648**.
  * Optimized effective rack usage ratio down from **68.8% to 62.3%** without a single capacity breach.

### 3. [Graph-Based Route Optimization](./Application-of-Route-Optimization-in-a-Fabric-Warehouse)
* **Objective:** Minimize the physical distance traveled by warehouse picking staff during order preparation.
* **Algorithmic Hybridization:**
  * **Dijkstra’s Algorithm:** Models aisles and racks as an interconnected network graph to compute the absolute shortest physical paths between points.
  * **Traveling Salesman Problem (TSP):** Calculates the ultimate, mathematically optimal sequencing order when a picker needs to visit multiple distinct racks.
  * **S-Shaped Routing Strategy:** Emulates practical, realistic human warehouse-movement workflows.
* **Tangible Output Example:** Streamlines picking batches to precise navigation streams (e.g., $\text{START} \rightarrow Y21 \rightarrow Y31 \rightarrow \dots \rightarrow \text{RAF\_565} \rightarrow \text{START}$) capping an sample multi-stop order path tightly at **176.99 meters**.

---

## 🛠️ Technology Stack & Tools

* **Core Language:** Python
* **Data & Analytics:** Pandas, NumPy, Scikit-Learn
* **Metaheuristics & Graph Theory:** Custom Evolutionary Core, NetworkX (Graph Modeling)
* **Visualization:** Matplotlib, Seaborn, Automated Multi-Sheet Excel Reports

---

## 🚀 Strategic Business Impact

1. **Space Efficiency:** Data-driven layout restructuring leads to a **~10.2% improvement** in warehouse floor space economics.
2. **Labor Optimization:** Integrating TSP-guided picking directly onto the GA-optimized layout reduces total order picking time and workforce fatigue significantly.
3. **Resilient Supply Chain:** Visualizing supplier dependencies and customer purchasing habits allows management to execute high-leverage contract negotiations and plan structural minimum-stock triggers.

# Entegre Kumaş Deposu Optimizasyon ve Veri Analitiği Sistemi 🏭📊

Bir tekstil kumaş deposunda alan verimliliğini artırmak, malzeme toplama sürelerini minimize etmek ve operasyonel süreçleri iyileştirmek amacıyla geliştirilmiş uçtan uca bir endüstriyel yazılım sistemidir. Proje; **Keşifsel Veri Analizi (EDA)**, **Meta-sezgisel Yöntemler (Genetik Algoritmalar)** ve **Graf Teorisi (TSP + Dijkstra)** yaklaşımlarını birleştirerek karar destek mekanizması sunar.

---

## 📈 Sistem Mimarisi ve Modül Dağılımı

Sistem, depo yönetim döngüsünü tamamlayan birbiriyle entegre 3 temel modülden oluşmaktadır. Her modülün teknik detayları ve kodları kendi klasörleri altındaki README dosyalarında yer almaktadır:

### 1. [Veri Analizi ve İş Zekası](./Data-analysis-study-in-a-fabric-warehouse-main)
* **Amaç:** 2.069 satırlık ham operasyonel veriyi temizlemek ve tedarik zincirine yönelik aksiyon alınabilir içgörüler üretmek.
* **Yapılan Temel Analizler:**
  * **Depo Alan Yoğunluğu Analizi:** Depoda en çok yer kaplayan ürünleri listeler (Örn: *POLYAMID OLYURETHAN DOKUMA_GRIS FONCE* kumaşı 483 kg ile en yüksek yoğunluğa sahiptir).
  * **Hareket Yoğunluğu (Kumaş & Renk):** Giriş-çıkış trendlerini belirler (En hareketli ilk 10 kumaş, toplam depo iş yükünün **%65**'ini oluşturur; *WHITE, ECRU, BLACK* en popüler renklerdir).
  * **Performans ve Bağlantı Ağları:** Tedarikçi hakimiyetini (İlk 5 tedarikçi girişlerin **%78**'ini karşılar) ve müşteri yoğunlaşmasını (İlk 10 müşteri çıkışların **%85**'ini tetikler) analiz eder.
* **Stratejik Değeri:** Stokların ABC/Pareto mantığına göre sınıflandırılması için ihtiyaç duyulan kesin metrikleri sağlar.

### 2. [Genetik Algoritma ile Yerleşim Optimizasyonu](./Application-of-Genetic-Algorithm-in-Fabric-Warehouse-Layout)
* **Amaç:** Kumaş toplarını, fiziksel kısıtları ve kuralları dikkate alarak raflara matematiksel olarak en ideal şekilde yerleştirmek.
* **Algoritma Detayları:** Turnuva seçimi, %70-80 çaprazlama ve %1-5 mutasyon oranları kullanılarak 1000–5000 nesil (jenerasyon) boyunca çalışan çok kriterli bir **Genetik Algoritma** tasarımı.
* **Uygunluk (Fitness) Fonksiyonu Bileşenleri:**
  * Raf başına hard-kapasite sınırı (Raf başına $500 \text{ kg}$ sınırı) ve %10 - %90 arası doluluk dengesi kısıtları.
  * **ABC Sınıfı Uyumu:** Hızlı sirküle olan A sınıfı ürünlerin alt kat ve ön alanlara, C sınıfı ürünlerin ise üst kat ve arka raflara otomatik yerleşimi.
  * Aynı kumaşın farklı raflara dağılmasını önleyen "parçalanma cezası" ve birlikte hareket eden ürünleri yan yana getiren "birliktelik bonusu".
* **Elde Edilen İyileştirmeler:** * Gerekli fiziksel raf sayısı **654'ten 648'e düşürüldü** (Yaklaşık %10.2 daha az raf).
  * Hiçbir rafta kapasite aşımı yaşanmadan, etkin raf kullanım oranı **%68.8'den %62.3'e** optimize edildi.

### 3. [Graf Tabanlı Rota Optimizasyonu](./Application-of-Route-Optimization-in-a-Fabric-Warehouse)
* **Amaç:** Depo çalışanlarının sipariş toplama hazırlığı sırasında kat ettiği fiziksel mesafeyi ve zamanı en aza indirmek.
* **Algoritmik Hibrit Yapı:**
  * **Dijkstra Algoritması:** Depo koridorlarını ve raflarını birbirine bağlı bir grafik ağı olarak modelleyerek iki nokta arasındaki en kısa fiziksel yolu hesaplar.
  * **Gezgin Satıcı Problemi (TSP):** Bir toplama personeli birden fazla rafa uğraması gerektiğinde, ziyaret edilecek en optimal sırayı belirler.
  * **S-Şekilli Rotalama Stratejisi:** İnsanların depo içindeki gerçekçi ve pratik hareket modellerini simüle eder.
* **Somut Çıktı Örneği:** Sipariş toplama listelerini optimize edilmiş rotalara dönüştürür (Örn: $\text{START} \rightarrow Y21 \rightarrow Y31 \rightarrow \dots \rightarrow \text{RAF\_565} \rightarrow \text{START}$) ve örnek bir çok duraklı toplama rotasını **176.99 metre** gibi minimum bir mesafede tamamlar.

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar

* **Ana Programlama Dili:** Python
* **Veri Analitiği:** Pandas, NumPy, Scikit-Learn
* **Optimizasyon ve Graf Teorisi:** Özel Geliştirilmiş Evrimsel Algoritma Çekirdeği, NetworkX (Graf Modelleme)
* **Görselleştirme:** Matplotlib, Seaborn, Otomatik Çok Sayfalı Excel Raporlama Çıktıları

---

## 🚀 Stratejik Ticari Faydaları

1. **Alan Verimliliği:** Veri odaklı yerleşim restriksiyonları sayesinde depo zemin ekonomisinde **%10.2'lik bir alan iyileştirmesi** sağlanmıştır.
2. **İş Gücü Optimizasyonu:** GA tarafından optimize edilen yerleşim planı üzerine TSP rotalamasının entegre edilmesi, toplam sipariş hazırlama sürelerini ve çalışan yorgunluğunu ciddi oranda azaltır.
3. **Dayanıklı Tedarik Zinciri:** Tedarikçi bağımlılıklarının ve müşteri satın alma alışkanlıklarının görselleştirilmesi, yönetimin stratejik sözleşme müzakereleri yapmasına ve dinamik minimum stok seviyeleri belirlemesine olanak tanır.
