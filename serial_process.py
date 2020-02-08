import serial
import time


class SerialProcess(object):

    def __init__(self):
        super().__init__()
        self.ser = serial.Serial("COM4", 921600)
        self.receive = ''

    def open_serial(self):
        pass

    def write_data(self, wd):
        self.ser.write(wd)

    def receive_data(self):
        temp = self.ser.read_until()

        if temp:
            self.receive = temp.decode('utf-8')
            return self.receive
        else:
            return ''


if __name__ == '__main__':
    ser = SerialProcess()
    count = 500
    time.sleep(1)
    while count > 0:
        data = ser.receive_data()
        if data:
            print(data)
            count -= 1
