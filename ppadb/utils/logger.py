import logging

logging.getLogger("ppadb").setLevel(logging.CRITICAL)


class AdbLogging:
    PACKAGE_NAME = "ppadb"
    _default_format: logging.Formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                                                           datefmt='%d-%m-%Y:%H:%M:%S')
    DEFAULT_LEVEL = logging.CRITICAL

    @classmethod
    def get_logger(cls, name: str):
        if not name.startswith(cls.PACKAGE_NAME):
            raise RuntimeError(
                "The package logger name should be 'adb.xxx.xxx' but {}".format(name))

        logger = logging.getLogger(name)
        if logger.handlers:
            logger.handlers[0].setFormatter(cls._default_format)

        return logger

    @classmethod
    def set_default_format(cls, format: logging.Formatter):
        cls._default_format = format

    @property
    def DEFAULT_FORMAT(cls):
        return cls._default_format

    @classmethod
    def disable(cls):
        logging.getLogger(cls.PACKAGE_NAME).setLevel(logging.CRITICAL)

    @classmethod
    def enable(cls, level: int = logging.DEBUG):
        logging.getLogger(cls.PACKAGE_NAME).setLevel(level)
