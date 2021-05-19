class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):
    def __init__(self, roll_no,mark,name,age,gender):
        super().__init__(name,age,gender)
        self.roll_no = roll_no
        self.mark=mark
    def print_stud(self):
        print(self.roll_no)
        print(self.mark)

stu = Student(30,97,"Neha",14,"Female")
stu.printdet()
stu.print_stud()