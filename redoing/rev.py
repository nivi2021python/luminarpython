num=int(input("enter number to b reversed:"))
res=0
while(num>0):
    dig=num%10
    res=(res*10)+dig
    num=num//10
print("reverse number is",res)

