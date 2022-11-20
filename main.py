#importing the modules and tkinter
from tkinter.ttk import Progressbar
from tkinter import *
import tkinter as tk
import time
import files

# Setting up the window
start= tk.Tk()
start.geometry("400x200")
start.title("Download Window")

# Actions
def startbar():
    lang = 100
    x = 0
    while(x <lang):
        time.sleep(0.01)
        bar["value"]+=1
        x+=1
        taskdone.set(str(int((x/lang)*100))+"%")
        text.set(str(x)+"/"+str(lang)+" loaded")
        start.update_idletasks()
        if (x==lang):
            files.homeh.home()
taskdone = StringVar()
text = StringVar()

# Progressbar
bar = Progressbar(start, orient=HORIZONTAL, length=300)

# Labels
percentlabel = Label(start, textvariable=taskdone)
tasklabel = Label(start, textvariable=text)

# Buttons
startbu=Button(start, text="Click here to start", command=startbar)

# Showing the elements
bar.pack(pady=20)
percentlabel.pack()
tasklabel.pack()
startbu.pack(pady=40)
    
# Main.loop
start.mainloop()
