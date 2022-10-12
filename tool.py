from lib import *
import sys
import pprint

def main():
    if len(sys.argv) == 1:
        print (f"{sys.argv[0]} <branch> <branch1> --first --second --versions")
    # default arguments 
    if "https" not in str (sys.argv):
        branch1 = "sisyphus"
        branch2 = "p10"
    else:
        branch1 = sys.argv[1]
        branch2 = sys.argv[2]
    dataset = ""
    if "--first" in sys.argv:
        dataset = set ( get_list(branch1) ) - set ( get_list(branch2 ) )
    elif "second" in sys.argv:
        dataset = set ( get_list(branch1) ) - set ( get_list(branch2 ) )
    if dataset:
        pprint.pprint(dataset, width = 20, compact = True)
if __name__ == "__main__":
    main()
