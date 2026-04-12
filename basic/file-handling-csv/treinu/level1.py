# level 1
# primeiro ita halo uluk ida ne'e
import csv

estudante = [
    ["naran", "idade", "hela-fatin"],
    ["Abinda", "22", "Hera"],
    ["Dito", "20", "Lurumata"],
    ["Ana", "26", "Becusse"]
]

with open("basic/file-handling-csv/treinu/estudante.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for lina in estudante:
        writer.writerow(lina) # hakerek lina ida

print("data rai ona ho susesu!")

# pois ita comment tiha

with open("basic/file-handling-csv/estudante.csv", "r") as file:
    reader = csv.DictReader(file)

    for lina in reader:
        print(f"Naran: {lina['naran']}, Idade: {lina['idade']}, Hela-fatin: {lina['hela-fatin']}")

print("dados Fo sai ho Susesu!")