class Employee:
    def setval(self,name,emp_id,designation):
        self.name=name
        self.emp_id=emp_id
        self.designation=designation
        print(self.name,self.emp_id,self.designation)
    def __str__(self):
         return self.name + str(self.emp_id)

emp=Employee()
emp.setval("Varkey",698,"Officer")
print(emp)