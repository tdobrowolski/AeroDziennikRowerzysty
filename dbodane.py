#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM ObliczoneDane")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        kilometryTotal_bd = row[0]
        kalorieTotal_bd = row[1]
        czasTotal_bd = row[2]
        treningiTotal_bd = row[3]
        celeTotal_bd = row[4]
