#!/usr/bin/env python3
hostname = input("What value should be set for hostname? ")
## Notice  how the next line has changed
##here we use the str.lower() method to return a lower case string
## Input hostname
if hostname.lower() == "mtg":
    ## determin if input matches vaule
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")
if hostname != "mtg":
    print("Try again dummy")

## Print exiting script
print("Exiting script")
