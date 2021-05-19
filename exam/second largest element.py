#second largest element from a list
a=[]
n=int(input("enter number of elements:"))
for i in range(1,n+1):
    b=int(input("enter elements in list:"))
    a.append(b)
print(a)
for i in a:
    if i>