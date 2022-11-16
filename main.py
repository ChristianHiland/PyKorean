#importing the modules
import module
from tkinter import tk

#Making the window name
main = Tk()

# setting the windows size
main.geometry("600x400")
main.title("Main Window")

#defining the actions for the buttons.
def english():
   module.english.koreantk()
    
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
