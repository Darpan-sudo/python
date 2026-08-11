class dog:
    def __init__(self, name, age):
        self.game = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now rolling")


my_dog = dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog = dog('Bruno', 8)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

