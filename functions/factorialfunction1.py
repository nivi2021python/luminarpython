#factorial using function method 1
def factorial():
    num=int(input("enter number:"))
    fact=1
    for i in range(1,num+1):
      fact*=i
    print(fact)
factorial()