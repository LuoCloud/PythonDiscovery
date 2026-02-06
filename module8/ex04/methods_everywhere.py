#!/usr/bin/env python3

import sys
#sys.argv = strings


def enlarge(strings):
    word = ""
    word += strings
    for i in range(0, (8 - len(word))):
        word += "Z"
    return word

def shrink(strings): 
    return strings[:8]


if len(sys.argv) == 1:
    print("none")

else:
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) > 8:
            print(shrink(sys.argv[i]))
        elif len(sys.argv[i]) < 8:
            enlarged = enlarge(sys.argv[i])
            print(enlarged)
        else:
            print(f"{sys.argv[i]}\n")


 
[hi   bye   hi]

hi

2

print

bye

3
    
    




        
    





        
    
    













    
