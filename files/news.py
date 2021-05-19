f=open("newspaper","r")
news_paper=[]
new_words=[]
num_words=0
for line in f:
    news_paper.append(line)
print(news_paper)
for line in news_paper:
    word=line.split()
    print(word)
for words in word:
    num_words+=1
print("number of words =",num_words)