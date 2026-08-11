class car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
        self.speed = 0
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} on it")

car = car("BWM","Black")
print(car.speed)

car.peed = 100
print(car.brand)
print(car.colour)
print(car.peed)
car.read_odometer()
