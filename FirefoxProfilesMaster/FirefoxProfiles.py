#Firefox Profiles 1.0
from tkinter import *
import os
from os import path
import shutil
import datetime
import time
from functools import partial
import sys


#Array to identify generated buttons
buttonIdentities = []
#Array for reading Profiles.txt
profileArray = []
#Array for stripping profileArray of its linebreaks (\n)
convertedArray = []

#///////////////////////////////////////////////////////////////


#EDIT ME
Profiles = "C:/Users/Ricochet/AppData/Roaming/Firefox Profiles"

#EDIT ME
ProfilesBS = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBS"

#EDIT ME
ProfilesBE = "C:/Users/Ricochet/AppData/Roaming/Firefox ProfilesBE"

#EDIT ME
MasterProfiles = "C:/Users/Ricochet/AppData/Roaming/FirefoxProfilesMaster/Profiles.txt"

#EDIT ME
sessionBackups = "C:/Users/Ricochet/AppData/Roaming/Mozilla/Firefox/Profiles/cndxvxhm.default/sessionstore-backups"

#EDIT ME
sessionStore = "C:/Users/Ricochet/AppData/Roaming/Mozilla/Firefox/Profiles/cndxvxhm.default/sessionstore.jsonlz4"

#EDIT ME
mozillaSessionBackups = "C:/Users/Ricochet/AppData/Roaming/Mozilla/Firefox/Profiles/cndxvxhm.default"

#///////////////////////////////////////////////////////////////

#This checks to see if the session restore file exists. If it doesn't, it warns the user, because that causes problems with usage.
if path.exists("C:/Users/Ricochet/AppData/Roaming/Mozilla/Firefox/Profiles/cndxvxhm.default/sessionstore.jsonlz4") == False:

    def cont():
        noSessionWindow.destroy()
        
    noSessionWindow = Tk()
    noSessionWindow.title("No sessionstore file!")
    infoDump = Label(noSessionWindow, text="Warning! The session restore file is NOT present. This means that either Firefox is NOT fully closed,\n or that the session restore file is still generating. This can be a \n result of a ton of tabs or windows. If Firefox is closed, \n please wait at least another 5-10 seconds. \n By continuing, you acknowledge that functions like adding new profiles, \n switching profiles, updating profiles, and reverting to backups WILL NOT WORK. \n Close this and then the program to retry")
    
    infoDump.grid(column=0, row=0)

    continueButton = Button(noSessionWindow, text="Ok/Continue", command=cont)
    continueButton.grid(column=0, row=1)
                     
    noSessionWindow.mainloop()


#This first gets the current time, so we can put two different items in the same file, and then uses that to generate a file and store the session restore file and backups in it.
#Then it calls the function so we backup once at the start of the program.
def backupS():
    currentTimeS = datetime.datetime.now().strftime("%m-%d-%y %H. %M. %S")
    shutil.copytree(Profiles, ProfilesBS + "/Profile Backup Start " + currentTimeS)
    shutil.copy2(MasterProfiles, ProfilesBS + "/Profile Backup Start " + currentTimeS)

backupS()

#This is the main window here
mainWindow = Tk()
mainWindow.title("Firefox Profiles")
mainWindow.geometry("400x400")


profileList = Label(mainWindow, text="Profile List")
profileList.grid(column=0, row=0)


#I'm importing other .py files as functions for two reasons: 1. the Tkinter command= option seems to work best with functions and 2. I tried to import them
#normally but it just ran them immediately, resulting in 3 guis popping up. Unfortunately this means that you can only open the backupGui or remove backup menus once per startup. 
def importRmBackup():
    import rmBackup
    

def importBackupGui():
    import backupGui



#This is the code that runs when you press the update a profile button on the main window  
def updateProfile():
    #Runs code to remove and copy files to destinations, as well as additionial functions for closing popup windows
    def update(n):
        def updateAck():
            windowUpdateSuccess.destroy()
            
        def updateAck2():
            windowUpdateSuccess.destroy()
            windowUpdateProfile.destroy()
        
        shutil.rmtree(Profiles + "/" + convertedArray[n])
        
        shutil.copytree(sessionBackups, Profiles + "/" + convertedArray[n] + "/backups")
        shutil.copy2(sessionStore, Profiles + "/" + convertedArray[n])

        print("Updated profile " + convertedArray[n])

        #Generates an exit window, functions are above
        windowUpdateSuccess = Tk()
        windowUpdateSuccess.title("Success")
        
        updateSuccess = Label(windowUpdateSuccess, text="Success! Profile " + convertedArray[n] + " updated.")
        updateSuccess.grid(column=0, row=0)

        updateAckButton = Button(windowUpdateSuccess, text="Ok", command=updateAck)
        updateAckButton.grid(column=0, row=1)

        updateAckButton2 = Button(windowUpdateSuccess, text="Ok, done updating", command=updateAck2)
        updateAckButton2.grid(column=0, row=2)

    windowUpdateProfile = Tk()
    windowUpdateProfile.title("Update profile")

    selectProfile = Label(windowUpdateProfile, text="Select a profile to update")
    selectProfile.grid(column=0, row=0)

    #This code generates buttons based on what you have in your profileArray, which is updated based on the Profiles.txt file.
    for y in range(len(profileArray)):
        button = Button(windowUpdateProfile, text=profileArray[y], command=partial(update, y))
        button.grid(column=0, row=y+1)
        buttonIdentities.append(button)
        

