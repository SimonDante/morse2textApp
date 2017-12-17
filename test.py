#!/usr/bin/python


from tkinter import *
from tkinter import ttk

#Dictionary for plain text to Morse Code.

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.' 
    }

#Dictionary for Morse Code to plain text

RCODE = {'.-' : 'A',     '-...' : 'B',   '-.-.' : 'C', 
    '-..' : 'D' ,    '.' : 'E' ,      '..-.' : 'F',
    '--.' : 'G',     '....' : 'H',    '..' : 'I',
    '.---' : 'J',    '-.-' : 'K',     '.-..' : 'L',
    '--' : 'M',     '-.' : 'N',      '---' : 'O',
    '.--.' : 'P',   '--.-' : 'Q',   '.-.':'R',
    '...':'S',    '-':'T',      '..-':'U',
    '...-':'V',   '.--':'W',    '-..-':'X',
    '-.--':'Y',   '--..':'Z',

    '-----':'0',  '.----':'1',  '..---':'2',
    '...--':'3',  '....-':'4',  '.....':'5',
    '-....':'6',  '--...':'7',  '---..':'8',
    '----.':'9' 

   }



#Create a class containing all the GUI elements along with the
#functions needed to create the buttons. Everything is tested except
#the print to file button but even if it doesn't work tweeking it
#shouldn't be too hard.

class App(Frame):
    def __init__(self , master= None):
        mainFrame = ttk.Frame(master , padding = "4 4 12 12")
        mainFrame.grid(column = 0 , row = 0 , sticky = (N , W , E , S))
        mainFrame.columnconfigure(0 , weight = 1)
        mainFrame.rowconfigure(0 , weight = 1)
        self.value1 = StringVar()
        self.value1.set("This is plain text section.")

        self.entry1 = ttk.Entry(mainFrame , width = 20 , textvariable = self.value1)
        self.entry1.grid(column = 1 , row = 1 , stick = W)

        self.labelVar = StringVar()
        self.labelVar.set("This is Morse Code section.")
        self.entry2 = ttk.Entry(mainFrame , width = 20,  textvariable = self.labelVar)
        self.entry2.grid(column = 1 , row = 3)


        ttk.Button(mainFrame , text = "Convert to Morse" , command = self.calculate).grid(column = 3 , row = 4 , sticky = W)
        self.entry1.focus() 

        ttk.Button(mainFrame , text = "Convert to plain text" , command = self.rcalc).grid(column = 2 , row = 4 , sticky = W)

        ttk.Button(mainFrame, text = "Save Morse to file" , command = self.printToFile).grid(column = 1 , row = 4 , sticky = W)


    #Function calculate is for Morse Code to plain text.

    def calculate(self):
        val1 = list(self.value1.get())
        morseCode = []
        for i in val1 :
            if (i == " "):
                morseCode.append("   ")
            else:
                morseCode.append(CODE[i.upper()])

            morseCode.append(" ")

        self.labelVar.set(''.join(morseCode))

    # Function rcalc is for converting plain text to Morse Code.

    def rcalc(self):
        val1 = str(self.labelVar.get()).split()
        plainText = []
        for i in val1:
            plainText.append(RCODE[i])

        self.value1.set(''.join(plainText))

    #Fucntion print to file prints the morse code to a file for 
    #future use. Generally since it is already an entry you can
    #just copy and paste the strings in a file on your own but 
    #it just makes your life easier for the Morse Code. 
    def printToFile():
        with open("morse.txt" , "w") as f:
            f.write(labelVar.get())


#For future use i could make it get some more "Codes" or add
#more symbols in the dictionary. The second part is pretty easy
#if you find the symbols you need or maybe a different language in 
#Morse Code. 



def main():
    root = Tk()
    app = App(root)
    #root.bind("<Return>" , calculate)
    root.mainloop()


if __name__ == '__main__':
    main()
