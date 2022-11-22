# Importing the modules
import files
from tkinter import *
import tkinter as tk
from files.about import about

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
   def about():
      main.destroy()
      about.about.abouth()

   # The buttons
   E = tk.Button(main, text ="English", command = english)
   #A = tk.Button(main, text ="About", command = about)
   B = tk.Button(main, text="Back", command=main.quit)
   # Showing the elements.
   E.place(x=100, y=50)
   #A.place(x=200, y=50)
   B.place(x=200, y=50)
   # If this is not here the window will not stay opened.
   main.mainloop()
