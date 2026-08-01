prompt = "\nPlease enter the city u want to visit"
prompt += "\n Enter quit when you are finished"

active = True

while active:
    city = input(prompt)

    if city == 'quit':
        active = False
    else:
        print(f"The name of the city u want to visit is {city}") 