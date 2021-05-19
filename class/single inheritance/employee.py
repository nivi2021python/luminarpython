class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def det(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def prints(self):
        print(self.emp_id)
        print(self.salary)
per=Person()
per.details("anu",32,"female")
per.printdet()
emp=Employee()
emp.details("arjun",30,"male")
emp.printdet()
emp.det(2343,29000)
emp.prints()