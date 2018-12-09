import os
import sys
from console import *
import bcc_main
import time
import glob
import traceback
import dataparsing
import sha256frompubkey
from os.path import expanduser

home = expanduser("~")


def check_key():
    with open('/var/log/auth.log') as file:
        log = file.read().strip().split('\n')[::-1]

        for line in log:
            if 'RSA SHA256' in line:
                raw_key = line.split()[-1]

                Console.print('SHA256 FINGERPRINT: %s' % raw_key, Colors.RED_BOLD)

                authorized = key_exists(raw_key)

                break

        if authorized:
            dataparsing.log(raw_key, 'LOGIN')
        else:
            dataparsing.log(raw_key, 'KICK')

        return authorized


def list_keys():
    valid_keys = []
    with open(home + '/.ssh/authorized_keys', 'r') as file:
        keys = file.read().strip().split('\n')

        for i in range(len(keys)):
            key = keys[i]

            if len(key.split()) == 6:
                valid_keys.append(' '.join(key.split()[3:]))

    return valid_keys


def key_exists(k):
    keys = list_keys()

    for i in range(len(keys)):
        key = keys[i]

        try:
            reference_key = sha256frompubkey.sha256_fingerprint_from_pub_key(key)

            if 'ssh-rsa' in k:
                k = sha256frompubkey.sha256_fingerprint_from_pub_key(k)

            if k == reference_key:
                return [keys, i]
        except:
            traceback.print_exc()
    else:
        return False


def add_key(key):
    if not key_exists(key):
        dataparsing.log(sha256frompubkey.sha256_fingerprint_from_pub_key(key), 'ADD-KEY')
        os.system(
            'echo \'command="python3 BlockChainChain/bcc_main.py $SSH_ORIGINAL_COMMAND",no-port-forwarding,no-x11-forwarding,no-agent-forwarding %s\' >> %s/.ssh/authorized_keys' % (
            key, home))
        return True
    else:
        return False


def revoke_key(key):
    k = key_exists(key)

    if k:
        del k[0][k[1]]

        dataparsing.log(sha256frompubkey.sha256_fingerprint_from_pub_key(key), 'REVOKE-KEY')
        with open(home + '/.ssh/authorized_keys', 'w') as file:
            file.write('\n'.join(k[0]))

        return True
    else:
        return False


def load_key(persist=False):
    old_time = time.time()

    Console.print('\nRetrieving keys...\n', Colors.BLACK_BOLD)

    keys = glob.glob("/keybase/public/" + bcc_main.user + "/gatekeeper/*")
    current_keys = set(list_keys())
    new_keys = set()

    Console.print('Loading keys...', Colors.BLUE_BOLD)
    Console.print('%i key(s) loaded.\n' % len(keys), Colors.CYAN_BOLD)

    for key in keys:
        key = open(key).read().strip()

        new_keys.add(key)

        if key not in current_keys:
            Console.print('[+] ' + sha256frompubkey.sha256_fingerprint_from_pub_key(key), Colors.GREEN_BOLD)
            add_key(key)

    # So revokes are verbose
    if not persist:
        for r in current_keys - new_keys:
            Console.print('[-] ' + sha256frompubkey.sha256_fingerprint_from_pub_key(r), Colors.RED)
            revoke_key(r)

    Console.print('Keys updated!\n\nCompleted update in %5.5f seconds\n' % (time.time() - old_time), Colors.BOLD)


if __name__ == '__main__':

    commands = sys.argv

    try:
        if commands[1] == 'add':
            print(add_key(' '.join(commands[2:])))
        elif commands[1] == 'revoke':
            print(revoke_key(commands[2]))
        elif commands[1] == 'list':
            print(list_keys())
        elif commands[1] == 'check':
            print(key_exists(commands[2]))
        else:
            print('Invalid arguments!')

    except:
        print('Something went wrong.')
        traceback.print_exc()
