alien_0 = {'color':'red','point':'5 pts'}

print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 23


print(alien_0)


# modifying values and deleting key-value pairs

alien_1={'color':'green','point':'10 pts','x_position':0,'y_position':25,'speed':'medium'}

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 


print(f"The current speed of the alien is {alien_1['x_position'] + x_increment}.")
del alien_1['point']
print(alien_1)