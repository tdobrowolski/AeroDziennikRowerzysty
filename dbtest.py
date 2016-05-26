#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def dbtest():
    con_test = lite.connect('baza.db')

    with con_test:

        cur_test = con_test.cursor()
        cur_test.execute("SELECT * FROM PodaneDane")

        while True:

            row_test = cur_test.fetchone()

            if row_test == None:
                break

            global imie_bd
            imie_bd = row_test[0]
            global nazwisko_bd
            nazwisko_bd = row_test[1]
            global wiek_bd
            wiek_bd = row_test[2]
            global plec_bd
            plec_bd = row_test[3]
            global wzrost_bd
            wzrost_bd = row_test[4]
            global waga_bd
            waga_bd = row_test[5]
            global cel_bd
            cel_bd = row_test[6]

    con_test.close()
