lst=[50,170,29,10,78,65,32,99]
print(lst)
large=lst[0]
for i in lst:
    if(i>large):
        large=i
        continue
print("largest number is:",large)