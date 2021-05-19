low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))
sum1=0
sum2=0
for i in range(low,upp+1):
    if(i%2==0):
        print("even",i)
        sum1=sum1+i
        i+=1
    else:
        print("odd",i)
        sum2=sum2+i
        i+=1

print("sum of even numbers is", sum1)
print("sum of odd numbers is",sum2)
