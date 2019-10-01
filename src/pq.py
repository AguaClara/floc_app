import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):

    def __init__(self):
        super().__init__()

        button = QPushButton('Open File', self)
        button.clicked.connect(self.handleOpen)

        self.title = 'Image Viewer'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.show()

    def handleOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "", "All Files (*)", options=options)
        if fileName:
            hbox = QHBoxLayout(self)
            pixmap = QPixmap("IMG_9870.jpeg")
            pixmap_resized = pixmap.scaled(400, 600)
            lbl = QLabel(self)
            lbl.setPixmap(pixmap_resized)
            hbox.addWidget(lbl)
            self.setLayout(hbox)
            self.setWindowTitle('hello')

            self.show()

    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)

    # def saveFileDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
