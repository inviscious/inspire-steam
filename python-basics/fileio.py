# Name : James Karuri
# Date: 24/02/2026
# Program to perform file operations

# create new file 
new_file = open("student_data.txt", "r+")

# write to new file
new_file.write("{Student Name : Keyaruga sama, ID : 99421219, email : keyarualpha@gmail.com}")
new_file.close()

# read from the file
new_file = open("student_data.txt", "r+")
data = new_file.read()

print(data)
new_file.close()

# delete file
#us on module
import os
os.remove("lamamelo.txt")

# delete folder
