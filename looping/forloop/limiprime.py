lim=int(input("enter the limit:"))
#num=int(input("enter the number:"))
#i=2
#flag=0
for l in range(2,lim+1):
    for i in range(2,l):
        if (l%i ==0):
            # print(num,"is not a prime")
            break
        else:
            print(l)

