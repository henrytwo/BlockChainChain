import os
from console import *


def main():
    with open('splash', 'r') as f:
        Console.print(f.read(), Colors.PURPLE_BOLD_BRIGHT)


if __name__ == '__main__':
    main()
