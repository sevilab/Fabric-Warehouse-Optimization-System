 Warehouse Route Optimization System

This module was developed to optimize material picking routes in a textile warehouse.

Objective
To minimize the distance traveled by warehouse staff while preparing orders and reduce picking time.

How It Was Implemented
1. Warehouse Graph Modeling: Warehouse aisles and racks were converted into a graph structure.
2. Two-Algorithm Combination:
   - Dijkstra's Algorithm: To find the shortest physical path between two racks.
   - TSP (Traveling Salesman Problem): To determine the optimal visiting sequence when multiple racks need to be visited.
3. S-Shaped Routing: To provide a realistic movement pattern within the warehouse.

Required Data
1. Warehouse Layout Plan
   - Rack coordinates (X, Y, level information)
   - Aisle widths and passage points
   - Starting point (goods receipt area)

2. Stock Data
   - Which fabric is located in which rack
   - Number of rolls and weight information in each rack

3. Demand List
   - Fabric types to be picked
   - How many rolls are requested of each fabric

Process Steps
1. The list of fabrics to be picked is obtained from the user.
2. The system checks suitable racks and stock status for each fabric.
3. Coordinates of the racks to be visited are determined.
4. The optimal visiting sequence is calculated using TSP.
5. The actual path between each rack pair is found using Dijkstra.
6. The entire route is combined and the total distance is calculated.

Outputs
1. Text Output
   Total Distance: 176.99 meters
   Route Sequence: START → Y21 → Y31 → ... → RAF_565 → RAF_209 → RAF_250 → START

2. Visual Output
   - Route drawn on the warehouse map
   - Display of rack locations and quantities to be picked

3. Detailed Information
   - Quantity of fabric to be picked from each rack
   - Each movement step
   - Estimated total picking time
*****************************************************************************************************************************
Depo İçi Rota Optimizasyonu Sistemi

Bu modül, bir tekstil deposunda malzeme toplama rotalarını optimize etmek için geliştirilmiştir.

Amaç
Depo çalışanlarının siparişleri hazırlarken kat ettiği mesafeyi minimize etmek ve toplama süresini azaltmak.

Nasıl Uygulandı?
1. Depo Grafik Modelleme: Depo koridorları ve raflar bir graf yapısına dönüştürüldü.
2. İki Algoritma Kombinasyonu:
   - Dijkstra Algoritması: İki raf arasındaki en kısa fiziksel yolu bulmak için.
   - TSP (Gezgin Satıcı Problemi)**: Birden fazla rafı ziyaret ederken en optimal sırayı belirlemek için.
3. S-Şekilli Rotalama: Depo içinde gerçekçi bir hareket modeli sağlamak için.

Gerekli Veriler
1. Depo Yerleşim Planı
   - Raf koordinatları (X, Y, kat bilgisi)
   - Koridor genişlikleri ve geçiş noktaları
   - Başlangıç noktası (mal kabul alanı)

2. Stok Verisi
   - Hangi kumaşın hangi rafta olduğu
   - Her raftaki top sayısı ve kilogram bilgisi

3. Talep Listesi
   - Alınacak kumaş türleri
   - Her kumaştan kaç top istenildiği

İşleyiş Adımları
1. Kullanıcıdan alınacak kumaş listesi alınır.
2. Sistem her kumaş için uygun rafları ve stok durumunu kontrol eder.
3. Ziyaret edilecek rafların koordinatları belirlenir.
4. TSP ile en optimal ziyaret sırası hesaplanır.
5. Dijkstra ile her raf çifti arasındaki gerçek yol bulunur.
6. Tüm rota birleştirilip toplam mesafe hesaplanır.

Çıktılar
1. Metinsel Çıktı
   Toplam Mesafe: 176.99 metre
   Rota Sırası: START → Y21 → Y31 → ... → RAF_565 → RAF_209 → RAF_250 → START
   

2. Görsel Çıktı
   - Depo haritası üzerinde çizilmiş rota
   - Rafların konumları ve alınacak miktarların gösterimi

3. Detaylı Bilgi
   - Her raftan alınacak kumaş miktarı
   - Her bir hareket adımı
   - Toplam toplama süresi tahmini


