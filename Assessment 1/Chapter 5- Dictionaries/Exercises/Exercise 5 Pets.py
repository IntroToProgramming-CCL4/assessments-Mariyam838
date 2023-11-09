#Define dictionary that represents different kind of pets name and about them.
pet1 = {'kind':'rabbit', 'owner':'zeeshan','color':'brown','age':'2'}
pet2 = {'kind': 'parrot', 'owner':'Muskan', 'color': 'green','age':'3'}
pet3 = {'kind': 'puppy', 'owner':'Areeba', 'color':'white', 'age':'5'}
#Store the disctionaries in a list called pets
pets = [pet1, pet2, pet3]
#Loop through the list of pets and print information about each pet
for pet in pets:
    print(f"This pet is a {pet['kind']} and is owned by {pet['owner']}.")
    print(f"It is {pet['color']} in color.")
    print(f"It is {pet['age']} years old.\n")