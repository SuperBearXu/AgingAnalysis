import threading

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QMessageBox
from qfluentwidgets import Dialog

from global_setting import GS
from gui.common_style import font_15_family, set_window_icon
from gui.logic.add_data_logic import AddDataDialog, global_temp_data
from gui.logic.add_enterprise_batch_dialog_logic import AddEnterpriseBatchDialogLogic
from gui.logic.add_enterprise_dialog_logic import AddEnterpriseDialogLogic
from gui.logic.import_data_dialog_logic import ImportDataDialogLogic
from gui.main_gui import Ui_MainWindow
from PyQt5.QtCore import QObject, pyqtSignal


from task.processing_data import open_excel, analysis_data
from utils.my_logger import my_logger as logger
from utils.my_utils import check_file_exists


class MainGuiLogic(QObject, Ui_MainWindow):
    signal_log = pyqtSignal(str)

    def __init__(self, main_window):
        from main import VERSION
        super().__init__()
        self.setupUi(main_window)
        set_window_icon(main_window)
        main_window.setWindowTitle(VERSION)
        self.init_font()
        self.connect_signal()

    def init_font(self):
        self.button_add_enterprise.setFont(font_15_family)
        self.button_add_enterprise_batch.setFont(font_15_family)
        self.button_add_data.setFont(font_15_family)
        self.button_start_analysis.setFont(font_15_family)
        self.button_export_excel.setFont(font_15_family)
        self.button_click_refresh.setFont(font_15_family)
        self.textEditLog.setFont(font_15_family)
        self.label.setFont(font_15_family)
        from main import VERSION
        self.label.setText(VERSION)

    def connect_signal(self):
        # self.button_add_enterprise.clicked.connect(self.open_dialog_add_enterprise)
        # self.button_add_enterprise_batch.clicked.connect(self.open_dialog_add_enterprise_batch)
        self.button_add_data.clicked.connect(self.open_dialog_import_data)
        self.button_start_analysis.clicked.connect(self.open_dialog_check_excel_name)
        # self.button_export_excel.clicked.connect(self.export_excel)
        # self.button_click_refresh.clicked.connect(self.delete_all_data)

        GS.gl.bind_signal(self.signal_log)
        self.signal_log.connect(self.send_textEditLog_log)

    # def open_dialog_add_enterprise(self):
    #     dialog = QDialog()
    #     # ui_dialog = Ui_Dialog()
    #     # ui_dialog.setupUi(self.dialog)
    #     ui_dialog = AddEnterpriseDialogLogic(dialog)
    #     dialog.show()
    #     dialog.exec_()  # 显示对话框并阻塞，直到关闭

    # def open_dialog_add_enterprise_batch(self):
    #     dialog = QDialog()
    #     ui_dialog = AddEnterpriseBatchDialogLogic(dialog)
    #     dialog.exec_()

    # def open_dialog_add_data(self):
    #     dialog = AddDataDialog()
    #     dialog.exec_()  # 显示对话框并阻塞，直到关闭

    def open_dialog_import_data(self):
        dialog = QDialog()
        ui_dialog = ImportDataDialogLogic(dialog)
        dialog.exec_()

    def open_dialog_check_excel_name(self):
        try:
            # # 启动分析线程
            # if len(global_temp_data) == 0:
            #     QMessageBox.information(None, "提示", "当前未添加借贷数据，请先添加数据后再尝试分析！")
            #     return
            # dialog = QDialog()
            # ui_dialog = ExcelNameDialogLogic(dialog)
            # dialog.exec_()
            analysis_thread = threading.Thread(target=analysis_data)
            analysis_thread.start()
        except Exception as e:
            logger.error(f"分析失败：{e}")
            QMessageBox.information(None, "提示", "分析失败，请重试！")

    # def export_excel(self):
    #     if not GS.excel_name:
    #         QMessageBox.information(None, "提示", "当前未设置表格名称，请先设置表格名称后再进行导出！")
    #         return
    #     if not check_file_exists(GS.excel_name):
    #         QMessageBox.information(None, "提示", "当前未生成相关表格，请添加数据后再进行导出！")
    #         return
    #     # 启动分析线程
    #     excel_thread = threading.Thread(target=open_excel)
    #     excel_thread.start()

    # def delete_all_data(self):
    #     try:
    #         GS.config.remove_config_section("企业列表")
    #         self.textEditLog.clear()
    #         QMessageBox.information(None, "提示", "已清空应用下所有数据，请重新添加企业和借贷数据！")
    #     except Exception as e:
    #         logger.error(f"清空数据失败：{e}")
    #         QMessageBox.information(None, "提示", "清空数据失败，请重试！")

    def send_textEditLog_log(self, log):
        self.textEditLog.appendPlainText(log)
        self.textEditLog.moveCursor(QtGui.QTextCursor.End)
