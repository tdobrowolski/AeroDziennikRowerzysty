#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import datetime
import dbcel
import dbtest

def popup2(root):
    global top
    top = Toplevel() #otwarcie okienka popup
    top.title("Dodaj trening") #tytul okienka popup

    domyslne1 = StringVar() #przypisanie wartosci domyslnej
    insert1 = Entry(top, textvariable=domyslne1, relief=FLAT) #pole insert nr1
    insert1.pack()

    domyslne2 = StringVar()
    insert2 = Spinbox(top, from_=0, to=23, textvariable=domyslne2) #godziny
    insert2.pack()

    domyslne2_1 = StringVar()
    insert2_1 = Spinbox(top, from_=0, to=59, textvariable=domyslne2_1) #minuty
    insert2_1.pack()

    domyslne2_2 = StringVar()
    insert2_2 = Spinbox(top, from_=0, to=59, textvariable=domyslne2_2) #sekundy
    insert2_2.pack()

    var_0 = StringVar(top)
    var_0.set("Samopoczucie") #tytul menu

    lista_samopoczucie = OptionMenu(top, var_0, "Bardzo dobre", "Ok", "Niezbyt dobre")
    lista_samopoczucie.pack()
    lista_samopoczucie.config(width=20)

    var_1 = StringVar(top)
    var_1.set("Pogoda") #tytul menu

    lista_pogoda = OptionMenu(top, var_1, "Slonecznie", "Pochmurnie", "Deszcz", "Burza", "Snieg", "Mgla")
    lista_pogoda.pack()
    lista_pogoda.config(width=20)

    domyslne4 = StringVar()
    insert4 = Text(top, height=5, width=23)
    insert4.pack()
    insert4.insert(END, "Notatki")

    domyslne1.set("Dystans") #domyslny tekst w polu insert nr1
    domyslne2.set("0")
    domyslne2_1.set("0")
    domyslne2_1.set("0")

    now = datetime.datetime.now() #pobranie daty i godziny
    data = str(now.day) + "." + str(now.month) + "." + str(now.year)
    godzina = str(now.hour) + ":" + str(now.minute)

    def exit():
        global top
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

        exit()

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

        exit()

    b = Button(top, text="Zapisz", command=callback) #przycisk zapisz
    b.pack(in_=top, side=LEFT)

    c = Button(top, text="Anuluj", command=exit) #przycisk wyjdz
    c.pack(in_=top, side=RIGHT)
