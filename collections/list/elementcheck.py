lst=[10,33,55,23,45,7,78,89]
print(lst)
element=int(input("enter the element to b checked in list:"))
flag=0
for i in lst:
    if(i==element):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("element found")
elif(flag==0):
    print("element not found")



