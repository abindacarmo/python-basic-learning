import csv

# level 2
# iha ne'e ita sei halo oinsa ita rasik mak input naran sira
naran = input("ita nia naran: ")
tinan = input("ita nia tinan: ")
municipio = input("ita nia municipio: ")


with open("basic/file-handling-csv/treinu/dados_input_estudante.csv", "a", newline="") as file: # ninia estrutura primeiro mak ida ne'e, primeiro ita sei simpan uluk nia naran, ita aumenta mos ninia mode ne'e mak "w" katak ita rasik mak sei hakerek, no attribute newline hodi halo lina foun
    fieldname = ("naran", "tinan", "municipio") # iha ne'e ita halo ninia koluna sira rai iha variable fieldname
    writer = csv.DictWriter(file, fieldnames = fieldname)
    writer.writeheader() # atu nune'e nia header ka tabela nia header iha
    writer.writerow({
        "naran": naran,
        "tinan": tinan,
        "municipio": municipio # nini adictionary sira ita rai iha nee
    })


print("dados rai ona!")