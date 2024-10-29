"""
Window1.py

Written:     Vern Hardingham

Date: 2024-10-28

Provides the opening window to the program
    - Identifies the program
    - Future versions may include a login to record the user actions
"""

from tkinter import *
import tkinter as tk

# Create the main window
mainWindow = tk.Tk()
mainWindow.title("Capricorn - Simply Parts")
mainWindow.geometry('266x460')

txt = "Simply Parts"
txt = txt.center(12)
lbl1 = Label(mainWindow, text = txt,
                        font = ('Helvetica, 24'))

lbl1.place(relx=0.5, rely=.5, anchor=tk.CENTER)

mainWindow.mainloop()