#!/bin/bash

workingdir=$(pwd)

#copies the below path to the cwd (working directory) and appends the date and time
cp /var/log/syslog $workingdir$(date +%m%d%Y%T) 
