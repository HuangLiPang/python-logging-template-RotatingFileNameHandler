#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2018 Jun.

@author: huanglipang

logging config doc:
https://docs.python.org/2/library/logging.config.html
"""
import logging
import datetime
import time

class UTCFormatter(logging.Formatter):
    converter = time.gmtime

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
            # "()" is a special key, which indicates a custom instantiation.
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
            "class": "logging.StreamHandler"
        },
        # FileHandler will store log in file
        # "file": { 
        #     "level": "INFO",
        #     "formatter": "complete",
        #     "class": "logging.FileHandler",
        #     "filename": datetime.datetime.now().strftime("%Y-%m-%d.log")
        # },

        # RotatingFileHandler will rotate the file automatically.
        # For example, 
        # backupCount = 5, filename = "app.log"
        # output => app.log, app.log.1, app.log.2, up to app.log.5. 
        # The file being written to is always app.log. When this file is filled, 
        # it is closed and renamed to app.log.1, and if files app.log.1, app.log.2, etc. exist, 
        # then they are renamed to app.log.2, app.log.3 etc. respectively.
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
        "handlers": ["default", "rotating"],
        "level": "INFO",
        "propagate": True
    }
}