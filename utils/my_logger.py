from loguru import logger


class GlobalLogger:
    def __init__(self, log_file_path):
        # 当前文件的目录路径
        self.signal_log = None
        self.log_file_path = log_file_path
        self.init_logger()

    def init_logger(self):
        logger.add(self.log_file_path, format="{time:YYYY-MM-D HH:mm:ss} | {level} | {message}", rotation="10MB",
                   level="DEBUG", backtrace=True, diagnose=True, )
        logger.add(self.emit_log, format="{time:YYYY-MM-D HH:mm:ss} | {level} | {message}", level="INFO")

    def bind_signal(self, signal_log):
        self.signal_log = signal_log

    def emit_log(self, log):
        # 自定义日志输出函数，将日志输出到文本框
        self.signal_log.emit(log)


# f'{self.current_path}\\log'

# gl = GlobalLogger(f"{GS.path_log}\\日志.log")
my_logger = logger
