import os
import glob
import keyrunner
import threading
import time
from console import *

user = "henrytwo"

def main():
    Console.splash()
    load_key()

    if keyrunner.check_key():
        Console.print('wooo u auth', Colors.YELLOW)
    else:
        Console.print('\nAccess denied. Key has been revoked.', Colors.RED_BOLD)


def load_key():

    old_time = time.time()

    Console.print('\nRetrieving keys...')

    keys = glob.glob("/keybase/public/" + user + "/*.key")
    current_keys = set(keyrunner.list_keys())
    new_keys = set()

    Console.print('Loading keys...')

    for key in keys:
        key = open(key).read()
        new_keys.add(key)

        if key not in current_keys:
            keyrunner.add_key(key)

    for k in current_keys - new_keys:
        keyrunner.revoke_key(k)

    print('Keys updated!\n\nCompleted update in %5.5f seconds\n' % (time.time() - old_time))



if __name__ == '__main__':
    main()


#hello
