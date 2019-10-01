import glob
import wx
import eyed3


# Editing the code from a tutorial
class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Name', width=140)
        self.list_ctrl.InsertColumn(1, 'Floc Count', width=140)
        self.list_ctrl.InsertColumn(2, 'Floc Size', width=200)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        edit_button = wx.Button(self, label='Edit')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    def on_edit(self, event):
        selection = self.list_ctrl.GetFocusedItem()
        if selection >= 0:
            mp3 = self.row_obj_dict[selection]
            dlg = EditDialog(mp3)
            dlg.ShowModal()
            self.update_mp3_listing(self.current_folder_path)
            dlg.Destroy()

    def update_mp3_listing(self, folder_path):
        self.current_folder_path = folder_path
        self.list_ctrl.ClearAll()

        self.list_ctrl.InsertColumn(0, 'Artist', width=140)
        self.list_ctrl.InsertColumn(1, 'Album', width=140)
        self.list_ctrl.InsertColumn(2, 'Title', width=200)
        self.list_ctrl.InsertColumn(3, 'Year', width=200)

        mp3s = glob.glob(folder_path + '/*.mp3')
        mp3_objects = []
        index = 0
        for mp3 in mp3s:
            mp3_object = eyed3.load(mp3)
            self.list_ctrl.InsertItem(index,
                                      mp3_object.tag.artist)
            self.list_ctrl.SetItem(index, 1,
                                   mp3_object.tag.album)
            self.list_ctrl.SetItem(index, 2,
                                   mp3_object.tag.title)
            mp3_objects.append(mp3_object)
            self.row_obj_dict[index] = mp3_object
            index += 1


class Mp3Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None,
                          title='Mp3 Tag Editor')
        self.panel = Mp3Panel(self)
        self.create_menu()
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, 'Open a File',
            'Open a folder with MP3s'
        )
        menu_bar.Append(file_menu, '&File')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_file,
            source=open_folder_menu_item,
        )
        self.SetMenuBar(menu_bar)

    def on_open_file(self, event):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open JPG file", wildcard="*.jpg",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    # self.doLoadDataOrWhatever(file)
                    print(file)
            except IOError:
                wx.LogError("Cannot open file '%s'." % file)


class EditDialog(wx.Dialog):
    def __init__(self, mp3):
        title = f'Editing "{mp3.tag.title}"'
        super().__init__(parent=None, title=title)
        self.mp3 = mp3
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.artist = wx.TextCtrl(
            self, value=self.mp3.tag.artist)
        self.add_widgets('Artist', self.artist)
        self.album = wx.TextCtrl(
            self, value=self.mp3.tag.album)
        self.add_widgets('Album', self.album)
        self.title = wx.TextCtrl(
            self, value=self.mp3.tag.title)
        self.add_widgets('Title', self.title)
        btn_sizer = wx.BoxSizer()
        save_btn = wx.Button(self, label='Save')
        save_btn.Bind(wx.EVT_BUTTON, self.on_save)
        btn_sizer.Add(save_btn, 0, wx.ALL, 5)
        btn_sizer.Add(wx.Button(
            self, id=wx.ID_CANCEL), 0, wx.ALL, 5)
        self.main_sizer.Add(btn_sizer, 0, wx.CENTER)
        self.SetSizer(self.main_sizer)

    def on_save(self, event):
        self.mp3.tag.artist = self.artist.GetValue()
        self.mp3.tag.album = self.album.GetValue()
        self.mp3.tag.title = self.title.GetValue()
        self.mp3.tag.save()
        self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    frame = Mp3Frame()
    app.MainLoop()
