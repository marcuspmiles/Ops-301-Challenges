# Python Script Challenge 11

# Creates a text file
f= open("file.txt","w+")

# Appends lines to text file
f=open("file.txt", "a+")
for i in range(1):
     f.write("Appended line1 %d\r\n" % (i+1))
     f.write("Appended line2 %d\r\n" % (i+1))
     f.write("Appended line3 %d\r\n" % (i+1))
f.close()

print ("Appended line1")

# Removes the file
import os
os.remove("file.txt")
