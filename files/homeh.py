# Importing the modules
import files
from tkinter import *
import tkinter as tk

def home():
   # Making the window name
   main = tk.Tk()

   # setting the windows size
   main.geometry("400x200")
   main.title("Home Window")

   # Actions
   def english():
      main.destroy()
      files.english.korean()

   # The buttons
   E = tk.Button(main, text ="English", command = english)
   B = tk.Button(main, text="Back", command=main.quit)

   # Showing the elements.
   E.place(x=100, y=50)
   B.place(x=200, y=50)

   # If this is not here the window will not stay opened.
   main.mainloop()
