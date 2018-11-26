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
elif user_input == '4'	 :
	commands.getoutput('yum  install httpd -y')
	content=raw_input("enter content for your page : ")
	commands.getoutput('echo '+content+' >/var/www/html/index.html')
	commands.getoutput('systemctl start httpd ')
	commands.getoutput('iptables -F')

elif  user_input  == '5' :
	commands.getoutput('yum  install nfs-utils -y')
	commands.getoutput('systemctl enable --now nfs-server')
	dir_name=raw_input("enter directory name with path:  ")
	cliip=raw_input("enter client IP  ")
	s_mode=raw_input("enter shareable mode like ro , rw   ")
	nfs_entry=dir_name+"   "+cliip+"("+s_mode+")"
	commands.getoutput('echo '+nfs_entry+' >>/etc/exports')
	commands.getoutput('exportfs -r')


	
else :
	print  "Invalid OPtion"



