class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Actor(Person):
    def det(self,industry,role):
        self.industry=industry
        self.role=role
    def prints(self):
        print(self.industry)
        print(self.role)
per=Person()
per.details("Abhishek Bachan",40,"male")
per.printdet()
act=Actor()
act.details("Abhishek Bachan",40,"male")
act.printdet()
act.det("Bollywood","Hero")
act.prints()