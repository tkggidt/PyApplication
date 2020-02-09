
import threading
import time

threadLock = threading.Lock()


class DataProcess(threading.Thread):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.current_cache = []
        self.angle_cache = []
        self.count = 0

    def run(self):
        current_data = []
        angle_data = []
        while True:
            temp_str = self.ser.receive_data()
            if temp_str:
                self.count += 1
                if temp_str[0] == 'C':
                    value = int(temp_str[1:5])
                    current_data.append(value)
                    if len(current_data) == 500:
                        temp_list = current_data.copy()
                        threadLock.acquire()
                        self.current_cache.append(temp_list)
                        if len(self.current_cache) == 3:
                            self.current_cache.pop(0)
                        threadLock.release()
                        current_data.clear()
                        print(self.current_cache)
                elif temp_str[0] == 'A':
                    value = int(temp_str[1:5])
                    angle_data.append(value)
                    if len(angle_data) == 500:
                        temp_list = angle_data.copy()
                        threadLock.acquire()
                        self.angle_cache.append(temp_list)
                        if len(self.angle_cache) == 3:
                            self.angle_cache.pop(0)
                        threadLock.release()
                        angle_data.clear()


class DataProcess2(threading.Thread):
    def __init__(self, ser, ui):
        super().__init__()
        self.ser = ser
        self.ui = ui
        self.string = ''
        self.count = 0

    def run(self):
        while True:
            temp_str = self.ser.receive_data()
            if temp_str:
                self.string += temp_str
                self.count += 1
                if self.count == 20:
                    self.count = 0
                    self.ui.textEdit.append(temp_str)
                    self.string = ""




class CentralProcess:

    def __init__(self, ui, ser):
        super().__init__()
        self.ui = ui
        self.ser = ser
        self.ui.pushButton.clicked.connect(self.test_function)
        self.ui.textEdit.append("Can you see it")


    def test_function(self):
        count = 10
        display = ''
        while count > 0:
            data = self.ser.receive_data()
            if data:
                display += data
                count -= 1
        self.ui.textEdit.append(display)



if __name__ == "__main__":
    from serial_process import SerialProcess

    sp = SerialProcess()
    p1 = DataProcess(sp)
    p1.start()
    p1.join()
