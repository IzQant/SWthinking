lst = [j for j in range(1, 6)]
for i in lst:
    if (6-i) - i >= 0:
        print("(%d, %d),"%(i, 6-i), end=' ')
