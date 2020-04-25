from random import randint
import time
import board
import neopixel
pixel_pin = board.D18
num_pixels = 320
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)






def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
quad0 = 0
quad1 = 40
quad2 = 80
quad3 = 120
quad4 = 160
quad5 = 200
quad6 = 240
quad7 = 280
GREEN = (0, 220, 0)
RED = (220, 0, 0)
BLUE = (0, 0, 220)
TEAL = (0, 110, 110)
PURPLE = (110, 0, 110)
WHITE = (110, 110, 110)
YELLOW = (110, 110, 0)
ORANGE = (170, 50, 0)
RANDOM = (randint(0, 220), randint(0, 220), randint(0, 220))

def A(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(2, 8):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+22)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 6):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+26)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()

def B(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        for i in range(3, 8):
            pixels[(i+quad+22)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        for i in range(0, 5):
            pixels[(i+quad+26)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 16)] = (color)
        pixels.show()
        
def C(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(2, 7):
            pixels[(i+quad)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
    else:
        for i in range(1, 6):
            pixels[(i+quad)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels.show()
        
def D(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        for i in range(1, 6):
            pixels[(i + quad + 24)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        for i in range(1, 6):
            pixels[(i + quad + 25)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels.show()
        
def E(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 16)] = (color)
        pixels.show()
def F(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()

def G(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(2, 7):
            pixels[(i+quad)] = (color)
        for i in range(0, 3):
            pixels[(i+quad + 25)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
    else:
        for i in range(1, 6):
            pixels[(i+quad)] = (color)
        for i in range(0, 3):
            pixels[(i+quad + 28)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()
        
def H(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+23)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 25)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()

def I(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 24)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show()
def J(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 7)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 25)] = (color)
        pixels.show()
def K(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 21)] = (color)
        pixels[(quad + 24)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 29)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 18)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 26)] = (color)
        pixels[(quad + 30)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show()
def L(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 24)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        pixels[(quad)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show()
def M(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+32)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 28)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 32)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 27)] = (color)
        pixels.show()
def N(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+23)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 25)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()
def O(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+24)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
    else:
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 24)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
def P(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        for i in range(6, 8):
            pixels[(i+quad+22)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        for i in range(0, 2):
            pixels[(i+quad+26)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 19)] = (color)
        pixels.show()
def Q(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+24)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 24)] = (color)
        pixels.show()
    else:
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 24)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show()
def R(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
        for i in range(6, 8):
            pixels[(i+quad+22)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 21)] = (color)
        pixels[(quad + 24)] = (color)
        pixels[(quad + 25)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
        for i in range(0, 2):
            pixels[(i+quad+26)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 18)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 30)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show()
def S(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        pixels[(quad + 2)] = (color)
        pixels[(quad + 3)] = (color)
        pixels[(quad + 7)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 17)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 26)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
    else:
        pixels[(quad)] = (color)
        pixels[(quad + 4)] = (color)
        pixels[(quad + 5)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 22)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 29)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
def T(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 30)] = (color)
        pixels[(quad + 33)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad + 16)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 25)] = (color)
        pixels[(quad + 38)] = (color)
        pixels.show()
def U(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+24)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 23)] = (color)
        pixels.show()
    else:
        for i in range(1, 7):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 24)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels.show()
def V(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 6):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+32)] = (color)
        pixels[(quad + 9)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 25)] = (color)
        pixels.show()
    else:
        for i in range(1, 6):
            pixels[(i+quad + 1)] = (color)
            pixels[(i + quad + 33)] = (color)
        pixels[(quad + 14)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 30)] = (color)
        pixels.show()
def W(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(1, 8):
            pixels[(i+quad)] = (color)
            pixels[(i + quad + 32)] = (color)
        pixels[(quad + 10)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 26)] = (color)
        pixels.show()
    else:
        for i in range(0, 7):
            pixels[(i+quad)] = (color)
            pixels[(i+quad+32)] = (color)
        pixels[(quad + 13)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 29)] = (color)
        pixels.show()
def X(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        pixels[(quad + 1)] = (color)
        pixels[(quad + 2)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 7)] = (color)
        pixels[(quad + 10)] = (color)
        pixels[(quad + 12)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 26)] = (color)
        pixels[(quad + 28)] = (color)
        pixels[(quad + 33)] = (color)
        pixels[(quad + 34)] = (color)
        pixels[(quad + 38)] = (color)
        pixels[(quad + 39)] = (color)
        pixels.show()
    else:
        pixels[(quad)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 5)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 11)] = (color)
        pixels[(quad + 13)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 27)] = (color)
        pixels[(quad + 29)] = (color)
        pixels[(quad + 32)] = (color)
        pixels[(quad + 33)] = (color)
        pixels[(quad + 37)] = (color)
        pixels[(quad + 38)] = (color)
        pixels.show()
def Y(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        for i in range(0, 5):
            pixels[(quad + i + 19)] = (color)
        pixels[(quad)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 13)] = (color)
        pixels[(quad + 29)] = (color)
        pixels[(quad + 32)] = (color)
        pixels[(quad + 33)] = (color)
        pixels.show()
    else:
        for i in range(0, 5):
            pixels[(quad + i + 16)] = (color)
        pixels[(quad + 26)] = (color)
        pixels[(quad) + 6] = (color)
        pixels[(quad) + 7] = (color)
        pixels[(quad) + 10] = (color)
        pixels[(quad + 38)] = (color)
        pixels[(quad + 39)] = (color)
        pixels.show()
def Z(quad, color):
    if(quad == 0 or quad == 80 or quad == 160 or quad == 240):
        pixels[(quad + 2)] = (color)
        pixels[(quad + 6)] = (color)
        pixels[(quad + 7)] = (color)
        pixels[(quad + 8)] = (color)
        pixels[(quad + 10)] = (color)
        pixels[(quad + 13)] = (color)
        pixels[(quad + 18)] = (color)
        pixels[(quad + 20)] = (color)
        pixels[(quad + 23)] = (color)
        pixels[(quad + 24)] = (color)
        pixels[(quad + 28)] = (color)
        pixels[(quad + 29)] = (color)
        pixels.show()
    else:
        pixels[(quad)] = (color)
        pixels[(quad + 1)] = (color)
        pixels[(quad + 5)] = (color)
        pixels[(quad + 10)] = (color)
        pixels[(quad + 13)] = (color)
        pixels[(quad + 15)] = (color)
        pixels[(quad + 16)] = (color)
        pixels[(quad + 19)] = (color)
        pixels[(quad + 21)] = (color)
        pixels[(quad + 26)] = (color)
        pixels[(quad + 27)] = (color)
        pixels[(quad + 31)] = (color)
        pixels.show() 
#MAIN



A(quad0, RED)
B(quad1, BLUE)
C(quad2, GREEN)
D(quad3, YELLOW)
E(quad4, TEAL)
F(quad5, ORANGE)
G(quad6, PURPLE)
H(quad7, WHITE)



    
