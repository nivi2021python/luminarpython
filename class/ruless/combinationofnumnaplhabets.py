#combination of numbers and alphabets
import re
n=input("enter ur inpput:")
x="([a-zA-z]+\d{1}$)"
match = re.fullmatch(x,n)
if match is not None:
     print("valid input")
else:
    print("invalid input")