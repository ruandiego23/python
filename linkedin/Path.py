from os import path
import time


def FileData():
    filethere = path.exists("New.txt")  # File exists?
    itsdirectory = path.isdir("New.txt")  # Is it a directory?
    pathFile = path.realpath("New.txt")  # What is the path
    pathRelative = path.relpath("New.txt")  # What is the relative path
    Created = time.ctime(path.getctime("New.txt"))  # What's the create time?
    Modify = time.ctime(path.getmtime("New.txt"))

    print(filethere)
    print(itsdirectory)
    print(pathFile)
    print(pathRelative)
    print(Created)
    print(Modify)


FileData()
