f = open("C:\\Users\\sonic\\projectbyyanjya\\소프트웨어적사고\\Vocabulary.txt", 'r')

w_list = f.read().split()
word_3_gram = {}

for i in w_list:
    for j in range(len(i)-2):
        gram = i[j:j+3]
        if gram not in word_3_gram:
            word_3_gram[gram] = 1
        else:
            word_3_gram[gram] += 1
print(word_3_gram)
result = dict(sorted(word_3_gram.items(), key = lambda x:x[1], reverse = True))