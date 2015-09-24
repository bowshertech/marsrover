from raspirobotboard import *

import sys
import pygame

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

def forward():
    rr.set_led1(1)
    rr.set_led2(1)
    rr.forward()


def reverse():
    rr.set_led1(0)
    rr.set_led2(0)
    rr.reverse()


def left():
    rr.set_led1(0)
    rr.set_led2(1)
    rr.left()


def right():
    rr.set_led1(1)
    rr.set_led2(0)
    rr.right()

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    forward()
                elif event.key == pygame.K_DOWN:
                    reverse()
                elif event.key == pygame.K_RIGHT:
                    right()
                elif event.key == pygame.K_LEFT:
                    left()
                elif event.key == pygame.K_SPACE:
                    rr.stop()
                    rr.set_led1(False)
                    rr.set_led2(False)

    except KeyboardInterrupt:
        print("Control C Received!")
        rr.stop()
        sys.exit(1)
