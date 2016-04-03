import Tkinter
from Tkinter import *
import tkFont

root = Tk() #otwarcie okna

w = Tkinter.Canvas(root, bd=0, height=600, width=800) #grafiki

font2 = tkFont.Font(family='Helvetica Neue Thin', size=23, ) #czcionka HN T 23

menu1 = w.create_text(67, 92, anchor=NW, text="Aktualnosci", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu2 = w.create_text(254, 92, anchor=NW, text="Moj dziennik", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu3 = w.create_text(450, 92, anchor=NW, text="Moje dane", font=font2, activefill="#D8D8D8", fill="#ffffff")

menu4 = w.create_text(631, 92, anchor=NW, text="Ustawienia", font=font2, activefill="#D8D8D8", fill="#ffffff")
