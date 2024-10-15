from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QWidget

from global_setting import GS
from gui.add_enterprise_batch_dialog import Ui_AddBatchDialog
from gui.common_style import font_16_family, font_15_family, set_window_icon
from utils.my_logger import my_logger as logger

global_temp_data = []


def get_debit_credit(list_debit_credit):
    inputs = []
    new_list = list_debit_credit[2:]
    for i in range(len(new_list)):
        inputs.append((new_list[i * 2], new_list[i * 2 + 1]))
        if i * 2 + 1 == len(new_list) - 1:
            break
    return inputs


class ImportDataDialogLogic(QWidget, Ui_AddBatchDialog):
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
        self.dialog.setWindowTitle("导入借贷数据")
        self.text_edit_add_batch.setPlaceholderText(
            "第一列为企业名称，第二列为期初余额，第三、四列为借贷数据，以此类推......")
        self.text_edit_add_batch.setFont(font_16_family)
        self.button_add_batch.setFont(font_15_family)

    def btn_connect(self):
        self.button_add_batch.clicked.connect(self.save_data)

    def save_data(self):
        list_lines = self.text_edit_add_batch.toPlainText().strip().split("\n")
        if len(list_lines) == 1 and list_lines[0] == "":
            QMessageBox.information(self, "提示", "当前未输入任何内容", QMessageBox.Ok)
            return
        for line in list_lines:
            new_list = line.split("\t")
            inputs = get_debit_credit(new_list)
            temp_data = {"企业": new_list[0], "初始值": new_list[1], "借贷": inputs}
            global_temp_data.append(temp_data)
        logger.info(f"本次共导入 {len(list_lines)} 项企业借贷数据！")
        self.dialog.close()
