#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def dbcel():
    con_cel = lite.connect('baza.db')

    with con_cel:

        cur_cel = con_cel.cursor()
        cur_cel.execute("SELECT * FROM CelDane")

        while True:

            row = cur_cel.fetchone()

            if row == None:
                break

            global kilometryCel_bd
            kilometryCel_bd = row[0]
            global kalorieCel_bd
            kalorieCel_bd = row[1]
            global treningiCel_bd
            treningiCel_bd = row[2]
            global postepCel_bd
            postepCel_bd = row[3]

    con_cel.close()
