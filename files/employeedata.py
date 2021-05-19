f=open("E:\WORD DOCUMENTS\customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    fname=data[1]
    age=data[3]
    cou=data[-1]
    lst=([fname,age,cou])
    for items in lst:
        if(lst[2]=="india"):
           print(lst)