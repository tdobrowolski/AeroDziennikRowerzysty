#!/bin/env python -u
#-*- coding: utf-8 -*-

import Tkinter
from Tkinter import *
import tkFont
import interface
import time
import sys
import tkMessageBox


root = Tk() #otwarcie okna
root.resizable(0,0) #zablokowanie rozmiaru okna
root.title('Aero - Dziennik rowerowy') #tytul okna
root.geometry('800x600+200+200') #rozmiar okna

#canvas UI
w = Tkinter.Canvas(root, bd=0, height=600, width=800) #grafiki
font2 = tkFont.Font(family='Helvetica Neue Thin', size=23, ) #czcionka HN T 23

def intro():
    intro = Tkinter.PhotoImage(file=r'intro.ppm')
    root.intro = intro  #zapobiegam wrzuceniu obrazka do smieci
    w.create_image((0,0), image=intro, anchor='nw', tags=("intro"))
    w.after(2000, w.delete, "intro") #usun intro po 2 sekundach

def clickAktualnosci(event):
    interface.interface1(root, w)
    menuUp(w)

def clickMojDziennik(event): #funkcja dla klikniecia w Moj Dziennik
    interface.interface2(root, w)
    menuUp(w)

def clickMojeDane(event):
    interface.interface3(root, w)
    menuUp(w)

def clickUstawienia(event):
    interface.interface4(root, w)
    menuUp(w)

def menuUp(w):
    w.tag_raise(menu1)
    w.tag_raise(menu2)
    w.tag_raise(menu3)
    w.tag_raise(menu4)

w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo

interface.interface1(root, w) #zaladowanie karty Aktualnosci
intro() #zaladowanie 3 sekundowego intro

menu3 = w.create_text(450, 92, anchor=NW, text="Moje dane", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu4 = w.create_text(631, 92, anchor=NW, text="Ustawienia", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu1 = w.create_text(67, 92, anchor=NW, text="Aktualnosci", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu2 = w.create_text(254, 92, anchor=NW, text="Moj dziennik", font=font2, activefill="#D8D8D8", fill="#ffffff")

w.tag_bind(menu1, "<ButtonPress-1>", clickAktualnosci) #wezel laczacy klikniecie z funkcja
w.tag_bind(menu2, "<ButtonPress-1>", clickMojDziennik) #wezel laczacy klikniecie z funkcja
w.tag_bind(menu3, "<ButtonPress-1>", clickMojeDane) #wezel laczacy klikniecie z funkcja
w.tag_bind(menu4, "<ButtonPress-1>", clickUstawienia) #wezel laczacy klikniecie z funkcja

w.pack()

root.mainloop() #petla zdarzen
