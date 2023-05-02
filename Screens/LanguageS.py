#!/usr/bin/env python3
from customtkinter import *
from Screens.Language.english import EnglishScreen

def LanguageScreen():
    # Setting up the theme, window, and font.
    set_appearance_mode("dark")
    languageScreen = CTk()
    languageScreen.geometry("900x500")
    languageScreen.title("PyKorean - Languages")
    from Screens.Define import TitleFont

    # Actions
    def English():
        EnglishScreen()

    # Title
    title = CTkLabel(languageScreen, text="Languages", font=TitleFont)
    title.pack(pady=30)

    # Create a frame
    frame = CTkFrame(master=languageScreen)
    frame.pack(pady=10,padx=30, fill='both', expand=True)

    # Elements
    english = CTkButton(master=frame, text="English", command=English)
    # Placing the elements down.
    english.pack(padx=10, pady=40)

    # Keeping the Window Open.
    languageScreen.mainloop()
