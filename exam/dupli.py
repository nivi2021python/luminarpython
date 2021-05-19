lst=[20,30,10,40,20,21,10,78,65]
new_lst=[]
dupli_lst=[]
for i in lst:
      if (i!=new_lst):
        new_lst.append(i)
      else:
        continue
for i in lst:
    for j in new_lst:
        if(i==j):
            dupli_lst.append(i)
        else:
            dupli_lst.append(i)

print(new_lst)
print(dupli_lst)

