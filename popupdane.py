#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *

def popup1(root):
    global top
    top = Toplevel() #otwarcie okienka popup
    top.title("Moje dane") #tytul okienka popup

    domyslne1 = StringVar() #przypisanie wartosci domyslnej
    insert1 = Entry(top, textvariable=domyslne1, relief=FLAT) #pole insert nr1
    insert1.pack()

    domyslne2 = StringVar()
    insert2 = Entry(top, textvariable=domyslne2, relief=FLAT)
    insert2.pack()

    domyslne3 = StringVar()
    insert3 = Entry(top, textvariable=domyslne3, relief=FLAT)
    insert3.pack()

    var_0 = StringVar(top)
    var_0.set("Plec") #tytul menu

    lista_plec = OptionMenu(top, var_0, "Kobieta", "Mezczyzna")
    lista_plec.pack()
    lista_plec.config(width=20)

    domyslne4 = StringVar()
    insert4 = Entry(top, textvariable=domyslne4, relief=FLAT)
    insert4.pack()

    domyslne5 = StringVar()
    insert5 = Entry(top, textvariable=domyslne5, relief=FLAT)
    insert5.pack()

    domyslne1.set("Imie") #domyslny tekst w polu insert nr1

    domyslne2.set("Nazwisko")

    domyslne3.set("Wiek")

    domyslne4.set("Wzrost (cm)")

    domyslne5.set("Waga")

    var_1 = StringVar(top)
    var_1.set("Cel") #tytul menu

    lista_cel = OptionMenu(top, var_1, "Popraw samopoczucie (Latwe)", "Popraw kondycje (Srednie)", "Popraw sylwetke (Trudne)")
    lista_cel.pack()
    lista_cel.config(width=20)

    def exit():
        global top
        top.destroy()

    def callback():
        import sqlite3 as lite
        import sys
        con_ppd = lite.connect('baza.db') #ppd - popupdane (skrot od nazwy pliku)
        insert11 = (insert1.get(), insert2.get(), int(insert3.get()), var_0.get(), int(insert4.get()), int(insert5.get()), var_1.get(), 1)
        with con_ppd:

            cur_ppd = con_ppd.cursor()
            cur_ppd.execute("DELETE FROM PodaneDane WHERE Id = 1")
            cur_ppd.execute("INSERT INTO PodaneDane VALUES(?,?,?,?,?,?,?,?)", insert11)
        exit()

    mssg1 = StringVar()
    msssg1_l = Message(top, text="Po zmianie danych potrzebny jest reset programu.", relief=FLAT, width=180)
    msssg1_l.pack()

    b = Button(top, text="Zapisz", command=callback) #przycisk zapisz
    b.pack(in_=top, side=LEFT)

    c = Button(top, text="Anuluj", command=exit) #przycisk wyjdz
    c.pack(in_=top, side=RIGHT)
