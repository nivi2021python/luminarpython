class School:
    def details_school(self,name,place,board):
        self.name=name
        self.place=place
        self.board=board
    def prnt_schooldetails(self):
        print(self.name)
        print(self.place)
        print(self.board)
class Teachers:
    def details_teachers(self,name,subject,department):
        self.name=name
        self.subject=subject
        self.department=department
    def prnt_teacherdetails(self):
        print(self.name)
        print(self.subject)
        print(self.department)
class Students(School,Teachers):
    def details_students(self,name,roll_no,standard):
        self.name=name
        self.roll_no=roll_no
        self.standard=standard
    def prnt_studentdetails(self):
        print(self.name)
        print(self.standard)
        print(self.roll_no)
sc=School()
tr=Teachers()
st=Students()
st.details_school("Holy Kings","Kochi","CBSE")
st.prnt_schooldetails()
st.details_teachers("Anita Mam","Biology","Science Department")
st.prnt_teacherdetails()
st.details_students("Angel",32,"VIII th")
st.prnt_studentdetails()