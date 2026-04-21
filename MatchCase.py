print()

day = int(input("Haftanin kacinci gununu ogrenmek istersin: "))
match day:
    case 1:
        print("pazartesi")
    case 2:
        print("sali")
    case 3:
        print("carsamba")
    case 4:
        print("persembe")
    case 5:
        print("cuma")
    case 6:
        print("cumartesi")
    case 7:
        print("pazar")
    case _:
        print("gecerli gun sayisi girmediniz")
print()

day = int(input("Enter a number (1-7): "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("this is weekday")
    case 6 | 7:
        print("this is weekend")

print()
"""
Ornek cikti:

Haftanin kacinci gununu ogrenmek istersin: 5
cuma

Enter a number (1-7): 6
this is weekend
"""
