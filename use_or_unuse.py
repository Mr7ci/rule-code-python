#use or unuse rule 
import os
import sys
import fileinput as fileinput

def userule(ssid):
    with fileinput.FileInput('/etc/snort/rules/test.rules', inplace=True, backup='.bak') as file:
        for num,line in enumerate(file,1):
           if ssid in line:
               if '#' in line :
                   # send message to web
                   print(line, end='')
               else:
                   print('#'+line, end='')
           else: 
               print(line,end='')

if __name__ == "__main__":
    #ssid = str(sys.argv[1])
    ssid=input("ssid:")
    userule(ssid)