from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QWidget

from global_setting import GS
from gui.add_batch_dialog import Ui_AddBatchDialog
from gui.common_style import font_16_family, font_15_family, set_window_icon
from utils.my_logger import my_logger as logger


class AddEnterpriseBatchDialogLogic(QWidget, Ui_AddBatchDialog):
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
        self.dialog.setWindowTitle("导入企业列表")
        self.text_edit_add_batch.setFont(font_16_family)
        self.button_add_batch.setFont(font_15_family)

    def btn_connect(self):
        self.button_add_batch.clicked.connect(self.save_enterprise_batch)

    def save_enterprise_batch(self):
        list_enterprise = self.text_edit_add_batch.toPlainText().split("\n")
        list_enterprise = [enterprise.strip() for enterprise in list_enterprise if enterprise.strip() != ""]
        if len(list_enterprise) == 0:
            QMessageBox.information(self, "提示", "当前未输入任何内容", QMessageBox.Ok)
            return
        for enterprise in list_enterprise:
            GS.config.update_config_value("企业列表", enterprise, "")
        logger.info(f"已添加{len(list_enterprise)}个企业, 企业列表：{list_enterprise}")
        self.dialog.close()
