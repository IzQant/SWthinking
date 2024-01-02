input = __import__('sys').stdin.readline
str1 = input()
l = []
for i in str1:
    if 96 < ord(i) < 123:
        l.append(ord(i)-32)
    elif 64 < ord(i) < 91:
        l.append(ord(i)+32)

lst = list(chr(j) for j in l)

print("".join(lst))
