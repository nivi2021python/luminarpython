lowr=int(input("enter lower limit:"))
uppr=int(input("enter upper limit:"))
flag=0
for i in range(lowr,uppr):
    for num in range(2,i):
       if(i%lowr==0):
         flag==1
         i+= 1
    #lowr+=1
       elif(flag==0):
          print("prime",i)
          i+=1
     #lowr+=1
