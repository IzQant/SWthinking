remainder = 0
decimal_num = 23
binary_num = ""
while decimal_num != 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num = decimal_num // 2