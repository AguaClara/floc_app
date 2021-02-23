from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtSql
#
import sys
import os
import sys
import cv2
import time
import sqlite3
import count_and_size
import database2

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

print(cv2.__version__)

database = r"sqlitedbpythonsqlite.db"
class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, data = np.empty(shape=(1,2))):
        ax = self.figure.add_subplot(111)
        ax.plot(data[:,0],data[:,1], 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Floc App")
        self.initUI()

        self.timer = QTimer(self)
        # timer.timeout.connect(self.take_photo)
        # timer.start(5000)
        # timer.start()
        width = self.width()
        height = self.height()
        self.setGeometry(10, 10, 900, 500)

        self.show()
        # database = r"C:sqlitedbpythonsqlite.db"
        # database = r"databse.db"

        sql_create_floc_table = """ CREATE TABLE IF NOT EXISTS flocs (
                                            id integer PRIMARY KEY,
                                            size integer NOT NULL
                                        ); """

        # create a database connection
        conn = database2.create_connection(database)
        conn.commit()

        # create tables
        if conn is not None:
            # create projects table
            database2.create_table(conn, sql_create_floc_table)

        else:
            print("Error! cannot create the database connection.")

    def initUI(self):
        self.init_menuBar()
        self.init_statusBar()
        self.init_camera()
        self.init_cameraBar()
        self.init_filterSideBar()
        self.show()
        # new widget for plots 
        # self.init_plot()

    def init_menuBar(self):
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        toolMenu = mainMenu.addMenu('Tools')

        self.init_fileMenu(fileMenu)
        self.init_viewMenu(viewMenu)
        self.init_toolMenu(toolMenu)

    def init_statusBar(self):
        self.status = QStatusBar()
        self.setStatusBar(self.status)

    def init_camera(self):
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            pass
        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder)
        self.select_camera(0)

    # def init_plot(self):


# Initialize Camera bar
    def init_cameraBar(self):
        camera_toolbar = QToolBar("Camera")
        camera_toolbar.setIconSize(QSize(45, 45))
        camera_toolbar.setMovable(False)
        self.addToolBar(Qt.BottomToolBarArea, camera_toolbar)

        def find_data_file(filename):
            if getattr(sys, 'frozen', False):
                # The application is frozen
                datadir = os.path.dirname(sys.executable)
            else:
                # The application is not frozen
                # Change this bit to match where you store your data files:
                # datadir = os.path.dirname('images')
                datadir = ''
            return os.path.join(datadir, 'images', filename)

        def init_cameraActionButton():
            self.save_path = ""
            photoAction = QAction(
                QIcon(find_data_file('camera-black.png')), "Take photo...", self)
            photoAction.setStatusTip("Take photo of current view")
            photoAction.triggered.connect(self.start_photo)
            camera_toolbar.addAction(photoAction)

        def init_camera_stop_button():
            photoAction = QAction(
                QIcon(find_data_file('end_s.png')), "Take photo...", self)
            photoAction.setStatusTip("pause")
            photoAction.triggered.connect(self.stop_photo)
            camera_toolbar.addAction(photoAction)

        def init_changeFolderButton():
            change_folder_action = QAction(QIcon(find_data_file('blue-folder-horizontal-open.png')), "Change save location...", self)
            change_folder_action.setStatusTip(
                "Change folder where photos are saved.")
            change_folder_action.triggered.connect(self.change_folder)
            camera_toolbar.addAction(change_folder_action)

        def init_cameraSelectDropdown():
            camera_selector = QComboBox()
            camera_selector.addItems([c.description()
                                      for c in self.available_cameras])
            camera_selector.currentIndexChanged.connect(self.select_camera)
            camera_toolbar.addWidget(camera_selector)

        # Initialize subParts Here
        init_cameraActionButton()
        init_camera_stop_button()
        init_changeFolderButton()
        init_cameraSelectDropdown()

