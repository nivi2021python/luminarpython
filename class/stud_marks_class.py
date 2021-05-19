class Student:
    def __init__(self,name,roll_no,batch,marks):
        self.name=name
        self.roll_no=roll_no
        self.batch=batch
        self.marks=marks
    def print_studdet(self):
        print(self.name)
        print(self.roll_no)
        print(self.batch)
        print(self.marks)
    def __str__(self):
        return self.name
lst=[]
f=open("stud_marks","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    name=data[0]
    roll_no=data[1]
    batch=data[2]
    marks=int(data[3])
    obj=Student(name,roll_no,batch,marks)
    lst.append(obj)
for i in lst:
    if(i.marks>=190):
        print(i)

