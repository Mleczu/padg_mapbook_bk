from tkinter import *
import tkintermapview
from mapbook_shared.controller import get_location

users: list = []

def show_users():
    listbox_lista_obiektow.delete(0, END)

    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user['name'])

def add_user():
    name = entry_imie.get()
    location = entry_miejscowosc.get()
    posts = entry_posty.get()

    users.append({
        'name': name,
        'location': location,
        'posts': int(posts),
    })

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    entry_imie.focus()

    show_users()

    deg_x, deg_y = get_location(location)
    marker = map_widget.set_marker(deg_x, deg_y, text=name)
    users[len(users) - 1]['marker'] = marker

def update_user(active_index: int):
    new_name = entry_imie.get()
    new_location = entry_miejscowosc.get()
    new_posts = entry_posty.get()

    users[active_index]['name'] = new_name
    users[active_index]['location'] = new_location
    users[active_index]['posts'] = new_posts

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    entry_imie.focus()

    show_users()

    deg_x, deg_y = get_location(new_location)
    marker = users[active_index]['marker']
    marker.set_position(deg_x, deg_y)
    marker.set_text(new_name)

    button_dodaj_obiekt.configure(text='Dodaj obiekt', command=add_user)

def remove_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        return

    marker = users[active_index]['marker']
    marker.delete()

    users.remove(users[active_index])
    show_users()

def details_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        label_imie_szczegoly_obiektu_wartosc.configure(text='.....')
        label_miejscowosc_szczegoly_obiektu_wartosc.configure(text='.....')
        label_posty_szczegoly_obiektu_wartosc.configure(text='.....')
        return
    name = users[active_index]['name']
    location = users[active_index]['location']
    posts = users[active_index]['posts']

    label_imie_szczegoly_obiektu_wartosc.configure(text=name)
    label_miejscowosc_szczegoly_obiektu_wartosc.configure(text=location)
    label_posty_szczegoly_obiektu_wartosc.configure(text=posts)

def edit_user():
    active_index = listbox_lista_obiektow.index(ACTIVE)
    if not users[active_index]:
        return

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_posty.delete(0, END)

    entry_imie.insert(0, users[active_index]['name'])
    entry_miejscowosc.insert(0, users[active_index]['location'])
    entry_posty.insert(0, users[active_index]['posts'])

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
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=7)

#Ramka lista obiektow
label_lista_obiektow = Label(ramka_lista_obiektow, text='Lista obiektow:')
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
button_pokaz_szczegoly = Button(ramka_lista_obiektow, text='Pokaz szczegoly', command=details_user)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt', command=edit_user)
button_usun_obiekt = Button(ramka_lista_obiektow, text='Usun obiekt', command=remove_user)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
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

label_formularz.grid(row=0, column=0)
label_name.grid(row=1, column=0)
label_location.grid(row=2, column=0)
label_posts.grid(row=3, column=0)
entry_imie.grid(row=1, column=1)
entry_miejscowosc.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
button_dodaj_obiekt.grid(row=4, column=0)

#Ramka szczegóły obiektu
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegóły obiektu:')
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imie:')
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')
label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Miejsowość:')
label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')
label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Posty:')
label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='.....')

label_szczegoly_obiektu.grid(row=0, column=0)
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