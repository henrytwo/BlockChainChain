import keychain
import time

while True:
    try:
        keychain.load_key(True)
    except:
        pass

    time.sleep(5)
