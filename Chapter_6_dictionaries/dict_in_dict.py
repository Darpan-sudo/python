profile = {
    'user1':{
        'name': 'John',
        'id': '123',
        'location': 'Paris',
    },
    'user2':{
        'name': 'John1',
        'id': '123',
        'location': 'Paris',
        },
    'user3':{
            'name': 'John2',
            'id': '123',
            'location': 'Paris',
        }
}


for names,info in profile.items():
    print(f"The username is {info['name']}")

