banned_users = ['andrew','maira','jill']
user = 'maira'
if user not in banned_users:
    print("You can post a new user")
else:
    print("You are banned from posting")