#

    def init_filterSideBar(self):
        sideBar = QToolBar("Sidebar")
        sideBar.setMovable(False)
        self.addToolBar(Qt.RightToolBarArea, sideBar)

        def init_filterLabelText():
            filter_label = QLabel("Export Data")
            sideBar.addWidget(filter_label)

        # def init_filterSelectDropdown():
        #     self.filters = ["Normal", "Black/White"]
        #     filter_selector = QComboBox()
        #     filter_selector.addItems([c for c in self.filters])
        #     sideBar.addWidget(filter_selector)

        def action_getDataButton():
            print("get data button")

        def init_getDataButton(self):
            button = QPushButton("Get Floc Size Data")
            button.setToolTip('Press here for real-time floc size data.')
            button.clicked.connect(action_getDataButton)
            sideBar.addWidget(button)


        # Data button

        def export(self):
            # database = r"C:\sqlite\db\pythonsqlite.db"

            # create a database connection
            conn = database2.create_connection(database)
            conn.commit()

            # create tables
            if conn is not None:
                # create projects table
                database2.expToCSV(conn)

            else:
                print("Error! cannot create the database connection.")

        def init_export():
            export_button = QPushButton("Export")
            export_button.clicked.connect(export)
            sideBar.addWidget(export_button)

        # Initialize SubParts here
        init_filterLabelText()
        # init_filterSelectDropdown()
        # init_addFilterButton()
        # init_applyFiltersButton()
        init_export()


#        def init_addFilterButton():
#            add_filterButton = QPushButton("Add")
#            add_filterButton.clicked.connect(init_filterSelectDropdown)  # FIX ME
#            sideBar.addWidget(add_filterButton)

#        def init_applyFiltersButton():
#            apply_button = QPushButton("Apply")
#            apply_button.clicked.connect(self.apply_filter)
#            sideBar.addWidget(apply_button)
        # Initialize SubParts here
#        init_filterLabelText()
#        init_filterSelectDropdown()
#        init_addFilterButton()
#        init_applyFiltersButton()
        init_getDataButton(self)

    def init_fileMenu(self, m):
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        m.addAction(exitButton)

    def init_viewMenu(self, m):
        zoomButton = QAction('Zoom', self)
        zoomButton.setShortcut('Ctrl + Shift+')
        zoomButton.triggered.connect(self.close)
        filters = QAction('Filters', self)
        filters.triggered.connect(self.close)
        m.addAction(zoomButton)
        m.addAction(filters)

    def init_toolMenu(self, m):
        exp = QAction('Export Data', self)
        exp.triggered.connect(self.close)
        m.addAction(exp)

    def select_filter(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(
            lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(
            lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(
            lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(
            lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0

    def apply_filter(self):
        print("applied")

    # def QImageToMat(self, qimg):
    #     """RGB888"""
    #     #qimg = QImage()
    #     # qimg.load("/home/auss/Pictures/test.png")
    #     qimg = qimg.convertToFormat(QImage.Format_RGB888)
    #     qimg = qimg.rgbSwapped()
    #     assert(qimg.byteCount() == qimg.width() * qimg.height() * 3)

    #     ptr = qimg.constBits()
    #     ptr.setsize(qimg.byteCount())

    #     mat = np.array(ptr).reshape(
    #         qimg.height(), qimg.width(), 3)  # Copies the data
    #     return mat

    def take_photo(self):
        self.viewfinder.setContrast(100)
        # self.viewfinder.setBrightness(0)

        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

        path = (os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        )))
        img = self.capture.capture(path)
        # qimg = QImage()
        # qimg.load('image.jpg')
        # img = self.QImageToMat(self.capture)
        # database = r"C:\sqlite\db\pythonsqlite.db"
        # create a database connection
        conn = database2.create_connection(database)
        conn.commit()
        is_empty = True
        while is_empty:
            img = cv2.imread(path)
            if img is not None:
                is_empty = False
        # create tables
        if conn is not None:
            # create projects table
            cur = conn.cursor()
            database2.add_flocs(img, cur)
            conn.commit()
            conn.close()

        else:
            print("Error! cannot create the database connection.")
        self.save_seq += 1

    def start_photo(self):
        # self.timer = QTimer(self)
        self.timer.timeout.connect(self.take_photo)
        self.timer.start(5000)
        self.timer.start()

    def stop_photo(self):
        remaining = self.timer.remainingTime()
        self.timer.stop()
        self.timer.setInterval(remaining)




    def change_folder(self):
        path = QFileDialog.getExistingDirectory(
            self, "Snapshot save location", "")
        if path:
            self.save_path = path
            self.save_seq = 0

    def alert(self, s):
        """
        Handle errors coming from QCamera dn QCameraImageCapture by displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Camera")
    model = QtSql.QSqlTableModel()

    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('flocs.db')

    # query = QtSql.QSqlQuery()
    # model = QtSql.QSqlTableModel()

    window = MainWindow()
    app.exec_()
