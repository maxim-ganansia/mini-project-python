import datetime

class Logger:

    def add_to_log(self, msg):
        f = open("/Users/maxim-ilangnansia/Desktop/ITC/Cours et Exos python/Mini-project/Day-1 "
                 "(daily task)/Log/log.txt", "a+")
        date = datetime.datetime.now()
        date = date.strftime("%d-%m-%Y %H:%M:%S")
        f.write(date + msg)

