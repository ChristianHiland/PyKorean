#!/usr/bin/env python3
from customtkinter import *
import tkinter as tk
from Screens.Language.Dictionary.words import wordsEnglish
from Screens.Language.EnglishSen import EnglishScreenS
import json

def EnglishScreen():
    # Setting up the theme.
    set_appearance_mode("dark")
    # Setting up the window.
    englishScreen = CTk()
    englishScreen.geometry("900x500")
    englishScreen.title("PyKorean - Language English & Korean")
    from Screens.Define import TitleFont, OutFont
    Dicionary = "Screens/Language/Dicionary/Words.json"

    # Actions
    def Enter():
        # Printing the Korean word from the Dicionary.
        text = entry.get()
        with open(Dicionary, "r") as Words:
            Data = json.load(Words)
            LowText = str(text.lower())
            theword = Data['English'][str(LowText)]
            output.set(str(newText))
            englishScreen.update_idletasks()
    def sentenceMode():
        EnglishScreenS()
    
    # Title
    title = CTkLabel(englishScreen, text="English & Korean", font=TitleFont)
    title.pack(pady=30)
    # Create a frame
    frame = CTkFrame(master=englishScreen)
    frame.pack(pady=10,padx=30, fill='both', expand=True)

    # Choice Menu
    sentenceButton = CTkButton(englishScreen, text="Try the Sentence mode", command=sentenceMode)
    sentenceButton.pack(padx=20, pady=(10, 10))
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
    englishScreen.bind("<Return>", (lambda event: Enter()))
    englishScreen.mainloop()