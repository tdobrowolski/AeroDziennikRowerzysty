#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *

def popup1(root, w):
    global top
    top = Toplevel(padx=10, pady=10) #otwarcie okienka popup
    top.title("Moje dane") #tytul okienka popup

    #domyslne1 = StringVar() #przypisanie wartosci domyslnej
    Label(top, text="Imie:").grid(row=0, sticky=W)
    insert1 = Entry(top) #pole insert nr1
    insert1.grid(row=0, column=1)

    #domyslne2 = StringVar()
    Label(top, text="Nazwisko:").grid(row=1, sticky=W)
    insert2 = Entry(top)
    insert2.grid(row=1, column=1)

    #domyslne3 = StringVar()
    Label(top, text="Wiek:").grid(row=2, sticky=W)
    insert3 = Entry(top)
    insert3.grid(row=2, column=1)

    var_0 = StringVar(top)
    var_0.set("Kobieta") #tytul menu

    Label(top, text="Plec:").grid(row=3, sticky=W)
    lista_plec = OptionMenu(top, var_0, "Kobieta", "Mezczyzna")
    lista_plec.grid(row=3, column=1)
    lista_plec.config(width=20)

    #domyslne4 = StringVar()
    Label(top, text="Wzrost (cm):").grid(row=4, sticky=W)
    insert4 = Entry(top)
    insert4.grid(row=4, column=1)

    Label(top, text="Waga (kg):").grid(row=5, sticky=W)
    insert5 = Entry(top)
    insert5.grid(row=5, column=1)

    #domyslne1.set("Imie") #domyslny tekst w polu insert nr1

    #domyslne2.set("Nazwisko")

    #domyslne3.set("Wiek")

    #domyslne4.set("Wzrost (cm)")

    #domyslne5.set("Waga")

    var_1 = StringVar(top)
    var_1.set("Popraw nastroj!") #tytul menu

    Label(top, text="Cel:").grid(row=6, sticky=W)
    lista_cel = OptionMenu(top, var_1, "Popraw nastroj!", "Popraw kondycje!", "Popraw sylwetke!")
    lista_cel.grid(row=6, column=1)
    lista_cel.config(width=20)

    def exit():
        top.destroy()

    def callback():
        import sqlite3 as lite
        import sys
        import interface
        con_ppd = lite.connect('baza.db') #ppd - popupdane (skrot od nazwy pliku)
        insert11 = (insert1.get(), insert2.get(), int(insert3.get()), var_0.get(), int(insert4.get()), int(insert5.get()), var_1.get(), 1)
        with con_ppd:

            cur_ppd = con_ppd.cursor()
            cur_ppd.execute("DELETE FROM PodaneDane WHERE Id = 1")
            cur_ppd.execute("INSERT INTO PodaneDane VALUES(?,?,?,?,?,?,?,?)", insert11)

        con_ppd.close()
        top.destroy()
        interface.interface1(root, w)

    b = Button(top, text="Zapisz", command=callback) #przycisk zapisz
    b.grid(row=7, column=1, pady=2)

    c = Button(top, text="Anuluj", command=exit) #przycisk wyjdz
    c.grid(row=7, column=0, pady=2)
