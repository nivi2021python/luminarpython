class Person:
        def details(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender

        def printdet(self):
            print(self.name)
            print(self.age)
            print(self.gender)
class Parent(Person):
    def parent_det(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
    def print_parent(self):
        print(self.job)
        print(self.place)
        print(self.salary)
class Child(Person):
    def child(self,school):
        self.school=school
    def print_child(self):
        print(self.school)

class Student(Child):
    def stud_details(self,roll_no):
        self.roll_no=roll_no
    def print_stud(self):
        print(self.roll_no)
per=Person()
ch=Child()
par=Parent()
stud=Student()

per.details("NITHYA",29,"FEMALE")
per.printdet()
ch.details("Kiran",12,"Male")
ch.printdet()
stud.stud_details(31)
stud.print_stud()
ch.child("Amrita Vidyalaya")
ch.print_child()
par.details("Varghese",65,"Male")
par.printdet()
par.parent_det("Railway Officer","Perumbavoor",30000)
par.print_parent()
stud.child("Amrita Vidyalaya")
stud.print_child()