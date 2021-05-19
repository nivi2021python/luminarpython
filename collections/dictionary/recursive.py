word="ABCDBCA"
for char in word:
    print(char)
dic={}
for char in word:
    if(char not in dic):
        dic[char]=1
    else:
        print("first recursive character",char)
        break