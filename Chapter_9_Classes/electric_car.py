class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model= model
        self.year = year

    def get_description(self):
        long_name = f"The model of the car is {self.model} released in the year {self.year}"
        return long_name.title()

class ElectricCar(Car):
    def get_description(self):
        long_name = f"The model of the car is {self.model} released in the year {self.year}"
        return long_name.title()


car = Car("sedan","sedan",2001)

print(car.get_description())


tesla = ElectricCar("sedan","roadstar",2025)
print(tesla.get_description())