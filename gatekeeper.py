import os
import glob
import keyrunner

splash = open('splash').read()

print(splash)

def clear():
    os.system('clear')

def load_key(user):
    keys = glob.glob("/keybase/public/"+user)

    for key in keys:
        key = open(key).read()

        print (key)

