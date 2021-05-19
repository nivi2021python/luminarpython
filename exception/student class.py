class Student:
    school="amrita vidyalayam"
    def studdetails(self,roll_no,name,standard,dob):
        self.roll_no=roll_no
        self.name=name
        self.standard=standard
        self.dob=dob
        #self.school=school
    def printVal(self):
        print(self.roll_no)
        print(self.name)
        print(self.standard)
        print(self.dob)
        print("school name",Student.school)

stud=Student()
stud.studdetails(23,"nivi",12,"29/06/2007")
stud.printVal()

stud1=Student()
stud1.studdetails(24,"parvathy",12,"31/05/2007")
stud1.printVal()

