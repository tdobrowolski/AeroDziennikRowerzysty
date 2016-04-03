#-*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import tkFont
import interface

root = Tk() #otwarcie okna
root.resizable(0,0) #zablokowanie rozmiaru okna
root.title('Projekt z Pythona') #tytul okna
root.geometry('800x600+200+200') #rozmiar okna

#canvas UI
w = Tkinter.Canvas(root, bd=0, height=600, width=800) #grafiki

def clickAktualnosci(event):
    interface.interface1(root, w)

def clickMojDziennik(event): #funkcja dla klikniecia w Moj Dziennik
    interface.interface2(root, w)

def clickMojeDane(event):
    interface.interface3(root, w)

def clickUstawienia(event):
    interface.interface4(root, w)

interface.interface1(root, w) #zaladowanie karty Aktualnosci

w.tag_bind(interface.menu1, "<ButtonPress-1>", clickAktualnosci) #wezel laczacy klikniecie z funkcja
w.tag_bind(interface.menu2, "<ButtonPress-1>", clickMojDziennik) #wezel laczacy klikniecie z funkcja
w.tag_bind(interface.menu3, "<ButtonPress-1>", clickMojeDane) #wezel laczacy klikniecie z funkcja
w.tag_bind(interface.menu4, "<ButtonPress-1>", clickUstawienia) #wezel laczacy klikniecie z funkcja

w.pack()

root.mainloop () #petla zdarzen
