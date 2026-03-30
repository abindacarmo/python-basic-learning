# len() mak method ida ne'ebe mak hodi sura total string ne'ebe mak iha
# user halo password: "abc"
# sistem cek → ohh password badak liu ❌

# user halo password: "abinda123"
# sistema cek → okay, minimal 8 karakter  ✅

# exemplo
password = "abinda123"

sura_password = len(password)
print(sura_password)

# len bele utiliza iha buat barak

# sura string nia naruk
naran = "Abinda"
print(len(naran))          # → 6

# sura item hira mak iha list ida nia laran
buah = ["apel", "haas", "lemon"]
print(len(buah))          # → 3

# sura key hira mak iha dictionary nia laran
mahasiswa = {"naran": "Abinda", "tinan": 22, "municipiu": "Dili"}
print(len(mahasiswa))     # → 3


# exemplo real
password = input("Halo password: ")

if len(password) < 8:
    print("password badak liu! minimal karakter 8 ❌")

else:
    print("Password oke! ✅")


# contoh real - validasaun naran
naran = input("Input naran: ")
naran = naran.strip()  # hamoos spasi

if len(naran) == 0:
    print("naran labele mamuk! ❌")
elif len(naran) < 3:
    print("naran badak liu! ❌")
else:
    print(f"Halo, {naran}! ✅")

# aumenta ho sira ne'ebe aprende ona
dados = "Abinda,22,Dili,Timor-Leste"

list_data = dados.split(",")

print(len(dados)) # sura total dados ne'ebe original
print(len(list_data)) # sura total dados ne'ebe split ona

# Treinu
# level 1

naran = "Abinda Carmo"
print(len(naran))

# level2
password1 = input("Halo ita nia password: ")

if len(password1) < 8:
    print("password ne'e badak liu!")
elif len(password1) >= 8:
    print("Password Ok!")
elif len(password1) >= 12:
    print("password naruk liu!")

else:
    print("invalidu")


# level3
kolega = ["Abinda", "Dito", "Maria", "Selly", "Ana"]
print(len(kolega))

for i in kolega:
    if len(i) >= 4:
        print(i)