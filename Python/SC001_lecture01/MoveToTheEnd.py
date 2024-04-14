"""
File: MoveToTheEnd.py
Name: TODO:
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    repeat()


def repeat():
    turn_left()
    while front_is_clear():
        move()
        put_beeper()
    repeat()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
