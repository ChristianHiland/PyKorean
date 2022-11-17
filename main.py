# Importing the modules
import module
from tkinter import tk
# Making the window name
main = Tk()
# setting the windows size
main.geometry("600x400")
main.title("Main Window")
# Actions
def english():
   module.english.koreantk()
def korean():
    module.korean.english()
def about():
   module.about.about()
# The buttons
E = Tkinter.Button(main, text ="English", command = english)
K = Tkinter.Button(main, text = "Korean", command = korean)
A = Tkinter.Button(main, text ="About", command = about)
# Showing the elements.
E.pack()
K.pack()
A.pack()
# If this is not here the window will not stay opened.
main.mainloop()
