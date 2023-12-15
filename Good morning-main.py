# Imports go at the top
from microbit import *
#_________ = _________
#variable  = value (expression)

answer = 42
hello_message = "Hi There"
display.scroll(hello_message)

# Code in a 'while True:' loop repeats forever
while True:
    display.scroll('Good')
    sleep(1000)
    display.scroll('Morning')
