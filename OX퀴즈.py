N = int(input())
c = 0
cl = []
for i in range(1, N+1):
    string = input()
    L = list(string)
    for j in L:
        if j == 'O':
            c = c + 1
            cl.append(c)
        else:
            c = 0
            cl.append(c)
    print(sum(cl))
    cl = []




