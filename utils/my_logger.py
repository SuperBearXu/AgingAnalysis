import os
from datetime import datetime

from loguru import logger


class GlobalLogger:
    def __init__(self):
        # 当前文件的目录路径
        self.signal_log = None
        self.init_logger()

    def init_logger(self):
        logger.add(self.emit_log, format="{time:YYYY-MM-D HH:mm:ss} | {level} | {message}", level="INFO")

    def bind_signal(self, signal_log):
        self.signal_log = signal_log

    def emit_log(self, log):
        # 自定义日志输出函数，将日志输出到文本框
        self.signal_log.emit(log)


gl = GlobalLogger()
my_logger = logger
