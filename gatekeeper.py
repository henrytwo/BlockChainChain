import os
import keychain
import dataparsing
from console import *

user = "henrytwo"

locked = True

def main():
    MenuFormatter.splash()
    keychain.load_key()

    if keychain.check_key():

        primed = False

        while True:

            if primed:
                Console.clear()
            else:
                primed = True

            Console.print('System State: %s' % 'LOCKED' if locked else 'UNLOCKED', Colors.WHITE)


            choice = MenuFormatter.option_list(['Lock' if not locked else 'Unlock',
                                       'View Log',
                                       'Clear Log',
                                       'Train',
                                       'Exit'])

            if choice == 1:
                pass
            elif choice == 2:
                dataparsing.print_log()
                Prompts.cn_prompt()
            elif choice == 3:
                state = Prompts.yn_prompt('Are you sure you want to clear system logs?', 'n')

                if state == 'y':
                    dataparsing.clear_log()

                    Console.clear()
                    Console.print('Logs cleared!')
                    Prompts.cn_prompt()
            elif choice == 4:
                os.system('sl')
            elif choice == 5:
                Console.print('Goodbye.', Colors.BLUE)
                break
            else:
                Console.print('Out of range.', Colors.RED)


    else:
        Console.print(
            '\nAccess denied! This key has been revoked.\nContact the owner securely over keybase for further instructions. (@%s)' % user,
            Colors.RED_BOLD)

if __name__ == '__main__':
    main()

# hello
