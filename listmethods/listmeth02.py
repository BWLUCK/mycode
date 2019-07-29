#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns') # this line will add dns to end of list
protoa.append('dns') # this line will add dns to end of list
print(proto)
proto2 = [22, 80, 443, 53 ] # a listof common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the extend method
print (protoa)
