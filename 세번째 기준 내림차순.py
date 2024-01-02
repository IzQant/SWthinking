a = [("k2", 2010, 93), ("k3", 206, 73), ("k1", 2004, 84)]
a.sort(key=lambda x:x[2], reverse=True)
print(a)