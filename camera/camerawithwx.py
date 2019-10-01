import cv2
import wx


class Camera (wx.Panel):
  def __init__(self, *args, **kw):
      super (Camera, self).__init__(*args, **kw)
      self.setWindowTitle("Floc App")
      self.initUI()
      width = self.width()
      height = self.height()
      self.setGeometry(10, 10, 800, 400)

      self.show()

  def InitUI(self):
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

  def init_camera(self):
      self.available_cameras = QCameraInfo.availableCameras()
      if not self.available_cameras:
          pass
      self.viewfinder = QCameraViewfinder()
      self.viewfinder.show()
      self.setCentralWidget(self.viewfinder)
      self.select_camera(0)