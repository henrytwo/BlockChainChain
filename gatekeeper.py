import os
import glob
import keyrunner
from console import *
import threading


def main():
    t = threading.Thread(target=load_key)
    t.start()

    with open('splash', 'r') as f:
        Console.print(f.read(), Colors.PURPLE_BOLD_BRIGHT)


def load_key():
    global waiting

    keys = glob.glob("/keybase/public/"+user + "/*.key")
    current_keys = set(keyrunner.list_keys())
    new_keys = set()

    for key in keys:
        key = open(key).read()
        new_keys.add(key)

        if key not in current_keys:
            keyrunner.add_key(key)

    for k in current_keys - new_keys:
        keyrunner.revoke_key(k)

    waiting = False

if __name__ == '__main__':
    main()

    waiting = True
    user = "henrytwo"
#hello
