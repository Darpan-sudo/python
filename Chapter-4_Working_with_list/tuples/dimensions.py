dimensions = (200,50)
for i in range(0,2):
    print(dimensions[i])

print("<-------------------------------------------------------------------------------------------------------------------------->")
# what if we try to chnage the tuple values

dimension = (200,50)
# dimension[0] = 100 #     dimension[0] = 100 TypeError: 'tuple' object does not support item assignment
print(dimension[0])
print(dimension[1])

print("<-------------------------------------------------------------------------------------------------------------------------->")
# we can reassign a tuple variable to a new tuple
dimensions = (400,100)       
for dimension in dimensions:
    print(dimension)

dimensions = (300,200)       
for dimension in dimensions:
    print(dimension)

