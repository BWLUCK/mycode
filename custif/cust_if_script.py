#!/usr/bin/env python3
##Determine type of tranportation solely based on miles traveled
message = "You should consider"

message1 = "Get a job! "


print("How many miles per week do you travel for work?")

miles = float(input())

if miles >= 1000:
    message = message + " moving."

elif miles >= 500:
    message = message + " a Hybrid."

elif miles >= 250:
    message = message + " a compact."

elif miles >= 100:
    message = message + " a bike."

elif miles >= 50:
    message = message + " walking."   

elif miles == 0:
    message = message1    

else:
    message = message + " youself lucky. "

print(message)
