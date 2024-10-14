from PyQt5 import QtGui
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QWidget

from global_setting import GS
from gui.add_enterprise_dialog import Ui_Dialog
from gui.common_style import font_16_family, font_15_family, set_window_icon
from utils.my_logger import my_logger as logger
from utils.my_utils import get_icon


class AddEnterpriseDialogLogic(QWidget, Ui_Dialog):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        set_window_icon(self.dialog)
        self.setupUi(dialog)
        self.init_font()
        self.btn_connect()
        self.dialog.setModal(True)
        self.dialog.setWindowFlags(Qt.WindowCloseButtonHint)

    def init_font(self):
        self.label_enterprise_name.setFont(font_16_family)
        self.lineEdit_enterprise_name.setFont(font_16_family)
        self.button_add_enterprise.setFont(font_15_family)
        self.button_save_and_close.setFont(font_15_family)

    def btn_connect(self):
        self.button_add_enterprise.clicked.connect(self.save_enterprise)
        self.button_save_and_close.clicked.connect(self.save_and_close)

    def save_enterprise(self):
        enterprise_name = self.lineEdit_enterprise_name.text().strip()
        if enterprise_name == "" or enterprise_name in GS.config.get_config_options("企业列表"):
            QMessageBox.information(self, "提示", "输入的企业名称为空或已存在！")
            return False
        GS.config.update_config_value("企业列表", self.lineEdit_enterprise_name.text(), "")
        self.lineEdit_enterprise_name.setText("")
        return True

    def save_and_close(self):
        self.dialog.close()
        list_enterprise = GS.config.get_config_options("企业列表")
        logger.info(f"已添加{len(list_enterprise)}个企业, 企业列表：{list_enterprise}")
