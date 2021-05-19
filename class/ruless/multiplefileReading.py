class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def print_studdet(self):
        print(self.name)
        print(self.roll_no)
    def __str__(self):
        return self.name
f=open("../stud_det", "r")
for i in f:
    data=i.rstrip("\n").split(",")
    print(data)
    name=data[0]
    roll_no=data[1]
    obj=Student(name,roll_no)
    print(obj)
    obj.print_studdet()
