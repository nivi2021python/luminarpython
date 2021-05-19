cday=int(input("enter current day:"))
cmon=int(input("enter current month:"))
cyear=int(input("enter current year:"))
print("current date is:",cday,"-",cmon,"-",cyear)
bday=int(input("enter your birth date:"))
bmon=int(input("enter your birth month:"))
byear=int(input("enter your birth year:"))
print("your birthday is on:",bday,"-",bmon,"-",byear)
years=cyear-byear
if(cmon==bmon):
    if (cday>bday):
      age=years
      print("age is",age)
    elif(cday<bday):
        age=years-1
        print("age is",age)
    elif(cday==bday):
        age=years
        print("age is",age)
elif(cmon>bmon):
    age=years
    print("age is",age)
elif(cmon<bmon):
     age=years-1
     print("age is",age)