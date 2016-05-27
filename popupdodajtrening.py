#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import datetime
import dbcel
import dbtest

def popup2(root):
    global top
    top = Toplevel(padx=10, pady=10) #otwarcie okienka popup
    top.title("Dodaj trening") #tytul okienka popup

    Label(top, text="Dystans (km):").grid(row=0, sticky=W)
    insert1 = Entry(top, width=20) #pole insert nr1
    insert1.grid(row=0, column=1)

    Label(top, text="Liczba godzin:").grid(row=1, sticky=W)
    insert2 = Spinbox(top, from_=0, to=23, width=18) #godziny
    insert2.grid(row=1, column=1)

    Label(top, text="Liczba minut:").grid(row=2, sticky=W)
    insert2_1 = Spinbox(top, from_=0, to=59, width=18) #minuty
    insert2_1.grid(row=2, column=1)

    Label(top, text="Liczba sekund:").grid(row=3, sticky=W)
    insert2_2 = Spinbox(top, from_=0, to=59, width=18) #sekundy
    insert2_2.grid(row=3, column=1)

    var_0 = StringVar(top)
    var_0.set("Bardzo dobre") #tytul menu

    Label(top, text="Samopoczucie:").grid(row=4, sticky=W)
    lista_samopoczucie = OptionMenu(top, var_0, "Bardzo dobre", "Ok", "Niezbyt dobre")
    lista_samopoczucie.grid(row=4, column=1)
    lista_samopoczucie.config(width=20)

    var_1 = StringVar(top)
    var_1.set("Slonecznie") #tytul menu

    Label(top, text="Pogoda:").grid(row=5, sticky=W)
    lista_pogoda = OptionMenu(top, var_1, "Slonecznie", "Pochmurnie", "Deszcz", "Burza", "Snieg", "Mgla")
    lista_pogoda.grid(row=5, column=1)
    lista_pogoda.config(width=20)

    insert4 = Text(top, height=5, width=39, borderwidth=1)
    insert4.grid(columnspan=2, sticky=W)
    insert4.insert(END, "Notatki")

    now = datetime.datetime.now() #pobranie daty i godziny
    data = str(now.day) + "." + str(now.month) + "." + str(now.year)
    godzina = str(now.hour) + ":" + str(now.minute)

    def exit():
        top.destroy()

    def callback():
        import sqlite3 as lite
        import sys

        con_ppdt = lite.connect('baza.db') #ppdt - popupdodajtrening (skrot od nazwy pliku)

        cur_ppdt = con_ppdt.cursor()

        cur_ppdt.execute("SELECT max(Id) FROM Treningi") #pobranie max Id

        ost_Id = cur_ppdt.fetchone()[0] #przypisanie pobranej wartosci

        dystansPodany_bd = int(insert1.get())

        godziny_spinbox = int(insert2.get())
        minuty_spinbox = int(insert2_1.get())
        sekundy_spinbox = int(insert2_2.get())
        czas_spinbox = (godziny_spinbox * 3600) + (minuty_spinbox * 60) + sekundy_spinbox

        srPredkoscPodany_bd = dystansPodany_bd*3600/czas_spinbox

        insert21 = (data, godzina, dystansPodany_bd, czas_spinbox, var_0.get(), var_1.get(), insert4.get("1.0",END), ost_Id+1)

        with con_ppdt:

            #cur_ppdt = con_ppdt.cursor()
            cur_ppdt.execute("INSERT INTO Treningi VALUES(?,?,?,?,?,?,?,?)", insert21)

        con_ppdt.commit()
        con_ppdt.close()

        con_ppdt2 = lite.connect('baza.db') #ppdt - popupdodajtrening (skrot od nazwy pliku)

        cur_ppdt2 = con_ppdt2.cursor()

        kilometryDodaj = dbcel.kilometryCel_bd + dystansPodany_bd
        kalorieDodaj = dbcel.kalorieCel_bd + int(dbtest.waga_bd*(czas_spinbox/60)*(0.6345*srPredkoscPodany_bd*srPredkoscPodany_bd+0.7563*srPredkoscPodany_bd+36.725)/(3600))
        treningiDodaj = dbcel.treningiCel_bd + 1
        postepDodaj = dbcel.postepCel_bd + dystansPodany_bd + czas_spinbox + 1

        insert22 = (kilometryDodaj, kalorieDodaj, treningiDodaj, postepDodaj)

        with con_ppdt2:

            #cur_ppdt2 = con_ppdt.cursor()
            cur_ppdt2.execute("DELETE FROM CelDane")
            cur_ppdt2.execute("INSERT INTO CelDane VALUES(?,?,?,?)", insert22)

        con_ppdt2.commit()
        con_ppdt2.close()
        top.destroy()

    b = Button(top, text="Zapisz", command=callback) #przycisk zapisz
    b.grid(row=7, column=1, pady=2)

    c = Button(top, text="Anuluj", command=exit) #przycisk wyjdz
    c.grid(row=7, column=0, pady=2)
