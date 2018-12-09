import os
import keychain
import dataparsing
import serialgao
import sha256frompubkey
from console import *

user = "henrytwo"

locked = True
andrew = serialgao.Andrewino('/dev/ttyACM2')


def main():
    global locked

    MenuFormatter.splash()
    keychain.load_key()

    key = keychain.check_key()

    if key:

        primed = False

        while True:

            if primed:
                Console.clear()
            else:
                primed = True

            Console.print('System State: %s' % ('LOCKED' if locked else 'UNLOCKED'), Colors.WHITE)

            choice = MenuFormatter.option_list(['Lock' if not locked else 'Unlock',
                                                'View Log',
                                                'Clear Log',
                                                'Train',
                                                'Exit'])

            if choice == 1:

                state = Prompts.yn_prompt(
                    'Are you sure you want to %s the chain?' % ('LOCK' if not locked else 'UNLOCK'), 'n')

                if state == 'y':
                    if andrew.status():
                        andrew.unlock(sha256frompubkey.sha256_fingerprint_from_pub_key(key[0][0]))
                    else:
                        andrew.lock(sha256frompubkey.sha256_fingerprint_from_pub_key(key[0][0]))

                    Console.print('Chain has been %s' % 'LOCKED' if not locked else 'UNLOCKED', Colors.PURPLE_BOLD_BRIGHT)
                    Prompts.cn_prompt()

                locked = andrew.status()

            elif choice == 2:
                dataparsing.print_log()
                Prompts.cn_prompt()
            elif choice == 3:
                state = Prompts.yn_prompt('Are you sure you want to clear system logs?', 'n')

                if state == 'y':
                    dataparsing.clear_log()

                    Console.clear()
                    Console.print('Logs cleared!', Colors.GREEN_BOLD_BRIGHT)
                    Prompts.cn_prompt()
            elif choice == 4:
                os.system('sl')
            elif choice == 5:
                Console.print('Goodbye.', Colors.BLUE_BOLD)
                break
            else:
                Console.print('Out of range.', Colors.RED_BOLD)


    else:
        Console.print(
            '\nAccess denied! This key has been revoked.\nContact the owner securely over keybase for further instructions. (@%s)' % user,
            Colors.RED_BOLD)


if __name__ == '__main__':
    main()

# hello
