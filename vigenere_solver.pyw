############################################
#
# Vignere Cipher Solver
# By: Tommy Stewart
#
############################################
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

alphabet = 'abcdefghijklmnopqrstuvwxyz'
specialChars = "[@_!#$%^&*()<>?/\|}{~:]'"

def solve(oper):
    msgCount = 0
    keyCount = 0
    out = ""
    msg = msgInput.get(1.0, "end-1c").lower()
    print(type(msg))
    key = keyInput.get(1.0, "end-1c").lower()
    if not msg:
        messagebox.showerror("Empty Input!", "No entry was detected, please try again!")
        return
    if ' ' in key:
        messagebox.showerror("Space in Key!", "Please do not use any spaces in the key!")
        return
    for i in msg:
        if keyCount == len(key):
            keyCount = 0
        if i in specialChars:
            print ("SPECIAL CHAR: " + i)
            out += i
            continue
        elif i.isspace():
            print("SPACE")
            out += i
            continue
        msgNum = alphabet.find(i)
        keyNum = alphabet.find(key[keyCount])
        print("This is msgNum: " + str(msgNum))
        print("This is keyNum: " + str(keyNum))
        if oper == "decrypt":
            decrNum = alphabet[((msgNum - keyNum)%26)]
            out += decrNum
        if oper == "encrypt":
            encrNum = alphabet[((msgNum + keyNum)%26)]
            out += encrNum
        msgCount+=1
        keyCount+=1
    charCount = 27 + len(out)
    decrBox = Toplevel(width=1)
    decrLable = Text(decrBox, height=1, width=charCount, wrap=WORD)
    decrLable.insert(1.0, ("Your " + oper + "ed message is: " + out))
    decrLable.pack()
    return

########################################################
#
#tkinter gui defintions
#
########################################################
main = tkinter.Tk()

main.title("Vigenere Solver")
msgLabel = Label(main, text="Please enter the message")
keyLabel = Label(main, text="Please enter the key")
msgInput = Text(main, height = 1, width = 30)
keyInput = Text(main, height = 1, width = 30)
encrButt = Button(main, text = "Encrypt!", command=partial(solve, "encrypt"))
decrButt = Button(main, text = "Decrypt!", command=partial(solve, "decrypt"))

msgLabel.grid(row = 0, column = 0)
msgInput.grid(row = 0, column = 1)
keyLabel.grid(row = 1, column = 0)
keyInput.grid(row = 1, column = 1)
encrButt.grid(row = 2, column = 0)
decrButt.grid(row = 2, column = 1)

main.mainloop()