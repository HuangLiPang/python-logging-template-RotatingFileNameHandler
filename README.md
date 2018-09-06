python-logging-template using RotatingFileNameHandler
---
Python logging template using dictConfig

Reference
---
- [logging config](https://docs.python.org/2/library/logging.config.html)
- [logging handlers](https://docs.python.org/2/library/logging.handlers.html)

Configuration
---
[logging_config.py](./logging_config.py)

Test File
---
[testLogger.py](./testLogger.py)

test output from [testLogger.py](./testLogger.py)
---
```
2018-06-27 03:58:15 PM - PID: 68496 - INFO - testLogger.py - info message
2018-06-27 03:58:15 PM - PID: 68496 - WARNING - testLogger.py - warn message
2018-06-27 03:58:15 PM - PID: 68496 - ERROR - testLogger.py - error message
2018-06-27 03:58:15 PM - PID: 68496 - CRITICAL - testLogger.py - critical message
```
