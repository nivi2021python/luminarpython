import re
n=input("enter ur inputt")
x="[K][L]\d{2}[A-Z]{2}\d{4}$"
match = re.fullmatch(x,n)
if match is not None:
     print("valid input")
else:
    print("invalid input")