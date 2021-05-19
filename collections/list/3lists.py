lst=[]
lstodd=[]
lsteve=[]
for i in range(1,101):
    lst.append(i)
    #print(lst[i])
for i in lst:
    if(i%2==0):
        lsteve.append(i)
    else:
        lstodd.append(i)
print(lst)
print(lstodd)
print(lsteve)
