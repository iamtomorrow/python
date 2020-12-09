#Check if File exist

import os

if os.path.exists("filetest.txt"):
    os.remove("filetest.txt")
else:
    print("The file does not exist.")
