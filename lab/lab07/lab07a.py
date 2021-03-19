# *******************************************************************
# lab07a.py
#
# Recursively translates words into digits
# *******************************************************************

def main():
    words = input("Please give a sequence of words: ")
    listOfWords = words.split()
    showDigits(listOfWords)

# Recursive function for translating a list of numeric words
# Into a sequence of digits (including a point) and print them
def showDigits(listOfWords):
    if len(listOfWords) == 1: # Base case
        printDigit(listOfWords[0])
    else: # Recursive case
        printDigit(listOfWords[0])
        showDigits(listOfWords[1:])

# Function for translating one word and printing the digit or point
def printDigit(word):
# Use a dictionary
    kamusKata = {'nol': '0', 'satu': '1', 'dua': '2', 'tiga': '3', 'empat': '4', 'lima': '5', 'enam': '6', 'tujuh': '7', 'delapan': '8', 'sembilan': '9', 'titik': '.'}
    print(kamusKata[word], end= '')

if __name__ == '__main__':
    main()
