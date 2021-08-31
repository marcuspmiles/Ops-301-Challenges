#!/bin/bash

#copies the below path to the cwd (working directory)
cp /var/log/syslog >> /home/marcus/Challenges 

#appends the month, day, year, and time to the filename
now=$(date +"%m_%d_%Y_%T") 
#echoes the result
echo "New : /var/log/syslog_$now"
