#!/usr/bin/env python3
from customtkinter import *
import tkinter as tk
from Screens.Language.Dictionary.words import wordsEnglishSen

def EnglishScreenS():
    # Setting up the theme.
    set_appearance_mode("dark")
    # Setting up the window.
    englishScreenS = CTk()
    englishScreenS.geometry("900x500")
    englishScreenS.title("PyKorean - Language English & Korean (Sentence Mode)")
    from Screens.Define import TitleFont, OutFont

    # Actions

    # Runs when the enter button has been clicked
    def TypeLang(typeMenu: str):
        if typeMenu == str("Word"):
            TypeDir = "Word"
        elif typeMenu == str("Sentence"):
            TypeDir = "Sentence"
        else:
            print(typeMenu)
    def Enter():
        text = entry.get()
        LowText = str(text.lower())
        LowTextSplit = LowText.split()
        OutLang = []
        for i in LowTextSplit:
            theword = wordsEnglishSen[str(i)]
            OutLang.append(theword)
        OutLang = ' '.join(OutLang)
        newText = str(OutLang.replace("'", " "))
        output.set(str(newText))
        englishScreenS.update_idletasks()
        
    # Title
    title = CTkLabel(englishScreenS, text="English & Korean (Sentence Mode)", font=TitleFont)
    title.pack(pady=30)
    # Create a frame
    frame = CTkFrame(master=englishScreenS)
    frame.pack(pady=10,padx=30, fill='both', expand=True)

    # Entry
    entry = CTkEntry(master=frame, placeholder_text="Hello", width=185, height=30)
    entry.pack(padx=20, pady=30)
    # Output
    output = tk.StringVar(frame)
    out = CTkLabel(master=frame, textvariable=output, font=OutFont)
    out.pack()
    # Button
    enter = CTkButton(master=frame, text="Enter", command=Enter)
    enter.pack(padx=10, pady=90)
    englishScreenS.bind("<Return>", (lambda event: Enter()))
    englishScreenS.mainloop()