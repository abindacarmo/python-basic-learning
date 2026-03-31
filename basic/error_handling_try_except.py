# tamba saida mak ita presiza error handling?

# exemplo ita iha calculator:
# numeru1 = 10
# numeru2 = 0
# result = numeru1 / numeru2
# print(result)

# saida mak sei akontese kuando:
# user hatama fali letra ka liafuan string → "abc" ← program CRASH! 💥
# user hatama 0 → dividir 0 ← program CRASH! 💥

# laho error handling program sei langsung para no user sei haree mensagen error ne'ebe menakutkan!

# # exemplo programa crash
# numeru = input("input numeru: ")
# user tau fali "abc"

# Output:
# ValueError: invalid literal for int() with base 10: 'abc'
# ← program sei para total 😱


# no nia solusaun mak' try/except'

# konseitu simples:
# Koko halao kode ida ne'e
# kuando iha error - kaer nia error, labele crash!

# nia strukture mak:

# try:
#     # kode ne'e dalaruma error
# except:
#     # karik error, halao ida ne'e

# TUIR MAI MAK ITA SEI HAREE KONABA TIPO ERROR NE'EBE MAK SEI MOSU

# 1. ValueError - value ne'ebe la sesuai
# akontese wainhira
# int("abc") - string labele sai integer
# int("12.5") - float labele sai fali integer

# exemplo real
print("=====exemplo ValueError=======")
try:
    numeru = int(input("input numeru: "))
    print(f"Ita nia numeru ne'ebe ita input", numeru)

except ValueError:
    print("ne'eba laos numeru! input numeru eehh")

# 2. ZeroDivisionError - dividir ho 0
# akontese wainhira:
# 10/0 - labele dividi ba 0

# exemplo real
print("=====exemplo ZeroDivisionError=======")
try:
    numeru1 = int(input("unput numeru 1: "))
    numeru2 = int(input("input numeru 2: "))
    result = numeru1 / numeru2
    print(f"resultado mak {result}")

except ZeroDivisionError:
    print("numeru hotu hotu labele dividi ba 0!")

print("=====exemplo FileNotFoundError=======")
# akontese wainhira loke file ne'ebe la existe
# exemplo real

try:
    file = open("data.csv", "r")
except:
    print("File la bele Hetan!")




print("=====exemplo KeyError=======")
# key dictionary la existe
# akontese wainhira:
# estudante = {"naran": "Abinda", "Tinan": 22}
# print(estudante["kota"]) # key "kota" la iha!

# exemplo real
estudante = {"naran": "Abinda", "Tinan": 22}

try:
    print(estudante["kota"])
except KeyError:
    print("Data kota la iha")



print("=====exemplo IndexError=======")
# index list la iha
# akontese wainhita 
# ai_fuan = ["apple", "pateka"]
# print(ai_fuan[5]) # index 5 la iha, iha leten ne'e so 0 ho 1 deit

# exemplo real
ai_fuan = ["apple", "pateka"]

try:
    print(ai_fuan[5])
except IndexError:
    print("index ne'e laiha iha list!")

print("=====exemplo ita halo error handling ne'ebe mak barak=======")
# kaer error ne'ebe barak
try:
    numeru3 = int(input("Input numeru 1: "))
    numeru4 = int(input("Input numeru 2: "))
    result = numeru3 / numeru4
    print(f"resultado mak {result}")

except ValueError:
    print("ida ne'eba laos numeru!")
except ZeroDivisionError:
    print("numeru saida deit labele dividi ba 0!")



print("=====exemplo Else & finally - kompletasaun try/except=======")

try:
    numeru5 = int(input("Input numeru: "))
except ValueError:
    print("ne'eba laos numeru")
else:
    print("susesu")
finally:
    print("Programa hotu")



# Rezumu strukture kompletu

# try:
#     # kode ne'ebe dalaruma error
# except NamaError:
#     # karik error ida ne'e akontese
# except NameError2:
#     # karik error ida ne'e akontese
# else:
#     karik la error 
# finally:
#     halao hela deit

### Relasaun ho data engineering
# lee file csv - FileNotFoundError
# koneksaun database - ConnectionError
# jere dados kantor - ValueError
# foti dados JSON - KeyError

# buat sira ne'e tenke uza try/except
# atu nunene pipeline data labele crash


# treinu
# level1

numeru6 = int(input("Input numeru 1: "))

try:
    print(f"numeru {numeru6} validu!")
except ValueError:
    print("ne'eba laos numeru oiii!")


# level2
