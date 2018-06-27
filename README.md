# python-logging-template
Python logging template using dictConfig

[logging config doc](https://docs.python.org/2/library/logging.config.html)

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
