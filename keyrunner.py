import os
import sys

def list_keys():

    valid_keys = []
    with open('../.ssh/authorized_keys', 'r') as file:
        keys = file.read().strip().split('\n')

        for i in range(len(keys)):
            key = keys[i]

            if len(key.split()) == 4:
                valid_keys.append(key.split()[3])


    return valid_keys

def key_exists(k):
    with open('../.ssh/authorized_keys', 'r') as file:
        keys = file.read().strip().split('\n')

        for i in range(len(keys)):
            key = keys[i]

            if len(key.split()) == 4 and k in key.split()[3]:
                return [keys, i]
        else:
            return False

def add_key(key):
    if not key_exists(key):
        os.system('echo \'command="python3 BlockChainChain/gatekeeper.py $SSH_ORIGINAL_COMMAND",no-port-forwarding,no-x11-forwarding,no-agent-forwarding %s\' >> ../.ssh/authorized_keys' % key)
        return True
    else:
        return False

def revoke_key(key):

    k = key_exists(key)

    if k:
        del k[0][k[1]]

        with open('../.ssh/authorized_keys', 'w') as file:
            file.write('\n'.join(k[0]))

        return True
    else:
        return False

if __name__ == '__main__':


    commands = sys.argv

    try:
        if commands[1] == 'add':
            print(add_key(commands[2]))
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
