sub1=int(input("enter first subject mark"))
sub2=int(input("enter second subject mark"))
sub3=int(input("enter third subject mark"))
sub4=int(input("enter fourth subject mark"))
total=sub1+sub2+sub3+sub4
if(total>=180)&(total<=200):
    print(total,"falls in A+")
elif(180>total>=160):
    print(total,"falls in A")
elif(140<=total<160):
    print(total, "falls in B+")
elif (120<=total<140):
    print(total, "falls in B")
elif (100<=total<120):
    print(total, "falls in C+")
elif (80<=total<100):
    print(total, "falls in c")
elif (60<=total<80):
    print(total, "falls in D+")
else:
    print(total,"is FAIL")