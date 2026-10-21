from mapbook_shared.model import users
from mapbook_shared.controller import show_users, add_user, remove_user, update_user

while True:
    print("=" * 50)
    print("Opcje:")
    print("* 0 = Exit")
    print("* 1 = List users")
    print("* 2 = Add user")
    print("* 3 = Remove user")
    print("* 4 = Update user")
    choose: int = int(input("Podaj opcję: "))
    if choose == 0: break
    elif choose == 1: show_users(users)
    elif choose == 2: add_user(users)
    elif choose == 3:
        if remove_user(users):
            print('Usunieto delikwenta z listy')
        else:
            print('Nie ma takiego delikwenta')
    elif choose == 4: update_user(users)
    else:
        print("Podaj poprawną opcję")