import re
x="[0-9]"
matcher=re.finditer(x,"ab cuh32")
for i in matcher:
    print ( i.start())
    print (i.group())
