#slicing a list

players = ["charles","martina","michael","florence","eli"]
print(players[0:3])
print(players[:4])
print(players[2:])

#looping through a slice 

players = ["charles","martina","michael","florence","eli"]
print("Here are the first three Player of My Team:")
for player in players[:3]:
    print(player.title())



#copying a list


my_food = ["Burger","Pizza","Chowmein"]
friends_food = my_food[:]

my_food.append("Ice-cream")
friends_food.append("Pasta")


print("My favorite food are:"+ str(my_food))
print("My firends favorite food are:"+ f"{friends_food}")