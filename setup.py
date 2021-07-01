from distutils.core import setup
import py2exe
'''
,
              "icon_resources":[(1, r"D:\my\16x16.jpg"),
                                (2, r"D:\my\24x24.jpg"),
                                (3, r"D:\my\32x32.jpg"),
                                (4, r"D:\my\48x48.jpg"),
                                (5, r"D:\my\256x256.jpg")]
'''

 
setup(
    name="Choose_KSG",
    version="1.0",
    description="A sample app to choose KSG by grouper",
    author="brykov93@gmail.com",
    icon_file=r"D:\my\64x64.ico",
    windows=[{"script":"Choose_KSG.py",
              "icon_resources":[(1, r"D:\my\16x16.ico"),
                                (1, r"D:\my\24x24.ico"),
                                (1, r"D:\my\32x32.ico"),
                                (1, r"D:\my\48x48.ico"),
                                (1, r"D:\my\64x64.ico"),
                                (1, r"D:\my\256x256.ico")]}],
    data_files = [
            ('imageformats', [
              r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qjpeg4.dll'
              ])],
    options={"py2exe": {"includes":["sip","PyQt4","_winreg"],
                        "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe",
                                          "mswsock.dll", "powrprof.dll"]}}
)
