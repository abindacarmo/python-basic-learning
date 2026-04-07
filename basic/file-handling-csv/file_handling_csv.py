# # saida mak file handling CSV
# CSV = comma separated values
# file teks baibain contain dados sira ne'ebe separa husi virgula 

# exemplo, file estudante.csv:
# naran,tinan,municipio
# Abinda,22,Dili
# Dito,20,Baucau
# Maria,18,Suai

# format sira ne'e mak baibain uza iha data engineering hodi rai no haruka dados sira

# tamba saida mak csv ne'e importante

# Excel    → so bele loke no haree husi deit excel
# CSV      → bele loke iha excel, python, database, whatever ✅

# iha buat rua ne'ebe prinsipal 
# 1. lee file CSV   → read
# 2. hakerek file CSV   → write

# exemplo:
# ita hakarak sai hanesan data engineering iha kompana ida. loron loron ita hetan file CSV.
# nia containing data transaksaun mak hanesan:

# data,naran,total
# 2026-03-01,Abinda,500000
# 2026-03-01,Dito,300000
# 2026-03-02,Maria,750000


# ita nia servisu:
# 1. lee file CSV Refere
# 2. jere data 
# 3. rai nia resultado ba iha file CSV foun

# KONSEITU FILE - loke, read, Close
# antes lee file, imaggina hanesan kadernu:

# 1. lee kadernu - open()
# 2. lee nia containg - read()
# 3. taka buku - close()

# solusaun - uza (with)

# python iha nia maneira rasik ne'ebe aman - uza with:

# with - loke file, uza, taka automatiku!
#         la presiza hanoin taka manual


# mode loke file:
# "r" - read - lee file Sira.
# "w" - write - hakerek file(hamoos containt uluk)
# "a" - append - aumenta data iha kraik (la hamoos)


import csv # hein import deita, iha tiha ona iha python

# iha tools prinsipar rua iha modul csv mak hanesan:

# cvs.reader  - hodi lee file csv
# csv.writer - hodi hakerek file csv

# flow hodi bele lee file csv

# # loke file estudante.csv-csv.reader lee linha por linha-kada lina sai LIST-["Abinda", "22", "Dili"]-jere dados

# flow hodi hakerek file csv
# # prepara dados iha list nia laran-loke file foun-csv.writer hakerek lina por lina-file csv rai ona

# relasiona ho ida ne'ebe ita aprende ona
# list         → kada lina csv sai list
# dictionary   → bele lee csv sai dictionary
# for loop     → hodi lee lina por lina
# string       → gere dados testu iha csv
# try/except   → kuando file la hetan

