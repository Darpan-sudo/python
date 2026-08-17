class Engine:
    def start(self):
        print("Engine started")


class Battery:
    def charge(self):
        print("Battery charging")


class Car:
    def __init__(self):
        self.engine = Engine()


class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.battery = Battery()


tesla = ElectricCar()

tesla.battery.charge()

bmw = Car()

bmw.engine.start()