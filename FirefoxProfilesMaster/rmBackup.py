import os
import shutil
from functools import partial
from tkinter import *

windowRmBackup = Tk()
windowRmBackup.title("Remove a backup")
windowRmBackup.geometry("423x300")

rmDirectoryS = []
rmButtonIdentitiesS = []
rmDirectoryE = []
rmButtonIdentitiesE = []

#///////////////////////////////////////////////////////////////

#EDIT ME
ProfilesBS = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBS"

#EDIT ME
ProfilesBE = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBE"

#///////////////////////////////////////////////////////////////

rmDirectoryS = os.listdir(ProfilesBS + "/")
rmDirectoryE = os.listdir(ProfilesBE + "/")

columnLabelS = Label(windowRmBackup, text="Starting backups")
columnLabelS.grid(column=0, row=0)

columnLabelE = Label(windowRmBackup, text="Ending backups")
columnLabelE.grid(column=1, row=0)


def rmBackupS(n):
    
    bname = (rmButtonIdentitiesS[n])

    try:
        shutil.rmtree(ProfilesBS + "/" + rmDirectoryS[n])
        print(rmDirectoryS[n] + " removed.")
    except: Exception


for x in range(len(rmDirectoryS)):
    button = Button(windowRmBackup, text=rmDirectoryS[x], command=partial(rmBackupS, x))
    button.grid(column=0, row=x+1)
    rmButtonIdentitiesS.append(button)











def rmBackupE(n):
    
    bname = (rmButtonIdentitiesE[n])

    try:    
        shutil.rmtree(ProfilesBE + "/" + rmDirectoryE[n])
        print(rmDirectoryE[n] + " removed.")
    except: Exception


for x in range(len(rmDirectoryE)):
    button = Button(windowRmBackup, text=rmDirectoryE[x], command=partial(rmBackupE, x))
    button.grid(column=1, row=x+1)
    rmButtonIdentitiesE.append(button)


