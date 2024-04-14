"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is on the right side of the wall,facing East
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is on the upper left of the wall
    """
    turn_left()
    # Facing North
    while not right_is_clear():
        move()
    # Facing East


def cross():
    """
    pre-condition:Karel is on the upper left of the wall
    post-condition:Karel is on the upper right of the wall
    """
    turn_right()
    # Facing East
    move()
    while not right_is_clear():
        move()
    turn_right()
    # Facing South


def down():
    """
    pre-condition:Karel is on the upper right of the wall
    poat-condition:Karel is on the right side of the wall,facing East
    """
    # Facing South
    while front_is_clear():
        move()
    turn_left()
    # Facing East


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
