#!/usr/bin/python

#   import is used for loading library 
import  commands  # library to use internal command of existing OS


#            #! she bang  / hash bang --- #  taking input from user 
print  "Press 1 to print Hello :  "
print  "Press 2 to know the current date and time  :  "
print   "Press  3  to  install HTTPD :  "
choice=raw_input()

#   condition 
if  int(choice)  ==  1 :               #  : is condition termination point 

	print           "Hello"
	print  "world"

elif  int(choice)  ==  2 :

	out=commands.getoutput("date")
	print out

elif  int(choice)  ==  3 :
	print  commands.getoutput('yum  install  httpd  -y')

else  :   # this is unmatched conditional handler 

	print  "you have entered wrong number : "
	print  "choice is not matched "

	


















