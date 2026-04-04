# saida mak modules?
# exemplo ita tein - ita laos halo bumbbu sira husi 0 maibe ita hola tiha bumbu sira ne'ebe sai ona iha toko

# nahh module mos hanesan:
# daripada ita halo mesak husi 0
# uza deit kode ne'ebe ema halo ona

# iha tipo 3 module:
# 1. Built-in module       - iha tiha ona iha python, hein uza
# 2. Third-party           - presiza install lai uza pip
# 3. Custom modules        - ita mak halo rasik


# 1. Built-in Modules - ida ne'ebe uza deit

# math - operasaun matematika

import math
print(math.pi)           # → 3.14159...
print(math.sqrt(16))     # → 4.0  (raiz kuadradu)
print(math.ceil(4.3))    # → 5    (aredonda ba boot)
print(math.floor(4.9))   # → 4    (aredonda ba kiik)
print(math.pow(2, 3))    # → 8.0  (2 elevado 3)

# random - numeru acakan

import random
print(random.randint(1, 10))    # → numeru acak 1-10
print(random.choice(["apel", "mangga", "jeruk"]))  # → hili acak


# datetime - data no oras

from datetime import datetime

agora = datetime.now()

print(agora)                        # → 2026-03-29 10:30:00
print(agora.strftime("%d-%m-%y"))   # → 29-03-2026


# os - operasaun file & folder

import os

print(os.getcwd())          # → lokasi folder agora
print(os.listdir())         # → list file hotu hotu iha folder nia laran



# maneira import ne'ebe diferente
# Import module hotu hotu
import math
print(math.sqrt(16))       # → tenke tau math iha nia oin

# Import spesifik
from math import sqrt
print(sqrt(16))            # → langsung tau laho math.

# Import ho alias (naran_badak)
import datetime as dt
print(dt.datetime.now())   # → uza dt. laos datetime.

# Import hotu hotu ←!
from math import *
print(sqrt(16))            # → bele langsung uza


# 3. custom module - ita mak halo rasik
# ida ne'e mak relevan ba ita nia project

# exemplo ita halo file rua:

# file kalkulator.py

# def mais(a,b):
#     return a + b
# def menus(a,b):
#     return a - b

# file main
# import kalkulator

# resultado = kalkulator.mais(10, 5)
# print(resultado)

# ita bele uza function husi file seluk laho hakerek ulang

# 4. third-party Modules - install lai uza pip

# pip install pandas
# pip install numpy

# depois mak ita import iha python 

# import pandas as pd
# import numpy as np

# # ida ne'e mak sei ita uza dala barak iha "data engineering"!

# # relasaun ho data engineering
# import pandas    → jere data CSV & Excel
# import numpy     → computing numeru
# import requests  → foti data husi internet
# import sqlalchemy → koneksaun ho database



# treinu
# level1

print(math.sqrt(144))
print(math.ceil(7.3))
print(math.floor(7.9))



# level2
# numero = input("siik numero entre 1 ate 10: ")
numero_acak = random.randint(1, 10)
while True:
    numero = int(input("siik numero entre 1 ate 10: "))
    if numero == numero_acak:
        print(f"{numero} los")
        break
    else:
        print("numeru sala!")







