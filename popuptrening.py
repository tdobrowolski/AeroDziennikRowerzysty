#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import dbtreninglast
import tkFont
import sqlite3 as lite
import sys
import dbtest

def popup3(nr_treningu):

    dbtest.dbtest()

    con_pptre = lite.connect('baza.db')

    with con_pptre:

        cur_pptre = con_pptre.cursor()
        cur_pptre.execute("SELECT * FROM Treningi WHERE Id = ?", (nr_treningu,))

        while True:

            row_pptre = cur_pptre.fetchone()

            if row_pptre == None:
                break

            dataWybrana_bd = row_pptre[0]
            godzinaWybrana_bd = row_pptre[1]
            dystansWybrana_bd = row_pptre[2]
            czasWybrana_bd = row_pptre[3]
            samopoczucieWybrana_bd = row_pptre[4]
            pogodaWybrana_bd = row_pptre[5]
            notatkiWybrana_bd = row_pptre[6]
            idWybrana_bd = row_pptre[7]

            #zamiana calkowitego czasu na h:m:s
            minutyWybrana_bd, sekundyWybrana_bd = divmod(czasWybrana_bd, 60)
            godzinyWybrana_bd, minutyWybrana_bd = divmod(minutyWybrana_bd, 60)

            #obliczanie km/h
            srPredkoscWybrana_bd = dystansWybrana_bd*3600/czasWybrana_bd

            #obliczanie kalorii
            kalorieWybrana_bd = int(dbtest.waga_bd*(czasWybrana_bd/60)*(0.6345*srPredkoscWybrana_bd*srPredkoscWybrana_bd+0.7563*srPredkoscWybrana_bd+36.725)/(3600))

    con_pptre.close()

    global top2
    top2 = Toplevel() #otwarcie okienka popup
    top2.title("Wybrany trening") #tytul okienka popup
    top2.resizable(0,0) #zablokowanie rozmiaru okna
    top2.geometry('365x422+200+200') #rozmiar okna

    w2 = Tkinter.Canvas(top2, bd=0, height=365, width=422) #grafiki

    font3 = tkFont.Font(family='Helvetica Neue Thin', size=19) #czcionka HN T 19
    font6 = tkFont.Font(family='Lato Regular', size=19, )

    w2.create_text(19, 67.45, anchor=NW, text=dataWybrana_bd, font=font3, tags=("delint")) #data - tekst dla karty Ostatni trening
    w2.create_text(298, 67.45, anchor=NW, text=godzinaWybrana_bd, font=font3, tags=("delint"))
    w2.create_text(19, 107.45, anchor=NW, text="Dystans: " + str(dystansWybrana_bd) + " km", font=font3, tags=("delint"))
    w2.create_text(19, 147.45, anchor=NW, text="Czas: " + str(godzinyWybrana_bd) + "g " + str(minutyWybrana_bd) + "m " + str(sekundyWybrana_bd) + "s ", font=font3, tags=("delint"))
    w2.create_text(19, 187.45, anchor=NW, text="Kalorie: " + str(kalorieWybrana_bd) + " kcal", font=font3, tags=("delint"))
    w2.create_text(19, 227.45, anchor=NW, text="Srednia predkosc: " + str(srPredkoscWybrana_bd) + " km/h", font=font3, tags=("delint"))
    w2.create_text(19, 267.45, anchor=NW, text="Samopoczucie: " + samopoczucieWybrana_bd, font=font3, tags=("delint"))
    w2.create_text(19, 307.45, anchor=NW, text="Warunki atmosferyczne: " + pogodaWybrana_bd, font=font3, tags=("delint"))
    w2.create_text(19, 347.45, anchor=NW, text="Notatki: " + notatkiWybrana_bd, font=font3, tags=("delint"))

    w2.create_text(14, 13, anchor=NW, text="Trening " + str(idWybrana_bd), font=font6, tags=("delint"))

    w2.create_line(0, 49, 365, 49, fill="#0175AE", tags=("delint"))

    w2.pack()

    top2.mainloop () #petla zdarzen
