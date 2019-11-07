from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
#
import os
import sys
import time


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Floc App")
        self.initUI()
        width = self.width()
        height = self.height()
        self.setGeometry(10, 10, 800, 400)

        self.show()

    def initUI(self):
        self.init_menuBar()
        self.init_statusBar()
        self.init_camera()
        self.init_cameraBar()
        self.init_filterSideBar()

        self.show()

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

# Initialize Camera bar
    def init_cameraBar(self):
        camera_toolbar = QToolBar("Camera")
        camera_toolbar.setIconSize(QSize(45, 45))
        camera_toolbar.setMovable(False)
        self.addToolBar(Qt.BottomToolBarArea, camera_toolbar)

        def init_cameraActionButton():
            self.save_path = ""
            photoAction = QAction(
                QIcon(os.path.join('images', 'camera-black.png')), "Take photo...", self)
            photoAction.setStatusTip("Take photo of current view")
            photoAction.triggered.connect(self.take_photo)
            camera_toolbar.addAction(photoAction)

        def init_changeFolderButton():
            change_folder_action = QAction(QIcon(os.path.join(
                'images', 'blue-folder-horizontal-open.png')), "Change save location...", self)
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
        init_changeFolderButton()
        init_cameraSelectDropdown()

#

    def init_filterSideBar(self):
        sideBar = QToolBar("Sidebar")
        sideBar.setMovable(False)
        self.addToolBar(Qt.RightToolBarArea, sideBar)

        def init_filterLabelText():
            filter_label = QLabel("Filter")
            sideBar.addWidget(filter_label)

        def init_filterSelectDropdown():
            self.filters = ["Normal", "Black/White"]
            filter_selector = QComboBox()
            filter_selector.addItems([c for c in self.filters])
            sideBar.addWidget(filter_selector)

        def action_getDataButton():
            print("get data button")

        def init_getDataButton(self):
            button = QPushButton("Get Floc Size Data")
            button.setToolTip('Press here for real-time floc size data.')
            button.clicked.connect(action_getDataButton)
            sideBar.addWidget(button)

        # Data button


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
        m.addAction(zoomButton)

    def init_toolMenu(self, m):
        filters = QAction('Filters', self)
        filters.triggered.connect(self.close)
        m.addAction(filters)

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

    def take_photo(self):
        self.viewfinder.setContrast(100)
        # self.viewfinder.setBrightness(0)

        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
        self.capture.capture(os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp
        )))
        self.save_seq += 1

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

    window = MainWindow()
    app.exec_()
