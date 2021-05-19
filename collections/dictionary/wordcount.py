line=("hai hello hai hello hai hello")
print(line)
words=line.split(" ")
print(words)
count=0
countt=0
for i in words:
    if i=="hai":
        count+=1
    elif i=="hello":
        countt+=1

print("hai",",",count)
print("hello",",",countt)