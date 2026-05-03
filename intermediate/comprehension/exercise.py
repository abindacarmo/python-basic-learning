funsionariu = [
    {"naran": "Ana", "salario": 2000000},
    {"naran": "Joao", "salario": 3500000},
    {"naran": "Maria", "salario": 1800000},
    {"naran": "Pedro", "salario": 4000000},
]

# list dados naran hotu
naran_funs = [f["naran"] for f in funsionariu]
print(naran_funs)

# list naran ne'ebe nia salario boot
salario_boot = [f["naran"] for f in funsionariu if f["salario"] > 2000000]
print(salario_boot)

# dict {naran: salario}
mapa_salario = {f["naran"]: f["salario"] for f in funsionariu}
print(mapa_salario)