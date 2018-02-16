import os
import sys
with open("test.rules","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for num,line in enumerate(new_f,1):
        if "567" not in line:
            f.write(line)
    f.truncate()
