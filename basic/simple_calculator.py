# tuir mai sei aprende halo calculator basika ida ne'ebe iha operasaun haat: (+, -, *, /)

# tuir mai ita sei uza function input() mak hanesan built-in fuction(funsaun ne'ebe iha nanis ona wainhira ita utiliza python) ne'ebe ita bele prense buat ruma ho manual
a = int(input("input numeru 1: ")) # ita uza int() atu nune'e bele input numeru integer laos string, karik ita la uza int numeru ne'ebe ita prense sei sai string automatikamente
b = int(input("input numeru 2: "))
operasaun = input("hili operasaun(+, -, *, /): ")

def mais(a, b):
    return a + b


def menus(a, b):
    return a - b


def vezes(a, b):
    return a * b


def dividir(a, b):
    return a / b



if operasaun == "+":
    maiss = mais(a, b)
    print("resustado: ", maiss)

elif operasaun == "-":
    menuss = menus(a, b)
    print("resustado: ", menuss)

elif operasaun == "-":
    vezess = vezes(a, b)
    print("resustado: ", vezess)

else:
    dividirr = dividir(a, b)
    print("resultado: ", dividirr)

