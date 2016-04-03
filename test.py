 #-*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import tkFont


#def quit():
#    import sys; sys.exit() #funkcja wychodząca z programu

root = Tk() #otwarcie okna
root.resizable(0,0) #zablokowanie rozmiaru okna
root.title('Projekt z Pythona') #tytul okna
root.geometry('800x600+200+200') #rozmiar okna

#czcionki
font1 = tkFont.Font(family='Helvetica Neue UltraLight', size=22, ) #czcionka HN UL
font2 = tkFont.Font(family='Helvetica Neue Thin', size=23, ) #czcionka HN T 23
font3 = tkFont.Font(family='Helvetica Neue Thin', size=19, ) #czcionka HN T 19
font4 = tkFont.Font(family='Helvetica Neue Thin', size=56, ) #czcionka HN T 56

#wersja = 'Wersja 0.0.2' #wersja programu
#lbl = Label(root, text=wersja) #przygotowanie etykiety
#lbl.pack(side=BOTTOM) #umieszczenie etykiety u dolu ekranu

#btn = Button(root, text="Koniec", command=quit) #przycisk do wyjscia z programu
#btn.pack(side=BOTTOM)

#canvas UI
w = Tkinter.Canvas(root, bd=0, height=600, width=800) #grafiki

w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
w.create_rectangle(23, 154, 23+366, 199+154, fill="#ffffff", width=0) #cel box
w.create_rectangle(23, 377, 23+366, 199+377, fill="#ffffff", width=0) #porady box
w.create_rectangle(412, 154, 412+366, 422+154, fill="#ffffff", width=0) #ost trening box

w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
w.create_text(67, 92, anchor=NW, text="Aktualnosci", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(254, 92, anchor=NW, text="Moj dziennik", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(450, 92, anchor=NW, text="Moje dane", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(631, 92, anchor=NW, text="Ustawienia", font=font2, activefill="#D8D8D8", fill="#ffffff")
w.create_text(37, 167, anchor=NW, text="Witaj Imie!", font=font3)
w.create_text(426, 167, anchor=NW, text="Ostatni trening", font=font3)
w.create_text(37, 390, anchor=NW, text="Porady", font=font3)

w.create_text(183.5, 229.45, anchor=NW, text="Cel: Popraw kondycję!", font=font3) #data - tekst dla karty Witaj
w.create_text(219, 261.45, anchor=NW, text="25%", font=font4)

w.create_text(431, 221.45, anchor=NW, text="22.02.2016", font=font3) #data - tekst dla karty Ostatni trening
w.create_text(707, 221.45, anchor=NW, text="17:00", font=font3)
w.create_text(431, 261.45, anchor=NW, text="Dystans: 7,45 km", font=font3)
w.create_text(431, 301.45, anchor=NW, text="Czas: 0g 24m 26s", font=font3)
w.create_text(431, 341.45, anchor=NW, text="Kalorie: 241 kcal", font=font3)
w.create_text(431, 381.45, anchor=NW, text="Srednia predkosc: 18,24 km/s", font=font3)
w.create_text(431, 421.45, anchor=NW, text="Samopoczucie: Bardzo dobre", font=font3)
w.create_text(431, 461.45, anchor=NW, text="Warunki atmosferyczne: Pogodnie", font=font3)
w.create_text(431, 501.45, anchor=NW, text="Notatki: Brak", font=font3)



w.create_line(46, 128.5, 194, 128.5, fill="#ffffff")#linia menu
w.create_line(23, 203, 388, 203, fill="#0175AE")#linie do box'ow
w.create_line(23, 423, 388, 423, fill="#0175AE")
w.create_line(412, 203, 777, 203, fill="#0175AE")

ikona2 = PhotoImage(file="ikona2.gif")
w.create_image(40, 220, image=ikona2, anchor=NW)

w.pack()

root.mainloop () #petla zdarzen
