input = __import__('sys').stdin.readline

n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        if (j == 1):
            x = i
            print(x, end = "")
        else:
            x = x+(n-j+1)
            print(' ', x, end = "")
    print()