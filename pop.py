import poplib
import RPi.GPIO as GPIO
import time
host = "exchange.whatever.com" #your pop3 server hostname
uname = "your username"
password = "your password"
led = 13 #found this number from the website listed below (This is really BCM 21)

GPIO.setup(led, GPIO.OUT) #Set the direction of the pin for the led
msgcount = 0 #initialize this variable
while True: #run this loop forever
    prevcount = msgcount #set the previous number of emails from the last check
    pop = poplib.POP3_SSL(host) #connect
    pop.user(uname) #sign in with my credentials
    pop.pass_(password)
    msgcount = pop.stat()[0] #get the number of messages at this check
    #print msgcount #old debug code
    if msgcount > prevcount: #if theres been a recent increase in the number of emails...
        #print "YOU'VE GOT MAIL!!" #old debug code
        GPIO.output(led, 1) #play the animation on the LED (BCD Pin 21 B+) (find the layouts at the bottom of this page for RPi.GPIO: http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi/217-getting-started-with-raspberry-pi-gpio-and-python)
        time.sleep(0.25)
        GPIO.output(led, 0)
        time.sleep(0.25)
        GPIO.output(led, 1)
        time.sleep(0.25)
        GPIO.output(led, 0)
        time.sleep(0.25)
        GPIO.output(led, 1)
        time.sleep(0.25)
        GPIO.output(led, 0)
        time.sleep(0.25)
        GPIO.output(led, 1)
        time.sleep(0.25)
        GPIO.output(led, 0)
        time.sleep(0.25)

    time.sleep(2)

pop.quit()