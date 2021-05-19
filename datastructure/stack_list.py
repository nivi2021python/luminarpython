stack=[]
top=0
size=int(input("enter the size:"))
n=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("enter the elements that need to be pushed"))
        stack.append(p)
        top+=1
        print(stack)
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stack.pop()
        top-=1
        print(stack)
while(n!=1):
    print("enter the operations u want to perform:")
    opt=int(input("press:: 1)push 2)pop "))
    if opt==1:
        push()
    elif opt==2:
        pop()
