favorite_languages = {
    'Darpan':'Python',
    'Yash':'c',
    'Prathamesh':'css'
    }

person = ['Darpan','Yash','Prathamesh','Ammar',]

for people in person:
    if people in favorite_languages:
        print("Thank You !! for taking the poll")
    else:
        print(f"Please take the poll {people}")