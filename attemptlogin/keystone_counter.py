#!/usr/bin/env python3
loginfail = 0
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1  # this is the same as loginfail = loginfail +1
print("The number of failed login attempts is " + str(loginfail))
keystone_file.close() # close the open file
