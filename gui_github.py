# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:10:29 2019

@author: bmlhs
"""

import tkinter as tk 
from tkinter import *

r = tk.Tk() 
r.iconbitmap('gui_icon_HEj_icon.ico') # This gives the icon to the GUI 
r.title('Flowers') # This is the title to the GUI 
r.geometry("500x700")

v = tk.IntVar() # I am looking for an integer.
u = tk.Label(r, text = 'Blue Flowers').pack()
e = tk.Entry(r, textvariable=v).pack() # Within a text book you expect an integer to be inserted.

def flower():
  white = 5
  blue = v.get()
  green = 2
  total_number_of_flowers = 15 
  F =  (blue/total_number_of_flowers)*100
  output.insert(END, F)

button = tk.Button(r, text = 'Flowers', width=25, command= flower)
button.pack()

lab = tk.Label(r, text = 'How many of the flowers will be blue:').pack()
output = tk.Text(r, width=40, height=2)
output.pack()

r.mainloop() 