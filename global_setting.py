import os

from utils.my_config import Config
from utils.my_logger import GlobalLogger
from utils.my_utils import create_folder_if_not_exists


class GlobalSetting:
    def __init__(self):
        self.path_log = None
        # self.path_config = None
        self.path_export = None
        self.excel_name = None
        self.current_path = os.getcwd()
        self.init_folder()
        # self.config = Config(f"{self.path_config}\\config.ini")
        self.gl = GlobalLogger(f"{self.path_log}\\日志.log")

    def init_folder(self):
        self.path_log = f'{self.current_path}\\log'
        # self.path_config = f'{self.current_path}\\config'
        self.path_export = f'{self.current_path}\\表格'
        # create_folder_if_not_exists(self.path_config)
        create_folder_if_not_exists(self.path_export)

    def set_excel_name(self, excel_name):
        self.excel_name = f'{self.path_export}\\{excel_name}.xlsx'


GS = GlobalSetting()


# os.getcwd() 适用于获取运行环境的当前工作目录。
# os.path.dirname(__file__) 适用于获取脚本文件的目录路径。
