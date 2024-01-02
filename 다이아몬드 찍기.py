input = __import__('sys').stdin.readline

n = int(input())
stars, space = 1, n-1

for i in range(2*n-1):
    for j in range(space):
        print(end = ' ')
    for j in range(stars):
        if j % 2 == 0:
            print(end='*')
        else:
            print(end = ' ')
    print()
    if i < n-1:
        stars += 2
        space -= 1
    else:
        stars -= 2
        space += 1
