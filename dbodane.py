#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest
import dbtreninglast

def dbodane():

    dbtreninglast.dbtreninglast()

    con_od = lite.connect('baza.db')

    i = 1
    global kilometryTotal_bd
    kilometryTotal_bd = 0
    global kalorieTotal_bd
    kalorieTotal_bd = 0
    global treningiTotal_bd
    treningiTotal_bd = dbtreninglast.idLast_bd
    global czasTotal_bd
    czasTotal_bd = 0

    while i <= dbtreninglast.idLast_bd:

        with con_od:

            cur_od = con_od.cursor()
            cur_od.execute("SELECT * FROM Treningi WHERE Id = ?", (i,))

            while True:

                row_od = cur_od.fetchone()

                if row_od == None:
                    break

                kilometryTotal_bd += row_od[2]

                srPredkoscLastek_bd = int(row_od[2])*3600/int(row_od[3])

                kalorieTotal_bd += int(dbtest.waga_bd*(row_od[3]/60)*(0.6345*srPredkoscLastek_bd*srPredkoscLastek_bd+0.7563*srPredkoscLastek_bd+36.725)/(3600))

                czasTotal_bd += row_od[3]

            cur_od.execute("SELECT * FROM ObliczoneDane")

            while True:

                row_od2 = cur_od.fetchone()

                if row_od2 == None:
                    break

                global celeTotal_bd
                celeTotal_bd = row_od2[4]

        i = i + 1

    con_od.close()

    global sekundyCalkowite_bd
    global minutyCalkowite_bd
    global godzinyCalkowite_bd
    minutyCalkowite_bd, sekundyCalkowite_bd = divmod(czasTotal_bd, 60)
    godzinyCalkowite_bd, minutyCalkowite_bd = divmod(minutyCalkowite_bd, 60)
