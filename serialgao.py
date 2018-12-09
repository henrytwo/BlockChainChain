import time
import serial
import dataparsing
import traceback

serial_disabled = False
locked = True


class Andrewino:
    def __init__(self, id):

        global serial_disabled

        try:
            self.s = serial.Serial(id)
        except:
            self.s = None
            serial_disabled = True
            # traceback.print_exc()
            print('Serial disabled.')

    def lock(self, key):
        global locked

        dataparsing.log(key, 'LOCK')

        if not serial_disabled:
            self.s.write(b'lock')
        else:
            locked = True
            #print('LOCK! (SERIAL OFFLINE)')

    def unlock(self, key):
        global locked

        dataparsing.log(key, 'UNLOCK')

        if not serial_disabled:
            self.s.write(b'unlock')
        else:
            locked = False
            #print('LOCK! (SERIAL OFFLINE)')

    def status(self):
        global locked

        if not serial_disabled:
            # Is it locked?
            self.s.write(b'status')

            return self.s.readline().decode().strip() == 'true'
        else:
            #print('STATUS! (SERIAL OFFLINE)')
            return locked
