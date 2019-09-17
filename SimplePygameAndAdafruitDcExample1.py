# keyboard1.py  Illustrate Keyboard input in PyGame
# P. Conrad for CS5nm, 11/02/08

"""Simple test for using adafruit_motorkit with a DC motor"""

from adafruit_motorkit import MotorKit
import pygame
import sys


####################################
# Functions to handle game events
####################################


def handleQuitEvent(event):
   print ("Have a good day")
   pygame.quit(); sys.exit()

def handleKeyDownEvent(event):
    if event.key == pygame.K_DOWN:
        handleDownKeyPressed(event)
    elif event.key == pygame.K_RIGHT:
        handleRightKeyPressed(event)
    elif event.key == pygame.K_LEFT:
        handleLeftKeyPressed(event)
    elif event.key == pygame.K_UP:
        handleUpKeyPressed(event)
    elif event.key == pygame.K_a:
        handleaKeyPressed(event)
    elif event.key == pygame.K_s:
        handlesKeyPressed(event)
def handleKeyUpEvent(event):
    if event.key == pygame.K_DOWN:
        handleDownKeyReleased(event)
    elif event.key == pygame.K_RIGHT:
        handleRightKeyReleased(event)
    elif event.key == pygame.K_LEFT:
        handleLeftKeyReleased(event)
    elif event.key == pygame.K_UP:
        handleUpKeyReleased(event)

def handleDownKeyPressed(event):
    print ("...led on")
    #GPIO.output(LedPin, GPIO.LOW)  # led on    
    #sshpass -p 'raspberry' ssh pi@192.168.1.58 python3 /home/pi/Desktop/led1.py
    
def handleDownKeyReleased(event):
    print ("Yo, you pressed the up key")
    
def handleUpKeyPressed(event):
    print ("Yo, you pressed the up key")
    kit.motor1.throttle = 0.5
def handleUpKeyReleased(event):
    print ("You released the up key")
    kit.motor1.throttle = 0.1
def handleLeftKeyPressed(event):
    print ("Yo, you pressed the left key")

def handleLeftKeyReleased(event):
    print ("You released the left key")

def handleRightKeyPressed(event):
    print ("Yo, you pressed the right key")

def handleRightKeyReleased(event):
    print ("You released the right key")

def handleaKeyPressed(event):
    print ("Yo, you pressed the a key")
    kit.motor1.throttle = 0.1
def handlesKeyPressed(event):
    print ("You released the s key")
    kit.motor1.throttle = 0
# Set up two colors using RGB tuples

white = (255,255,255)
black = (0,0,0)
kit = MotorKit()

pygame.init() # Start up the Pygame software
screen = pygame.display.set_mode((640,480))  # Make screen be 640 x 480

##############################################################
# Draw the next frame.    The frame is drawn, but is NOT yet
# shown on the screen until we get to pygame.display.update()
##############################################################

# paint the whole screen white, 
# then draw a line from position 10,20 to position 30,40 of thickness 5

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            handleQuitEvent(event)
        elif event.type == pygame.KEYDOWN:
            handleKeyDownEvent(event)
        elif event.type == pygame.KEYUP:
            handleKeyUpEvent(event)

    #############################################################
    # Now show the next frame
    #############################################################
        
    screen.fill(white)
    pygame.draw.line(screen,black,(10,20),(30,40),5)

    #############################################################
    # Now show the next frame
    #############################################################

    pygame.display.update()

    # That's all!

