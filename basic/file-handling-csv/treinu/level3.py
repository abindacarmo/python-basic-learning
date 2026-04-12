import csv

# level 3
# ita sei halo programa ida nuza while loop

def haree_dados():
    with open("basic/file-handling-csv/treinu/dados_input_estudante.csv", "r") as file:
        reader = csv.DictReader(file)

        for lina in reader:
            print(f"Naran: {lina['naran']}, tinan: {lina['tinan']}, municipio: {lina['municipio']}")

def aumenta_dados():
    naran = input("ita nia naran: ")
    tinan = input("ita nia tinan: ")
    municipio = input("ita nia municipio: ")

    with open("basic/file-handling-csv/treinu/dados_input_estudante.csv", "a", newline="") as file: # ninia estrutura primeiro mak ida ne'e, primeiro ita sei simpan uluk nia naran, ita aumenta mos ninia mode ne'e mak "w" katak ita rasik mak sei hakerek, no attribute newline hodi halo lina foun
        writer = csv.writer(file)
        writer.writerow([naran, tinan, municipio])


while True:
    print("1. Hakarak haree dados sira!")
    print("2. Hakarak aumenta dados!")
    print("3. Sai husi programa!")

    opsaun = input("Hili opsaun: ")

    if opsaun == "1":
        haree_dados()
    
    elif opsaun == "2":
        aumenta_dados()

    elif opsaun == "3":
        break

    else: 
        print("opsaun la loos!")

print("===============")