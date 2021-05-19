age=int(input("enter age"))
sex=input("enter sex")
marital=input("enter marital status")
if(sex=='F'):
    print("employee have to work in urban areas only")
elif((sex=='M') & (20<=age<40)):
    print("employee can work anywhere")
elif((sex=='M') & (40<=age<=60)):
    print("employee have to work in urban areas only")
else:
    print("error")