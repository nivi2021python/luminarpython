class Vehicle:
    def details(self,wheels,model,fuel_type):
        self.wheels=wheels
        self.model=model
        self.fuel_type=fuel_type
    def printdet(self):
        print(self.wheels)
        print(self.model)
        print(self.fuel_type)
class Bus(Vehicle):
    def det(self,bus_owner,bus_number,bus_colour):
        self.bus_owner=bus_owner
        self.bus_number=bus_number
        self.bus_colour=bus_colour
    def prints(self):
        print(self.bus_owner)
        print(self.bus_number)
        print(self.bus_colour)
veh=Vehicle()
veh.details("six wheel",2010,"diesel")
veh.printdet()
bu=Bus()
bu.details("six wheels",2010,"diesel")
bu.printdet()
bu.det("tolins","KL40FG6789","blue")
bu.prints()