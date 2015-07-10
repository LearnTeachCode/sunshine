'''
Created on Jul 9, 2015

@author: Hung
'''

import pygame
import sys

def main():
    pygame.init()
    runProgram = True

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()

    # COLOR LIST
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)
    
    # Code to create the initial window
    screen_w = 1080
    screen_h = 900
    window_size = (screen_w, screen_h)
    SCREEN = pygame.display.set_mode(window_size)

    # set the title of the window
    pygame.display.set_caption("Hello Politicians")
    
    display_event = "prompt"

    while runProgram:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == quit:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()
        if display_event == "prompt":
            display_event = displayPrompt()
        elif display_event == "names":
            display_event = displayNames()
        elif display_event == "lsa":
            display_event = displayLSA()
        elif display_event == "messages":
            display_event = displayMessages()
        elif display_event == "goodbye":
            display_event = displayGoodbye()
        else: runProgram = False
        
def displayPrompt():
    print "Executing displayPrompt"
    
def displayNames():
    print "Executing displayNames"
    
def displayLSA():
    print "Executing displayLSA"

def displayMessages():
    print "Executing displayMessages"

def displayGoodbye():
    print "Executing displayGoodbye"

