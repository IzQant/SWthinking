import sys
import math
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
Y, M, D = map(int, sys.stdin.readline().split())
Y = Y-1
M = M-1
days = Y*365
days = days + int(math.floor(Y/4))#floor는 내림
days = days - int(math.floor(Y/100))
days = days + int(math.floor(Y/400))
for i in range(0, M):
    days = days+date[i]
days = days+D
days = days-1
result = days%7
print(weeks[result])
#교수님 질문