f1=open("daemon","r")


f2=open("daemoncopy","w")
#f.write(daemon)
for i in f1:
    f2.write(i)
print(f2)