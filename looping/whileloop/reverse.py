num=int(input("enter the number"))
print("the number is",num)
rev=0
while(num>0):
    dig=num%10
    rev=(rev*10)+dig
    num=num//10
print("reverse number is",rev)
