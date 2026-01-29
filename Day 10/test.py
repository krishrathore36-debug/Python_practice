import os

folders = input ("Please Provide List of folders nameswith spaces in between:").split()

for folder in folders:
    files = os.listdir(folder)
    print("===  listing files for the folder -" + folder)
    for file in files:
        print(file)

  