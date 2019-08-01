#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to screen - .read()
configblog = configfile.read()

## break configblog across line boundries (strips out \n)
configlist = configblog.splitlines()

##display list woth no "\n"
print(configlist)



## Always close your file
configfile.close()
