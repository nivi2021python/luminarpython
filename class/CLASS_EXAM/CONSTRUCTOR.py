class Animal:
    def __init__(self,name,type,legs):
        self.name=name
        self.type=type
        self.legs=legs
    def print_animaldet(self):
        print(self.name)
        print(self.type)
        print(self.legs)
class Dog(Animal):
    def dog_details(self,breed,colour,age):
        self.breed=breed
        self.colour=colour
        self.age=age
    def print_dogdet(self):
        print(self.breed)
        print(self.colour)
        print(self.age)
dg=Dog()
dg.dog_details("GermanSheperd","grey",4)
dg.print_dogdet()
anml=Animal("jacky","dog",4)
anml.print_animaldet()