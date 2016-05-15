#!/usr/bin/python
# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import dbtreninglast
import tkFont

def popup3():
    global top
    top = Toplevel() #otwarcie okienka popup
    top.title("Wybrany trening") #tytul okienka popup
    top.resizable(0,0) #zablokowanie rozmiaru okna
    top.geometry('365x422+200+200') #rozmiar okna

    w2 = Tkinter.Canvas(top, bd=0, height=365, width=422) #grafiki

    font3 = tkFont.Font(family='Helvetica Neue Thin', size=19) #czcionka HN T 19


    w2.create_text(19, 67.45, anchor=NW, text=dbtreninglast.dataLast_bd, font=font3, tags=("delint")) #data - tekst dla karty Ostatni trening
    w2.create_text(298, 67.45, anchor=NW, text=dbtreninglast.godzinaLast_bd, font=font3, tags=("delint"))
    w2.create_text(19, 107.45, anchor=NW, text="Dystans: " + str(dbtreninglast.dystansLast_bd) + " km", font=font3, tags=("delint"))
    w2.create_text(19, 147.45, anchor=NW, text="Czas: " + str(dbtreninglast.godzinyLast_bd) + "g " + str(dbtreninglast.minutyLast_bd) + "m " + str(dbtreninglast.sekundyLast_bd) + "s ", font=font3, tags=("delint"))
    w2.create_text(19, 187.45, anchor=NW, text="Kalorie: " + str(dbtreninglast.kalorieLast_bd) + " kcal", font=font3, tags=("delint"))
    w2.create_text(19, 227.45, anchor=NW, text="Srednia predkosc: " + str(dbtreninglast.srPredkoscLast_bd) + " km/h", font=font3, tags=("delint"))
    w2.create_text(19, 267.45, anchor=NW, text="Samopoczucie: " + dbtreninglast.samopoczucieLast_bd, font=font3, tags=("delint"))
    w2.create_text(19, 307.45, anchor=NW, text="Warunki atmosferyczne: " + dbtreninglast.pogodaLast_bd, font=font3, tags=("delint"))
    w2.create_text(19, 347.45, anchor=NW, text="Notatki: " + dbtreninglast.notatkiLast_bd, font=font3, tags=("delint"))

    w2.create_text(14, 13, anchor=NW, text="Trening " + str(1), font=font3, tags=("delint"))

    w2.create_line(0, 49, 365, 49, fill="#0175AE", tags=("delint"))

    w2.pack()

    top.mainloop () #petla zdarzen

popup3()
