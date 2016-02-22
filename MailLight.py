import poplib, imaplib
import RPi.GPIO as GPIO
import time
host = "exchange.whatever.com"
uname = "your uname"
password = "your password"
newled = 13 #flashes when new mail comes in, found these numbers from the website listed below (This is really BCM 21)
unreadled = 22; #lit if theres unread mail


M = imaplib.IMAP4_SSL(host)
M.login(uname,password)
M.select('INBOX')
GPIO.setup(unreadled, GPIO.OUT)
GPIO.setup(newled, GPIO.OUT) #Set the direction of the pin for the newled
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
        GPIO.output(newled, 1) #play the animation on the newLED (BCD Pin 21 B+) (find the layouts at the bottom of this page for RPi.GPIO: http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi/217-getting-started-with-raspberry-pi-gpio-and-python)
        time.sleep(0.25)
        GPIO.output(newled, 0)
        time.sleep(0.25)
        GPIO.output(newled, 1)
        time.sleep(0.25)
        GPIO.output(newled, 0)
        time.sleep(0.25)
        GPIO.output(newled, 1)
        time.sleep(0.25)
        GPIO.output(newled, 0)
        time.sleep(0.25)
        GPIO.output(newled, 1)
        time.sleep(0.25)
        GPIO.output(newled, 0)
        time.sleep(0.25)
    urm = M.search(None, '(UNSEEN)')[1][0]
    if urm == '':
        GPIO.output(unreadled, False)
    else:
        GPIO.output(unreadled, True)
    time.sleep(2)

pop.quit()