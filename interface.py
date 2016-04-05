#-*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
import tkFont


def interface3(root, w):

    w.delete("delint")

    #w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
    #w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #wpisane box
    w.create_rectangle(412, 154, 412+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #obliczone box

    #w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

    #w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
    w.create_text(37, 167, anchor=NW, text="Wpisane dane", font=font3, tags=("delint"))
    w.create_text(426, 167, anchor=NW, text="Obliczone dane", font=font3, tags=("delint"))

    w.create_text(42, 221.45, anchor=NW, text="Imie: Tobiasz", font=font3) #data - tekst dla karty Wpisane dane
    w.create_text(42, 261.45, anchor=NW, text="Nazwisko: Dobrowolski", font=font3, tags=("delint"))
    w.create_text(42, 301.45, anchor=NW, text="Wiek: 19 lat", font=font3, tags=("delint"))
    w.create_text(42, 341.45, anchor=NW, text="Plec: Mezczyzna", font=font3, tags=("delint"))
    w.create_text(42, 381.45, anchor=NW, text="Wzrost: 182 cm", font=font3, tags=("delint"))
    w.create_text(42, 421.45, anchor=NW, text="Waga: 68 kg", font=font3, tags=("delint"))

    w.create_text(431, 221.45, anchor=NW, text="Wartosc BMI: 20,53", font=font3, tags=("delint")) #data - tekst dla karty Obliczone dane
    w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: 24 km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: 1200 kcal", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Calkowity czas: 1g 23m 17s", font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Wykonane treningi: 3", font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Zdobyte cele: 0", font=font3, tags=("delint"))

    w.create_line(426, 128.5, 574, 128.5, fill="#ffffff", tags=("delint"))#linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint"))#linie do box'ow
    w.create_line(412, 203, 777, 203, fill="#0175AE", tags=("delint"))

def interface1(root, w):

    w.delete("delint")

    #czcionki
    global font1
    font1 = tkFont.Font(family='Helvetica Neue UltraLight', size=22, ) #czcionka HN UL
    global font2
    font2 = tkFont.Font(family='Helvetica Neue Thin', size=23, ) #czcionka HN T 23
    global font3
    font3 = tkFont.Font(family='Helvetica Neue Thin', size=19, ) #czcionka HN T 19
    global font4
    font4 = tkFont.Font(family='Helvetica Neue Thin', size=56, ) #czcionka HN T 56
    global font5
    font5 = tkFont.Font(family='Helvetica Neue Thin', size=15, ) #czcionka HN T 15

    w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
    w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
    w.create_rectangle(23, 154, 23+366, 199+154, fill="#ffffff", width=0, tags=("delint")) #cel box
    w.create_rectangle(23, 377, 23+366, 199+377, fill="#ffffff", width=0, tags=("delint")) #porady box
    w.create_rectangle(412, 154, 412+366, 422+154, fill="#ffffff", width=0, tags=("delint")) #ost trening box

    w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

    w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
    w.create_text(37, 167, anchor=NW, text="Witaj Imie!", font=font3, tags=("delint"))
    w.create_text(426, 167, anchor=NW, text="Ostatni trening", font=font3, tags=("delint"))
    w.create_text(37, 390, anchor=NW, text="Porady", font=font3, tags=("delint"))

    w.create_text(183.5, 229.45, anchor=NW, text="Cel: Popraw kondycję!", font=font3, tags=("delint")) #data - tekst dla karty Witaj
    w.create_text(219, 261.45, anchor=NW, text="25%", font=font4, tags=("delint"))

    w.create_text(431, 221.45, anchor=NW, text="22.02.2016", font=font3, tags=("delint")) #data - tekst dla karty Ostatni trening
    w.create_text(707, 221.45, anchor=NW, text="17:00", font=font3, tags=("delint"))
    w.create_text(431, 261.45, anchor=NW, text="Dystans: 7,45 km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Czas: 0g 24m 26s", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Kalorie: 241 kcal", font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Srednia predkosc: 18,24 km/s", font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Samopoczucie: Bardzo dobre", font=font3, tags=("delint"))
    w.create_text(431, 461.45, anchor=NW, text="Warunki atmosferyczne: Pogodnie", font=font3, tags=("delint"))
    w.create_text(431, 501.45, anchor=NW, text="Notatki: Brak", font=font3, tags=("delint"))

    w.create_line(46, 128.5, 194, 128.5, fill="#ffffff", tags=("delint"))#linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint"))#linie do box'ow
    w.create_line(23, 423, 388, 423, fill="#0175AE", tags=("delint"))
    w.create_line(412, 203, 777, 203, fill="#0175AE", tags=("delint"))

    #photo = PhotoImage(file="ikona2.gif")
    #w.create_image(40, 220, image=photo, anchor=NW, tags=("delint"))

def interface2(root, w):

    w.delete("delint")

    #w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
    #w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #moje treningi box
    w.create_rectangle(412, 486, 412+366, 486+90, fill="#ffffff", width=0, tags=("delint")) #pasek box
    w.create_rectangle(412, 154, 412+366, 154+308, fill="#ffffff", width=0, tags=("delint")) #postep box
    w.create_rectangle(412, 486, 412+91, 486+90, fill="#039CE8", width=0, tags=("delint")) #pasek postepu box

    #w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

    #w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff") #imie i nazwisko
    w.create_text(37, 167, anchor=NW, text="Moje treningi", font=font3, tags=("delint"))
    w.create_text(426, 167, anchor=NW, text="Postep", font=font3, tags=("delint"))

    w.create_rectangle(23, 203, 23+365, 203+63, fill="#fafafa", width=0, tags=("delint")) #mini box, data - tekst + prostokaty dla karty Moje treningi
    w.create_rectangle(23, 266, 23+365, 266+63, fill="#fafafa", width=0, tags=("delint"))
    w.create_rectangle(23, 329, 23+365, 329+63, fill="#fafafa", width=0, tags=("delint"))

    w.create_line(23.5, 265.5, 387.5, 265.5, fill="#e7e7e7", tags=("delint")) #linia rozdzielajaca mini boxy
    w.create_line(23.5, 328.5, 387.5, 328.5, fill="#e7e7e7", tags=("delint"))
    w.create_line(23.5, 387.5, 387.5, 387.5, fill="#e7e7e7", tags=("delint"))

    w.create_text(42, 221.38, anchor=NW, text="Trening 1", font=font3, tags=("delint")) #tekst
    w.create_text(272, 221.38, anchor=NW, text="19.02.2016", font=font3, tags=("delint"))
    w.create_text(42, 284.38, anchor=NW, text="Trening 2", font=font3, tags=("delint"))
    w.create_text(272, 284.38, anchor=NW, text="20.02.2016", font=font3, tags=("delint"))
    w.create_text(42, 347.38, anchor=NW, text="Trening 3", font=font3, tags=("delint"))
    w.create_text(272, 347.38, anchor=NW, text="22.02.2016", font=font3, tags=("delint"))

    w.create_oval(320, 506, 320+48, 506+48, fill = "#039CE8", activefill="#27ADF0", width=0, tags=("delint")) #FAB button
    w.create_text(337, 513, anchor=NW, text="+", font=font2, fill="#ffffff", tags=("delint")) #plus do FAB

    w.create_text(431, 221.45, anchor=NW, text="Wybrany cel: Popraw kondycje", font=font3, tags=("delint")) #data - tekst dla karty Postęp + Pasek postepu
    w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: 24 / 150 km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: 1200 / 10000 kcal", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Wykonane treningi: 3 / 10", font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Postep w procentach: 25%", font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Samopoczucie: Bardzo dobre", font=font3, tags=("delint"))
    w.create_text(551, 517.88, anchor=NW, text="Jestes na dobrej drodze!", font=font3, tags=("delint"))

    w.create_line(238, 128.5, 386, 128.5, fill="#ffffff", tags=("delint"))#linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint"))#linie do box'ow
    w.create_line(412, 203, 777, 203, fill="#0175AE", tags=("delint"))

