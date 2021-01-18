import os
import pwd

class Helper:
    def ls(path):
        for entry in os.listdir(path):
            print(pwd.getpwuid(os.stat(path).st_uid).pw_name, "||", f'{entry}', "||", os.path.getsize(path))

class ls:
    help = Helper()
    path = str(input("insert path"))
    Helper.ls(path)

