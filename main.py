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
def quit():
   main.destroy
# The buttons
E = Tkinter.Button(main, text ="English", command = english)
K = Tkinter.Button(main, text = "Korean", command = korean)
A = Tkinter.Button(main, text ="About", command = about)
Q = Tkinter.Button(main, text ="Quit", command = quit)
# Showing the elements.
E.pack()
K.pack()
A.pack()
Q.pack()
# If this is not here the window will not stay opened.
main.mainloop()
