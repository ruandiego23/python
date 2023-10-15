import os
from os import path
import shutil


def copyfile():
    if path.exists("New.txt"):
        path_current = path.realpath("New.txt")
        new_path = path_current + ".bkp"
        shutil.copy(path_current, new_path)
        shutil.copystat(path_current, new_path)


copyfile()


def renamefile():
    if path.exists("New.txt.bkp"):
        os.rename("New.txt.bkp", "ChangedFile.txt")


renamefile()
