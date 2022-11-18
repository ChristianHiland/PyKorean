# Importing the modules
import module
import tkinter as tk
# Making the window name
main = tk.Tk()
# setting the windows size
main.geometry("400x400")
main.title("Main Window")
# Actions
def english():
   module.english.korean()
def korean():
    module.korean.english()
def about():
   module.about.about()
def quit():
   main.destroy
# The buttons
E = tk.Button(main, text ="English", command = english)
K = tk.Button(main, text = "Korean", command = korean)
A = tk.Button(main, text ="About", command = about)
Q = tk.Button(main, text ="Quit", command = quit)
# Showing the elements.
E.pack()
K.pack()
A.pack()
Q.pack()
# If this is not here the window will not stay opened.
main.mainloop()
