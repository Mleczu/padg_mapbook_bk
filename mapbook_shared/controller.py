def show_users(user_list: list)->None:
    for user in user_list:
        print(f'Znajomy {user["name"]} z {user["location"]} ma {user["posts"]} postow')

def add_users(user_list: list)->None:
    user_list.append({'name': input('Podaj imie: '), 'posts': int(input('Podaj liczbe postów: ')), 'location': input('Podaj lokalizacje: ')})