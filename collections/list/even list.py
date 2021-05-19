lst=[33,98,65,43,44,21,48]
even_lst=[]
for i in lst:
    if (i%2==0):
        even_lst.append(i)
        #print(i,"is an even number..!!")
        continue
print(even_lst)
