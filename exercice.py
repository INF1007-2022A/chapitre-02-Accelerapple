#!/usr/bin/env python
# -*- coding: utf-8 -*-
ok = True


def majusculation(texte):
    lettres = list(texte)
    output = ""
    for i in lettres:
        dec = ord(i)
        if 97 <= dec <= 122:
            maj = dec - 32
            output += (chr(maj))
        else:
            output += i

    print(output)


def minuculation(texte):
    lettres = list(texte)
    output = ""
    for i in lettres:
        dec = ord(i)
        if 65 <= dec <= 90:
            maj = dec + 32
            output += (chr(maj))
        else:
            output += i

    print(output)


def choice():
    global ok

    while True:
        choix = input("maj ou min?: ")
        if choix == "maj" or choix == "min":
            break
        elif choix == "end":
            print("Bye")
            ok = False
            print("\n", "last words?")
            break
        else:
            print("bruh")

    entre = input("ecrire ici: ")
    if choix == "maj":
        majusculation(entre)
    elif choix == "min":
        minuculation(entre)
    elif not ok:
        choix = "End"

    print("end with option: ", choix, "\n")


while ok:
    choice()

