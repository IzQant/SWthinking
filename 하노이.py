input = __import__('sys').stdin.readline
def hanoi(n, s, m, e):
    if n == 1:
        print("%d : %c -> %c" %(n, s, e))
    else:
        hanoi(n-1, s, e, m)
        print("%d : %c -> %c" %(n, s, e))
        hanoi(n-1, m, s, e)
n = int(input())
hanoi(n, 'a', 'b', 'c')