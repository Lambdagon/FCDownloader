"""
Master module. Runs basic checks and then offloads all
of the real work to functions defined in other files.
"""
import os
import traceback
import ctypes
from platform import system
from shutil import which
from subprocess import run
import sys
from sys import argv, exit, stdin
#from rich import print
from tkinter import messagebox
from gettext import gettext as _
from PyQt5 import QtCore, QtGui, QtWidgets
import gettext
#import gui
import functions

# Disable QuickEdit so the process doesn't pause when clicked
if system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))

#if system() == 'Linux':
    #print(_("[bold red]Due to multiple problems when running FCDownloader Qt5 Version on Linux.[/bold red]"))
    #print(_("[bold red]Linux support will be cut off.[/bold red]"))


def sanity_check():
    """
    This is mainly for Linux, because it's easy to launch it by double-clicking it, which would
    run it in the background and not show any output. PyInstaller has no way to force a terminal
    open for this on Linux. We could implement something similar to what we do to force using WT,
    but it's not a priority right now since Linux users can figure out how to use the terminal.
    """
    if not stdin or not stdin.isatty():
        print(_("Looks like we're running in the background. We don't want that, so we're exiting."))
        exit(1)

if sys.stdout.encoding == 'ascii':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding == 'ascii':
    sys.stderr.reconfigure(encoding='utf-8')

class Ui_Dialog(object):
    def setupUi(self, mainmenuDialog):
        mainmenuDialog.setObjectName("mainmenuDialog")
        mainmenuDialog.resize(400, 317)
        self.frame = QtWidgets.QFrame(mainmenuDialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 401, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.install_updateButton_1 = QtWidgets.QPushButton(self.frame)
        self.install_updateButton_1.setGeometry(QtCore.QRect(150, 170, 75, 23))
        self.install_updateButton_1.setObjectName("install_updateButton_1")
        self.mainmenuLabel_0 = QtWidgets.QLabel(self.frame)
        self.mainmenuLabel_0.setGeometry(QtCore.QRect(120, 60, 141, 21))
        self.mainmenuLabel_0.setObjectName("mainmenuLabel_0")
        self.install_updateButton_0 = QtWidgets.QPushButton(self.frame)
        self.install_updateButton_0.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.install_updateButton_0.setObjectName("install_updateButton_0")
        self.frame_2 = QtWidgets.QFrame(mainmenuDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 270, 381, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.settingsButton = QtWidgets.QPushButton(self.frame_2)
        self.settingsButton.setGeometry(QtCore.QRect(0, 10, 21, 23))
        self.settingsButton.setObjectName("settingsButton")
        self.helpButton = QtWidgets.QPushButton(self.frame_2)
        self.helpButton.setGeometry(QtCore.QRect(360, 10, 21, 23))
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(mainmenuDialog)
        QtCore.QMetaObject.connectSlotsByName(mainmenuDialog)

        self.install_updateButton_0.clicked.connect(functions.install)
        self.install_updateButton_1.clicked.connect(functions.update)

    def retranslateUi(self, mainmenuDialog):
        _translate = QtCore.QCoreApplication.translate
        mainmenuDialog.setWindowTitle(_translate("mainmenuDialog", "FCDownloader"))
        self.install_updateButton_1.setText(_translate("mainmenuDialog", "Update"))
        self.mainmenuLabel_0.setText(_translate("mainmenuDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">FCDownloader</span></p></body></html>"))
        self.install_updateButton_0.setText(_translate("mainmenuDialog", "Install"))
        self.settingsButton.setText(_translate("mainmenuDialog", "⚙︎"))
        self.helpButton.setText(_translate("mainmenuDialog", "?"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())