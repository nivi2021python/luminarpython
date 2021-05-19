lst=[50,70,29,10,78,65,32,99]
print(lst)
small=lst[0]
for i in lst:
    if(i<small):
        small=i
        continue
print("smallest number is:",small)