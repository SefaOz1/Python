print()

print("input a number: ")
number = int(input())

for x in range(1, 11):
    for y in range(1, number + 1):
        print(y, 'X', x, "=", y * x, end=', ')
    print()

print()
"""

output for number = 3:

1 X 1 = 1, 2 X 1 = 2, 3 X 1 = 3, 
1 X 2 = 2, 2 X 2 = 4, 3 X 2 = 6, 
1 X 3 = 3, 2 X 3 = 6, 3 X 3 = 9,
...
...

"""
