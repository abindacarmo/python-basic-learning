# iha ne'e ita sei aprende konba custome_models ne'ebe funcion ida ita rasik mak sei halo no sei bolu ba iha file sira seluk
# nia function sira ne'e ita sei halo iha file ida ne'e no ita sei bolu ba iha file string_utils.py ne'ebe iha mos folder ne'ebe hanesan nia laran

def hamoos_teks(teks):
    hamoos = teks.strip().lower()
    return hamoos

def sura_liafuan(teks):
    teks_moss = teks.strip()
    list_liafuna = teks_moss.split(" ")
    return len(list_liafuna)


def fila_letra(teks):
    fila = teks[::-1]
    return fila



# bainhira mak ita bele uza return?

# nia konseitu basica mak:
#     fo resultadu husi function atu nune'e bele utiliza iha liur