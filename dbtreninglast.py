#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Treningi WHERE Id = (select max(Id) from Treningi)")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        dataLast_bd = row[0]
        godzinaLast_bd = row[1]
        dystansLast_bd = row[2]
        czasLast_bd = row[3]
        samopoczucieLast_bd = row[4]
        pogodaLast_bd = row[5]
        notatkiLast_bd = row[6]

        #zamiana calkowitego czasu na h:m:s
        minutyLast_bd, sekundyLast_bd = divmod(czasLast_bd, 60)
        godzinyLast_bd, minutyLast_bd = divmod(minutyLast_bd, 60)

        #obliczanie km/h
        srPredkoscLast_bd = dystansLast_bd*3600/czasLast_bd

        #obliczanie kalorii
        kalorieLast_bd = int(dbtest.waga_bd*(czasLast_bd/60)*(0.6345*srPredkoscLast_bd*srPredkoscLast_bd+0.7563*srPredkoscLast_bd+36.725)/(3600))
