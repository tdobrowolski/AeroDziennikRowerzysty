#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from random import randint

con = lite.connect('baza.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Porady")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        porada1 = row[randint(0,9)]
