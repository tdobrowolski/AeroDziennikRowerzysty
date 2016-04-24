#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM PodaneDane")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        imie_bd = row[0]
        nazwisko_bd = row[1]
        wiek_bd = row[2]
        plec_bd = row[3]
        wzrost_bd = row[4]
        waga_bd = row[5]
