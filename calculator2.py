# -*- coding: utf-8 -*-
# print welcome to user

print "Herzlich Willkommen! Du hast einen Taschenrechner entdeckt"
# read user input for operation

oper = str(raw_input("Bitte gib deine gewünschte Rechenoperation ein (+-/*): "))
print "Deine gewünschte Operation ist: " + str(oper)

if oper != "+" and oper != "-" and oper != "*" and oper != "/":
    print "Falsche Eingabe"
    quit()
# read user input for first value

num1 = float(raw_input("Bitte gib die erste Zahl ein: "))
print "Deine erste Zahl ist " + str(num1)
num2 = float(raw_input("Bitte gib die zweite Zahl ein: "))
print "Deine zweite Zahl ist " + str(num2)
# calculate



if oper == "+":
    result = num1+num2
elif oper == "-":
    result = num1-num2
elif oper == "/":
    result = num1/num2
elif oper == "*":
    result = num1*num2

print "Das Ergebnis ist: " + str(result)
