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
w.create_text(37, 167, anchor=NW, text="Wpisane dane", font=font3)
w.create_text(426, 167, anchor=NW, text="Obliczone dane", font=font3)

w.create_text(42, 221.45, anchor=NW, text="Imie: Tobiasz", font=font3) #data - tekst dla karty Wpisane dane
w.create_text(42, 261.45, anchor=NW, text="Nazwisko: Dobrowolski", font=font3)
w.create_text(42, 301.45, anchor=NW, text="Wiek: 19 lat", font=font3)
w.create_text(42, 341.45, anchor=NW, text="Plec: Mezczyzna", font=font3)
w.create_text(42, 381.45, anchor=NW, text="Wzrost: 182 cm", font=font3)
w.create_text(42, 421.45, anchor=NW, text="Waga: 68 kg", font=font3)

w.create_text(431, 221.45, anchor=NW, text="Wartosc BMI: 20,53", font=font3) #data - tekst dla karty Obliczone dane
w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: 24 km", font=font3)
w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: 1200 kcal", font=font3)
w.create_text(431, 341.45, anchor=NW, text="Calkowity czas: 1g 23m 17s", font=font3)
w.create_text(431, 381.45, anchor=NW, text="Wykonane treningi: 3", font=font3)
w.create_text(431, 421.45, anchor=NW, text="Zdobyte cele: 0", font=font3)

w.create_line(426, 128.5, 574, 128.5, fill="#ffffff")#linia menu
w.create_line(23, 203, 388, 203, fill="#0175AE")#linie do box'ow
w.create_line(412, 203, 777, 203, fill="#0175AE")

w.pack()

root.mainloop () #petla zdarzen
