import os
from tkinter import *
from functools import partial
import shutil

windowRevertBackup = Tk()
windowRevertBackup.title("Revert to a backup")
windowRevertBackup.geometry("423x300")

directoryS = []
buttonIdentitiesS = []

#///////////////////////////////////////////////////////////////

#EDIT ME
Profiles = "C:/Users/Ricochet/AppData/Roaming/Firefox Profiles"

#EDIT ME
ProfilesBS = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBS"

#EDIT ME
ProfilesBE = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBE"

#EDIT ME
MasterProfiles = "C:/Users/Ricochet/AppData/Roaming/FirefoxProfilesMaster/Profiles.txt"

#///////////////////////////////////////////////////////////////


directoryS = os.listdir(ProfilesBS + "/")

columnLabelS = Label(windowRevertBackup, text="Starting backups")
columnLabelS.grid(column=0, row=0)

columnLabelE = Label(windowRevertBackup, text="Ending backups")
columnLabelE.grid(column=1, row=0)


def useBackupS(n):
    
    bname = (buttonIdentitiesS[n])

    try:
        shutil.rmtree(Profiles)
        os.remove(MasterProfiles)
        print("Removed old profiles..")
    except: Exception
        
    shutil.copytree(ProfilesBS + "/" + directoryS[n], Profiles + "/")
    shutil.copy2(ProfilesBS + "/" + directoryS[n] + "/Profiles.txt", MasterProfiles) 
    
    print("Reverted to " + directoryS[n] + ".")



for x in range(len(directoryS)):
    button = Button(windowRevertBackup, text=directoryS[x], command=partial(useBackupS, x))
    button.grid(column=0, row=x+1)
    buttonIdentitiesS.append(button)


directoryE = []
buttonIdentitiesE = []

directoryE = os.listdir(ProfilesBE + "/")


def useBackupE(n):
    
    bname = (buttonIdentitiesE[n])

    try:
        shutil.rmtree(Profiles)
        os.remove(MasterProfiles)
        print("Removed old profiles..")
    except: Exception
        
    shutil.copytree(ProfilesBE + "/" + directoryE[n], Profiles + "/")
    shutil.copy2(ProfilesBE + "/" + directoryE[n] + "/Profiles.txt", MasterProfiles)
    
    print("Reverted to " + directoryE[n] + ".")



for x in range(len(directoryE)):
    button = Button(windowRevertBackup, text=directoryE[x], command=partial(useBackupE, x))
    button.grid(column=1, row=x+1)
    buttonIdentitiesE.append(button)




