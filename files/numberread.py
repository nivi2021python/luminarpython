f=open("numbers","r")
lst=[]
sum=0
for num in f:
    lst.append(int(num))
print(lst)
for i in lst:
    sum=sum+i
print(sum,"is the sum")