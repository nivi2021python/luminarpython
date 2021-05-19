#fibonacci series
num=int(input("enter number of elements:"))
a=0
b=1
if num<=0:
    print("the series is",a)
else:
    print(a,b,end=" ")
    for i in range(2,num):
        nxt=a+b
        print(nxt,end=" ")
        a=b
        b=nxt