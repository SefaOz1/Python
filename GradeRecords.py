print()

notlar = {}  # bos dictionary

adet = int(input("kac ogrenci ve notu girilecek? "))

for x in range(1, adet + 1):
    key = str(input(f"{x}. ogrenci adini giriniz: "))
    value = int(input(f"{x}. ogrenci notunu giriniz: "))

    notlar[key] = value
    print()

print("Girilen bilgiler kaydedilmistir:")
print(notlar)
print()

# 2. ekrana basma yontemi
for x in notlar.items():
    print(x)

print()
"""
Ornek cikti:

kac ogrenci ve notu girilecek? 3
1. ogrenci adini giriniz: Ali
1. ogrenci notunu giriniz: 70

2. ogrenci adini giriniz: Ahmet
2. ogrenci notunu giriniz: 80

3. ogrenci adini giriniz: Muhammed
3. ogrenci notunu giriniz: 90

Girilen bilgiler kaydedilmistir:
{'Ali': 70, 'Ahmet': 80, 'Muhammed': 90}

('Ali', 70)
('Ahmet', 80)
('Muhammed', 90)
"""
