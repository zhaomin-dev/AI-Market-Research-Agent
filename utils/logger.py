import logging
import os
from datetime import datetime

LOG_DIR = "logs"


def setup_logger():
    """初始化日志系统（只执行一次）"""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"agent_{current_date}.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # 防止重复添加 handler
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stream_handler)


def get_logger(name: str):
    """获取模块级 logger"""
    return logging.getLogger(name)