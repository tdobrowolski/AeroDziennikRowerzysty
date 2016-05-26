#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import dbtest
import dbcel
import dbceldeadline
import Tkinter
from Tkinter import *
import tkMessageBox

def sprawdzanieCelu(root):

    dbcel.dbcel()
    dbceldeadline.dbceldeadline()
    dbtest.dbtest()

    if dbcel.postepCel_bd >= dbceldeadline.postepCelEnd_bd:

        con_sc = lite.connect('baza.db')

        insert00 = (0, 0, 0, 0)

        with con_sc:

            cur_sc = con_sc.cursor()
            cur_sc.execute("DELETE FROM CelDane")
            cur_sc.execute("INSERT INTO CelDane VALUES(?,?,?,?)", insert00)
            cur_sc.execute("SELECT * FROM ObliczoneDane")

            while True:

                row = cur_sc.fetchone()

                if row == None:
                    break

                updateCel = row[4] + 1
                insert01 = (0,0,0,0,updateCel)
                cur_sc.execute("DELETE FROM ObliczoneDane")
                cur_sc.execute("INSERT INTO ObliczoneDane VALUES(?,?,?,?,?)", insert01)

        con_sc.commit()
        con_sc.close()

        tkMessageBox.showinfo("Uzyskales cel", "Brawo, zaliczyles swoj cel. Wybierz nowy lub sprobuj osiagnac go jeszcze raz. Zresetuj program aby zaktualizowac dane.")
