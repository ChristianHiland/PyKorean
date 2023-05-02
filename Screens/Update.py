#!/usr/bin/env python3
from customtkinter import *
from Screens import *
import urllib.request

def UpdateScreen(ThemeScr):
    # URLs
    Version = "https://github.com/ChristianHiland/PyKorean/raw/master/versions.txt"
    READMEF = "https://github.com/ChristianHiland/PyKorean/raw/master/README.md"
    Defines = "https://github.com/ChristianHiland/PyKorean/raw/master/Defines.py"
    PyKorean = "https://github.com/ChristianHiland/PyKorean/raw/master/PyKorean.py"
    SettingsS = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/SettingsS.py"
    LanguageS = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/LanguageS.py"
    Define = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Define.py"
    About = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/About.py"
    init1 = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/__init__.py"
    init2 = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Language/__init__.py"
    English = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Language/english.py"
    EnglishSen = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Language/EnglishSen.py"
    Words = "https://github.com/ChristianHiland/PyKorean/raw/master/Screens/Language/Dictionary/words.py"

    # Setting up the theme, window, and font.
    set_default_color_theme(ThemeScr)
    update = CTk()
    update.geometry("900x500")
    update.title("PyKorean - Update")
    from Defines import titleFont

    # Title
    Title = CTkLabel(update, text="Updating", font=titleFont)
    Title.pack(pady=30)
    
    WarningText = "Warning! Wait A Minute Before Closing The Window."
    WarningTexts = StringVar(update, value=UpdateNeedText)
    
    # Actions
    def UpdateRun():
        # Downloading Files
        filename, headers = urllib.request.urlretrieve(Version, filename="Versions.txt")
        filename, headers = urllib.request.urlretrieve(READMEF, filename="README.md")
        filename, headers = urllib.request.urlretrieve(Defines, filename="Defines.py")
        filename, headers = urllib.request.urlretrieve(PyKorean, filename="PyKorean.py")
        filename, headers = urllib.request.urlretrieve(SettingsS, filename="Screens/SettingsS.py")
        filename, headers = urllib.request.urlretrieve(LanguageS, filename="Screens/LanguageS.py")
        filename, headers = urllib.request.urlretrieve(Define, filename="Screens/Define.py")
        filename, headers = urllib.request.urlretrieve(About, filename="Screens/About.py")
        filename, headers = urllib.request.urlretrieve(init1, filename="Screens/__init__.py")
        filename, headers = urllib.request.urlretrieve(init2, filename="Screens/Language/__init__.py")
        filename, headers = urllib.request.urlretrieve(English, filename="Screens/Language/english.py")
        filename, headers = urllib.request.urlretrieve(EnglishSen, filename="Screens/Language/EnglishSen.py")
        filename, headers = urllib.request.urlretrieve(Words, filename="Screens/Language/Dictionary/words.py")
        WarningText = "Updated Installed You May Close The Window."
        update.update_idletasks()
   
    # Warning Label
    Warning = CTkLabel(update, textvariable=WarningTexts, font=titleFont)
    Warning.pack(pady=40)
    # Update Button
    UpdateButton = CTkButton(update, text="Update", command=UpdateRun)
    UpdateButton.pack(pady=20)
    
    update.mainloop()
