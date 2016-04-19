#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None #w razie braku dostepu do bazy danych (np. gdy nie ma miejsca na dysku), zapobiegamy bledom

try:
    con = lite.connect('test.db') #laczymy sie z baza danych

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()') #wykonujemy nasze polecenie

    data = cur.fetchone()

    print "SQLite version: %s" % data #wypisujemy to co dostalismy

except lite.Error, e:

    print "Error %s:" % e.args[0] #w razie wyjatku wypisujemy blad i wychodzimy
    sys.exit(1)

finally:

    if con:
        con.close() #zamykamy
