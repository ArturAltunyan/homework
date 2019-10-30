a = 2**6

def count():
	for i in range(0,15):
		print(i, a)

count()




import threading
import logging
import datetime
import time




def tim():
	for i in range(0,10):
		print(logging.count(),datetime.datetime.now())
		time.sleep(0.001)
x = threading.Thread(target=tim)

x.start()
