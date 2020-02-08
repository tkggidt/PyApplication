
class CentralProcess(object):

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

