arr=[1,2,3,4,5,6]
from functools import *
sum=reduce(lambda num1,num2:num1+num2,arr)
print(sum)

highest=reduce(lambda num1,num2: num1 if num1>num2 else num2,arr)
print(highest)