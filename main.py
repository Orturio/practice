#!/usr/bin/env python3
import os
import pwd
import sys

class Helper:
    def ls(path):
        if os.path.exists(path):
            currentPath = path
            for sequanceNumber, folder in enumerate(os.listdir(path)):
                currentFolderPath = currentPath + folder
                sizeOfFolder = os.path.getsize(currentFolderPath)
                authorOfFolder = pwd.getpwuid(os.stat(currentFolderPath).st_uid).pw_name
                print(sequanceNumber, '||', authorOfFolder, "||", folder, "||", sizeOfFolder)
        else:
            print('directory not found')

class ls:
    help = Helper()
    path = str(sys.argv[1])
    Helper.ls(path)
