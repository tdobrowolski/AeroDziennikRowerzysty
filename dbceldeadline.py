#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest

if dbtest.cel_bd == "Popraw nastroj!": #Id aby wybrać odpowiedni do celu wiersz z danymi deadline
    uId = 1
elif dbtest.cel_bd == "Popraw kondycje!":
    uId = 2
else:
    uId = 3

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM CelDeadline WHERE Id=?", (uId,))

    while True:

        row = cur.fetchone()

        if row == None:
            break

        kilometryCelEnd_bd = row[0]
        kalorieCelEnd_bd = row[1]
        treningiCelEnd_bd = row[2]
        postepCelEnd_bd = kilometryCelEnd_bd + kalorieCelEnd_bd + treningiCelEnd_bd

        #Id 1 - Popraw nastroj (easy)
        #Id 2 - Popraw kondycje (medium)
        #Id 3 - Popraw sylwetke (hard)
