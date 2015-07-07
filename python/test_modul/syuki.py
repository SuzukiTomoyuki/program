# -*- coding: utf-8 -*- 

import threading
import time
import datetime

class TestThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print "  === start sub thread ==="
        while True:
            time.sleep(5)
            print "  sub thread : " + str(datetime.datetime.today())
        print "  === end sub thread ==="

if __name__ == "__main__":
    
    th = TestThread()
    th.start()
    