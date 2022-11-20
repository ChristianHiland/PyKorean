# Importing the modules
import files.module as module
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
      module.english.korean()
   def korean():
      module.korean.english()
   def about():
      module.about.about()

   # The buttons
   E = tk.Button(main, text ="English", command = english)
   K = tk.Button(main, text = "Korean", command = korean)
   A = tk.Button(main, text ="About", command = about)
   B = tk.Button(main, text="Back", command=main.quit)
   # Showing the elements.
   E.pack()
   K.pack()
   A.pack()
   B.pack()
   # If this is not here the window will not stay opened.
   main.mainloop()
