# replace mak method ida ne'ebe mak ita bele uza hodi troka liafuan

# exemplo 
# dados ne'ebe mai husi database mak hanesan:
# "Hau moris iha Bali"
# "Hau hetan Bali"
# "Bali adalah pulau indah"

# liafuan bali ne'e ita hakarak troka ba Dili
# maibe tidak mungking ita muda idak-idak wainhira dados ne'e barak demais!

lifuan = "Hau moris iha Dili"

result = lifuan.replace("Bali", "Dili")
print(result)

# nia estrutura
# teks.replace("liafuan_tuan", "liafuan_foun")

# exemplo balun
# troka liafuan
liafuan = "Hau hadomi Bali"
print(liafuan.replace("Bali", "Dili"))
# → "Hau hadomi Dili"

# troka karakter
numeru = "+670-7784-8920"
print(numeru.replace("-", ""))
# → "081234567890"

# troka space ba underscrore
naran = "Abinda Carmo"
print(naran.replace(" ", "-"))
# → "Abinda-Carmo"

# exemplo real
folin = "$. 500.000"

# hamoos tiha kalkulator atu nune'e bele sura
folin_mos = folin.replace("$", "")
folin_mos = folin_mos.replace(".", "")

print(folin_mos)
print(int(folin_mos)) #prepara ona hodi sura


liafuan2 = "Hau moris iha Bali"

liafuan2.replace("Bali", "Dili")  # ❌ seidauk rai!
print(liafuan2)                    # → "Hau moris iha Bali"

liafuan2 = liafuan2.replace("Bali", "Dili")  # ✅
print(liafuan2)                              # → "Hau moris iha Dili"

# treinu
# level 1
liafuan3 = "Hau moris iha Manila"
liafuan3_hadia = liafuan3.replace("Manila", "Viqueue")
print(liafuan3_hadia)

# level2
nu_telefone = "0812-3456-7890"
nu_telefone_hadia = nu_telefone.replace("-", "")
print(nu_telefone_hadia)

# level3
dados_foer = "$. 1.500.000"
dados_mos = dados_foer.replace("$", "")
dados_mos = dados_mos.replace(".", "")
dados_int = int(dados_mos)

print(dados_int)