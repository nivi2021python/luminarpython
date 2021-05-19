class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno)
        print(self.school)
per=Person()
per.details("anu",23,"female")
per.printdet()
st=Student()
st.details("arun",24,"male")
st.printdet()