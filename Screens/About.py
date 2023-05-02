#!/usr/bin/env python3
from customtkinter import *

def AboutScreen():
    # Setting up the theme, window, and fonts.
    set_appearance_mode("dark")
    aboutScreen = CTk()
    aboutScreen.geometry("900x500")
    aboutScreen.title("PyKorean - About")
    from Screens.Define import TitleFont
    from Screens.Define import NamesFont

    # Title
    title = CTkLabel(aboutScreen, text="About", font=TitleFont)
    title.pack(pady=30)
    # Create a frames
    frame = CTkFrame(master=aboutScreen)
    frame.pack(pady=10,padx=30, fill='both', expand=True)
    # Maker & Developer
    makerFrame = CTkFrame(master=frame)
    makerFrame.pack(pady=10, padx=30, fill='both', expand=True)
    # Design/Colour
    designFrame = CTkFrame(master=frame)
    designFrame.pack(pady=5, padx=30, fill='both', expand=True)
    
    # Elements

    # Maker
    makerTitle = CTkLabel(makerFrame, text="Maker/Developer/Language:", font=NamesFont)
    makerTitle.pack(pady=5)
    maker = CTkLabel(makerFrame, text="Christian Hiland", font=NamesFont)
    maker.pack(pady=5)

    # Design
    makerTitle = CTkLabel(designFrame, text="Design/Colour:", font=NamesFont)
    makerTitle.pack(pady=5)
    maker = CTkLabel(designFrame, text="None", font=NamesFont)
    maker.pack(pady=5)
    
    aboutScreen.mainloop()