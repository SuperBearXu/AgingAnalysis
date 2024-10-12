import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from gui.add_enterprise_dialog import Ui_Dialog
# from gui.gui import Ui_MainWindow
# from utils.my_logger import my_logger as logger
from gui.logic.main_gui_logic import MainGuiLogic

VERSION = "账龄分析工具 v1.1"

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainGuiLogic(MainWindow)
    MainWindow.show()
    # FirstDialog = QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(FirstDialog)
    # FirstDialog.show()
    sys.exit(app.exec_())

