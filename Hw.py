import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.IN)
while True:
       key=input("Type to control. WASD is what we'll use.")
       i=GPIO.input(27)
       if i==1:                 
             GPIO.output(27, GPIO.LOW)
             GPIO.output(18, GPIO.LOW)
             GPIO.output(16, GPIO.LOW)
             GPIO.output(13, GPIO.LOW)
             GPIO.output(11, GPIO.LOW
       elif key == "w":                  #forward
            GPIO.output(11, GPIO.HIGH)
            sleep(1)
            GPIO.output(11, GPIO.LOW)
       elif key == "s":                #reverse
            GPIO.output(13, GPIO.HIGH)
            sleep(1)
            GPIO.output(13, GPIO.LOW)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            elif key == "a":                #steers left
            GPIO.output(16, GPIO.HIGH)
            sleep(1)
            GPIO.output(16, GPIO.LOW)
       elif key == "d":                #steers right
            GPIO.output(18, GPIO.HIGH)
            sleep(1)
            GPIO.output(18, GPIO.LOW)
       elif key == "z":                #quits the program
            GPIO.cleanup()
            print("Motors on safe, exiting.")
            sleep(1)import RPi.GPIO as GPI