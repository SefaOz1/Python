print()

import time

kirilacak_sifre = "3612"
denenen_sifre_elemanlari = "0123456789"
flag_1 = False

print("KOMBINASYONLAR DENENIYOR:")

# kirilacak sifrenin 4 basamaktan ve rakamlardan olustugunu biliyoruz varsayalim
for basamak_1 in denenen_sifre_elemanlari:
    for basamak_2 in denenen_sifre_elemanlari:
        for basamak_3 in denenen_sifre_elemanlari:
            for basamak_4 in denenen_sifre_elemanlari:
                kombinasyon = basamak_1 + basamak_2 + basamak_3 + basamak_4
                print(f"Kombinasyon: {kombinasyon}")
                time.sleep(0.001)

                if kombinasyon == kirilacak_sifre:
                    print("            ---BULUNDU---")
                    print(f"Sifre = {kombinasyon}")
                    flag_1 = True
                
                if flag_1 == True:
                    break
            if flag_1 == True:
                    break
        if flag_1 == True:
                    break
    if flag_1 == True:
                    break

print()
"""
Ornek cikti:

KOMBINASYONLAR DENENIYOR:
Kombinasyon: 0000
Kombinasyon: 0001
Kombinasyon: 0002
Kombinasyon: 0003
Kombinasyon: 0004
...
...
...
Kombinasyon: 3608
Kombinasyon: 3609
Kombinasyon: 3610
Kombinasyon: 3611
Kombinasyon: 3612
            ---BULUNDU---
Sifre = 3612
"""
