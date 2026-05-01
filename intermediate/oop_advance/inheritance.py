# inheritance ka gerasaun mak hanesan ita bele bolu "blueprint" geral, maibe nia spesifiku liu


# exemplo iha animal(geral) maibe se print sai asu ka busa sira ne'e mak ita bolu dehan espesifiku

# Hewan (geral)
# ├── Asu (spesifik)
# └── Busa (spesifik)

# asu no busa gerasaun husi animal nia hahalok, maibe bele iha behaviour sira seluk.

class Animal: # ita kria Super class
    
    def __init__(self, naran):
        self.naran = naran

    def han(self):
        print(f"{self.naran} han naan!")

class Asu(Animal): # ita kria sub class ida no extend husi super class
    def hatenu(self):
        print(f"{self.naran} bele hatenu: auuuu auuuu")


asu = Asu("Desi")

asu.han()
asu.hatenu()


print("=========utiliza super()===========")


class Busa(Animal): # ita kria sub class ida no extend husi super class
    def __init__(self, naran, rasa):
        super().__init__(naran) # super() signifika ita bele bolu variable husi parent mai iha child class sira, 
        self.rasa = rasa        # exemplo super() dehan: "bolu uluk parent nian mak bolu hau nian"
    

busa = Busa("muti", "Mutin")
print(busa.naran) # wainhira ita bolu deit variable entaun la presiza uza () ex: los: busa.naran, sala: busa.naran(), so ita bolu funsaun mak ita ble aumenta () hanesan asu.han(), tamba han ne'e function/method ida iha class ida nia laran
print(busa.rasa)




