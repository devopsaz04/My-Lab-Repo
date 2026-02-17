import os


if os.path.exists("myfile.txt"):
    print("File exists.")
    os.remove("myfile.txt")
else:
    print("File does not exist.")
