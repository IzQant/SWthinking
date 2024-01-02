try:
    f = open(fileName, 'r',encoding="UTF8")
    myDict = {}
    for line in f:
        words = line.split()
        for w in words:
            if len(w) not in myDict:
                myDict[len(w)] = 1
            else:
                myDict[len(w)] += 1
    f.close()
except:
    print("file error")
