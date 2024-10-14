import threading

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox

from global_setting import GS
from gui.common_style import font_15_family, font_16_family, set_window_icon
from gui.excel_name_dialog import Ui_ExcelNameDialog
from task.processing_data import analysis_data
from utils.my_utils import get_current_date, check_file_exists


class ExcelNameDialogLogic(QWidget, Ui_ExcelNameDialog):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        set_window_icon(self.dialog)
        self.setupUi(self.dialog)
        self.dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        self.init_font()
        self.init_name()
        self.btn_connect()

    def init_font(self):
        self.label.setFont(font_15_family)
        self.lineEdit.setFont(font_15_family)
        self.pushButton.setFont(font_16_family)

    def init_name(self):
        today = get_current_date()
        self.lineEdit.setText(f"{today}")

    def btn_connect(self):
        self.pushButton.clicked.connect(self.check_and_analysis)

    def check_and_analysis(self):
        res = self.check_excel_name()
        if res:
            analysis_thread = threading.Thread(target=analysis_data)
            analysis_thread.start()

    def check_excel_name(self):
        try:
            result = check_file_exists(f'{GS.path_export}\\{self.lineEdit.text()}.xlsx')
            if result:
                res = QMessageBox.warning(self, "提示", "该文件已存在，是否覆盖？", QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
                if res == QMessageBox.Cancel:
                    return False
            GS.set_excel_name(self.lineEdit.text())
            self.dialog.close()
            return True
        except Exception as e:
            print(e)
