from raspirobotboard import *

import sys
import pygame

rr = RaspiRobot()

pygame.init()
pygame.joystick.init()

screen = pygame.display.set_mode((640, 480))

controller = pygame.joystick.Joystick(0)
controller.init()

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

state = None
blink_state = 1
timer = 0


CONTROLLER_PAD_UP = 4
CONTROLLER_PAD_RIGHT = 5
CONTROLLER_PAD_DOWN = 6
CONTROLLER_PAD_LEFT = 7
CONTROLLER_PAD_STOP= 14
CONTROLLER_TRIGGER_UP= 9
CONTROLLER_TRIGGER_DOWN= 8
CONTROLLER_PAD_STOP= 13


def reverse():
    global state
    state = "reverse"
    rr.set_led1(1)
    rr.set_led2(1)
    rr.forward()


def forward():
    global state
    state = "forward"
    rr.set_led1(1)
    rr.set_led2(1)
    rr.reverse()


def right():
    global state
    state = "right"
    rr.set_led1(1)
    rr.set_led2(0)
    rr.left()


def left():
    global state
    state = "left"
    rr.set_led1(0)
    rr.set_led2(1)
    rr.right()


def stop():
    global state
    state = "stopped"
    rr.stop()
    rr.set_led1(0)
    rr.set_led2(0)


def blinkleds():
    global blink_state
    blink_state = not blink_state
    rr.set_led1(blink_state)
    rr.set_led2(blink_state)


def execute_state():
    global timer
    timer += 1

    if state == "reverse":
        if timer % 1000 == 0:
            blinkleds()

        if timer > 10000:
            timer = 0

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
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
                    stop()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == CONTROLLER_PAD_UP:
                    forward()
                if event.button == CONTROLLER_PAD_DOWN:
                    reverse()
                if event.button == CONTROLLER_PAD_LEFT:
                    left()
                if event.button == CONTROLLER_PAD_RIGHT:
                    right()
                if event.button == CONTROLLER_PAD_STOP:
                    stop()
                if event.button == CONTROLLER_TRIGGER_UP:
                    forward()
                if event.button == CONTROLLER_TRIGGER_DOWN:
                    reverse()







        execute_state()

    except KeyboardInterrupt:
        print("Control C Received!")
        rr.stop()
        sys.exit(1)
