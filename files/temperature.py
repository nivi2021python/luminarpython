f=open("E:\WORD DOCUMENTS\Temperature","r")
dic={}
var=0
for temp in f:
    data=temp.rstrip("\n").split(" ")
    print(data)
    year=data[0]
    temp=data[1]
    if (year not in dic):
        dic[year]=data[0]
        dic[temp]=data[1]

for year,temp in dic.items():
    print(year,",",temp)
