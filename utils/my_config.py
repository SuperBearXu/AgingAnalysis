import configparser

from utils.my_logger import my_logger as logger
from utils.my_utils import create_file_if_not_exists


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        create_file_if_not_exists(self.config_path)
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.init_config()

    def init_config(self):
        try:
            if not self.config.has_section("企业列表"):
                # ===== 写入新配置 =====
                self.config.add_section('企业列表')  # 添加一个新的 section
                # ===== 如果已经使用 read 读取配置，可直接使用 open(config_path, 'w') 覆盖写入 =====
                with open(self.config_path, 'w') as f:
                    self.config.write(f)
        except Exception as e:
            logger.error(f"配置文件创建失败或配置写入失败：{str(e)}")

    def get_config_value(self, section, key):
        try:
            return self.config.get(section, key)
        except Exception as e:
            print(f"配置文件读取失败：" + str(e))
            return None

    def set_config_value(self, section, key, value):
        try:
            self.config.set(section, key, value)
            self.config.write(open(self.config_path, 'a'))  # 保存数据
        except Exception as e:
            print(f"配置文件写入失败：" + str(e))

    def update_config_value(self, section, key, value):
        try:
            if self.config.has_section(section):
                self.config.set(section, key, value)
                self.config.write(open(self.config_path, 'w'))  # 保存数据
            else:
                print(f"配置文件中不存在指定的节：{section}")
        except Exception as e:
            print(f"配置文件写入失败：" + str(e))

    def get_config_options(self, section):
        try:
            return self.config.options(section)
        except Exception as e:
            print(f"配置文件读取失败：" + str(e))
            return None

    def remove_config_section(self, section):
        try:
            if self.config.has_section(section):
                self.config.remove_section(section)
                self.config.write(open(self.config_path, 'w'))  # 保存数据
                self.init_config()
        except Exception as e:
            print(f"配置文件写入失败：" + str(e))

# if __name__ == '__main__':
#     file_path = ".\\config.ini"
#     print(get_config_value(file_path, '界面配置', '会议纪要'))
#     update_config_value(file_path, '界面配置', '会议纪要', '123456')
