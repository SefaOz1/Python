print()

satir = 1

yukseklik = int(input("ucgenin yuksekligini giriniz: "))

# Ucgenin ilk satiri:
for x in range(1, yukseklik):
    print(" ", end='')  # yani yukseklik - 1 kadar bosluk birak
print("X")
satir += 1

# Ucgenin orta kismi:
for y in range(1, yukseklik - 1): # yukseklik - 2 (ilk ve son satir) kadar
    for z in range(1, yukseklik - satir + 1):
        print(" ", end='')
    print('X', end='')

    for a in range(1, (2 * (satir - 1))):
        print(" ", end='')  # iki 'X'in arasindaki bosluklar
    print('X')
    satir += 1

# Ucgenin alt kismi:
for b in range(1, yukseklik * 2):
    print("X", end='')

print()
"""
ornek cikti:

ucgenin yuksekligini giriniz: 5
    X
   X X
  X   X
 X     X
XXXXXXXXX
"""
