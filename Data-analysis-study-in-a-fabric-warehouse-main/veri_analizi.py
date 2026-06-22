import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excel dosyasını yükleme
file_path = 'C:/Users/HP/Desktop/talu/kumas_depo_veri.xlsm'  # Dosya yolunu buraya girin
excel_data = pd.ExcelFile(file_path)
data = excel_data.parse('Sayfa1', header=1)
print(data.columns)

# Gerekli kolonların seçilmesi (Kolon adlarını kontrol edin ve buna göre değiştirin)
columns_needed = ['TEDARİKÇİ FİRMA', 'MÜŞTERİ ADI', ' KUMAŞ CİNSİ', 'RENK', 'PARTİ', 
                  'TOP SAYISI', 'KG ', 'TOP SAYISI_1', 'KG_1', 'TOP SAYISI_2', 'KG_2']
data_needed = data[columns_needed]

# 1. Eksik Verilerin Kontrolü
missing_data_count = data_needed.isnull().sum()
print("\nEksik veri sayısı (sütun bazında):\n", missing_data_count)

# 2. Eksik Verileri İçeren Satırların Silinmesi
data_cleaned = data_needed.dropna()
print("\nEksik veriler silindikten sonra temizlenmiş veri setindeki eksik veriler:")
print(data_cleaned.isnull().sum())

# Çıktı dosyası yolu
output_file = 'C:/Users/HP/Desktop/talu/depo_kullanim_verimliligi_analizleri.xlsx'

# Tüm kumaş cinsleri, renk, müşteri ve tedarikçi isimlerini kaydetme
unique_kumaslar = data_cleaned[' KUMAŞ CİNSİ'].unique()
unique_renkler = data_cleaned['RENK'].unique()
unique_musteriler = data_cleaned['MÜŞTERİ ADI'].unique()
unique_tedarikciler = data_cleaned['TEDARİKÇİ FİRMA'].unique()

# Depo alanı yoğunluğu analizi (TOP SAYISI_2 ve KG_2 üzerinden)
depo_yogunluk = data_cleaned.groupby([' KUMAŞ CİNSİ', 'RENK']).agg({
    'TOP SAYISI_2': 'sum',
    'KG_2': 'sum'
}).reset_index()
depo_yogunluk = depo_yogunluk.sort_values(by=['KG_2'], ascending=False)

# Hareket yoğunluğu analizi - Kumaş (adet ve KG bazında)
hareket_yogunluk_kumas = data_cleaned.groupby([' KUMAŞ CİNSİ']).agg({
    'TOP SAYISI': 'sum',
    'TOP SAYISI_1': 'sum',
    'KG ': 'sum',
    'KG_1': 'sum'
}).reset_index()
hareket_yogunluk_kumas['Toplam Hareket Adet'] = (hareket_yogunluk_kumas['TOP SAYISI'] + 
                                                  hareket_yogunluk_kumas['TOP SAYISI_1'])
# "Toplam Hareket KG" hesaplanıyor ancak Excel aktarımında kullanılmayacak:
hareket_yogunluk_kumas['Toplam Hareket KG'] = (hareket_yogunluk_kumas['KG '] + 
                                                hareket_yogunluk_kumas['KG_1'])

# Hareket yoğunluğu analizi - Renk (adet ve KG bazında)
hareket_yogunluk_renk = data_cleaned.groupby(['RENK']).agg({
    'TOP SAYISI': 'sum',
    'TOP SAYISI_1': 'sum',
    'KG ': 'sum',
    'KG_1': 'sum'
}).reset_index()
hareket_yogunluk_renk['Toplam Hareket Adet'] = (hareket_yogunluk_renk['TOP SAYISI'] + 
                                                 hareket_yogunluk_renk['TOP SAYISI_1'])
hareket_yogunluk_renk['Toplam Hareket KG'] = (hareket_yogunluk_renk['KG '] + 
                                               hareket_yogunluk_renk['KG_1'])

# 1. Tedarikçi Performans Analizi (adet bazlı)
tedarikci_performance = data_needed.groupby('TEDARİKÇİ FİRMA').agg({
    'TOP SAYISI': 'sum',
    'KG ': 'sum'
}).reset_index()
tedarikci_performance = tedarikci_performance.sort_values(by=['TOP SAYISI', 'KG '], ascending=False)

# 2. Müşteri Performans Analizi (adet bazlı)
musteri_performance = data_needed.groupby('MÜŞTERİ ADI').agg({
    'TOP SAYISI': 'sum',
    'KG ': 'sum'
}).reset_index()
musteri_performance = musteri_performance.sort_values(by=['TOP SAYISI', 'KG '], ascending=False)

# 3. Tedarikçi ve Müşteri En İyi Kumaş Bağlantıları (Güncellenmiş)
# Tedarikçi için:
tedarikci_kumas_baglanti = data_needed.groupby(['TEDARİKÇİ FİRMA', ' KUMAŞ CİNSİ']).agg({
    'TOP SAYISI': 'sum',
    'KG ': 'sum',
    'TOP SAYISI_1': 'sum',
    'KG_1': 'sum'
}).reset_index()
tedarikci_kumas_baglanti['Toplam Hareket'] = (tedarikci_kumas_baglanti['TOP SAYISI'] + 
                                               tedarikci_kumas_baglanti['TOP SAYISI_1'])
