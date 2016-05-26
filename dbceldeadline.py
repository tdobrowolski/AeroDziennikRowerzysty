#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest

def dbceldeadline():

    dbtest.dbtest()

    global uId

    if dbtest.cel_bd == "Popraw nastroj!": #Id aby wybrać odpowiedni do celu wiersz z danymi deadline
        uId = 1
    elif dbtest.cel_bd == "Popraw kondycje!":
        uId = 2
    else:
        uId = 3

    con_celd = lite.connect('baza.db')

    with con_celd:

        cur_celd = con_celd.cursor()
        cur_celd.execute("SELECT * FROM CelDeadline WHERE Id=?", (uId,))

        while True:

            row_celd = cur_celd.fetchone()

            if row_celd == None:
                break

            global kilometryCelEnd_bd
            kilometryCelEnd_bd = row_celd[0]
            global kalorieCelEnd_bd
            kalorieCelEnd_bd = row_celd[1]
            global treningiCelEnd_bd
            treningiCelEnd_bd = row_celd[2]
            global postepCelEnd_bd
            postepCelEnd_bd = kilometryCelEnd_bd + kalorieCelEnd_bd + treningiCelEnd_bd

    con_celd.close()

            #Id 1 - Popraw nastroj (easy)
            #Id 2 - Popraw kondycje (medium)
            #Id 3 - Popraw sylwetke (hard)
