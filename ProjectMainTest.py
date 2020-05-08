##############################################################
#Group 9: Albert O'Connell, Isaiah Coody, Ethan Ubeda
#Date: 5/1/2020
#Description: This program runs the control for the led sign as part of our CS-132 project
##############################################################
from Project3 import *
from time import sleep

# Value of starting points on the LED Screen
quad = [0, 40, 80, 120, 160, 200, 240, 280]


# Used to divide words into a list of 8 character strings.
def processing(word):
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
def parse(word, color):
    word = word[0:8]
    print(word)
    word = [i for ele in word for i in ele]
    print(word)

    for counter in range(len(word)):
        print("{}, {}, {}".format(word[counter], color, quad[counter]))
        if(word[counter] == "a"):
            A(quad[counter], color)
        if(word[counter] == "b"):
            B(quad[counter], color)
        if(word[counter] == "c"):
            C(quad[counter], color)
        if(word[counter] == "d"):
            D(quad[counter], color)
        if(word[counter] == "e"):
            E(quad[counter], color)
        if(word[counter] == "f"):
            F(quad[counter], color)
        if(word[counter] == "g"):
            G(quad[counter], color)
        if(word[counter] == "h"):
            H(quad[counter], color)
        if(word[counter] == "i"):
            I(quad[counter], color)
        if(word[counter] == "j"):
            J(quad[counter], color)
        if(word[counter] == "k"):
            K(quad[counter], color)
        if(word[counter] == "l"):
            L(quad[counter], color)
        if(word[counter] == "m"):
            M(quad[counter], color)
        if(word[counter] == "n"):
            N(quad[counter], color)
        if(word[counter] == "o"):
            O(quad[counter], color)
        if(word[counter] == "p"):
            P(quad[counter], color)
        if(word[counter] == "q"):
            Q(quad[counter], color)
        if(word[counter] == "r"):
            R(quad[counter], color)
        if(word[counter] == "s"):
            S(quad[counter], color)
        if(word[counter] == "t"):
            T(quad[counter], color)
        if(word[counter] == "u"):
            U(quad[counter], color)
        if(word[counter] == "v"):
            V(quad[counter], color)
        if(word[counter] == "w"):
            W(quad[counter], color)
        if(word[counter] == "x"):
            X(quad[counter], color)
        if(word[counter] == "y"):
            Y(quad[counter], color)
        if(word[counter] == "z"):
            Z(quad[counter], color)
        if(word[counter] == " "):
            space(quad[counter], color)
        #else:
            #print("NO NUMBER/CHARACTER SUPPORT YET")


# receives an input
def get_word():
    word = input("What word would you like to print? ")
    return word

def fill(color):
    pixels.fill(color)
    pixels.show()
def background(color, color2):
    pixels.fill(color)
    pixels.show
    temp = get_word()
    parse(temp, color2)

    
#MAIN
while(True):
    pixels.fill(0)
    aWord = get_word()
    words = processing(aWord)
    for word in range(len(words)):
        parse(words[word], PURPLE)
        sleep(1)
        pixels.fill(0)
        print(word)


