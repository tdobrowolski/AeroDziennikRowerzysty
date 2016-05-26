#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest

def dbtreninglast():
    dbtest.dbtest()

    con_tl = lite.connect('baza.db')

    with con_tl:

        cur_tl = con_tl.cursor()
        cur_tl.execute("SELECT * FROM Treningi WHERE Id = (select max(Id) from Treningi)")

        while True:

            row_tl = cur_tl.fetchone()

            if row_tl == None:
                break

            global dataLast_bd
            dataLast_bd = row_tl[0]
            global godzinaLast_bd
            godzinaLast_bd = row_tl[1]
            global dystansLast_bd
            dystansLast_bd = row_tl[2]
            global czasLast_bd
            czasLast_bd = row_tl[3]
            global samopoczucieLast_bd
            samopoczucieLast_bd = row_tl[4]
            global pogodaLast_bd
            pogodaLast_bd = row_tl[5]
            global notatkiLast_bd
            notatkiLast_bd = row_tl[6]
            global idLast_bd
            idLast_bd = row_tl[7]

            #zamiana calkowitego czasu na h:m:s
            global sekundyLast_bd
            global minutyLast_bd
            global godzinyLast_bd
            minutyLast_bd, sekundyLast_bd = divmod(czasLast_bd, 60)
            godzinyLast_bd, minutyLast_bd = divmod(minutyLast_bd, 60)

            #obliczanie km/h
            global srPredkoscLast_bd
            srPredkoscLast_bd = dystansLast_bd*3600/czasLast_bd

            #obliczanie kalorii
            global kalorieLast_bd
            kalorieLast_bd = int(dbtest.waga_bd*(czasLast_bd/60)*(0.6345*srPredkoscLast_bd*srPredkoscLast_bd+0.7563*srPredkoscLast_bd+36.725)/(3600))

    con_tl.close()