def interface4(root, w):

    w.delete("delint")

    #w.create_rectangle(0, 0, 800, 600, fill="#EEEEEF", width=0) #gorne tlo
    #w.create_rectangle(0, 0, 800, 130, fill="#039CE8", width=0) #gorne tlo
    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #wpisane box
    w.create_rectangle(412, 154, 412+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #obliczone box

    #w.create_oval(24, 24, 59, 59, fill = "#ffffff", width=0) #avatar

    #w.create_text(71, 29, anchor=NW, text="Imie Nazwisko", font=font1, fill="#ffffff", tags=("delint")) #imie i nazwisko
    w.create_text(37, 167, anchor=NW, text="Moje dane", font=font3, tags=("delint"))

    w.create_text(42, 221.45, anchor=NW, text="Imie:", font=font3, tags=("delint")) #data - tekst dla karty Moje dane
    w.create_text(42, 261.45, anchor=NW, text="Nazwisko:", font=font3, tags=("delint"))
    w.create_text(42, 301.45, anchor=NW, text="Wiek:", font=font3, tags=("delint"))
    w.create_text(42, 341.45, anchor=NW, text="Plec:", font=font3, tags=("delint"))
    w.create_text(42, 381.45, anchor=NW, text="Wzrost:", font=font3, tags=("delint"))
    w.create_text(42, 421.45, anchor=NW, text="Waga:", font=font3, tags=("delint"))
    w.create_text(42, 462.45, anchor=NW, text="Wyzeruj program", font=font3, activefill="#636363", tags=("delint"))

    w.create_text(517.5, 460, anchor=NW, text="Dziennik rowerzysty", font=font3, tags=("delint")) #data - tekst dla karty Dane programu
    w.create_text(532, 489, anchor=NW, text="Tobiasz Dobrowolski", font=font5, tags=("delint"))
    w.create_text(580, 514, anchor=NW, text="2016", font=font5, tags=("delint"))
    w.create_text(562, 537, anchor=NW, text="Wersja 0.1", font=font5, tags=("delint"))

    w.create_line(608, 128.5, 756, 128.5, fill="#ffffff", tags=("delint")) #linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint")) #linie do box'ow
