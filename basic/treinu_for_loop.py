# tuir mai ita sei aprende halo tabuada uza for loop
# antes ne ita sei koalia konaba parameter sira ne'ebe iha range nia laran nee mak
# range(start)
# range(start, stop)
# range(start, stop, step)

print("==Ezemplu primeiro==")
for i in range(0, 11, 2): # nia sei fo sai numeru ne'ebe liu etapa 2
     print(i) # nia output sei sai 0, 2, 4, 6, 8, 10 antes tama 11

print("==Ezemplu segundo==")
# iha ezemplo ida ne'e ita atu fo sai tabuada numero 3 nian
numeru = 3

for i in range(1, 10): # range sei hahu husi numeru 1 no to 9 antes atu tama 10 tamba iha ne'eba fo sai stop = 10
     result = numeru * i

     print(numeru ,"*", i ,"=", result)


print("==Ezemplu terceiro==")
# atu fo sai numero par no impar

for i in range(1, 21): # fo sai numeru 1 to 20
     
    if i % 2 == 0: # karik numero i modulu 2 restu 0 entaun
          print(i ,"numero par") # fo sai numero par
    
    else: # selae
     print(i ,"numero impar") # fo sai numero impar
print("==Ezemplu quarto==")
# fo sai numero sira ne'ebe dividi ba 3 mak resto 0 entaun fo sai Fizz karik dividi ba 5 mak nia 0 fo sai Buzz no dividi ba sira nain rua mak 0 entaun FizzBuzz selau laos FizzBuzz

for i in range(1, 21):

    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")

    elif i % 3 == 0:
        print(i ,"Fizz")

    elif i % 5 == 0:
        print(i, "Buzz")
    
    else:
        print(i ,"Laos FizzBuzz!")

