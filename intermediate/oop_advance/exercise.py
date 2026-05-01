class Funsionario:
    def __init__(self, naran, salario):
        self.naran = naran
        self.__salario = salario

    def salario_sae(self, persent):
        self.__salario = self.__salario * (1 + persent / 100)


    def info(self):
        print(f"funsionario naran: {self.naran} nia salario hetan: {self.__salario}")

class Manager(Funsionario):
    def __init__(self, naran, salario, departamento):
        super().__init__(naran, salario)
        self.depart = departamento
    
    def info(self):
        super().info()
        print(f"Departamento: {self.depart}")


f = Funsionario("Ana", 2000000)
f.info()
f.salario_sae(10)
f.info()

print("---")

m = Manager("Joao", 5000000, "TI")
m.info()
m.salario_sae(20)
m.info()



