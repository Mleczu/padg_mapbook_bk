from mapbook_shared.model import users
from mapbook_shared.controller import show_users, add_users

while True:
    print("=" * 50)
    print("Opcje:")
    print("* 0 = Exit")
    print("* 1 = List users")
    print("* 2 = Add user")
    choose: int = int(input("Podaj opcję: "))
    if choose == 0: break
    elif choose == 1: show_users(users)
    elif choose == 2: add_users(users)