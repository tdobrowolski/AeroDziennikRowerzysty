#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest
import dbtreninglast


con = lite.connect('baza.db')

i = 1
kilometryTotal_bd = 0
kalorieTotal_bd = 0
treningiTotal_bd = dbtreninglast.idLast_bd
czasTotal_bd = 0



while i <= dbtreninglast.idLast_bd:

    with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM Treningi WHERE Id = ?", (i,))

        while True:

            row = cur.fetchone()

            if row == None:
                break

            kilometryTotal_bd += row[2]

            srPredkoscLastek_bd = int(row[2])*3600/int(row[3])

            kalorieTotal_bd += int(dbtest.waga_bd*(row[3]/60)*(0.6345*srPredkoscLastek_bd*srPredkoscLastek_bd+0.7563*srPredkoscLastek_bd+36.725)/(3600))

            czasTotal_bd += row[3]

        cur.execute("SELECT * FROM ObliczoneDane")

        while True:

            row = cur.fetchone()

            if row == None:
                break

            celeTotal_bd =  row[4]

            #exit()

    i = i + 1



minutyCalkowite_bd, sekundyCalkowite_bd = divmod(czasTotal_bd, 60)
godzinyCalkowite_bd, minutyCalkowite_bd = divmod(minutyCalkowite_bd, 60)
