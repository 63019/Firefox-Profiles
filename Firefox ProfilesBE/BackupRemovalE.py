import datetime
import time
import shutil
import os

startTime = time.time()
rootDir = os.getcwd()

for directories in os.listdir(os.getcwd()): 

    if not os.path.isdir(directories) or not os.stat(directories).st_ctime < time.time()-(172800): 
        continue
    os.chdir(directories)
    os.chdir(rootDir)
    shutil.rmtree(directories)
