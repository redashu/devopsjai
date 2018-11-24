#!/usr/bin/python2

import  commands
import time

# checking  RAM in every 5  seconds 

while  5 > 2 :
	print  commands.getoutput('free -m')
	time.sleep(5)   # delaying  5 sec 
