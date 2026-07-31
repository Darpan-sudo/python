aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','speed':'fast','points':'20 pts'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    print(alien)

print(f"total number of aliens are {len(aliens)}")