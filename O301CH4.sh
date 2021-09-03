#!bin/bash

#Please run this script using sudo bash

#Script Name: Clear Logs
#Author: Marcus
#Date of last revision: 9/3/21
#Description: Clears the /var/log/syslog & /var/log/wtmp
#Variables: None
#Functions: None

echo %%%%%%% BEFORE CONTENTS %%%%%%%
cat /var/log/syslog
cat /var/log/wtmp

echo -n "" > /var/log/syslog
echo -n "" > /var/log/wtmp

echo %%%%%%% AFTER CONTENTS %%%%%%%
cat /var/log/syslog
cat /var/log/wtmp
