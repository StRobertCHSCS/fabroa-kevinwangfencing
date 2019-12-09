from microbit import*

while True:
    if accelerometer.was_gesture ('shake'):
        display.scoll(temperture())