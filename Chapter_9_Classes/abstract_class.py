from abc import ABC,abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14*5**4


class Rectangle(Shape):
    def area(self):
        return 4*4



circle = Circle()

rectangle = Rectangle()


print(circle.area())

print(rectangle.area())