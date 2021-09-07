#Python3 Script

#Please use Python3 to run this script
#This script runs bash commands inside python

print ("Welcome to my script")

print ("%%%%%% WHOAMI %%%%%%")
import getpass
print(getpass.getuser())

print ("%%%%%% LIST HARDWARE %%%%%%")
print ("%%% PLATFORM %%%")
import platform
print(platform.system())
print ("%%% RELEASE %%%")
print(platform.release())
print ("%%% VERSION %%%")
print(platform.version())
print ("%%% PROCESSOR %%%")
print(platform.processor())
