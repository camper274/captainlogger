import logging
import colorlog
from .Static import *
import functools


class CamperLogger:

    def __init__(self, function_name, **kwargs):
        self.name = function_name
        self.debug = kwargs.get('debug')
        self.log_path = kwargs.get('log_path')
        self.logger = None
        self.__init_logger()

    def __init_logger(self):
        colorlog.basicConfig(format=colorlog_format)
        self.logger = logging.getLogger(self.name)

        if self.debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        if self.log_path is None or self.log_path == '' or type(self.log_path) != str:
            self.log_path = './log/'
        elif not self.log_path.endswith('/'):
            self.log_path += '/'

    def warning(self, message):
        if self.logger is not None and message is not None:
            fh = logging.FileHandler(self.log_path + 'app-warning.log')
            fh.setLevel(logging.WARNING)
            formatter = logging.Formatter(log_format)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.warning(message)
            self.logger.removeHandler(fh)

    def error(self, message):
        if self.logger is not None and message is not None:
            fh = logging.FileHandler(self.log_path + 'app-error.log')
            fh.setLevel(logging.ERROR)
            formatter = logging.Formatter(log_format)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.error(message)
            self.logger.removeHandler(fh)

    def info(self, message):
        if self.logger is not None and message is not None:
            fh = logging.FileHandler(self.log_path + 'app-info.log')
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter(log_format)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            self.logger.info(message)
            self.logger.removeHandler(fh)


class CamperException:
    @staticmethod
    def catch(function):

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            logger = CamperLogger('camper_exception')
            try:
                return function(*args, **kwargs)
            except Exception as e:
                # log the exception
                err = " Path : {path} \n" \
                      " Function : {func} \n" \
                      " Error: {error}".format(
                    path=str(function.__code__.co_filename),
                    func=function.__name__,
                    error=e
                )
                logger.error(err)

        return wrapper
