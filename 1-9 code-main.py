from microbit import *

hungryness = 0

while True:
    if button_a.was_pressed():
        hungryness = hungryness + 1
        display.show(hungryness)
    if button_b.was_pressed():
        hungryness = 0
        display.show(hungryness)