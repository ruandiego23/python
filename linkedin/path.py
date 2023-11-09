from os import path
import time


def file_data():
    file_there = path.exists("New.txt")  # File exists?
    its_directory = path.isdir("New.txt")  # Is it a directory?
    path_file = path.realpath("New.txt")  # What is the path
    path_relative = path.relpath("New.txt")  # What is the relative path
    created = time.ctime(path.getctime("New.txt"))  # What's the create time?
    modify = time.ctime(path.getmtime("New.txt"))

    print(file_there)
    print(its_directory)
    print(path_file)
    print(path_relative)
    print(created)
    print(modify)


file_data()
