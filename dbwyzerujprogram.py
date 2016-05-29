#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def wyzerujprogram():
    con_wp = lite.connect('baza.db')

    with con_wp:

        cur_wp = con_wp.cursor()

        cur_wp.execute("DELETE FROM ObliczoneDane")
        insert_zeros = (0,0,0,0,0)
        cur_wp.execute("INSERT INTO ObliczoneDane VALUES(?,?,?,?,?)", insert_zeros)

        cur_wp.execute("DELETE FROM Treningi")
        insert_zeros1 = (0,0,0,1,0,0,0,0)
        cur_wp.execute("INSERT INTO Treningi VALUES(?,?,?,?,?,?,?,?)", insert_zeros1)

        cur_wp.execute("DELETE FROM CelDane")
        insert_zeros2 = (0,0,0,0)
        cur_wp.execute("INSERT INTO CelDane VALUES(?,?,?,?)", insert_zeros2)

    con_wp.commit()
    con_wp.close()
