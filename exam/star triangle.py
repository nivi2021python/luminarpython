#star triangle
row_num=int(input("enter number of rows:"))
x=1
for i in range(0,row_num):
    for j in range(0,x):
        print("*",end=" ")
    x=x+1
    print()