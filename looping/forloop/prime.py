num=int(input("enter the number:"))
#i=2
flag=0
for i in range(2,num):
    if(num%i==0):
       # print(num,"is not a prime")
        flag=1
   # else:
      #  flag=0
if(flag>0):
    print("is not a prime")
else:
    print("is a prime")