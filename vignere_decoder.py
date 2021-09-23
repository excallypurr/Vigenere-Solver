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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
specialChars = "[@_!#$%^&*()<>?/\|}{~:]'"

def decrypt():
    ################################################
    #
    # Variable Declaration
    #
    ################################################
    msgCount = 0
    keyCount = 0
    decrOut = ""
    msg = msgInput.get(1.0, END).lower()
    key = keyInput.get(1.0, END).lower()
    keyLen=len(key)

    if not msg:
        emptyMsg = messagebox.showerror("Empty Input!", "No entry was detected, please try again!")
        return
    if ' ' in key:
        spaceMsg = messagebox.showerror("Space in Key!", "Please do not use any spaces in the key!")
        return
    for i in msg:
        if keyCount == keyLen:
            keyCount = 0
        if i in specialChars:
            print ("SPECIAL CHAR: " + i)
            decrOut += i
            continue
        elif i.isspace():
            print("SPACE")
            decrOut += i
            continue
        msgNum = alphabet.find(i)
        keyNum = alphabet.find(key[keyCount])
        print("This is msgNum: " + str(msgNum))
        print("This is keyNum: " + str(keyNum))
        decrNum = alphabet[((msgNum - keyNum)%26)]
        decrOut += decrNum
        msgCount+=1
        keyCount+=1
    charCount = 27 + len(decrOut)
    decrBox = Toplevel(width=1)
    decrLable = Text(decrBox, height=1, width=charCount, wrap=WORD)
    decrLable.insert(1.0, ("Your decrypted message is: " + decrOut))
    decrLable.pack()

    return

def encrypt():
    ################################################
    #
    # Variable Declaration
    #
    ################################################
    msgCount = 0
    keyCount = 0
    encrOut = ""
    msg = msgInput.get(1.0, END).lower()
    key = keyInput.get(1.0, END).lower()
    keyLen=len(key)

    if not msg:
        emptyMsg = messagebox.showerror("Empty Input!", "No entry was detected, please try again!")
        return
    if ' ' in key:
        spaceMsg = messagebox.showerror("Space in Key!", "Please do not use any spaces in the key!")
        return
    for i in msg:
        if keyCount == keyLen:
            keyCount = 0
        if i.isspace():
            print("SPACE")
            encrOut += i
            continue
        if i in specialChars:
            print ("SPECIAL CHAR: " + i)
            encrOut += i
            continue
        msgNum = alphabet.find(i)
        keyNum = alphabet.find(key[keyCount])
        print("This is msgNum: " + str(msgNum))
        print("This is keyNum: " + str(keyNum))
        encrNum = alphabet[((msgNum + keyNum)%26)]
        encrOut += encrNum
        msgCount+=1
        keyCount+=1
    charCount = 27 + len(encrOut)
    encrBox = Toplevel(width=1)
    encrLable = Text(encrBox, height=1, width=charCount, wrap=WORD)
    encrLable.insert(1.0, ("Your encrypted message is: " + encrOut))
    encrLable.pack()

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
encrButt = Button(main, text = "Encrypt!", command = encrypt)
decrButt = Button(main, text = "Decrypt!", command = decrypt)

msgLabel.grid(row = 0, column = 0)
msgInput.grid(row = 0, column = 1)
keyLabel.grid(row = 1, column = 0)
keyInput.grid(row = 1, column = 1)
encrButt.grid(row = 2, column = 0)
decrButt.grid(row = 2, column = 1)

main.mainloop()