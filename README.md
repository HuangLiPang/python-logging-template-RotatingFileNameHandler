python-logging-template
---
Python logging template using dictConfig

Reference
---
[logging config](https://docs.python.org/2/library/logging.config.html)
[logging handlers](https://docs.python.org/2/library/logging.handlers.html)

Configuration
---
[logging_config.py](./logging_config.py)
```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        # local time
        "standard": { 
            "format": "%(asctime)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        },
        "complete": {
            "format": "%(asctime)s - PID: %(process)d"\
                      " - %(levelname)s - %(filename)s - %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        },
        "utc": {
            "()": UTCFormatter,
            "format": "%(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p"
        }
    },
    "handlers": {
        # StreamHandler will show log in console
        "default": { 
            "level": "INFO",
            "formatter": "complete",
            "class": "logging.StreamHandler",
        },
        # FileHandler will show log in file
        "file": { 
            "level": "INFO",
            "formatter": "complete",
            "class": "logging.FileHandler",
            "filename": datetime.datetime.now().strftime("%Y-%m-%d.log"),
        },
        # RotatingFileHandler will rotate the file automatically.
        "rotating": { 
            "level": "INFO",
            "formatter": "complete",
            "class": "logging.handlers.RotatingFileHandler",
            # need an absolute path for log file
            "filename": "example.log",
            "maxBytes": 1024,
            "backupCount": 3
        }
    },
    # root logger
    "root": {
        "handlers": ["default", "file"],
        "level": "INFO",
        "propagate": True
    }
}
```
Test File
---
[testLogger.py](./testLogger.py)
```python
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
```

test output from [testLogger.py](./testLogger.py)
---
```
2018-06-27 03:58:15 PM - PID: 68496 - INFO - testLogger.py - info message
2018-06-27 03:58:15 PM - PID: 68496 - WARNING - testLogger.py - warn message
2018-06-27 03:58:15 PM - PID: 68496 - ERROR - testLogger.py - error message
2018-06-27 03:58:15 PM - PID: 68496 - CRITICAL - testLogger.py - critical message
```
