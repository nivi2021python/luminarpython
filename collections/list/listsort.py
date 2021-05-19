lst=[80,20,30,23,45,90]
length=len(lst)
for i in range(length):
    for j in range(i+1,length):
        if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("elements after sorting is",lst)
