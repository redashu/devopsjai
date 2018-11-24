#!/usr/bin/python2
import time   #  to  fetch current time from machine 
import  commands   #  to use base of command in python 
options='''
Press 1  to check current date and time 
Press 2  to create directory  
Press 3  to add a new user
Press 4  to install apache web server and host index.html page
Press 5  to  share a directory via NFS
Press 6  to reboot your system  
'''
print options
user_input=raw_input()
#  now implementing  conditional statement 
if  user_input ==  '1' :
	print  time.ctime()
elif user_input == '2' :
	dir_name=raw_input("plz enter directory name with or without path :  ")
	print  commands.getoutput("mkdir  "+dir_name)
	
else :
	print  "Invalid OPtion"



