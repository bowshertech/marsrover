from raspirobotboard import *
import sys

rr = RaspiRobot()


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


while True:
    try:
        forward(2)
        left(3)
        right(3)
        reverse(3)
    except KeyboardInterrupt:
        print("Control C Received!")
        rr.stop()
        sys.exit(1)
