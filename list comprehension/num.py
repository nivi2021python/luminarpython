lst=[3,5,8,2,9]
new_lst=[num+1 if num>5 else num-1 for num in lst]
print(new_lst)