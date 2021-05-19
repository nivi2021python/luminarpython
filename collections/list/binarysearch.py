lst=[12,3,1,6,55,76,55]
print(lst )
lst.sort()
element=int(input("enter the element to b searched:"))
#print(lst)
flag=0
low=0
upp=len(lst)-1

while(low<=upp):
    mid=(low+upp)//2
    if (element>lst[mid]):
        low=mid+1
    elif (element<lst[mid]):
        upp=mid-1
    elif (element==lst[mid]):
        flag=1
        break
if (flag>0):
    print("element found in list")
else:
    print("element not found in list")
