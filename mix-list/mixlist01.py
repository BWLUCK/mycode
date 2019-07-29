#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]

##the line below prints the Address
print("The first item in the list (IP): " + my_list[0])

##the line below prints the Port
print("The second item in the list (port): " + str(my_list[1]))

##the line below prints the port state
print("The last item in the list (state): " + my_list[2])

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "SSH" ]

print("When I: " + new_list[5] + "into IP addresses:" + new_list[3] + "or" + new_list[4] + "I am unable to ping:" + str(new_list[0]) + "," + new_list[1] + ", or" + str(new_list[2])) 

# print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping: " + str(new_list[:3]))  

