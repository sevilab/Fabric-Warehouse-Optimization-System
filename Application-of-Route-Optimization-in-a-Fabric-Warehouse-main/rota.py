import pandas as pd 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import traveling_salesman_problem

# 1️⃣ Yol düğümleri
yol_dugumleri = {
    "Y11": (-19.7, 19), "Y12": (-19.7, 0), "Y13": (-19.7, -17),
    "Y21": (-15.1, 19), "Y22": (-15.1, 0), "Y23": (-15.1, -19),
    "Y31": (-8.1, 19), "Y32": (-8.1, 0), "Y33": (-8.1, -19),
    "Y41": (-3.5, 19), "Y42": (-3.5, 0), "Y43": (-3.5, -19),
    "Y51": (3.5, 19), "Y52": (3.5, 0), "Y53": (3.5, -21),
    "Y61": (8.1, 19), "Y62": (8.1, 0), "Y63": (8.1, -21),
    "Y71": (15.1, 19), "Y72": (15.1, 7), "Y73": (15.1, -5),
    "Y81": (19.7, 25), "Y82": (19.7, 10), "Y83": (19.7, -5),
    "Y74": (15.1, -21)
}
yol_dugumleri["START"] = (-22, 21)  # Giriş noktası

# 2️⃣ Excel dosya yolu
excel_path = "C:/Users/evrim/OneDrive/Masaüstü/rafs.xlsx"

# 3️⃣ Bağlantı tablosunu oku ve edges oluştur
baglanti_df = pd.read_excel(excel_path, sheet_name="baglanti")
baglanti_df.set_index(baglanti_df.columns[0], inplace=True)

edges = set()
for row_name in baglanti_df.index:
    for col_name in baglanti_df.columns:
        if str(baglanti_df.loc[row_name, col_name]).strip().upper() == "E":
            if row_name != col_name:
                edge = tuple(sorted([row_name, col_name]))
                edges.add(edge)
edges = list(edges)

# START bağlantılarını ekle (en yakın 1-2 düğüm)
start_coord = yol_dugumleri["START"]
yol_dugumleri_Y = [k for k in yol_dugumleri if k.startswith("Y")]
kac_dugume_baglansin = 2
mesafeler = [(d, np.hypot(yol_dugumleri[d][0] - start_coord[0], yol_dugumleri[d][1] - start_coord[1])) for d in yol_dugumleri_Y]
mesafeler = sorted(mesafeler, key=lambda x: x[1])
for d, m in mesafeler[:kac_dugume_baglansin]:
    edges.append(("START", d))

# 4️⃣ GRAF OLUŞTUR
G = nx.Graph()
for node, pos in yol_dugumleri.items():
    G.add_node(node, pos=pos)
for n1, n2 in edges:
    G.add_edge(n1, n2, weight=np.hypot(
        yol_dugumleri[n1][0] - yol_dugumleri[n2][0],
        yol_dugumleri[n1][1] - yol_dugumleri[n2][1]))

# 5️⃣ VERİ OKUMA
kumas_df = pd.read_excel(excel_path, sheet_name="kumas")
konum_df = pd.read_excel(excel_path, sheet_name="konum")

# 6️⃣ Kullanıcıdan kumaş ismi ve adedi al
istenen_kumaslar = []
n = int(input("Kaç farklı kumaş istiyorsunuz? "))
for i in range(n):
    ad = input(f"{i+1}. kumaşın tam adını yazın: ").strip()
    adet = int(input(f"{ad} kumaşından kaç top almak istiyorsunuz? "))
    istenen_kumaslar.append({"KUMAS_CINS_RENK": ad, "ADET": adet})

# 7️⃣ Alınacak rafları bul
alinacak_toplar = []
for talep in istenen_kumaslar:
    kumas_ad = talep["KUMAS_CINS_RENK"]
    adet = talep["ADET"]
    kumaslar = kumas_df[kumas_df["KUMAS_CINS_RENK"] == kumas_ad]
    if kumaslar.empty:
        print(f"{kumas_ad} rafta bulunamadı!")
        continue
    for _, row in kumaslar.iterrows():
        mevcut_top = row["YERLESEN_TOP"]
        alinacak = min(mevcut_top, adet)
        if alinacak > 0:
            raf_no = row["RAF_NO"]
            raf_bilgi = konum_df[konum_df["NO"] == raf_no].iloc[0]
            alinacak_toplar.append({
                "KUMAS_CINS_RENK": kumas_ad,
                "RAF_NO": raf_no,
                "ALINACAK_TOP": alinacak,
                "X": float(str(raf_bilgi["X"]).replace(",", ".")),
                "Y": float(str(raf_bilgi["Y"]).replace(",", ".")),
                "KAT": int(raf_bilgi["Z"])
            })
            adet -= alinacak
        if adet <= 0:
            break
    if adet > 0:
        print(f"{kumas_ad} için {adet} top eksik!")

if not alinacak_toplar:
    print("Hiçbir raf bulunamadı! Program durdu.")
    exit()

