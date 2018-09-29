import sys
from PyQt5.QtWidgets import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'File Dialog'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 640
        button = QPushButton('click')
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        self.show()

    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec_()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
