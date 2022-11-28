# Importing the modules
import files
from tkinter import *
import tkinter as tk

def grammar():
    # Making the window name
    part = tk.Tk()

    # setting the windows size
    part.geometry("600x600")
    part.title("Particles Window")

    # Actions

    # The buttons
    B = tk.Button(part, text="Back", command=part.quit)

    # Showing the elements.
    B.pack()

    # If this is not here the window will not stay opened.
    part.mainloop()