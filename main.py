# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtWidgets import (QApplication, QMainWindow)

from ui.ui_main import Ui_Main

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Main(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
