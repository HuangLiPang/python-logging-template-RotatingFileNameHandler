import logging
import logging.config
import logging_template
from RotatingFileNameHandler import RotatingFileNameHandler

# load config file
logging.config.dictConfig(logging_template.LOGGING)

# create logger
logger = logging.getLogger()
# RotatingFileNameHandler(filename, logPath, maxBytes=1024, backupCount=3)
logger.addHandler(RotatingFileNameHandler(__file__, "./log", maxBytes=1024, backupCount=3))

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")