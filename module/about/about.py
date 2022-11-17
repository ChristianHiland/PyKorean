from tkinter import tk

# Making the window & settings
about= tk.Tk()
about.geometry("600x400")
about.title("About")
# Actions

# Labels
A = Label(about, text="This is a Korean dictionary that I made called, PyKorean. It's coded in Python").pack
# Button
B = Button(root, text="Back", command=about.destroy)
# Showing the elements
A.pack()
B.pack()
about.mainloop()
