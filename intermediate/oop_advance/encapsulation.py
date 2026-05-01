# # encapsulation - dados ne'ebe ita salva ka labele modifika arbiru
# dalaruma attribute iha class larang labele modifika arbiru iha liu. maneira uza prefix _ (konvensi: labele asesu diretamente) ka __(subar tiha kedas)

# exemplo:

class RekeningBank:
    def __init__(self, saldo_inisiu):
        self.__saldo = saldo_inisiu

    def setor(self, montante):
        if montante > 0:
            self.__saldo += montante


    def haree_saldo(self):
        return self.__saldo
    
setor_tama = int(input("setor hira: "))

rek = RekeningBank(10000)
rek.setor(setor_tama)

print(rek.haree_saldo())

# print(rek.__saldo) # ida ne'e sei error tamba labele asesu diretamente, tenke liu husi method haree_saldo()


# tuir mai ita sei haree dunder method(magic methods)
# dunder method = double underscore, method spesial ne'ebe python bolu automatiku iha situasaun espesifiku.

# method          bainhira mak bolu
# __init__        wainhira halo object
# __str__         wainhira print(object)
# __len__         wainhira len(object)
# __eq__          wainhira object1 == object2

print("=====koko mehtod spesial=====")
class Product:
    def __init__(self, naran, folin):
        self.naran = naran
        self.folin = folin
    
    def __str__(self):
        return f"{self.naran} - ${self.folin}"
    
    def __eq__(self, other):
        return self.folin == other.folin
    
    

p1 = Product("laptop", 500)
p2 = Product("phone", 139)

print(p1)
# print(len(p1))
print(p1 == p2)









