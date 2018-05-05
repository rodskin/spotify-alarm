from gpiozero import LED, Button
from signal import pause
import time

led = LED(25)
button = Button(23, False)

button.when_pressed = led.on
button.when_released = led.off

def buttonPressed ():
    print('Pressed')
    start = time.time()
    time.sleep(0.2)
    while button.is_pressed:
        time.sleep(0.01)
        if ((time.time() - start) > 3 ) :
            print("Long Press > 3")
            
    length = time.time() - start

    if length <= 3:
        print("Short Press")

#button.when_pressed = buttonPressed

pause()