# # kazu situasaun rela
# ita iha file estudante.csv ne'ebe containt dados estudante. ita nia assignment mak lee, fo sai no aumenta dados foun

# step 1 halo file CSV uluk
# halo file foun estudante.csv iha folder ne'ebe hanesan

# naran,tinan,municipio
# Abinda,22,Dili
# Dito,20,Baucau
# Maria,18,Suai



# step 2 - lee file csv

import csv

# # lee file csv
# with open("mahasiswa.csv", "r") as file:
#     reader = csv.reader(file)
    
#     for baris in reader:
#         print(baris)

# Output:
# ['naran', 'tinan', 'municipio']    ← ida ne'e mak header!
# ['Abinda', '22', 'Dili']
# ['Dito', '20', 'Baucau']
# ['Maria', '18', 'Suai']



# lee rapi liu tan utiliza directReader

# with open("mahasiswa.csv", "r") as file:
#     reader = csv.DictReader(file)  # ← lee sai dictionary!
    
#     for baris in reader:
#         print(f"Naran: {baris['nama']}, Tinan: {baris['tinan']}, Kota: {baris['kota']}")

# Output:
# Naran: Abinda, Tinan: 22, municipio: Dili
# Naran: Dito, Tinan: 20, municipio: Baucau
# Naran: Maria, Tinan: 18, municipio: Suai


# directreader otomatis uza lina primeiro hanesan key dictionary
# step 4 - hakerek file CSV

data_foun = [
    ["naran", "tinan", "municipio" ],
    ["Celly", "21", "hera"],
    ["dito", "20", "lurumata"]
]

with open("data_foun.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for lina in data_foun:
        writer.writerow(lina)

print("file rai ona")

# step 5 -aumenta dados utiliza append

estudante_foun = ["luis", "32", "Dili"]

with open("data_foun.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(estudante_foun)

print("dados rai ona")

# step 6 - kombinasaun ho try/except

try:
    with open("dataa_foun.csv", "r") as file:
        reader = csv.DictReader(file)
        for lina in reader:
            print(f"Naran: {lina['naran']}, municipio: {lina['municipio']}")

except FileNotFoundError:
    print("File la existe")
except Exception as e:
    print(f"Iha error: {e}")



# Aksi                Mode        Tool
# read file           "r"         csv.reader / csv.DictReader
# write new file     "w"          csv.writer
# insert data         "a"         csv.writer






