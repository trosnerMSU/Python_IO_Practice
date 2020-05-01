import sys

## Author: Tanner Rosner

def SplitWord(word):
    return [char for char in word]

letters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0,
           "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
           "Y": 0, "Z": 0}

file = "1030 Project 04 02 Sentences.txt"
outputFile = open("TannerRosner03_04_02Output.txt", "w")


with open(file) as inp:
    lines = inp.readlines()

for line in lines:
    outputFile.write(line)


for line in lines:
    words = SplitWord(line)
    if words and line.strip():
        for char in words:
            char = char.upper()
            if char.isalpha() and char in letters:
                letters[char] += 1


## Output
outputFile.write("\n\n")
outputFile.write("{:>6}  {:>6}".format("Letter", "Frequency") + "\n")
for element in letters:
    outputFile.write("{:>6}  {:>6}".format(element, letters[element]) + "\n")


outputFile.close()
inp.close()







