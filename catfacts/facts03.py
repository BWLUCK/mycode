#!/usr/bin/env python3
"""ALta3 Research | Author: RZFeeser@alta3.com"""

#imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    ## catfacts is our iterable -- that just means it will take on the values found within
    ## r.json()["all"],  one after the next -- which happensto be a dictionary 
    ## the code within the loop, says, "from that single dictionary print the value associated with text"

    for catfact in r.json()["all"]:
        print(catfact.get("text"))   # the .get() method retuns NONEif key not found

main()
