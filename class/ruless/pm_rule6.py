import re
x="\W"
matcher=re.finditer(x,"ab cu# h%32e")
for i in matcher:
    print ( i.start())
    print (i.group())
