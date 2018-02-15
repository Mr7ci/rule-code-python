#add new rule
import os
import sys
import fileinput as fileinput

def addrule(rule):
    with open('test.rules', 'a') as file:
        file.write(rule)

if __name__ == "__main__":
   rule = input("rule:")
   #rule = str(sys.argv[1])
   addrule(rule)