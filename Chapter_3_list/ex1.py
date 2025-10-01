guest = ['Alice', 'Bob', 'Charlie']
guest_cant_come = guest.pop(1)
guest.insert(1,"David")
guest.insert(0,'Eve')
guest.append("Frank")
print("You are invited to dinner,"+ guest[0])
print("You are invited to dinner,"+ guest[1])
print("You are invited to dinner,"+ guest[2])
print("You are invited to dinner,"+ guest[3])
print("You are invited to dinner,"+ guest[4])
print("Guest who cant make it "+guest_cant_come)

del guest[-2:-1]

print(guest)