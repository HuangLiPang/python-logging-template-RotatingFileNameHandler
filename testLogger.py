import logging
import logging.config
import logging_config
from logging_config import RotatingFileNameHandler

logging.config.dictConfig(logging_config.LOGGING)

# create logger
logger = logging.getLogger()
logger.addHandler(RotatingFileNameHandler(__file__, "./log"))

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")