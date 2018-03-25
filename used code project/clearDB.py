import subprocess
import os
#subprocess.call(["rm","snort.log.*"])
#subprocess.call(["rm","alert.csv"])
os.system('sudo rm /var/log/snort/snort.log.*')
os.system('sudo rm /var/log/snort/alert.csv')

