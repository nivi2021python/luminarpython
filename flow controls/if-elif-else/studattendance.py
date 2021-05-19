held=int(input("enter number of classes held"))
attended=int(input("enter number of classes attended"))
percent=((attended/held)*100)
if(percent<75):
    print(percent,"percent so student is not allowed to write exam")
else:
    print(percent,"percent so student can attend exam")