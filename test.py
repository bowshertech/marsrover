from raspirobotboard import *
from pygame import *

import sys

rr = RaspiRobot()

GPIO.setwarnings(False)


def forward(seconds):
    rr.set_led1(1)
    rr.set_led2(1)
    rr.forward(seconds)


def reverse(seconds):
    rr.set_led1(0)
    rr.set_led2(0)
    rr.reverse(seconds)


def left(seconds):
    rr.set_led1(1)
    rr.set_led2(0)
    rr.left(seconds)


def right(seconds):
    rr.set_led1(0)
    rr.set_led2(1)
    rr.right(seconds)

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    rr.forward()
                    rr.set_led1(True)
                    rr.set_led2(True)
                elif event.key == K_DOWN:
                    rr.set_led1(True)
                    rr.set_led2(True)
                    rr.reverse()
                elif event.key == K_RIGHT:
                    rr.set_led1(False)
                    rr.set_led2(True)
                    rr.right()
                elif event.key == K_LEFT:
                    rr.set_led1(True)
                    rr.set_led2(False)
                    rr.left()
                elif event.key == K_SPACE:
                    rr.stop()
                    rr.set_led1(False)
                    rr.set_led2(False)

    except KeyboardInterrupt:
        print("Control C Received!")
        rr.stop()
        sys.exit(1)
