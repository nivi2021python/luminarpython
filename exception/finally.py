a=[1,78,87,54]
b=int(input("enter index"))

try:
    print(a[b])
except:
    print("index error")
finally:
    print("inside finally")   #finally block works always