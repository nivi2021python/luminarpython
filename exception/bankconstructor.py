class BankEmp:
    def __init__(self,name,emp_id,sal):
        self.name=name
        self.emp_id=emp_id
        self.sal=sal
    def printval(self):
        print(self.name)
        print(self.emp_id)
        print(self.sal)
per=BankEmp("nivi",2569,25000)
per.printval()