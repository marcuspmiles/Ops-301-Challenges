# Python Script

# Importing the request library
import requests

# Two inputs asking for a URL and an HTTP method along with a print outputting a list
str_in = input("Please enter a destination URL: ")
print ("GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS - Select GET for demo purposes")
method_in = input("Please enter an HTTP Method of the following options: ")

# Conformation text
print ("You are about to send a",(method_in),"request to",(str_in))

# Conformation input
con_firm = input("Are you sure you want to proceed? y/n: ")

# If statement to follow conformation
if con_firm == "y":
 print (requests.get(str_in))

# Response variable
response = requests.get(str_in)

# Translating response code to plain text
if response:
  print ('Success')
else:
  print ('Error')
