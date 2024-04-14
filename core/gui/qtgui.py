import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Title
        self.setWindowTitle("Logan's Chop Shop")
        
        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        test = qtw.QLabel("Test")
        self.layout().addWidget(test) 

        
        self.show()
        


def run():
    app = qtw.QApplication([])
    mw = MainWindow()

    app.exec_()