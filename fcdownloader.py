"""
Master module. Runs basic checks and then offloads all
of the real work to functions defined in other files.
"""
import os
import sys

from PySide6.QtWidgets import QLabel

import functions
from tkinter import messagebox as mb

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledAoZjWg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    #statusLabel: QLabel

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(686, 457)
        self.actionDownload = QAction(MainWindow)
        self.actionDownload.setObjectName(u"actionDownload")
        self.actionDownload.triggered.connect(self.run_clone)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionUpdate.triggered.connect(self.run_pull)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        #self.actionSettings.triggered.connect(self.tabWidget.setCurrentIndex(1))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        #self.actionExit.triggered.connect(sys.exit())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 291, 31))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 691, 401))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 40, 111, 16))
        self.installButton = QPushButton(self.tab)
        self.installButton.setObjectName(u"installButton")
        self.installButton.setGeometry(QRect(120, 60, 61, 23))
        self.installButton.clicked.connect(self.run_clone)
        #self.installButton.clicked.connect(functions.install)
        self.updateButton = QPushButton(self.tab)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(120, 90, 61, 23))
        self.updateButton.clicked.connect(self.run_pull)
        #self.updateButton.clicked.connect(functions.update)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.settingsLabel = QLabel(self.tab_2)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setGeometry(QRect(10, 0, 331, 31))
        """self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 60, 82, 17))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 51, 16))"""
        self.tabWidget.addTab(self.tab_2, "")
        #global statusLabel
        #self.statusLabel = QLabel(self.centralwidget)
        #self.statusLabel.setObjectName(u"statusLabel")
        #self.statusLabel.setGeometry(QRect(0, 400, 671, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 686, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionDownload)
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FCDownloader", None))
        self.actionDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Welcome to FCDownloader</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Install/Update FC</span></p><p><br/></p></body></html>", None))
        self.installButton.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        #self.statusLabel.setText(QCoreApplication.translate("MainWindow",
        #                                                    u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ready!</span></p></body></html>",
        #                                                    None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Settings (coming soon)</span></p></body></html>", None))
        #self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        #self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Themes</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

    def run_clone(self):
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Installing FC...</span></p></body></html>")
        functions.install()
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Installation complete!</span></p></body></html>")
        mb.showinfo("FCDownloader", "The installation has been completed.\nIf you don't see the mod in your library, restart Steam\nMake sure you have TF2 and Source SDK Base 2013 Multiplayer installed!")
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ready!</span></p></body></html>")

    def run_pull(self):
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Updating FC...</span></p></body></html>", None)
        functions.update()
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Update complete!</span></p></body></html>",None)
        mb.showinfo("FCDownloader", "Fortress Connected is now on the latest branch, you can play now!")
        #self.statusLabel.setText("<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ready!</span></p></body></html>")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())