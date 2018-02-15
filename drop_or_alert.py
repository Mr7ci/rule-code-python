#change rule to drop or alert
import os
import sys
import fileinput as fileinput
def changeRuleAction(ssid,action):
    #check ssid and action correct form ? or 
    #path for pi = '/etc/snort/rules/local.rules'
    with fileinput.FileInput('test.rules', inplace=True, backup='.bak') as file:
        for num,line in enumerate(file,1):
           if ssid in line:
                if 'drop' in line:
                    print(line.replace('drop',action), end = '')
                elif 'alert' in line:
                    print(line.replace('alert',action), end = '')
           else:
                print(line, end = '')

if __name__ == "__main__":
  #changeRuleAction
  #ssid = str(sys.argv[1])
  #action = str(sys.argv[2])
  #print(ssid + action)
  #userule(ssid)
  ssid=input("ssid:")
  action=input("act:")
  changeRuleAction(ssid,action)