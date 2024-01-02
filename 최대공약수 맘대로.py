import math
A = int(input())
B = int(input())
l = []
for i in range(1, A + 1):
    if A % i == 0:
        l.append(i)
for i in range(1, B + 1):
    if B % i == 0:
        l.append(i)
R = []
for v in l:
    if l.count(v) != 1:
        R.append(v)
print(max(R))
        
        




