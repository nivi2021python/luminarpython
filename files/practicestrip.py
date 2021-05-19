f=open("practice","r")
words_practice=[]
for words in f:
    print(words)
    words_practice.append(words)
print(words_practice)
for words in words_practice:
    words_split=words.split()
print(words_split)
