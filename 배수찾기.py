cnt  = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        cnt += i
print(cnt)
