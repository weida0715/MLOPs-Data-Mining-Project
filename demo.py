import sys

from marital_satisfaction.logger import logging
from marital_satisfaction.exception import MLException

if __name__ == "__main__":
    try:
        logging.info("Logging Started")
        a = 1/0
    except Exception as e:
        logging.info(e)
        raise MLException(e, sys)
