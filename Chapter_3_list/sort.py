#using sort method
car = ['bmw','audi','toyota','subaru']
print(sorted(car)) #sorted function is used to sort the list temporarily

car.sort(reverse=True) # here reverse fuction is used to sort in descending order permanently
print(car)

car.reverse() #reverse function is used to reverse the order of list permanently
print(car)

print(len(car))