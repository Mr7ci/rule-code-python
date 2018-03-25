#add new rule
import os
import sys
import fileinput as fileinput

def addrule(rule):
	#with open('/etc/snort/rules/local.rules', 'a') as file:
	#	file.write(rule)


	with open('/etc/snort/rules/local.rules', "r+U") as f:
	    try:
		f.seek(-1, 2)
		while f.read(1) == "\n":
		    f.seek(-2, 1)      
		                       
	    except IOError:            
		f.seek(0)              
	    else:
		f.write("\n")          
	    f.write(rule+"\n")

if __name__ == "__main__":
	#rule = input("rule:")
	#rule = str(sys.argv[1])
	rule = sys.argv[1]
	addrule(rule)