lst=[3,4,8]
sum=0
low=3
mid=4
upp=8
for i in lst:
    sum=sum+i
print(sum)
new_lst=[sum-low,sum-mid,sum-upp]
print(new_lst)