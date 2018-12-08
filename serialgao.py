import time
import serial


class Andrewino:
    def __init__(self):
        self.s = serial.Serial('/dev/ttyACM2')
        self.unlock()

    def set_idle(self):
        self.s.write(b'idle')

    def lock(self):
        self.s.write(b'lock')

    def unlock(self):
        self.s.write(b'unlock')
        
    def status(self):
        self.s.write(b'status')

