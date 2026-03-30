# f-string mak tau variable iha teks

# exemplo iha apkikasaun Bank

# "Halo Abinda, ita nia saldo 500000"
# "Halo Dito, ita nia saldo 300000"
# "Halo Maria, ita nia saldo 750000"


# ← tidak mungkin ketik manual idak idak! 😱
# ← tenke otomatis!

# maneira tuan
naran = "Abinda"
saldo = 500000

# Cara lama — pakai +
print("Halo " + naran + ", ita nia saldo " + str(saldo))
# problema:
# 1. sabraut simal + barak los
# 2. numeru tenke mida tiha lai ba string uza str()
# 3. bele sala lalais!


# maneira foun 
naran1 = "Abinda"
saldo = 500000

print(f"Halo {naran1}, ita nia saldo {saldo}")
# → "Halo Abinda, ita nia saldo 500000"
# presiza sinal f iha string nia oin pois mak variable tama utiliza {}

# ninia estrutura
# f"teks baibain {variabel} teks baibain"


# exemplo balun
naran2 = "Abinda"
tinan = 22
municipio = "Dili"

# Sisipkan string
print(f"Hau nia naran {naran2}")
# → "Naran hau Abinda"

# Sisipkan angka
print(f"Hau nia tinan {tinan}")
# → "Tinan hau 22"

# Sisipkan banyak variabel
print(f"Hau nia naran {naran2}, tinan {tinan}, hau moris iha {municipio}")
# → "Hau nia naran Abinda, tinan 22, hau moris iha Dili"

# Bisa langsung hitung di dalam {}
print(f"Tinan oin hau sei iha tinan {tinan + 1}")
# → "Tinan kotuk hau sei iha tinan 23"

# formatu numeru ho f-string
folin = 1500000
valor = 95.5678

# aumenta ponto rihun
print(f"folin: {folin:,}")
# → "folin: 1,500,000"

# limitasaun decimal
print(f"valor: {valor:.2f}")
# → ": 95.57"

# exemplo real
estudante = [
    {"naran": "Abinda", "nilai": 95},
    {"naran": "Dito", "nilai": 80},
    {"naran": "Maria", "nilai": 72}
]

for m in estudante:
    if m["nilai"] >= 90:
        print(f"Parabens {m['naran']}! Ita hetan valor {m['nilai']} — Odamatan! 🎉")
    elif m["nilai"] >= 75:
        print(f"Diak {m['naran']}! Ita hetan valor {m['nilai']} — Kontinua! 💪")
    else:
        print(f"{m['naran']}, ita hetan valor {m['nilai']} — estuda tan! 📚")


# treinu
# level1
naran3 = "Abinda"
tinan = 22
municipio1 = "Dili"

print(f"hau nia naran {naran3}, hau nia tinan {tinan}, hau hela iha municipio {municipio}")

# level2
folin = 1500000
diskontu = 0.1

diskontu1 = (folin * diskontu)
result_folin = folin - diskontu1

print(f"folin_original: {folin:,}")
print(f"Total diskon {diskontu1:,}")
print(f"Resultado restu Diskon husi folin original {result_folin:,}")


# level3
produto = [
    {"naran": "Laptop", "folin": 8000000},
    {"naran": "Mouse", "folin": 150000},
    {"naran": "Keyboard", "folin": 300000}
]

for n in produto:
    print(f"produto {n["naran"]}, ho folin $ {n["folin"]:,}")
