#!~/anaconda3/bin/python

from tkinter import *
import tkinter as tk
import pyshorteners

#creating gui
window = tk.Tk()

window.geometry('500x300')
window.title("URL Shortener")

label1 = Label(window, text = "Enter your URL : ")
label1.grid(row = 1, column = 0, pady = 5, padx = 5)

input_box = Entry(window, width = 50)
input_box.grid(row = 1, column = 1, pady = 5, padx = 5)


def short_url() :

    url = input_box.get()
    psr = pyshorteners.Shortener()
    shorted_url = psr.tinyurl.short(url)

    label2 = Label(window, text = 'Your shorted URL is :- ')
    label2.grid(row = 2, column = 0, pady = 5, padx = 5)

    label3 = Label(window, text = shorted_url)
    label3.grid(row = 2, column = 1, pady = 5, padx = 5)

    print(f"shorted URL :- {shorted_url}")      #copy shorted URL from terminal.

button = tk.Button(window, text = 'proceed', bg = 'green', command = short_url).place(x = 200, y = 80)

window.mainloop()