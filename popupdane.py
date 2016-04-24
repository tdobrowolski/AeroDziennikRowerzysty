#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *

def popup1(root):
    global top
    top = Toplevel() #otwarcie okienka popup
    top.title("Moje dane") #tytul okienka popup

    domyslne1 = StringVar() #przypisanie wartosci domyslnej
    insert1 = Entry(top, textvariable=domyslne1) #pole insert nr1
    insert1.pack()

    domyslne2 = StringVar()
    insert2 = Entry(top, textvariable=domyslne2)
    insert2.pack()

    domyslne3 = StringVar()
    insert3 = Entry(top, textvariable=domyslne3)
    insert3.pack()

    domyslne4 = StringVar()
    insert4 = Entry(top, textvariable=domyslne4)
    insert4.pack()

    domyslne5 = StringVar()
    insert5 = Entry(top, textvariable=domyslne5)
    insert5.pack()

    domyslne1.set("Imie") #domyslny tekst w polu insert nr1

    domyslne2.set("Nazwisko")

    domyslne3.set("Wiek")

    domyslne4.set("Wzrost")

    domyslne5.set("Waga")

    def callback():
        import sqlite3 as lite
        import sys
        con_ppd = lite.connect('baza.db') #ppd - popupdane (skrot od nazwy pliku)
        insert11 = ((insert1.get(), insert2.get(), int(insert3.get()), 'Mezczyzna', int(insert4.get()), int(insert5.get()), 1))
        with con_ppd:

            cur_ppd = con_ppd.cursor()
            cur_ppd.execute("DELETE FROM PodaneDane WHERE Id = 1")
            cur_ppd.execute("INSERT INTO PodaneDane VALUES(?,?,?,?,?,?,?)", insert11)

    def exit():
        global top
        top.destroy()

    msg = Message(top, text="Zmiana danych wymaga restartu programu")
    msg.pack()

    b = Button(top, text="Zapisz", command=callback) #przycisk zapisz
    b.pack()

    c = Button(top, text="Anuluj", command=exit) #przycisk wyjdz
    c.pack()
