import time
import os

start_time = time.time()
while True:
	# os.system("cls") # on windows
	print (time.strftime("%H:%M:%S"))
	print("%s seconds" % round((time.time() - start_time)))
	time.sleep(1)
