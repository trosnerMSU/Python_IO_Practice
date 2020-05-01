import sys

## Author: Tanner Rosner

#Create splitword method to make things a bit easier
def SplitWord(word):
    return [char for char in word]

letters = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5,
           "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
           "Y": 4, "Z": 10}
entries = []
points = []
total = 0

fileName = "1030 Project 04 01 Words.txt"

## Input file and processing
with open(fileName) as inp:
    lines = inp.readlines()

for words in lines:
    word = SplitWord(words)
    score = 0
    if words and words.strip():     #This checks for any blank lines that have been read
        for char in word:
            char = char.upper()
            if char.isalpha() and char in letters:
                score += letters.get(char)
        total += score
        points.append(score)
        entries.append(words)


## Output
print('{:>12}  {:>12}'.format("Words", "Points"))
i = 0
while i < len(entries):
    line = '{:>12}  {:>12}'.format(entries[i], points[i])
    print(line)
    i += 1
print('{:>12}  {:>12}'.format("Total", total))









