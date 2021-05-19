num=int(input("enter the number:"))  #num=5
flag=0                               #flag=0
for i in range(2,num):               #i=2              i=3            i=4             i=5
    if(num%i==0):                    #5%2=1 flag=0     5%3=2 flag=0   5%4=1 flag=0
        flag=1

    # else:
    #     flag=0
    #     #i+=1

if(flag==0):
    print(num,"is a prime number")
elif(flag==1):
    print(num,"is not a prime number")




