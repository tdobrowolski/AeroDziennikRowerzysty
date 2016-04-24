#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM DaneUzytkownika")

    while True:

        dupa = cur.fetchone()

        if dupa == None:
            break

        print dupa[0], dupa[1]
