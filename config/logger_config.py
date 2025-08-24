import logging


def setup_logger(name: str = "APIClient", log_file: str = "..\\logs\\api.log", level=logging.DEBUG):
    print(log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Форматтер
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Хендлер для файла
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Хендлер для консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Добавляем хендлеры (избегаем дублирования)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
