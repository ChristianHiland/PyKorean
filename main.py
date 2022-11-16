import module
from tkinter import tk

main = Tk()

#defining the actions for the buttons.
def english():
   module.english.korean()
def korean():
    module.korean.english()

#The buttons
E = Tkinter.Button(top, text ="English", command = english)
K = Tkinter.Button(top, text = "Korean", command = korean)

#Showing the elements.
E.pack()
K.pack()

#If this is not here the window will not stay opened.
main.mainloop()

type = input("What langage are you from? ")
