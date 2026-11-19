from tkinter import *
import tkintermapview
from mapbook_shared.controller import get_location

users: list = []

class User:
    def __init__(self, name: str, location: str, posts: int):
        self.name = name
        self.location = location
        self.posts = posts

        self.coords: list = get_location(location)
        self.marker = map_widget.set_marker(self.coords[0], self.coords[1])

    def __del__(self):
        self.marker.delete()

    def set_name(self, name: str):
        self.name = name
        self.marker.set_text(name)

    def set_location(self, location: str):
        self.location = location
        self.coords: list = get_location(location)
        self.marker.set_position(self.coords[0], self.coords[1])

    def set_posts(self, posts: int):
        self.posts = posts


def show_users():
    listbox_lista_obiektow.delete(0, END)

    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user.name)

def add_user():
    name = entry_imie.get()
    location = entry_miejscowosc.get()
    posts = int(entry_posty.get())

    user = User(name, location, posts)
    users.append(user)

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    entry_imie.focus()
    show_users()

def update_user(active_index: int):
    new_name = entry_imie.get()
    new_location = entry_miejscowosc.get()
    new_posts = entry_posty.get()

    user = users[active_index]
    user.set_name(new_name)
    user.set_location(new_location)
    user.set_posts(new_posts)

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    entry_imie.focus()

    show_users()

    button_dodaj_obiekt.configure(text='Dodaj obiekt', command=add_user)

def remove_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        return

    users.pop(active_index)
    show_users()

def details_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        label_imie_szczegoly_obiektu_wartosc.configure(text='.....')
        label_miejscowosc_szczegoly_obiektu_wartosc.configure(text='.....')
        label_posty_szczegoly_obiektu_wartosc.configure(text='.....')
        map_widget.set_position(52.23, 21)
        map_widget.set_zoom(6)
        return
    user = users[active_index]
    name = user.name
    location = user.location
    posts = user.posts
    deg = user.coords

    label_imie_szczegoly_obiektu_wartosc.configure(text=name)
    label_miejscowosc_szczegoly_obiektu_wartosc.configure(text=location)
    label_posty_szczegoly_obiektu_wartosc.configure(text=posts)

    map_widget.set_position(deg[0], deg[1])
    map_widget.set_zoom(12)

def edit_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        return

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    user = users[active_index]

    entry_imie.insert(0, user.name)
    entry_miejscowosc.insert(0, user.location)
    entry_posty.insert(0, user.posts)

    button_dodaj_obiekt.configure(text='Zapisz zmiany', command=lambda: update_user(active_index))

root = Tk()
root.geometry('1024x768')
root.title('Mapbook')

#Ramki
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
ramka_mapa.grid(row=2, column=0, columnspan=7)

#Ramka lista obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista obiektow:')
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaz szczegoly', command=details_user)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_user)
button_usun_obiekt = Button(ramka_lista_obiektow, text='Usun obiekt', command=remove_user)

label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt.grid(row=2, column=2)

#Ramka formularz
label_formularz = Label(ramka_formularz, text='Formularz:')
label_name = Label(ramka_formularz, text='Imie:')
label_location = Label(ramka_formularz, text='Miejscowość:')
label_posts = Label(ramka_formularz, text='Liczba postów:')
entry_imie = Entry(ramka_formularz)
entry_miejscowosc = Entry(ramka_formularz)
entry_posty = Entry(ramka_formularz)
button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj obiekt', command=add_user)

label_formularz.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0, sticky=W)
label_location.grid(row=2, column=0, sticky=W)
label_posts.grid(row=3, column=0, sticky=W)
entry_imie.grid(row=1, column=1)
entry_miejscowosc.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
button_dodaj_obiekt.grid(row=4, column=0, columnspan=2)

#Ramka szczegóły obiektu
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegóły obiektu:')
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imie:')
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....', width=10)
label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Miejsowość:')
label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....', width=10)
label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Posty:')
label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....', width=10)

label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0)
label_miejscowosc_szczegoly_obiektu.grid(row=1, column=2)
label_posty_szczegoly_obiektu.grid(row=1, column=4)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)

#Ramka mapa
label_mapa = Label(ramka_mapa, text='Mapa:')
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1050, height=500, corner_radius=5)
map_widget.set_position(52.23, 21)
map_widget.set_zoom(6)
label_mapa.grid(row=0, column=0)
map_widget.grid(row=1, column=0, columnspan=7)


root.mainloop()