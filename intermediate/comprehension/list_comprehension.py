# comprehension mak hanesan maneira hodi hakerek loop ho badak deit iha lina ida. nia resultado hanesan, maibe nia kode mak badak tiha no sai "pythonic" liu tan.

# baibain ita uza 

numero = [1, 2, 3, 4, 5]
kuadrado = []

for n in numero:
    kuadrado.append(n ** 2)

print(kuadrado)


# ho list_comprehension

kuadrado = [n **2 for n in numero]
# nia pola ne'e sempre hanesan
# [espresaun for item in iterable]

print(kuadrado)

# fo sai numeru par

numeru_par = [n for n in numero if n % 2 == 0]

print(numeru_par)