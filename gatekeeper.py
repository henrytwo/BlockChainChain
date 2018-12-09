import os
import glob
import keychain
import threading
import time
from console import *

user = "henrytwo"


def main():
    MenuFormatter.splash()
    keychain.load_key()

    if keychain.check_key():
        Console.print('wooo u auth', Colors.YELLOW)
    else:
        Console.print(
            '\nAccess denied! This key has been revoked.\nContact the owner securely over keybase for further instructions. (@%s)' % user,
            Colors.RED_BOLD)

if __name__ == '__main__':
    main()

# hello
