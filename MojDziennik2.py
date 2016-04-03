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
w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0) #moje treningi box
w.create_rectangle(412, 486, 412+366, 486+90, fill="#ffffff", width=0) #pasek box
w.create_rectangle(412, 154, 412+366, 154+308, fill="#ffffff", width=0) #postep box
w.create_rectangle(412, 486, 412+91, 486+90, fill="#039CE8", width=0) #pasek postepu box

w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
w.create_text(67, 92, anchor=NW, text="Aktualnosci", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(254, 92, anchor=NW, text="Moj dziennik", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(450, 92, anchor=NW, text="Moje dane", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(631, 92, anchor=NW, text="Ustawienia", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(37, 167, anchor=NW, text="Moje treningi", font=font3)
w.create_text(426, 167, anchor=NW, text="Postep", font=font3)

w.create_rectangle(23, 203, 23+365, 203+63, fill="#fafafa", width=0) #mini box, data - tekst + prostokaty dla karty Moje treningi
w.create_rectangle(23, 266, 23+365, 266+63, fill="#fafafa", width=0)
w.create_rectangle(23, 329, 23+365, 329+63, fill="#fafafa", width=0)

w.create_line(23.5, 265.5, 387.5, 265.5, fill="#e7e7e7") #linia rozdzielajaca mini boxy
w.create_line(23.5, 328.5, 387.5, 328.5, fill="#e7e7e7")
w.create_line(23.5, 387.5, 387.5, 387.5, fill="#e7e7e7")

w.create_text(42, 221.38, anchor=NW, text="Trening 1", font=font3) #tekst
w.create_text(272, 221.38, anchor=NW, text="19.02.2016", font=font3)
w.create_text(42, 284.38, anchor=NW, text="Trening 2", font=font3)
w.create_text(272, 284.38, anchor=NW, text="20.02.2016", font=font3)
w.create_text(42, 347.38, anchor=NW, text="Trening 3", font=font3)
w.create_text(272, 347.38, anchor=NW, text="22.02.2016", font=font3)

w.create_oval(320, 506, 320+48, 506+48, fill = "#039CE8", activefill="#27ADF0", width=0) #FAB button
w.create_text(337, 513, anchor=NW, text="+", font=font2, fill="#ffffff") #plus do FAB

w.create_text(431, 221.45, anchor=NW, text="Wybrany cel: Popraw kondycje", font=font3) #data - tekst dla karty Postęp + Pasek postepu
w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: 24 / 150 km", font=font3)
w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: 1200 / 10000 kcal", font=font3)
w.create_text(431, 341.45, anchor=NW, text="Wykonane treningi: 3 / 10", font=font3)
w.create_text(431, 381.45, anchor=NW, text="Postep w procentach: 25%", font=font3)
w.create_text(431, 421.45, anchor=NW, text="Samopoczucie: Bardzo dobre", font=font3)
w.create_text(551, 517.88, anchor=NW, text="Jestes na dobrej drodze!", font=font3)

w.create_line(238, 128.5, 386, 128.5, fill="#ffffff")#linia menu
w.create_line(23, 203, 388, 203, fill="#0175AE")#linie do box'ow
w.create_line(412, 203, 777, 203, fill="#0175AE")

w.pack()

root.mainloop () #petla zdarzen
