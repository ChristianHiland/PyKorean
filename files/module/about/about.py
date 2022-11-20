from tkinter import tk

# Making the window & settings
about= tk.Tk()
about.geometry("400x400")
about.title("About")
# Actions

# Labels
A = tk.Label(about, text="This is a Korean dictionary that I made called, PyKorean. It's coded in Python").pack
# Button
B = tk.Button(about, text="Back", command=about.destroy)
# Showing the elements
A.pack()
B.pack()
about.mainloop()
