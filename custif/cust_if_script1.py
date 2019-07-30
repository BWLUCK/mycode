#!/usr/bin/env python3
##Determine type of tranportation based on miles traveled and price of gas. 
message = "You should consider"

message1 = "Get a job! "


print("How many miles per week do you travel for work?")

miles = float(input())

print("Fuel cost per gallon")

fuel = float(input())

if miles >= 1000 and fuel >= 3:
    message = message + " moving."

elif miles >= 1000 and fuel < 3:
    message = message + " a Hybrid."

elif miles >= 500 and fuel >= 3:
    message = message + " a Hybrid."

elif miles >= 500 and fuel < 3:
    message = message + " a compact."

elif miles >= 100 and fuel >= 3:
    message = message + " an electric vehicle."

elif miles >= 100 and fuel < 3:
    message = message + " a bicycle."    

elif miles >= 50:
    message = " Buy whatever you like."

elif miles == 0:
    message = message1

else:
    message = message + " youself lucky. "

print(message)
