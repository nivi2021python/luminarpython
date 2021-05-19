class Vehicle:
  def print(self,type,brand,year):
        self.type=type
        self.brand=brand
        self.year=year
        print("inside print method",self.type,self.brand,self.year)
ve=Vehicle()
ve.print("car","honda",2021)