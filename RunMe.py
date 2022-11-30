# This is were I import the modules.
import tkinter as tk
import time
from tkinter.ttk import Progressbar
import files
import urllib.request

# Setting up the loading window.
start= tk.Tk()
start.geometry("400x200")
start.title("Update Window")

# URLs for the files
home = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/files/homeh.py"
english = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/files/words/english.py"
readme1 = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/README.md"
readme2 = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/files/words/README.md"
linux = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/main/Linuxfirst.sh"

# Actions
def startbar():
    lang = 100
    x = 0
    # This gets some of the files form GitHub and updates the other files. 
    filename, headers = urllib.request.urlretrieve(home, filename="files/homeh.py")
    filename, headers = urllib.request.urlretrieve(english, filename="files/words/english.py")
    filename, headers = urllib.request.urlretrieve(readme1, filename="README.md")
    filename, headers = urllib.request.urlretrieve(readme2, filename="files/words/README.md")
    filename, headers = urllib.request.urlretrieve(linux, filename="Linuxfirst.sh")
    
    while(x <lang):
        # This moves the progressbar.
        time.sleep(0.1)
        bar["value"]+=1
        x+=1
        taskdone.set(str(int((x/lang)*100))+"%")
        text.set(str(x)+"/"+str(lang)+" loaded words")

        # This updates the screen to show the screen.
        start.update_idletasks()
        
        # If true then start the window.
        if (x==lang):
            start.destroy()
            files.homeh.home()
taskdone = tk.StringVar()
text = tk.StringVar()

# Progressbar
bar = Progressbar(start, orient=tk.HORIZONTAL, length=300)

# Labels
percentlabel = tk.Label(start, textvariable=taskdone)
tasklabel = tk.Label(start, textvariable=text)

# Buttons
startbu= tk.Button(start, text="Click here to start", command=startbar)

# Showing the elements
bar.pack(pady=20)
percentlabel.pack()
tasklabel.pack()
startbu.pack(pady=40)
    
# Main.loop
start.mainloop()