tedarikci_kumas_baglanti = tedarikci_kumas_baglanti.sort_values(by='Toplam Hareket', ascending=False)

# Müşteri için:
musteri_kumas_baglanti = data_needed.groupby(['MÜŞTERİ ADI', ' KUMAŞ CİNSİ']).agg({
    'TOP SAYISI': 'sum',
    'KG ': 'sum',
    'TOP SAYISI_1': 'sum',
    'KG_1': 'sum'
}).reset_index()
musteri_kumas_baglanti['Toplam Hareket'] = (musteri_kumas_baglanti['TOP SAYISI'] + 
                                             musteri_kumas_baglanti['TOP SAYISI_1'])
musteri_kumas_baglanti = musteri_kumas_baglanti.sort_values(by='Toplam Hareket', ascending=False)

# Grafik: Hareket Yoğunluğu - Kumaş (Adet bazında)
plt.figure(figsize=(12, 6))
sns.barplot(data=hareket_yogunluk_kumas.sort_values('Toplam Hareket Adet', ascending=False).head(20),
            x='Toplam Hareket Adet', y=' KUMAŞ CİNSİ', palette='coolwarm')
plt.title('Ürün Hareket Yoğunluğu (En Çok Hareket Eden İlk 20 Kumaş - Adet)', fontsize=14)
plt.xlabel('Toplam Hareket Adet (Giriş + Çıkış)', fontsize=12)
plt.ylabel('Kumaş Cinsi', fontsize=12)
plt.tight_layout()
plt.show()

# Grafik: Hareket Yoğunluğu - Renk (Adet bazında)
plt.figure(figsize=(12, 6))
sns.barplot(data=hareket_yogunluk_renk.sort_values('Toplam Hareket Adet', ascending=False).head(20),
            x='Toplam Hareket Adet', y='RENK', palette='coolwarm')
plt.title('Ürün Hareket Yoğunluğu (En Çok Hareket Eden İlk 20 Renk - Adet)', fontsize=14)
plt.xlabel('Toplam Hareket Adet (Giriş + Çıkış)', fontsize=12)
plt.ylabel('Renk', fontsize=12)
plt.tight_layout()
plt.show()

# Müşteri performansı toplam kumaş hareketi (adet bazında)  
plt.figure(figsize=(12, 6))
sns.barplot(data=musteri_performance.head(20), x='TOP SAYISI', y='MÜŞTERİ ADI', palette='viridis')
plt.title('Müşteri Performansı (Toplam Kumaş Hareketi - Adet)', fontsize=14)
plt.xlabel('Toplam Hareket (Giriş + Çıkış)', fontsize=12)
plt.ylabel('Müşteri Adı', fontsize=12)
plt.tight_layout()
plt.show()

# Tedarikçi performansı toplam kumaş hareketi (adet bazında)
plt.figure(figsize=(12, 6))
sns.barplot(data=tedarikci_performance.head(20), x='TOP SAYISI', y='TEDARİKÇİ FİRMA', palette='plasma')
plt.title('Tedarikçi Performansı (Toplam Kumaş Hareketi - Adet)', fontsize=14)
plt.xlabel('Toplam Hareket (Giriş + Çıkış)', fontsize=12)
plt.ylabel('Tedarikçi Firma', fontsize=12)
plt.tight_layout()
plt.show()

# Müşteri-Kumaş Bağlantısı (adet bazında)
top_kumaslar = (
    data_cleaned.groupby(' KUMAŞ CİNSİ')['TOP SAYISI']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
)
musteri_kumas = (
    data_cleaned[data_cleaned[' KUMAŞ CİNSİ'].isin(top_kumaslar)]
    .groupby(['MÜŞTERİ ADI', ' KUMAŞ CİNSİ'])[['TOP SAYISI', 'TOP SAYISI_1']]
    .sum()
    .reset_index()
)
musteri_kumas['Toplam Hareket'] = musteri_kumas['TOP SAYISI'] + musteri_kumas['TOP SAYISI_1']
musteri_kumas_pivot = musteri_kumas.pivot(index='MÜŞTERİ ADI', columns=' KUMAŞ CİNSİ', values='Toplam Hareket').fillna(0)
top_customers = musteri_kumas_pivot.sum(axis=1).sort_values(ascending=False).head(20).index
musteri_kumas_top20 = musteri_kumas_pivot.loc[top_customers]

