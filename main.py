import re
import string
import difflib
from tkinter import *
import tkinter

def Exit():
    print("Exiting Program!!")
    exit(0)

def checkSpell():
    file = open("words.txt", "r")
    userInput = input("Enter the word to check - ").lower()

    for line in file.readlines():
        if re.findall('\\b'+userInput+'\\b', line.lower(), re.I):
            print("Spelling is correct")
            Exit()
        else:
            continue;

    file.close()
    file = open("words.txt", "r")

    print("Word is incorrectly spelled")

    line = "";

    lines = [word.split(",") for word in file.readlines()]

    print("Did you mean ? : ")

    modList = [];

    for words in lines:
        for word in words:
            modList.append(word)

    word = "";

    strippedList = [word.rstrip() for word in modList]

    result = difflib.get_close_matches(str(userInput), strippedList, 1)

    print(str(result))

    file.close()


#main
root = tkinter.Tk()
word = Entry(root)
word.pack(side=RIGHT)
#checkSpell()
root.mainloop()