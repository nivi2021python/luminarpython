#starting with a and ending with b
import re
n=input("enter ur inputt")
x="(^a[a-zA-Z0-9\W]*b$)"
match = re.fullmatch(x,n)
if match is not None:
     print("valid input")
else:
    print("invalid input")