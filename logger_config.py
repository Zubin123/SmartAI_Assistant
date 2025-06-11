import logging

def setup_logger(name="assistant_logger", log_file="assistant_log.txt", level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # Prevent duplicate logs in some environments
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
