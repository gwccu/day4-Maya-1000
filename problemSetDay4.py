# file name: problemSetDay4.py
# file name: problemSetDay4.py
from random import randint
number=int(input("Choose a number between 1 and 1000."))
chosen=randint(1,1000)

print(chosen)

while number != chosen:
    if number > chosen:
        print("Too high. Try again!")
    elif number < chosen:
        print("Too low. Try again!")
    number=int(input("Choose a number between 1 and 1000."))

if number == chosen:
    print("Congrats! You got it!")

print("-----------------------------------------------")

strength=6

print("Your current strength is 5.")

while strength <= 10:
    print(strength)
    strength += 1
    print("Now your strength is one greater.")

strength=9
if strength == 9:
    print("Error 404: Too strong at game. GAME OVER!")

print("-----------------------------------------------")

n=int(input("Choose a number between 1-10."))
m=int(input("Choose another number between 1-5."))

print(n**m)
print("That is your first number raised to the power of your second number.")

print("-----------------------------------------------")

print("I am going to teach you how to play hangman.")
a=input("First things first, hangman is a game where you try to guess a word or a phrase made up by another person. Does that make sense?")
b=input("Okay, good. The way that you guess the other phrase is by guessing individual letters, like a or e. If the word/phrase has that letter, all of that letter gets filled in on a board that shows you how many letters there are. Okay?")
c=input("However, you have to beware; if you guess a letter that is not in the phrase, a body part of a stick figure gets drawn on a hanger.")
d=input("If you guess too many wrong letters and get to the point where the whole stick figure is drawn, you loose.")
e=input("You can also try to guess the whole word/phrase if you think you know it.")
f=input("That's about it! Let's try it. I am thinking of a 3 letter word. Guess a letter.")

while f != "p" or f != "i" or f != "g":
    print("Sorry, that is wrong. Try again.")
    f=input("Guess another letter.")
if f == "p":
    print("Good job! That is the first letter of the word.")

print("Not done yet so not all has been tested or edited :)")