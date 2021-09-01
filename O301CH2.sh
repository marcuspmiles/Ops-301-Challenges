#!/bin/bash

echo %%%% WELCOME %%%%

#inputs asking the user for a dir path and a permissions number
read -p 'Please input a directory path: ' path
read -p 'Please input permissions number: ' number
#changing directory to the input path
cd $path
#performing chmod command on the inputted permissions number
chmod -R $number
#prints all directory contents to the screen
ls -a
#shows permission settings for everything in the directory
stat -c "%a %n" $path
