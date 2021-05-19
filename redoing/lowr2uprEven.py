lowr=int(input("enter lower limit:"))
uppr=int(input("enter upper limit:"))
#flag=0
for i in range(lowr,uppr+1):
    if(i%2==0):
        #flag==1
        print(i, "is an even number..!!")
        i+=1
    else:
        print(i, "is an odd number..!!")
        #flag==0
        i+=1
#if(flag==1):

#elif(flag==0):
