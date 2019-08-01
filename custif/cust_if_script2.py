#!/usr/bin/env python3
##Determine type of transportation based on commute miles/week and average fuel price. 





message = "You should consider"

message1 = "You are very fortunate. "


print("How many miles per week do you commute to and from work?")

miles = float(input())
if miles.isdigit():
    miles = float(input())

print("Approximate cost of fuel per gallon")

fuel = float(input())
if fuel.isdigit():
    fuel = float(input())
    
else:
    print("bad input, enter numbers only")
        


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

elif miles >= 10:
    message = " Buy whatever you like."

elif miles == 0:
    message = message1

else:
    message = message + " yourself lucky. "

print(message)
