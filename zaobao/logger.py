import os
import logging
from logging.config import fileConfig

class Logger(object):
    logger = None

    @staticmethod
    def getLogger():
        if Logger.logger is None:
            directory = os.path.dirname(os.path.realpath(__file__))
            conf_file = os.path.join(directory, "logging.conf")
            fileConfig(conf_file)
            Logger.logger = logging.getLogger("file")
        return Logger.logger

