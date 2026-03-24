# Looping controler utiliza atu controla flow looping iha for no while.

# iha keyword prinsipal ne'e mak:
# 1. break
# 2. continue
# 3. pass

print("====BREAK====")
# exemplo break - (hapara loop) sai kedas husi loop, masek kondisaun seidauk hotu
for i in range(10): # hakarak fo sai 0 to 5
    if i == 5: # maibe iha ne'e iha kondisaun karik i = 5
        break # entaun para
    print(i) # no sei fo sai husi 0 to 4

print("====CONTINUE====")
# exemplo continue - haksoit ba iterasaun tuir mai(haksoit liu kode restu iha iterasaun agora, no diretamente kontinya ba iterasaun tuir mai)
for item in range(6): # hakrak fo sai 0, 1, 2, 3, 4, 5
    if i == 2: # maibe iha ne'e iha kondisaun karik i = 2 entaun haksoit liu 2
        continue # kontinua ba iterasaun tuir mai
    print(item) 

# Output: la iha 2 iha output
# 0
# 1
# 3
# 4
# 5

print("====PASS====")

# exemplo pass - la halo buat ruma(placeholder, baibain uza wainhira sintaks python presiza buatruma maibe seidaun hakarak atu hakerek kode)
for i in range(5):
    pass # nia sei la exekuta buat ida

print("====PASS KONTINUASAUN====")
for i in range(5): # hakarak fo sai numeru 0 to 5
    if i == 1: # maibe iha ne'e iha kondisaun katak karik i = 1 entaun para
        pass # maibe iha ne'e ita utiliza controler/keyword pass entaun kondisaun if ne'e lavale
    print(i) # no kode sei ezekuta nafatin 0 to 4
