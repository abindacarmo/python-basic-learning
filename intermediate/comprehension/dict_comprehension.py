# dict comprehension hanesan mos ho list comprehension maibe nia resultado dictionary {}

naran_list = {"Ana", "Joao", "Maria"}
altura = {naran: len(naran) for naran in naran_list}

print(altura)

# ninia patter ne'e mak
# {key: value for item in iterable}
