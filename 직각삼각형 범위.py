answer = 0
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, min(101, a+b)):
            if a**2 + b**2 == c**2:
                print("a = {} b = {} c = {}".format(a, b, c))
                answer += 1
print("삼각형 갯수 = {}".format(answer))