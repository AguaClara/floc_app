from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files = ['images'])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('camera.pyw', base=base)
]
# def find_data_file(filename):
#     if getattr(sys, 'frozen', False):
#         # The application is frozen
#         datadir = os.path.dirname(sys.executable)
#     else:
#         # The application is not frozen
#         # Change this bit to match where you store your data files:
#         datadir = os.path.dirname('')
#     return os.path.join(datadir, filename)

setup(name='FlocApp',
      version = '0.1',
      description = 'Runs scirpt that sizes and counts Flocs',
      options = dict(build_exe = buildOptions),
      executables = executables)
