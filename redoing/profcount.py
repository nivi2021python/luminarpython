f=open("E:\WORD DOCUMENTS\customer","r")
d={}
for line in f:
    dta=line.rstrip("\n").split(",")
    dp=dta[4]
    if dp not in d:
        d[dp]=1
    else:
         d[dp]+=1
print(d)