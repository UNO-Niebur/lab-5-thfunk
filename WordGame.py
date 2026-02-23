#Word Game is a knock-off version of a popular online word-guessing game.

import random

#Decides if letter is in the word at all.
def inWord(letter, word):
    if letter in word:
        return True
    else: return False

#Decides if letter is in the right spot.
def inSpot(letter, word, spot):
    if (letter == word[spot]):
        return True
    else: return

#Rates guess lower case if letter is in the word but in the wrong spot, capital letter if the letter is in the right spot, and * if the letter is not in the word at all.
def rateGuess(myGuess, word):
    rating = ""
    for i in range(len(myGuess)):
        if (inSpot(myGuess[i], word, i)):
            rating = rating + myGuess[i].upper()
        elif (inWord(myGuess[i], word)):
            rating = rating + myGuess[i].lower()
        else:
            rating = rating + "*"
    return rating


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)
    print("You will have 6 changes to guess my 5 letter word. A capital letter will indicate that the letter is in the right spot, a lowercase letter will mean that the letter is in the word but in the wrong spot, and a * will mean that the letter is not in the word at all.")
    #6 changes to guess the word:
    count = 1
    while (count < 7):
         print("Guess #", count)
         guess = input("Enter your guess: ").lower()
         while (len(guess) != 5):
             print("Your guess must be 5 letters long. Try again.")
             guess = input("Enter your guess: ").lower()
         print(rateGuess(guess, todayWord))
         if (guess == todayWord):
             print("Congratulations! You guessed the", todayWord," in ", count, "guesses!")
             break
         count += 1
    if (count == 7):
        print("Sorry, you ran out of guesses. The word was", todayWord)
    

if __name__ == '__main__':
  main()
