import sys
import math
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
Y, M, D = map(int, sys.stdin.readline().split())
normal = 0
leap = 0
days = 0
for i in range(1, Y):
    if (i%400 == 0) or ((i%4 == 0) and (not (i%100 == 0))):
        leap += 1
    else:
        normal += 1
for j in range(0, M):
    if (Y%400 == 0) or ((Y%4 == 0) and (not (Y%100 == 0))):
        date[1] = 29
        days = days+date[j]
    else:
        days = days+date[j]
result = (leap*366+normal*365+days+D)%7
print(weeks[result])
