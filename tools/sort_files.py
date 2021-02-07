import os
import shutil

def sorf_files(directory):
    os.chdir(directory)
    if not os.path.isdir("systeminfo"):
        os.mkdir("systeminfo")
    if not os.path.isdir("logicaldisk"):
        os.mkdir("logicaldisk")
    if not os.path.isdir("product"):
        os.mkdir("product")
    for file in os.listdir():
        if "systeminfo.csv" in file:
            shutil.move(file, "systeminfo")
        elif "logicaldisk.csv" in file:
            shutil.move(file, "logicaldisk")
        elif "product.csv" in file:
            shutil.move(file, "product")


