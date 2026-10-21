def show_users(user_list: list)->None:
    for i, user in enumerate(user_list):
        print(f'{i} > Znajomy {user["name"]} z {user["location"]} ma {user["posts"]} postow')

def add_user(user_list: list)->None:
    user_list.append({'name': input('Podaj imie: '), 'posts': int(input('Podaj liczbe postów: ')), 'location': input('Podaj lokalizacje: ')})

def remove_user(user_list: list)->bool:
    name: str = input('Podaj imie delikwenta: ')
    for user in user_list:
        if user['name'] == name:
            user_list.remove(user)
            return True
    return False