# -*- coding: utf-8 -*-
import random
print "Willkommen bei: *Errate die richtige Zahl!*"
print "*"*60

result = random.randint(0, 100)
name = raw_input("Bitte gib deinen Namen ein: ")
print "Hallo " + name + "! Schön, dass du da bist!"

guess = raw_input(name + ", bitte gib eine Zahl zwischen 0 und 100 ein: ")
guess = int(guess)

while True:
    if guess == result:
        print "Gratulation, "+ name, "du hast die richtige Zahl erraten!"
        break
    elif guess > result:
        print "Das Ergebnis ist kleiner!"
    elif guess < result:
        print "Das Ergebnis ist größer!"

    guess = raw_input("Schade "+ name + ", gib noch eine Zahl ein:")
    guess = int(guess)

print "Es war toll mit dir zu spielen! :)"


