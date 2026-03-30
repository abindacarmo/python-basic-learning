# slicing mak hanesan metodo ida ne'e mak ita uza hodi foti deit teks balun

# numeru kartaun kreditu: "1234567890123456"
# ida ne'ebe mak bele fo sai:  "************3456"
# ← so 4 digit ikus deit mak ita bele fo sai!

# hanoin hetan index ida uluk ne katak
# kada karakter idak idak iga nia numeru pozisaun idak idak

# exemplo
# naran = "Abinda"
#          012345 index husi karuk(pozitivu)

#          -6-5-4-3-2-1 index hudi los(negativu)

# ninia strukture[Start:stop]
# hahu            hahu  para

# exemplo

naran = "Abinda"
print(naran[0:3]) # → "Abi"   husi index 0 to 2
print(naran[2:5]) # → "ind"   husi index 2 to 4
print(naran[0:6]) # → "Abinda" hotu-hotu


# shortcut ne'ebe baibain uza
naran = "Abinda"
print(naran[:3])    # → "Abi"    husi inisiu to index 2
print(naran[3:])    # → "nda"   husi index 3 to ikus
print(naran[-4:])   # → "inda"   karakter 4 ikus
print(naran[:-2])   # → "Abind"  hotu hotu excepto 2 ikus

# exemplo real - subar kartaun kreditu
kartaun = "1234567890123456"

safe = "*" * 12 + kartaun[-4:]
print(safe)
# → "************3456" ✅

# exemplo real - foti tangal balun
dia = "2026-03-29"

tinan = dia[:4]     # → "2026"
fulan = dia[5:7]    # → "03"
loron  = dia[8:]     # → "29"

print(f"tinan: {tinan}")
print(f"fulan: {fulan}")
print(f"loron : {loron}") # iha data engineering ida ne'e mak baibain ema uza hodi jere dados kalendar

# bele uza step mos hotu
teks = "Abinda"

print(teks[::2])    # → "Aid"   foti kada karakter 2
print(teks[::-1])   # → "adnibA" string fila!


# treinu
# level1
naran1 = "Abinda Carmo"
print(naran1[0:6])
print(naran1[-5:])

# level2
kartaun1 = "1234567890123456"
aman = "*" * 12 + kartaun1[-4:]
print(aman)


# level3
dia = "2026-03-29"
print(f"Tinan {dia[0:4]}")
print(f"Fulan {dia[5:7]}")
print(f"loron {dia[8:]}")

print(f"Ohin loron  {dia[8:]} fulan {dia[5:7]} tinan {dia[0:4]}")

