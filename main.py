users =[
    {'name': 'Emil', 'posts': 100, 'location': 'Warszawa'},
    {'name': 'Natalka', 'posts': 10, 'location': 'Bialystok'},
    {'name': 'Mikolaj', 'posts': 1000, 'location': 'Warszawa'},
]

def show_users(user_list: list)->None:
    for user in user_list:
        print(f'Znajomy {user["name"]} z {user["location"]} ma {user["posts"]} postow')

def add_users(user_list: list)->None:
    user_list.append({'name': input('Podaj imie: '), 'posts': int(input('Podaj liczbe postów: ')), 'location': input('Podaj lokalizacje: ')})

show_users(users)
add_users(users)
show_users(users)