import os
import glob
import keyrunner
from console import *


def main():
    with open('splash', 'r') as f:
        Console.print(f.read(), Colors.PURPLE_BOLD_BRIGHT)


def load_key(user):
    keys = glob.glob("/keybase/public/"+user)

    for key in keys:
        key = open(key).read()

        print (key)

if __name__ == '__main__':
    main()
#hello
