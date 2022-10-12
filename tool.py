#!/usr/bin/python3.7
from lib import *
import sys
import pprint

def toprint(arg:str):
    pprint.pprint(arg, width = 50, compact = True)

def main():
    if len(sys.argv) == 1:
        print (f"{sys.argv[0]} <branch> <branch1> --first --second --versions")
        sys.exit(0)
    # default arguments 
    if "--" in str (sys.argv[1:2]):
        # list added for future functionality to compare not only 2 branches 
        branches = ["p10", "sisyphus"]
    else:
        #custom links
        branches = sys.argv[1:2]
    dataset = ""
    if "--first" in sys.argv:
        dataset = substraction(branches)
    elif "--second" in sys.argv:
        dataset = substraction(branches[::-1])
    if dataset:
        toprint(dataset)
    if "--versions":
        toprint(check_versions(branches))

if __name__ == "__main__":
    main()
