# level 1
# primeiro ita halo uluk ida ne'e
import csv

# estudante = [
#     ["naran", "idade", "hela-fatin"],
#     ["Abinda", "22", "Hera"],
#     ["Dito", "20", "Lurumata"],
#     ["Ana", "26", "Becusse"]
# ]

# with open("estudante.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     for lina in estudante:
#         # print(f"Naran: {lina['naran']}, no Hela-fatin: {lina['hela-fatin']}")
#         # print(lina)
#         writer.writerow(lina) # hakerek lina ida

# print("data rai ona ho susesu!")

# pois ita comment tiha

# with open("basic/file-handling-csv/estudante.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for lina in reader:
#         print(f"Naran: {lina['naran']}, Idade: {lina['idade']}, Hela-fatin: {lina['hela-fatin']}")

# print("dados Fo sai ho Susesu!")



# level 2

input_dados = {
    "naran": input("input naran: "),
    "idade": input("input idade: "),
    "municipio": input("input municipio: ")
}

with open("dados_input_estudante.csv", "a", newline="") as file:
    filednames = ["naran", "idade", "municipio"]
    writer = csv.DictWriter(file, fieldnames=filednames)
    writer.writerow(input_dados)

print("dados rai ona!")


# level 3

# while True:

#     with open("basic/file-handling-csv/dados_input_estudante.csv", "r") as file_read:
#         reader = csv.DictReader(file_read)

#         for lina_dados in reader:
#             print(f"Naran: {lina_dados['naran']}, Tinan: {lina_dados['tinan']}, Municipio: {lina_dados['municipio']}")
    
#     # print("haree ho susesu!")


