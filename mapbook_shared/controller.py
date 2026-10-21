import requests
from bs4 import BeautifulSoup
import folium

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

def update_user(user_list: list)->None:
    name: str = input('Podaj stare imie: ')
    for user in user_list:
        if user['name'] == name:
            user['name'] = input('Podaj imie: ')
            user['location'] = input('Podaj lokalizacje: ')
            user['posts'] = int(input('Podaj liczbe postów: '))
            return

    print("Nie znaleziono usera po imieniu.")

def get_location(location: str)->list:
    url = f'https://pl.wikipedia.org/wiki/{location}'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    latitude = float(soup.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(soup.select('.longitude')[1].text.replace(',', '.'))
    return latitude, longitude

def generate_map(user_list: list)->None:
    m = folium.Map(location=(52.23, 21.00), zoom_start=6)

    for user in user_list:
        latitude, longitude = get_location(user['location'])

        folium.Marker(
            location=[latitude, longitude],
            tooltip=f"{user['name']}",
            popup=f"{user['location']}",
            icon=folium.Icon(icon="pin"),
        ).add_to(m)

    m.save('index.html')