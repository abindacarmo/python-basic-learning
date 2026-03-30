# user regista uza email:
# "abindagmail.com"  ← la iha @ , la valid! ❌
# "abinda@gmail.com" ← iha @, valid! ✅

# program presiza cek @ iha glae 

email = "abinda@gmail.com"

print(email.find("@"))   # → 6 tamba ita bele dehan nia iha index 6

# karik la hetan @
email = "abindagmail.com"

print(email.find("@"))   # → -1 kuando la hetan nia sei fo sai -1 ne'e importante hodi hanoin hetan

# exemplo real

email = input("Masukkan email: ")

if email.find("@") == -1:
    print("Email la valido, la iha @❌")
else:
    print("Email valid! ✅")


liafuan = "Hau moris iha Dili"

print(liafuan.find("Dili"))    # → 14  (pozisaun letra D)
print(liafuan.find("Bali"))    # → -1  (la iha)
print(liafuan.find("moris"))   # → 4   (pozisaun letra m), tenke hanoin katak space mos program sei sura hotu

# diferente entre find() vs in
email = "abinda@gmail.com"

# find() → fo hatene pozisaun
print(email.find("@"))      # → 6

# in → fo hatene True/False
print("@" in email)         # → True

# bainhira mak utiliza ida ne'ebe
# presiza hatene nia pozisaun uza find()
# hakarak hatene deit nia existe ka lae uza in

# treinu
# level1

email = "abindacarmo@gmail.com"
print(email.find("@"))
print(email.find("."))
print(email.find("z"))

# level2
email = input("Input ita nia email: ")
if email.find("@") == -1:
    print("Email la validu! la iha @")
elif email.find(".") == -1:
    print("email la validu! la iha .!")
else:
    print("Email Valido!")


# level3
data = "Nama: Abinda, municipio: Dili, Umur: 22"

if data.find("municipio")  != -1:
    print("Data municipio iha")
else:
    print("dados municipio la iha")
