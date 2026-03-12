# kondisaun iha python ita utiliza atu cek afirmasaun no sezekusaun kode so deit kondisaun ne'e rasik los(True) ka laloos(Sala)
# iha python iha kondisaun sira ne'ebe mak hanesan:

# if
# elif(else if)
# else

# ESTRUTURA BASICA
# if kondisaun:
#     # kode sei ezekuta wainhira kondisaun true
# elif kondisaun_seluk:
#     # kode sei ezsekuta wainhira kondisi_lain True
# else:
#     # Kode sei ezekuta wainhira kondisaun false

# EZEMPLU:
idade = 18

if idade >= 18:
    print("Ita boot dewasa ona!")
else:
    print("Ita boot seidauk dewasa!")


print("==========")
# Operador kondisaun sira
# hodi halo kondisaun, baibain utiliza operador mak hanesan:

# Operador	  Exemplo	         Signifika
#    ==	    idade == 18	        hanesan mos
#    !=	    idade != 18	        la hanesan ho
#    >	    idade > 18	        boot liu husi
#    <	    idade < 18	        kiik liu husi
#    >=	    idade >= 18	        boot liu ka hanesan
#    <=	    idade <= 18	        kiik liu ka hanesan 

# ITA MOS BELE HALO KONJUNTO KONDISAUN HO (and, or no not)

# EXEMPLU:

idade = 19
naran = "Binda"

if idade >= 19 or naran == "Dito":
    print("Nia naran: ", naran, "ho idade: ",idade)
else:
    print("la ihaa dados ida hanesan ne'e!")