from tkinter import *
#from ProjectMain import *
import neopixel
import board
import time
from time import sleep

class UserInput(Frame):
    def __init__(self, parent, entry = None, color = (110, 0, 110)):
        Frame.__init__(self, parent, bg="white")
        self.entry = entry
        self.color = color
        self.pixels = neopixel.NeoPixel(board.D18, 320, brightness=0.3, auto_write=False)
        self.setupGUI()
        #self.window.bind("<F11>", self.toggleFullScreen)
        #self.window.bind("<Escape>", self.quitFullScreen)

    def setupGUI(self):
        self.display = Label(self, text="", fg="black", anchor=E, bg="white", height=2)

        self.display.grid(row=0, column=0, columnspan=4, sticky=N+E+W+S)
                
        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(2):
            Grid.columnconfigure(self, col, weight=1)



        # first row
        label = Label(self, fg="black", text=\
                        "Enter text and click a color. Press Enter to commit changes.")
        label.grid(row=0, column=0, sticky=N+S+E+W)

        # second row
        self.entry = Entry(self, bg="white", fg="black")
        self.entry.grid(row=1, column=0, sticky=N+W+S+E)
        button = Button(self, bg="white", text="enter", borderwidth=0,\
                        highlightthickness=1, activebackground="white")
        button.grid(row=1, column=1, sticky=N+E+W+S)
        button.bind("<Button-1>", self.getWord)

        #third row
        button0 = Button(self, bg="Red", text="Red", borderwidth=0,\
                        highlightthickness=1, activebackground="white")
        button0.grid(row=3, column=0, sticky=N+E+W+S)
        button0.bind("<Button-1>", self.Red)
        button1 = Button(self, bg="Blue", text="Blue", borderwidth=0,\
                        highlightthickness=1, activebackground="white")
        button1.grid(row=3, column=1, sticky=N+E+W+S)
        button1.bind("<Button-1>", self.Blue)

        #fourth row

        button2 = Button(self, bg="Green", text="Green", borderwidth=0,\
                        highlightthickness=1, activebackground="white")
        button2.grid(row=4, column=0, sticky=N+E+W+S)
        button2.bind("<Button-1>", self.Green)
        button3 = Button(self, bg="Purple", text="Purple", borderwidth=0,\
                        highlightthickness=1, activebackground="white")
        button3.grid(row=4, column=1, sticky=N+E+W+S)
        button3.bind("<Button-1>", self.Purple)


        self.pack(fill=BOTH, expand=1)
    def Red(self, event):
        #print ("red button clicked")
        self.color = (220, 0, 0)
        #print (color)
    def Blue(self, event):
        #print ("blue button clicked")
        self.color = (0, 0, 220)
        #print (color)
    def Green(self, event):
        #print ("green button clicked")
        self.color = (0, 220, 0)
        #print (color)
    def Purple(self, event):
        #print ("purple button clicked")
        self.color = (110, 0, 110)
        #print (color)
    def getWord(self, event):
        word = self.entry.get()
        tempcolor = self.color
        self.displayWord(word, tempcolor)
        print (word, tempcolor)
    def displayWord(self, word, color):
        self.pixels.fill(0)
        words = self.processing(word)
        for word in range(len(words)):
            self.parse(words[word], color)
            sleep(1)
            self.pixels.fill(0)
    def space(self, quad, color):
        self.pixels[quad] = (0, 0, 0)
    def A(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(2, 8):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+22)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 6):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+26)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()

    def B(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            for i in range(3, 8):
                self.pixels[(i+quad+22)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            for i in range(0, 5):
                self.pixels[(i+quad+26)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels.show()
            
    def C(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(2, 7):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels.show()
        else:
            for i in range(1, 6):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels.show()
            
    def D(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            for i in range(1, 6):
                self.pixels[(i + quad + 24)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            for i in range(1, 6):
                self.pixels[(i + quad + 25)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels.show()
            
    def E(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad+7)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 27)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad+9)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 28)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels.show()
    def F(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()

    def G(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(2, 7):
                self.pixels[(i+quad)] = (color)
            for i in range(0, 3):
                self.pixels[(i+quad + 25)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels.show()
        else:
            for i in range(1, 6):
                self.pixels[(i+quad)] = (color)
            for i in range(0, 3):
                self.pixels[(i+quad + 28)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()
            
    def H(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+23)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 25)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()

    def I(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def J(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 7)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels.show()
    def K(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 21)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 18)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def L(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def M(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+32)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 28)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 32)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 27)] = (color)
            self.pixels.show()
    def N(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+23)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 25)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()
    def O(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 6):
                self.pixels[(i+quad + 1)] = (color)
                self.pixels[(i+quad+24)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels.show()
        else:
            for i in range(2, 7):
                self.pixels[(i+quad - 1)] = (color)
                self.pixels[(i + quad + 24)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels.show()
    def P(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            for i in range(6, 8):
                self.pixels[(i+quad+22)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            for i in range(0, 2):
                self.pixels[(i+quad+26)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels.show()
    def Q(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+24)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels.show()
        else:
            for i in range(1, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 24)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def R(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
            for i in range(6, 8):
                self.pixels[(i+quad+22)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 21)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
            for i in range(0, 2):
                self.pixels[(i+quad+26)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 18)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def S(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            self.pixels[(quad + 2)] = (color)
            self.pixels[(quad + 3)] = (color)
            self.pixels[(quad + 7)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 17)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
        else:
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 4)] = (color)
            self.pixels[(quad + 5)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 22)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
    def T(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels[(quad + 33)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad + 16)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels[(quad + 38)] = (color)
            self.pixels.show()
    def U(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+24)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels.show()
        else:
            for i in range(1, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 24)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels.show()
    def V(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 6):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+32)] = (color)
            self.pixels[(quad + 9)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 25)] = (color)
            self.pixels.show()
        else:
            for i in range(1, 6):
                self.pixels[(i+quad + 1)] = (color)
                self.pixels[(i + quad + 33)] = (color)
            self.pixels[(quad + 14)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 30)] = (color)
            self.pixels.show()
    def W(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(1, 8):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i + quad + 32)] = (color)
            self.pixels[(quad + 10)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 7):
                self.pixels[(i+quad)] = (color)
                self.pixels[(i+quad+32)] = (color)
            self.pixels[(quad + 13)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels.show()
    def X(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 2)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 7)] = (color)
            self.pixels[(quad + 10)] = (color)
            self.pixels[(quad + 12)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels[(quad + 28)] = (color)
            self.pixels[(quad + 33)] = (color)
            self.pixels[(quad + 34)] = (color)
            self.pixels[(quad + 38)] = (color)
            self.pixels[(quad + 39)] = (color)
            self.pixels.show()
        else:
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 5)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 11)] = (color)
            self.pixels[(quad + 13)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 27)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels[(quad + 32)] = (color)
            self.pixels[(quad + 33)] = (color)
            self.pixels[(quad + 37)] = (color)
            self.pixels[(quad + 38)] = (color)
            self.pixels.show()
    def Y(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            for i in range(0, 5):
                self.pixels[(quad + i + 19)] = (color)
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 13)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels[(quad + 32)] = (color)
            self.pixels[(quad + 33)] = (color)
            self.pixels.show()
        else:
            for i in range(0, 5):
                self.pixels[(quad + i + 16)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels[(quad) + 6] = (color)
            self.pixels[(quad) + 7] = (color)
            self.pixels[(quad) + 10] = (color)
            self.pixels[(quad + 38)] = (color)
            self.pixels[(quad + 39)] = (color)
            self.pixels.show()
    def Z(self, quad, color):
        if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
            self.pixels[(quad + 2)] = (color)
            self.pixels[(quad + 6)] = (color)
            self.pixels[(quad + 7)] = (color)
            self.pixels[(quad + 8)] = (color)
            self.pixels[(quad + 10)] = (color)
            self.pixels[(quad + 13)] = (color)
            self.pixels[(quad + 18)] = (color)
            self.pixels[(quad + 20)] = (color)
            self.pixels[(quad + 23)] = (color)
            self.pixels[(quad + 24)] = (color)
            self.pixels[(quad + 28)] = (color)
            self.pixels[(quad + 29)] = (color)
            self.pixels.show()
        else:
            self.pixels[(quad)] = (color)
            self.pixels[(quad + 1)] = (color)
            self.pixels[(quad + 5)] = (color)
            self.pixels[(quad + 10)] = (color)
            self.pixels[(quad + 13)] = (color)
            self.pixels[(quad + 15)] = (color)
            self.pixels[(quad + 16)] = (color)
            self.pixels[(quad + 19)] = (color)
            self.pixels[(quad + 21)] = (color)
            self.pixels[(quad + 26)] = (color)
            self.pixels[(quad + 27)] = (color)
            self.pixels[(quad + 31)] = (color)
            self.pixels.show()
    def processing(self, word):
        strings = []
        if (len(word) < 9):
            strings.append(word)
        else:
            strings = []
            for n in range(len(word)):
                if ((n + 8) < (len(word)+ 1)):
                    strings.append(word[n:(n + 8)])
        return strings

    # Used to divide a word into a string of characters to be used
    # in projecting letters to the screen.
    def parse(self, word, color):
        quad = [0, 40, 80, 120, 160, 200, 240, 280]
        word = word[0:8]
        #print(word)
        word = [i for ele in word for i in ele]
        #print(word)

        for counter in range(len(word)):
            print("{}, {}, {}".format(word[counter], color, quad[counter]))
            if(word[counter] == "a"):
                self.A(quad[counter], color)
            if(word[counter] == "b"):
                self.B(quad[counter], color)
            if(word[counter] == "c"):
                self.C(quad[counter], color)
            if(word[counter] == "d"):
                self.D(quad[counter], color)
            if(word[counter] == "e"):
                self.E(quad[counter], color)
            if(word[counter] == "f"):
                self.F(quad[counter], color)
            if(word[counter] == "g"):
                self.G(quad[counter], color)
            if(word[counter] == "h"):
                self.H(quad[counter], color)
            if(word[counter] == "i"):
                self.I(quad[counter], color)
            if(word[counter] == "j"):
                self.J(quad[counter], color)
            if(word[counter] == "k"):
                self.K(quad[counter], color)
            if(word[counter] == "l"):
                self.L(quad[counter], color)
            if(word[counter] == "m"):
                self.M(quad[counter], color)
            if(word[counter] == "n"):
                self.N(quad[counter], color)
            if(word[counter] == "o"):
                self.O(quad[counter], color)
            if(word[counter] == "p"):
                self.P(quad[counter], color)
            if(word[counter] == "q"):
                self.Q(quad[counter], color)
            if(word[counter] == "r"):
                self.R(quad[counter], color)
            if(word[counter] == "s"):
                self.S(quad[counter], color)
            if(word[counter] == "t"):
                self.T(quad[counter], color)
            if(word[counter] == "u"):
                self.U(quad[counter], color)
            if(word[counter] == "v"):
                self.V(quad[counter], color)
            if(word[counter] == "w"):
                self.W(quad[counter], color)
            if(word[counter] == "x"):
                self.X(quad[counter], color)
            if(word[counter] == "y"):
                self.Y(quad[counter], color)
            if(word[counter] == "z"):
                self.Z(quad[counter], color)
            if(word[counter] == " "):
                self.space(quad[counter], color)
            #else:
                #print("NO NUMBER/CHARACTER SUPPORT YET")

def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
app = Tk()
app.attributes('-fullscreen', True)  
#app.fullScreenState = False
#app.bind("<F11>", toggleFullScreen)
#app.bind("<Escape>", quitFullScreen)
p = UserInput(app)    
app.mainloop()

