import os
from os import path
import  shutil
from shutil import make_archive
from zipfile import ZipFile


def CreateZipMode1():
    shutil.make_archive("CompressedFile", "zip", "C:\\Users\\ruand\\PycharmProjects\\Meus_exercicios\\ExerciciosListas")


CreateZipMode1()


def CreateZipMode2():
    with ZipFile("CompressedFile2.zip", "w") as newZip:
        newZip.write("New.txt")


CreateZipMode2()


def DeleteFile():
    os.remove("CompressedFile2.zip")


DeleteFile()

