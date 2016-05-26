#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from random import randint

def dbporady():
    con_por = lite.connect('baza.db')

    with con_por:

        cur_por = con_por.cursor()
        cur_por.execute("SELECT * FROM Porady")

        while True:

            row_por = cur_por.fetchone()

            if row_por == None:
                break

            global porada1
            porada1 = row_por[randint(0,9)]

    con_por.close()
