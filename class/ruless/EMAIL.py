import re
n=input("enter ur inputt")
x="([a-zA-Z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9]+$)"
match = re.fullmatch(x,n)
if match is not None:
     print("valid input")
else:
    print("invalid input")