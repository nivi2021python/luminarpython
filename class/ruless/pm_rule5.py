import re
x="[^a-zA-Z0-9]"
matcher=re.finditer(x,"ab#cuh$32")
for i in matcher:
    print ( i.start())
    print (i.group())
