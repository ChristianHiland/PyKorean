#!/usr/bin/env python3
# Importing the modules.
from customtkinter import *
import tkinter as tk
from Screens import *
import urllib.request
from PIL import Image, ImageTk


## Pre-setup

# Updating The Update File, in case there is any new files made that was here before.
Update = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Update.py"
filename, headers = urllib.request.urlretrieve(Update, filename="Screens/Update.py")
# Checking for config files, and with varables.
Themes = open("Screens/Theme.txt", "r")
Theme = Themes.read()
Versions = open("versions.txt", "r")
VersionNumbers = Versions.read()


## App Window

# Setting up the theme, and Window and font, and icon.
set_default_color_theme(Theme)
main = CTk()
main.geometry("900x500")
main.title("PyKorean")
from Defines import titleFont
main.iconphoto(False, tk.PhotoImage(file='Images/Icons/PyKorean.png'))

# Version Number
VersionNumber = StringVar(main, value=VersionNumbers)

# Actions
def Language():
    LanguageScreen()
def About():
    AboutScreen()
def Settings():
    SettingScreen(Theme, VersionNumbers)

# Title
PyKoreanLogo = CTkImage(dark_image=Image.open("Images/Icons/PyKorean.png"), size=(90, 90))
Logo = CTkLabel(main, image=PyKoreanLogo, text="")
Logo.pack(pady=15)
title = CTkLabel(main, text="PyKorean", font=titleFont)
title.pack(pady=20)

# Create a frame
frame = CTkFrame(master=main)
frame.pack(pady=15, padx=30, fill='both', expand=True)

# Elements
lang = CTkButton(master=frame, text="Languages", command=Language)
settings = CTkButton(master=frame, text="Settings", command=Settings)
about = CTkButton(master=frame, text="About", command=About)
version = CTkLabel(master=main, textvariable=VersionNumber)

# Placing Elements Down
lang.pack(padx=9, pady=20)
about.pack(padx=10, pady=50)
settings.pack(padx=10, pady=10)
version.pack(anchor=tk.SE)

# Keeping the window open.
main.mainloop()
