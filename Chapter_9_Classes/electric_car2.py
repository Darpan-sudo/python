class Car:
    def __init__(self,model,make,battery):
        self.model = model
        self.make = make
        self.battery = battery

class ElectricCar(Car):
    def __init__(self, model, make, battery):
        super().__init__(model, make, battery)




car = Car('BMW','M3','2001')
tesla = ElectricCar("Tesla",'test','2020')

print(tesla.make)
print(car.make)