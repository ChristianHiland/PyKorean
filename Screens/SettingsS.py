#!/usr/bin/env python3
from customtkinter import *
from Screens.Update import UpdateScreen
import urllib.request

def SettingScreen(ThemeScr, VersionNumbers):
    
    # Setting up the theme, window, and font.
    set_default_color_theme(ThemeScr)
    settings = CTk()
    settings.geometry("900x500")
    settings.title("PyKorean - Settings")
    from Defines import titleFont

    # Checking the Version to see if there is a update.
    versionCheck = "https://raw.githubusercontent.com/ChristianHiland/PyKorean/master/versions.txt"
    filename, headers = urllib.request.urlretrieve(versionCheck, filename="Check/VersionCheck.txt")
    with open("Check/VersionCheck.txt", "r") as VersionCheck:
        VersionNew = VersionCheck.read()
        with open("versions.txt", "r") as Version:
            VersionOld = Version.read()
            if VersionCheck.read() != Version.read():
                UpdateNeed = "Need Update"
            else:
                UpdateNeed = "No Update"
    
    # Title
    label = CTkLabel(settings, text="Settings", font=titleFont)
    label.pack(pady=30)

    # Actions
    def themeSelect(choice):
        Theme = str("Screens/Themes/" + choice + ".json")
        ThemeScreenP = str("Themes/" + choice + ".json")
        set_default_color_theme(Theme)
        with open("Theme.txt", "w") as File:
            File.write(Theme)
        with open("ThemeScreen.txt", "w") as ThemeScreenF:
            ThemeScreenF.write(ThemeScreenP)
    def Update():
        UpdateScreen(ThemeScr)

    # Elements

    # Tabs
    tabview = CTkTabview(settings, width=900, height=400)
    tabview.pack(padx=20, pady=20)
    tabview.add("Theme")  # add tab at the end
    tabview.add("Update")  # add tab at the end
    
    # Theme
    ThemeLabel = CTkLabel(master=tabview.tab("Theme"), text="Sorry. but the Theme selection area has not yet been Made.", font=titleFont)

    # Checks what to show on the label.
    UpdateNeedText = str("There is an Update!\n" + "Current Version: " + VersionOld + "New Version: " + VersionNew)
    if UpdateNeed == "Need Update":
        VersionUpdate = StringVar(tabview.tab("Update"), value=UpdateNeedText)
    else:
        VersionUpdate = StringVar(tabview.tab("Update"), value="There is no need for an update.")
    # Update Elements
    UpdateLabel = CTkLabel(master=tabview.tab("Update"), textvariable=VersionUpdate, font=titleFont)
    UpdateButton = CTkButton(master=tabview.tab("Update"), text="Update", command=Update)
    # Placing the Elements down.
    ThemeLabel.pack(padx=20, pady=20)
    UpdateLabel.pack(padx=20, pady=20)
    UpdateButton.pack(padx=20, pady=30)
    
    # Keeping the Window Open.
    settings.mainloop()
