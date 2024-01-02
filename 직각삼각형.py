n = int(input('n>'))
number = 1
for i in range(1, n+1):
    for j in range(i, 2*i):
        print(number, end=" ")
        number += 2
    print()
