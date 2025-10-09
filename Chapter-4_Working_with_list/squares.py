squares = []
for numbers in range(1,10):
    # square = numbers**2
    squares.append(numbers**2)
print(squares)


#list comprehension
square = [values**2 for values in range(1,10)]
print(square)

#syntax
#name_of_list = [expression for the value then goes the for loop]