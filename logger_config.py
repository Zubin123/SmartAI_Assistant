# logger_config.py
import logging
import os

def setup_logger():
    logger = logging.getLogger("assistant_logger")

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        # Create log directory if not exists
        log_path = "assistant_log.txt"
        log_dir = os.path.dirname(log_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        file_handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
