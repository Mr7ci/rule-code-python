import os
import sys

def deleterule(ssid):
	with open("test.rules","r+") as f:
	    new_f = f.readlines()
	    f.seek(0)
	    for num,line in enumerate(new_f,1):
		if ssid not in line:
		    f.write(line)
	    f.truncate()

if __name__ == "__main__":
	ssid = str(sys.argv[1])
	deleterule(ssid)
	
