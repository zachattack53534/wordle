#Imports
import random
import nltk
from nltk.corpus import words

#Text files 
text_file = open("answers.txt", "r")
text_file1 = open("5-letter-dict.txt", "r")

#Colours
green = "\033[0;30;42m{}"
yellow = "\033[0;30;41m{}"
grey = "\033[0;30;47m{}"
reset = "\033[0;30;0m{}"
black = "\u001b[0;30;40m{}"


#Word lists
word_list = []
random_words = []
while True:
    a = text_file.readline()
    if not a: break
    random_words.append(a[0:5])
while True:
    b = text_file1.readline()
    if not b: break
    word_list.append(b[0:5])
full_word_list = words.words()
for i in range(len(full_word_list)):
    if len(full_word_list[i]) == 5:
        word_list.append(full_word_list[i])

#Guess list
guesses = []

#Other Variables
display = ""
letters = []
keyboard = list("|Q|W|E|R|T|Y|U|I|O|P|\n |A|S|D|F|G|H|J|K|L| \n  |Z|X|C|V|B|N|M|    ")
keyboard1 = list("|Q|W|E|R|T|Y|U|I|O|P|\n |A|S|D|F|G|H|J|K|L| \n  |Z|X|C|V|B|N|M|    ")
error = ""

#Randomly chosen word
word = random_words[random.randint(0, len(random_words) - 1)]
word = word[0:5]
word.lower()
score = 0

#GUI
def GUI():
    for i in range(50):
        print()
    print("{}".format(error))
    print()
    print("{:^21}".format("WORDLE"))
    print(black.format("-" * 21) + reset.format(""))
    for i in range(len(guesses)):
        print(black.format("|") + reset.format("") + guesses[i] + " ")
        print(black.format("-" * 21) + reset.format(""))
    for i in range(6 - len(guesses)):
        print((black.format("|") + reset.format("") +  " " * 3) * 5 + black.format("|") + reset.format(""))
        print(black.format("-" * 21) + reset.format(""))
    print("".join(keyboard))
        

GUI()

#Main Code
for j in range(6):
    letters = []
    score = 0
    display = ""
    while True:
        error = ""
        try:
            guess = input("Please make a guess: ")
            guess.lower()
            verified = word_list.count(guess)
            if len(guess) == 5 and verified >= 1: break
            elif len(guess) != 5: 
                error = "Please enter a 5 letter word!"
            elif verified == 0: 
                error = "Word does not exist!"
            GUI()
        except:
            error = "There was an error with your input!"
            GUI()
    for repeat in range(2):
        for i in range(5):
            ok = word.count(guess[i])
            ok = ok - letters.count(guess[i])
            if guess[i] == word[i] and repeat == 0:
                letters.append(guess[i])
                score = score + 1
            elif guess[i] == word[i] and repeat == 1:
                l = guess[i].upper()
                k = keyboard1.index(l)
                keyboard[k] = green.format(l) + reset.format("")
                display = display + reset.format("") + green.format(" " + guess[i] + " ") + reset.format("") + black.format("|") + reset.format("")
            elif ok >= 1 and repeat == 1:
                l = guess[i].upper()
                k = keyboard1.index(l)
                if keyboard[k] == green.format(l) + reset.format(""):
                    pass
                else:
                    keyboard[k] = yellow.format(l) + reset.format("")
                letters.append(guess[i])
                display = display + reset.format("") + yellow.format(" " + guess[i] + " ") + reset.format("") + black.format("|") + reset.format("")
            elif repeat == 1:
                l = guess[i].upper()
                k = keyboard1.index(l)
                if keyboard[k] == green.format(l) + reset.format("") or keyboard[k] == yellow.format(l) + reset.format(""):
                    pass
                else:
                    keyboard[k] = grey.format(l) + reset.format("")
                display = display + reset.format("") + grey.format(" " + guess[i] + " ") + reset.format("") + black.format("|") + reset.format("")
                try:
                    letters_allowed.remove(guess[i] + ", ")
                except:
                    pass
    guesses.append(display + reset.format(""))
    GUI()
    if score == 5:
        break


if score <= 4:
    error = "The word was " + word
    GUI()
