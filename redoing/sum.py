lowr=int(input("enter lower limit:"))
uppr=int(input("enter upper limit:"))
#flag=0
sumeve=0
sumodd=0
for i in range(lowr,uppr+1):
    if(i%2==0):
        #flag==1
        print(i, "is an even number..!!")
        sumeve=sumeve+i
        i+=1
    else:
        print(i, "is an odd number..!!")
        sumodd=sumodd+i
        #flag==0
        i+=1
print("sum of even numbers is",sumeve)
print("sum of odd numbers is",sumodd)