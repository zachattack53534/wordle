alphabetFrequency = {"e" : 12.02, 
                     "t" : 9.10, 
                     "a" : 8.12, 
                     "o" : 7.68, 
                     "i" : 7.31, 
                     "n" : 6.95, 
                     "s" : 6.28, 
                     "r" : 6.02, 
                     "h" : 5.92, 
                     "d" : 4.32, 
                     "l" : 3.98,
                     "u" : 2.88,
                     "c" : 2.71,
                     "m" : 2.61,
                     "f" : 2.30,
                     "y" : 2.11,
                     "w" : 2.09,
                     "g" : 2.03,
                     "p" : 1.82,
                     "b" : 1.49,
                     "v" : 1.11,
                     "k" : 0.69,
                     "x" : 0.17,
                     "q" : 0.11,
                     "j" : 0.10,
                     "z" : 0.07}
alphabet = "abcdefghijklmnopqrstuvwxyz"
textFile = open("dict.txt", "r")
textFile1 = open("wrongWords.txt", "r")
dictionary = []
wrongLetters = ""
okLetters = ""
okLettersPlace = ["", "", "", "", ""]
correctLetters = ["", "", "", "", ""]
found = False
go = 1
startLetters = ""
wrongWords = []

while True:
    word = textFile.readline()
    if not word: break
    else: dictionary.append(word[0:5])

while True:
    word = textFile1.readline()
    if not word: break
    else: wrongWords.append(word[0:5])

textFile1.close()

while not found and go <= 6:
    valid = True
    word = ""
    value = 0    
    for i in range(len(dictionary)):
        number = 0
        wrong = False
        item = dictionary[i]
        item = item.lower()
        if item in wrongWords: 
            wrong = True
        if go <= 3 and not wrong:
            for j in range(26):
                if item.count(alphabet[j]) >= 2: 
                    wrong = True
            for i in range(5):
                if item[i] in startLetters: 
                    wrong = True
        else:
            if item[0] in wrongLetters or item[1] in wrongLetters or item[2] in wrongLetters or item[3] in wrongLetters or item[4] in wrongLetters: 
                wrong = True
            if len(okLetters) >= 1 and not wrong:
                for j in range(len(okLetters)):
                    if okLetters[j] not in item and len(okLetters) > 0: 
                        wrong = True
            if not wrong:
                for j in range(5):
                    if item[j] in okLettersPlace[j]: 
                        wrong = True
            if not wrong:
                for j in range(5):
                    if item[j] not in correctLetters[j] and len(correctLetters[j]) == 1: 
                        wrong = True
        if not wrong:
            for j in range(5):
                number += alphabetFrequency[item[j]]
            if number > value:
                word = item
                value = number
    print(word)
    correct = input("Was that the answer? [Y/n] ")
    correct = correct.lower()
    if correct =="y":
        found = True
    if not found:
        verification = input("Is that a word? [Y/n] ")
        verification = verification.lower()
        if verification == "n": 
            valid = False
            wrongWords.append(word)
        if valid:
            go += 1
            startLetters += word
            for i in range(5):
                answer = input("What was letter " + str(i+1) + "? [C/M/W] ")
                answer = answer.lower()
                if answer == "c":
                   correctLetters[i] = word[i]
                elif answer == "m":
                    okLetters += word[i]
                    okLettersPlace[i] = word[i]
                elif answer == "w":
                    wrongLetters += word[i]

if found:
    print("Congratulations!")
else:
    print("Better luck next time!")

textFile3 = open("wrongWords.txt", "w")

for i in range(len(wrongWords)):
  textFile3.writelines(wrongWords[i] + "\n")

textFile3.close()