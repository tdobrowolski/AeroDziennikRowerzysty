#-*- coding: utf-8 -*-
from __future__ import division
import Tkinter
from Tkinter import *
import tkFont
import dbtest
import dbporady
import popupdane
import dbodane
import dbcel
import dbceldeadline
import popupdodajtrening
import dbtreninglast


def interface3(root, w):

    w.delete("delint")

    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #wpisane box
    w.create_rectangle(412, 154, 412+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #obliczone box

    w.create_text(37, 167, anchor=NW, text="Wpisane dane", font=font3, tags=("delint"))
    w.create_text(426, 167, anchor=NW, text="Obliczone dane", font=font3, tags=("delint"))

    w.create_text(42, 221.45, anchor=NW, text="Imie: " + dbtest.imie_bd, font=font3) #data - tekst dla karty Wpisane dane
    w.create_text(42, 261.45, anchor=NW, text="Nazwisko: " + dbtest.nazwisko_bd, font=font3, tags=("delint"))
    w.create_text(42, 301.45, anchor=NW, text="Wiek: " + str(dbtest.wiek_bd) + " lat", font=font3, tags=("delint"))
    w.create_text(42, 341.45, anchor=NW, text="Plec: " + dbtest.plec_bd, font=font3, tags=("delint"))
    w.create_text(42, 381.45, anchor=NW, text="Wzrost: " + str(dbtest.wzrost_bd) + " cm", font=font3, tags=("delint"))
    w.create_text(42, 421.45, anchor=NW, text="Waga: " + str(dbtest.waga_bd) + " kg", font=font3, tags=("delint"))

    w.create_text(431, 221.45, anchor=NW, text="Wartosc BMI: " + str(dbtest.waga_bd//((dbtest.wzrost_bd/100) * (dbtest.wzrost_bd/100))), font=font3, tags=("delint")) #data - tekst dla karty Obliczone dane
    w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: " + str(dbodane.kilometryTotal_bd) + " km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: " + str(dbodane.kalorieTotal_bd) + " kcal", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Calkowity czas: " + str(dbodane.godzinyCalkowite_bd) + "g " + str(dbodane.minutyCalkowite_bd) + "m " + str(dbodane.sekundyCalkowite_bd) + "s", font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Wykonane treningi: " + str(dbodane.treningiTotal_bd), font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Zdobyte cele: " + str(dbodane.celeTotal_bd), font=font3, tags=("delint"))

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

    w.create_text(71, 29, anchor=NW, text=dbtest.imie_bd + " " + dbtest.nazwisko_bd, font=font1, fill="#ffffff") #imie i nazwisko
    w.create_text(37, 167, anchor=NW, text="Witaj " + dbtest.imie_bd + "!", font=font3, tags=("delint"))
    w.create_text(426, 167, anchor=NW, text="Ostatni trening", font=font3, tags=("delint"))
    w.create_text(37, 390, anchor=NW, text="Porady", font=font3, tags=("delint"))

    w.create_text(42, 441.45, anchor=NW, text=dbporady.porada1, font=font3, tags=("delint"))

    w.create_text(183.5, 229.45, anchor=NW, text="Cel: " + dbtest.cel_bd, font=font3, tags=("delint")) #data - tekst dla karty Witaj
    w.create_text(219, 261.45, anchor=NW, text=str(dbcel.postepCel_bd) + "%", font=font4, tags=("delint"))

    w.create_text(431, 221.45, anchor=NW, text=dbtreninglast.dataLast_bd, font=font3, tags=("delint")) #data - tekst dla karty Ostatni trening
    w.create_text(707, 221.45, anchor=NW, text=dbtreninglast.godzinaLast_bd, font=font3, tags=("delint"))
    w.create_text(431, 261.45, anchor=NW, text="Dystans: " + str(dbtreninglast.dystansLast_bd) + " km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Czas: " + str(dbtreninglast.godzinyLast_bd) + "g " + str(dbtreninglast.minutyLast_bd) + "m " + str(dbtreninglast.sekundyLast_bd) + "s ", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Kalorie: " + str(dbtreninglast.kalorieLast_bd) + " kcal", font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Srednia predkosc: " + str(dbtreninglast.srPredkoscLast_bd) + " km/h", font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Samopoczucie: " + dbtreninglast.samopoczucieLast_bd, font=font3, tags=("delint"))
    w.create_text(431, 461.45, anchor=NW, text="Warunki atmosferyczne: " + dbtreninglast.pogodaLast_bd, font=font3, tags=("delint"))
    w.create_text(431, 501.45, anchor=NW, text="Notatki: " + dbtreninglast.notatkiLast_bd, font=font3, tags=("delint"))

    w.create_line(46, 128.5, 194, 128.5, fill="#ffffff", tags=("delint"))#linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint"))#linie do box'ow
    w.create_line(23, 423, 388, 423, fill="#0175AE", tags=("delint"))
    w.create_line(412, 203, 777, 203, fill="#0175AE", tags=("delint"))

    wybrana_ikona = Tkinter.PhotoImage(file=r'ikona'+str(dbceldeadline.uId)+'.ppm')
    root.wybrana_ikona = wybrana_ikona  #zapobiegam wrzuceniu obrazka do smieci
    w.create_image((40,220), image=wybrana_ikona, anchor='nw', tags=("delint"))


def interface2(root, w):

    w.delete("delint")

    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #moje treningi box
    w.create_rectangle(412, 486, 412+366, 486+90, fill="#ffffff", width=0, tags=("delint")) #pasek box
    w.create_rectangle(412, 154, 412+366, 154+308, fill="#ffffff", width=0, tags=("delint")) #postep box
    w.create_rectangle(412, 486, 412+(366 * (dbcel.postepCel_bd/100)), 486+90, fill="#039CE8", width=0, tags=("delint")) #pasek postepu box

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

    dodajtrening = w.create_oval(320, 506, 320+48, 506+48, fill = "#039CE8", activefill="#27ADF0", width=0, tags=("delint")) #FAB button
    w.create_text(337, 513, anchor=NW, text="+", font=font2, fill="#ffffff", tags=("delint")) #plus do FAB

    w.create_text(431, 221.45, anchor=NW, text="Wybrany cel: " + dbtest.cel_bd, font=font3, tags=("delint")) #data - tekst dla karty Postęp + Pasek postepu
    w.create_text(431, 261.45, anchor=NW, text="Przejechane kilometry: " + str(dbcel.kilometryCel_bd) + " / " +  str(dbceldeadline.kilometryCelEnd_bd) + " km", font=font3, tags=("delint"))
    w.create_text(431, 301.45, anchor=NW, text="Spalone kalorie: " + str(dbcel.kalorieCel_bd) + " / " + str(dbceldeadline.kalorieCelEnd_bd) + " kcal", font=font3, tags=("delint"))
    w.create_text(431, 341.45, anchor=NW, text="Wykonane treningi: " + str(dbcel.treningiCel_bd) + " / " + str(dbceldeadline.treningiCelEnd_bd), font=font3, tags=("delint"))
    w.create_text(431, 381.45, anchor=NW, text="Postep w procentach: " + str(dbcel.postepCel_bd) + "%", font=font3, tags=("delint"))
    w.create_text(431, 421.45, anchor=NW, text="Oby tak dalej!", font=font3, tags=("delint"))
    w.create_text(551, 517.88, anchor=NW, text="Jestes na dobrej drodze!", font=font3, tags=("delint"))

    w.create_line(238, 128.5, 386, 128.5, fill="#ffffff", tags=("delint"))#linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint"))#linie do box'ow
    w.create_line(412, 203, 777, 203, fill="#0175AE", tags=("delint"))

    def clickDodajTrening(event):
        popupdodajtrening.popup2(root) #testowe okienko

    w.tag_bind(dodajtrening, "<ButtonPress-1>", clickDodajTrening) #wezel laczacy klikniecie z funkcja

def interface4(root, w):

    w.delete("delint")

    w.create_rectangle(23, 154, 23+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #wpisane box
    w.create_rectangle(412, 154, 412+366, 154+422, fill="#ffffff", width=0, tags=("delint")) #obliczone box

    w.create_text(37, 167, anchor=NW, text="Moje dane", font=font3, tags=("delint"))

    zmiendane = w.create_text(145, 354, anchor=NW, text="Zmien dane", activefill="#D8D8D8", font=font2, tags=("delint")) #data - tekst dla karty Moje dane

    w.create_text(517.5, 460, anchor=NW, text="Dziennik rowerzysty", font=font3, tags=("delint")) #data - tekst dla karty Dane programu
    w.create_text(532, 489, anchor=NW, text="Tobiasz Dobrowolski", font=font5, tags=("delint"))
    w.create_text(580, 514, anchor=NW, text="2016", font=font5, tags=("delint"))
    w.create_text(562, 537, anchor=NW, text="Wersja 0.6", font=font5, tags=("delint"))

    w.create_line(608, 128.5, 756, 128.5, fill="#ffffff", tags=("delint")) #linia menu
    w.create_line(23, 203, 388, 203, fill="#0175AE", tags=("delint")) #linie do box'ow

    def clickZmienDane(event):
        popupdane.popup1(root) #testowe okienko

    w.tag_bind(zmiendane, "<ButtonPress-1>", clickZmienDane) #wezel laczacy klikniecie z funkcja
