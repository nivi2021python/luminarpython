class Person:
    def details_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def prnt_persondetails(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Filmindustry:
    def details_filmindustry(self,language,role):
        self.language=language
        self.role=role
    def prnt_filmindustrydetails(self):
        print(self.language)
        print(self.role)
class Actor(Person,Filmindustry):
    def details_actor(self,year_of_starting,awards_received,remuneration):
        self.year_of_starting=year_of_starting
        self.remuneration=remuneration
        self.awards_received = awards_received
    def prnt_actortdetails(self):
        print(self.year_of_starting)
        print(self.awards_received)
        print(self.remuneration)
per=Person()
filmind=Filmindustry()
actr=Actor()
actr.details_person("Mohanlal",55,"Male")
actr.prnt_persondetails()
actr.details_filmindustry("Malayalam","Hero")
actr.prnt_filmindustrydetails()
actr.details_actor("1975",16,"3 lakh")
actr.prnt_actortdetails()