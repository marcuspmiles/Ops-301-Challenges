#!bin/bash

#Please use BASH to run the script and not SH
echo Hello! Welcome to my Ops301 3rd Bash Challenge
echo %%%% OPTIONS %%%%
echo OPTION 1 - Hello World
echo OPTION 2 - Ping Self
echo OPTION 3 - IP Info
echo OPTION 4 - Exit

#while loop to bring up the menu once the user selects an option
#inside the loop are conditional if statements that answer to a particular input
while [ true ]
do
  echo "Enter an option number:"
  read op
  if [ "$op" == "1" ]; then
  echo Hello World
  fi
  if [ "$op" == "2" ]; then
#pings the loopback address 4 times
  ping 127.0.0.1 -c 4
  fi
  if [ "$op" == "3" ]; then
#prints network adapter info
  ifconfig
  fi
  if [ "$op" == "4" ]; then
  echo Type CTRL + C to Exit
  fi
done
