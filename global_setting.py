import os

from utils.my_config import Config
from utils.my_logger import my_logger as logger
from utils.my_utils import create_folder_if_not_exists, get_current_date


class GlobalSetting:
    def __init__(self):
        self.path_config = None
        self.path_export = None
        self.excel_name = None
        self.current_path = os.getcwd()
        self.init_folder()
        self.config = Config(f"{self.path_config}\\config.ini")

    def init_folder(self):
        self.path_config = f'{self.current_path}\\config'
        self.path_export = f'{self.current_path}\\表格'
        create_folder_if_not_exists(self.path_config)
        create_folder_if_not_exists(self.path_export)

        today = get_current_date()
        self.excel_name = f'{self.path_export}\\{today}应收账款账龄分析表.xlsx'


GS = GlobalSetting()


# os.getcwd() 适用于获取运行环境的当前工作目录。
# os.path.dirname(__file__) 适用于获取脚本文件的目录路径。
