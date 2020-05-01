import sys

## Author: Tanner Rosner

numFiles = 3
count = 0
filesList = []

# Import the text file names
files = "1030 Project 04 03 Files.txt"
with open(files) as inp:
    lines = inp.readlines()
for line in lines:
    filesList.append(line.strip() + '.txt')

# initiate output file
outputFile = open("TannerRosner03_04_03Output.txt", "w")

while count != (numFiles - 1):
    file = filesList[count]
    with open(file) as inp:
        lines = inp.readlines()
    for line in lines:
        outputFile.write(line)
    count += 1
