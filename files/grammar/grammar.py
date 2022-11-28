# Importing the modules
import files
from tkinter import *
import tkinter as tk
import particles

def grammarh():
    # Making the window name
    gram = tk.Tk()

    # setting the windows size
    gram.geometry("400x200")
    gram.title("Home Window")

    # Actions
    def part():
        particles()

    # The buttons
    E = tk.Button(gram, text ="Particles", command = part)
    B = tk.Button(gram, text="Back", command=gram.quit)

    # Showing the elements.
    E.place(x=100, y=50)
    B.place(x=200, y=50)

    # If this is not here the window will not stay opened.
    gram.mainloop()
