users =[
    {'name': 'Emil', 'posts': 100, 'location': 'Warszawa'},
    {'name': 'Natalka', 'posts': 10, 'location': 'Bialystok'},
    {'name': 'Mikolaj', 'posts': 1000, 'location': 'Warszawa'},
]
for user in users:
    print(f'Znajomy {user["name"]} z {user["location"]} ma {user["posts"]} postow')