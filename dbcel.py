#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM CelDane")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        kilometryCel_bd = row[0]
        kalorieCel_bd = row[1]
        treningiCel_bd = row[2]
        postepCel_bd = row[3]
