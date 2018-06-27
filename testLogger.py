import logging
import logging.config
import logging_config

logging.config.dictConfig(logging_config.LOGGING)

# create logger
logger = logging.getLogger("testLogger")

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")