plt.figure(figsize=(14, 7))
musteri_kumas_top20.plot(kind='bar', stacked=True, colormap='tab20')
plt.title('Müşteri-Kumaş Bağlantısı (İlk 20 Müşteri & İlk 10 Kumaş) - Toplam Hareket (Adet)', fontsize=14)
plt.xlabel('Müşteri Adı', fontsize=12)
plt.ylabel('Toplam Hareket ', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Kumaş Cinsi', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Tedarikçi-Kumaş Bağlantısı (adet bazında)
tedarikci_kumas = (
    data_cleaned[data_cleaned[' KUMAŞ CİNSİ'].isin(top_kumaslar)]
    .groupby(['TEDARİKÇİ FİRMA', ' KUMAŞ CİNSİ'])[['TOP SAYISI', 'TOP SAYISI_1']]
    .sum()
    .reset_index()
)
tedarikci_kumas['Toplam Hareket'] = tedarikci_kumas['TOP SAYISI'] + tedarikci_kumas['TOP SAYISI_1']
tedarikci_kumas_pivot = tedarikci_kumas.pivot(index='TEDARİKÇİ FİRMA', columns=' KUMAŞ CİNSİ', values='Toplam Hareket').fillna(0)
top_suppliers = tedarikci_kumas_pivot.sum(axis=1).sort_values(ascending=False).head(20).index
tedarikci_kumas_top20 = tedarikci_kumas_pivot.loc[top_suppliers]

plt.figure(figsize=(14, 7))
tedarikci_kumas_top20.plot(kind='bar', stacked=True, colormap='tab20')
plt.title('Tedarikçi-Kumaş Bağlantısı (İlk 20 Tedarikçi & İlk 10 Kumaş) - Toplam Hareket (Adet)', fontsize=14)
plt.xlabel('Tedarikçi Firma', fontsize=12)
plt.ylabel('Toplam Hareket ', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Kumaş Cinsi', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Excel'e aktarım:
with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:
    # Kumaş cinsleri ve Renkler
    pd.DataFrame({'Kumaş Cinsleri': unique_kumaslar}).to_excel(writer, sheet_name='Kumaş Cinsleri', index=False)
    pd.DataFrame({'Renkler': unique_renkler}).to_excel(writer, sheet_name='Renkler', index=False)
    
    # Depo alanı yoğunluğu exportu
    depo_yogunluk.to_excel(writer, sheet_name='Depo Alanı Yoğunluğu', index=False)
    
    # Hareket Yoğunluğu - Kumaş exportu
    hareket_yogunluk_kumas_export = hareket_yogunluk_kumas[[' KUMAŞ CİNSİ', 'TOP SAYISI', 'KG ', 
                                                             'TOP SAYISI_1', 'KG_1', 'Toplam Hareket Adet']].copy()
    # Sütun isimlerinde boşlukları temizleme
    hareket_yogunluk_kumas_export.rename(columns={'KG ':'KG', 'KG_1':'KG1'}, inplace=True)
    # Toplam Hareket Adet sütununa göre büyükten küçüğe sıralama
    hareket_yogunluk_kumas_export = hareket_yogunluk_kumas_export.sort_values(by='Toplam Hareket Adet', ascending=False)
    hareket_yogunluk_kumas_export.to_excel(writer, sheet_name='Hareket Yoğunluğu - Kumaş', index=False)
    
    # Hareket Yoğunluğu - Renk exportu
    hareket_yogunluk_renk_export = hareket_yogunluk_renk[['RENK', 'TOP SAYISI', 'KG ', 
                                                           'TOP SAYISI_1', 'KG_1', 'Toplam Hareket Adet']].copy()
    hareket_yogunluk_renk_export.rename(columns={'KG ':'KG', 'KG_1':'KG1'}, inplace=True)
    hareket_yogunluk_renk_export = hareket_yogunluk_renk_export.sort_values(by='Toplam Hareket Adet', ascending=False)
    hareket_yogunluk_renk_export.to_excel(writer, sheet_name='Hareket Yoğunluğu - Renk', index=False)
    
    # Performans analizleri
    tedarikci_performance.to_excel(writer, sheet_name='Tedarikçi Performansı', index=False)
    musteri_performance.to_excel(writer, sheet_name='Müşteri Performansı', index=False)
    
    # Tedarikçi Kumaş Bağlantıları exportu
    tedarikci_kumas_baglanti_export = tedarikci_kumas_baglanti[['TEDARİKÇİ FİRMA', ' KUMAŞ CİNSİ', 
                                                                 'TOP SAYISI', 'KG ', 
                                                                 'TOP SAYISI_1', 'KG_1', 'Toplam Hareket']].copy()
    tedarikci_kumas_baglanti_export.rename(columns={'KG ':'KG', 'KG_1':'KG1'}, inplace=True)
    tedarikci_kumas_baglanti_export.to_excel(writer, sheet_name='Tedarikçi Kumaş Bağlantıları', index=False)
    
    # Müşteri Kumaş Bağlantıları exportu
    musteri_kumas_baglanti_export = musteri_kumas_baglanti[['MÜŞTERİ ADI', ' KUMAŞ CİNSİ', 
                                                             'TOP SAYISI', 'KG ', 
                                                             'TOP SAYISI_1', 'KG_1', 'Toplam Hareket']].copy()
    musteri_kumas_baglanti_export.rename(columns={'KG ':'KG', 'KG_1':'KG1'}, inplace=True)
    musteri_kumas_baglanti_export.to_excel(writer, sheet_name='Müşteri Kumaş Bağlantıları', index=False)

print(f"Analiz sonuçları '{output_file}' dosyasına başarıyla kaydedildi.")
