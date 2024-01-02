list = []
i = 0
N = int(input())
print("side:", N)
for i in range(N):
    a = int(input())
    list.append(a)
if N == 3:
    if list[0]**2 + list[1]**2 > list[2]**2:
        print("acute triangle")
    elif list[0]**2 + list[1]**2 == list[2]**2:
        print("right triangle")
    else:
        print("obtuse triangle")
if N == 4:
    Sf = sum(list)
    if Sf/N == a:
        print("square")
    else:
        print("rectangle")
if N > 4:
    S = sum(list)
    if S/N == a:
        print("right",N)
    else:
        print(N)