# 8️⃣ Hedef yol düğümlerini bul
def raf_onu_yol_dugumu(raf_x, raf_y):
    min_x_dist = 1e9
    en_yakin_dikeyler = []
    for ad, (x, y) in yol_dugumleri.items():
        if ad.startswith('Y'):
            x_dist = abs(x - raf_x)
            if x_dist < min_x_dist:
                min_x_dist = x_dist
    for ad, (x, y) in yol_dugumleri.items():
        if ad.startswith('Y') and abs(x - raf_x) == min_x_dist:
            en_yakin_dikeyler.append((ad, y))
    min_y_dist = 1e9
    en_yakin_ad = None
    for ad, y in en_yakin_dikeyler:
        y_dist = abs(y - raf_y)
        if y_dist < min_y_dist:
            min_y_dist = y_dist
            en_yakin_ad = ad
    return en_yakin_ad

target_nodes = []
etiketler = []
for i, item in enumerate(alinacak_toplar):
    yol_hedef = raf_onu_yol_dugumu(item["X"], item["Y"])
    target_nodes.append(yol_hedef)
    etiketler.append({
        "node": yol_hedef,
        "text": f"{item['KUMAS_CINS_RENK']}\nRAF:{item['RAF_NO']}\n({item['ALINACAK_TOP']})"
    })

# 9️⃣ TSP için mesafe matrisi oluştur
tsp_nodes = ["START"] + target_nodes
distance_matrix = {}
for i, n1 in enumerate(tsp_nodes):
    distance_matrix[n1] = {}
    for j, n2 in enumerate(tsp_nodes):
        if i != j:
            distance_matrix[n1][n2] = nx.shortest_path_length(G, n1, n2, weight="weight")
        else:
            distance_matrix[n1][n2] = 0

# 1️⃣0️⃣ TSP çözümü
def custom_weight(u, v, d=None):
    return distance_matrix[u][v]

tsp_path = traveling_salesman_problem(
    nx.complete_graph(tsp_nodes), nodes=tsp_nodes, cycle=False, weight=custom_weight
)
if tsp_path[0] != "START":
    tsp_path = tsp_path[tsp_path.index("START"):] + tsp_path[:tsp_path.index("START")]

# 1️⃣1️⃣ Gerçek yol rotası oluştur
full_route = []
for i in range(len(tsp_path) - 1):
    part = nx.shortest_path(G, tsp_path[i], tsp_path[i + 1], weight="weight")
    if i > 0:
        part = part[1:]  # tekrarlı eklemeyi önler
    full_route += part

# 1️⃣2️⃣ Toplam mesafe
full_length = 0
for i in range(len(full_route) - 1):
    full_length += G[full_route[i]][full_route[i + 1]]['weight']

# 1️⃣3️⃣ Sonuçları yazdır ve çiz
print("\nToplama Rotası (Yol düğümleri sıralı):", full_route)
print("Toplam Mesafe: %.2f" % full_length)
print("\nRota Adımları:")
for n in tsp_path:
    if n in target_nodes:
        idx = target_nodes.index(n)
        print(f"RAF_NO: {alinacak_toplar[idx]['RAF_NO']} - KUMAŞ: {alinacak_toplar[idx]['KUMAS_CINS_RENK']} → {alinacak_toplar[idx]['ALINACAK_TOP']} top alınacak.")

plt.figure(figsize=(14, 8))
kat_marker = {1: ("o", "black"), 2: ("s", "dodgerblue"), 3: ("P", "purple")}
for kat in [1, 2, 3]:
    alt_df = konum_df[konum_df["Z"] == kat]
    plt.scatter(alt_df["X"], alt_df["Y"], s=25, marker=kat_marker[kat][0],
                color=kat_marker[kat][1], label=f"{kat}. Kat Raflar", alpha=0.2)
nx.draw_networkx_nodes(
    G, nx.get_node_attributes(G, 'pos'),
    nodelist=[k for k in yol_dugumleri if k.startswith("Y")],
    node_size=420, node_color="lightblue",
    edgecolors="gray", linewidths=2,
)
nx.draw_networkx_labels(G, nx.get_node_attributes(G, 'pos'), font_weight="bold")
nx.draw_networkx_edges(
    G, nx.get_node_attributes(G, 'pos'),
    edgelist=G.edges(),
    width=2, alpha=0.3, edge_color="gray"
)
path_edges = list(zip(full_route[:-1], full_route[1:]))
nx.draw_networkx_edges(
    G, nx.get_node_attributes(G, 'pos'),
    edgelist=path_edges,
    width=5, edge_color="red"
)
for etiket in etiketler:
    x, y = yol_dugumleri[etiket["node"]]
    plt.scatter([x], [y], s=400, marker="D", color="gold", edgecolor="black", zorder=20)
    plt.text(x, y-1.6, etiket["text"], color="crimson",
             fontsize=13, ha="center", va="top", fontweight="bold",
             bbox=dict(facecolor="white", alpha=0.95, edgecolor="red"))
plt.scatter(start_coord[0], start_coord[1], color="blue", s=300, label="Başlangıç (Giriş)", marker="P", edgecolor="black", zorder=25)
plt.title("Kumaş Deposu Toplama Rotası (Gerçekçi TSP)", fontsize=16)
plt.xlabel("X Koordinatı")
plt.ylabel("Y Koordinatı")
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()