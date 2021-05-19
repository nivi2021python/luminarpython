num1=input("enter first number")
num2=input("enter second number")
num3=input("enter third number")
if(num1>num2) & (num1>num3):
    if(num2>num3):
        print(num2,"is second largest")
    else:
        print(num3,"is second largest")
elif(num2>num3)&(num2>num1):
    if(num3>num1):
        print(num3,"is second largest")
    else:
        (num1,"is second largest")
elif(num3>num2)& (num3>num1):
    if(num2>num1):
        print(num2,"is second largest")
    else:
        print(num1,"is second largest")