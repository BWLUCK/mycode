#!/usr/bin/env python3
"""ALta3 Research | Author: RZFeeser@alta3.com"""

#imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # this is much easier than using the urllib.request library

    print( r.json() )
    
main()
