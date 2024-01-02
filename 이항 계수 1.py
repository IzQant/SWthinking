N, K = map(int, input().split())
s = 1
S = 1
ss = 1
if 0 <= K <= N:
  for i in range(1, N + 1):
    s *= i
  for j in range(1, K + 1):
    S *= j
  for k in range(1, N-K+1):
    ss *= k
  nk = s // (S * ss)
else:
  print(0)
print(nk)