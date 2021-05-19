lst=[2,1,5,6,8,7]
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)