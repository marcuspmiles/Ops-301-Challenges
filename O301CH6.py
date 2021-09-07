#Python3 Script

#Please use Python3 to run this script
#This script runs bash commands inside python

print ("Welcome to my script")

# Importing the OS
import os

# Getting user ID
print ("%%%% WHO AM I? %%%%")
euid = os.geteuid()
print("User ID is:", euid)

# Getting Hardware Information
print ("%%%% FETCH HARDWARE INFO %%%%")
hardware = os.uname()
print("Hardware:", hardware)

# Getting Username
print ("%%%%%% WHOAMI %%%%%%")
import getpass
print(getpass.getuser())


