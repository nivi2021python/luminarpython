sal=int(input("enter your salary"))
service=int(input("enter number of years worked"))
if(service>5):
    bon=(((5/100)*sal)+sal)
    print("new salary is",bon)
else:
    print("service is less than 5 years so no change in salary")