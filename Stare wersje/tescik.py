from Tkinter import *
import tkFont
import Tkinter
import dbtreninglast
import popuptrening

def scrollTreningi(root):
    global frame
    frame = Frame(root, width=346, height=363)
    frame.grid(row = 0, column = 0)
    frame.place(x = 23, y = 204)
    w3 = Tkinter.Canvas(frame, bd=0, height=363, width=346, scrollregion=(0, 0, 346, dbtreninglast.idLast_bd*63)) #grafiki

    font3 = tkFont.Font(family='Helvetica Neue Thin', size=19) #czcionka HN T 19

    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command = w3.yview)


    def clickPokazTrening(event, i):
        popuptrening.popup3(i) #testowe okienko


    #wypelnienie
    lista_treningow = [None] * dbtreninglast.idLast_bd
    i = 1
    while i <= dbtreninglast.idLast_bd:
        w3.create_line(0.5, 62.5+((i-1)*63), 346.5, 62.5+((i-1)*63), fill="#e7e7e7", tags=("delint")) #linia rozdzielajaca mini boxy
        index_dla_listy = i-1
        lista_treningow[index_dla_listy] = w3.create_text(19, 18.38+((i-1)*63), anchor=NW, text="Trening " + str(i), font=font3, tags=("delint")) #tekst
        w3.tag_bind(lista_treningow[index_dla_listy], "<ButtonPress-1>", lambda event, arg=i: clickPokazTrening(event, arg)) #wezel laczacy klikniecie z funkcja
        i = i + 1

    w3.config(width = 346, height = 363)
    w3.config(yscrollcommand = vbar.set)
    w3.pack(side = LEFT, expand = True, fill = BOTH)

    #w3.pack()
