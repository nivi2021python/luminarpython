f=open("E:\WORD DOCUMENTS\customer","r")
dic={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    profession=data[4]
    #print(profession)
    #for prof in profession:
    if profession not in dic:
       dic[profession]=1
    else:
       dic[profession]+=1
for k,v in dic.items():
    print(k,",",v)