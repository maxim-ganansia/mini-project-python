import datetime
import os
from pathlib import Path


class Logger:

    def __init__(self):
        self.path = Path(__file__)

    def add_to_log(self, msg):
        new_path = open(os.path.join(self.path.parent.parent, "Log/log.txt"), "a+")
        date = datetime.datetime.now()
        date = date.strftime("%d-%m-%Y %H:%M:%S")
        new_path.write(date + msg)
