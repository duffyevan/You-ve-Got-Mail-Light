import imaplib, time, RPi.GPIO as g
led = 22 #aka gpio 25, list can be found in pop.py

M = imaplib.IMAP4_SSL("exchange.whatever.com")
M.login("your username","your password")
M.select('INBOX')
g.setup(22, g.OUT)
while True:
    urm = M.search(None, '(UNSEEN)')[1][0]
    #print urm #debug code
    if urm == '':
        #print "Read All Mail" #Debug Code
        g.output(22, False)
    else:
        #print "Unread Mail" #Debug code
        g.output(22, True)
    time.sleep(2)
M.quit()
