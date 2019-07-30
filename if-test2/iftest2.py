#!/usr/bin/env python3
#user input
ipchk = input("Apply an IP Address")

#IP Match
if ipchk == "192.168.70.1":
    print("Looks like the IP address was set to Gateway: " + ipchk + "This is not recommended.")

#No IP
elif ipchk:
    print("IP not set: " + ipchk)
    
#no input
else:
    print("No data provided.")
