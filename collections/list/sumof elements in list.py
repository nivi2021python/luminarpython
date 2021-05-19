lst=[5,9,6]
print(lst)
sum=0
low=5
mid=9
upp=6
for i in lst:
    sum=sum+i
print(sum)
new_lst=[sum-low,sum-mid,sum-upp]
print(new_lst)
