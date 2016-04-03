#-*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import tkFont


root = Tk() #otwarcie okna
root.resizable(0,0) #zablokowanie rozmiaru okna
root.title('Projekt z Pythona') #tytul okna
root.geometry('800x600+200+200') #rozmiar okna

#czcionki
font1 = tkFont.Font(family='Helvetica Neue UltraLight', size=22, ) #czcionka HN UL
font2 = tkFont.Font(family='Helvetica Neue Thin', size=23, ) #czcionka HN T 23
font3 = tkFont.Font(family='Helvetica Neue Thin', size=19, ) #czcionka HN T 19
font4 = tkFont.Font(family='Helvetica Neue Thin', size=56, ) #czcionka HN T 56
font5 = tkFont.Font(family='Helvetica Neue Thin', size=15, ) #czcionka HN T 15

#canvas UI
w = Tkinter.Canvas(root, bd=0, height=600, width=800) #grafiki

w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0) #wpisane box
w.create_rectangle(412, 154, 412+366, 154+422, fill="#ffffff", width=0) #obliczone box

w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
w.create_text(67, 92, anchor=NW, text="Aktualnosci", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(254, 92, anchor=NW, text="Moj dziennik", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(450, 92, anchor=NW, text="Moje dane", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(631, 92, anchor=NW, text="Ustawienia", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(37, 167, anchor=NW, text="Moje dane", font=font3)

w.create_text(42, 221.45, anchor=NW, text="Imie:", font=font3) #data - tekst dla karty Moje dane
w.create_text(42, 261.45, anchor=NW, text="Nazwisko:", font=font3)
w.create_text(42, 301.45, anchor=NW, text="Wiek:", font=font3)
w.create_text(42, 341.45, anchor=NW, text="Plec:", font=font3)
w.create_text(42, 381.45, anchor=NW, text="Wzrost:", font=font3)
w.create_text(42, 421.45, anchor=NW, text="Waga:", font=font3)
w.create_text(42, 462.45, anchor=NW, text="Wyzeruj program", font=font3, activefill="#636363")

w.create_text(517.5, 460, anchor=NW, text="Dziennik rowerzysty", font=font3) #data - tekst dla karty Dane programu
w.create_text(532, 489, anchor=NW, text="Tobiasz Dobrowolski", font=font5)
w.create_text(580, 514, anchor=NW, text="2016", font=font5)
w.create_text(562, 537, anchor=NW, text="Wersja 0.1", font=font5)

w.create_line(608, 128.5, 756, 128.5, fill="#ffffff") #linia menu
w.create_line(23, 203, 388, 203, fill="#0175AE") #linie do box'ow

w.pack()

root.mainloop () #petla zdarzen
