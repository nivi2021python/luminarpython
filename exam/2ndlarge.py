lst=[100,200,39,43,22,12,65,44,73]
print("original list is",lst)
length=len(lst)
print("length of list is",length)
i=0
j=0
for i in range(length):
    for j in range(i+1,length):
       if(lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("sorted list is",lst)
print("second largest element is:",lst[length-2])