#Code that runs when you press the delete a profile button
def delButton():
    def confirmDel():
        
        def restartProfiles():
            windowResetRequired.destroy()
            windowDeleteProfile.destroy()
            mainWindow.destroy()
            
        def killWinResetRequired():
            windowResetRequired.destroy()
            
        #Error catching for if the user does not input anything. This results in the loss of profiles if not prevented.
        if profName.get() == "":
            windowErrWarning = Tk()
            windowErrWarning.title("WARNING")
            warning = Label(windowErrWarning, text="When deleting a profile, the name cannot be empty. \n This will result in the loss of all of your profiles. \n Close this window to try again")
            warning.pack()
            return


        #Reading the Profiles.txt file, then writing it back without the profile name we typed in. 
        with open(MasterProfiles, "r") as f:
            lines = f.readlines()
        with open(MasterProfiles, "w") as f:
            for line in lines:
                if line.strip("\n") != profName.get():
                    f.write(line)
                    try:
                        shutil.rmtree(Profiles + "/" + profName.get())
                    except: Exception

        #Generates an exit window, functions are above
        windowResetRequired = Tk()
        windowResetRequired.title("Restart Required")
        restartWinResetRequired = Label(windowResetRequired, text="Restart required for changes to visually take effect")
        restartWinResetRequired.grid(column=0, row=0)
        restartProfilesButton = Button(windowResetRequired, text="Ok", command=restartProfiles)
        restartProfilesButton.grid(column=0, row=1)
        notNowWin = Button(windowResetRequired, text="Not now", command=killWinResetRequired)
        notNowWin.grid(column=0, row=2)
                 
    
    windowDeleteProfile = Tk()
    windowDeleteProfile.title("Delete a profile")
    
    delName = Label(windowDeleteProfile, text="Name of profile to delete")
    delName.grid(column=0, row=0)

    profName = Entry(windowDeleteProfile)
    profName.grid(column=0, row=1)

    deleteProf = Button(windowDeleteProfile, text="Confirm", command=confirmDel)
    deleteProf.grid(column=0, row=2)
    

#Code that runs when you press add a new profile
def makeButton():
    def confirmNew():
        def restartProfiles():
            windowRestartRequired.destroy()
            mainWindow.destroy()
        def noWayButton():
            windowRestartRequired.destroy()

        #This opens the Profiles.txt as a file to append to, sets itself to a new line, and writes the profile name we entered on the line marked below with #PROFILE ENTRY
        f = open (MasterProfiles, "a")
        f.write("\n")
        f.write(newButton.get())
        f.close()

        #Making folders based on the new profile and copying data
        os.mkdir(Profiles + "/" + newButton.get())
        shutil.copytree(sessionBackups, Profiles + "/" + newButton.get() + "/backups")
        shutil.copy2(sessionStore, Profiles + "/" + newButton.get())


        windowNewButton.destroy()
        windowRestartRequired = Tk()
        windowRestartRequired.title("Restart required")
        restart = Label(windowRestartRequired, text="Restart required for new profiles to appear")
        restart.pack()
        restartButton = Button(windowRestartRequired, text="Ok", command=restartProfiles)
        restartButton.pack()
        noWayButton = Button(windowRestartRequired, text="Not now", command=noWayButton)
        noWayButton.pack()
        
    windowNewButton = Tk()
    windowNewButton.title("New button")
    direction = Label(windowNewButton, text="New profile name")
    direction.pack()

    #PROFILE ENTRY - Detects/stores user input
    newButton = Entry(windowNewButton)
    newButton.pack()
    
    confirm = Button(windowNewButton, text="Confirm", command=confirmNew)
    confirm.pack()
    
    windowNewButton.mainloop()

#This code chunk reads the Profiles.txt file and appends it to the profileArray array.
f= open(MasterProfiles, "r")
for line in f:
    profileArray.append(line)
f.close()

#This code chunk takes the profileArray and strips the linebreaks \n out of it, because this makes getting folder locations and such impossible.
for element in profileArray:
    convertedArray.append(element.strip())
    

#This runs when you press any of the profiles that generate on the left hand side. Pretty straightforward, removes the items currently stored in Mozilla
#and then puts the items from the profile you clicked on into the Mozilla folder.
def switchProfiles(n):
    
    try:
        shutil.rmtree(sessionBackups)
        os.remove(sessionStore)
    except Exception:
        pass
    shutil.copytree(Profiles + "/" + convertedArray[n] + "/backups", sessionBackups)
    shutil.copy2(Profiles + "/" + convertedArray[n] + "/sessionstore.jsonlz4", mozillaSessionBackups)
    print("Switched profiles to " + convertedArray[n])

#Generates the buttons on the left hand side.
for y in range(len(profileArray)):
    button = Button(mainWindow, text=profileArray[y], command=partial(switchProfiles, y))
    button.grid(column=0, row=y+1)
    buttonIdentities.append(button)


#Buttons that activate the corresponding function.
addProfile = Button(mainWindow, text="Add new profile", command=makeButton)
addProfile.grid(column=2, row=0)

delProf = Button(mainWindow, text="Delete a profile", command=delButton)
delProf.grid(column=3, row=0)

updateProf = Button(mainWindow, text="Update a profile", command=updateProfile)
updateProf.grid(column=2, row=1)

revertBackup = Button(mainWindow, text="Revert to backup", command=importBackupGui)
revertBackup.grid(column=3, row=1)

rmBackup = Button(mainWindow, text="Remove a backup", command=importRmBackup)
rmBackup.grid(column=3, row=2)


mainWindow.mainloop()

#Identical to the backup at the start, but goes into a different folder and is done at the end of the program.
def backupE():
    currentTimeE = datetime.datetime.now().strftime("%m-%d-%y %H. %M. %S")
    shutil.copytree(Profiles, ProfilesBE + "/Profile Backup End " + currentTimeE)
    shutil.copy2(MasterProfiles, ProfilesBE + "/Profile Backup End " + currentTimeE)
backupE()


