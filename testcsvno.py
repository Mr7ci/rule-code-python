import os
import time
import json
import csv
import csvmapper
#from bson import json_util
from pymongo import MongoClient
from datetime import datetime
client = MongoClient('co-project1.eg.mahidol.ac.th:443')
db = client.snorttest

def follow(name):
    while not os.path.exists(name):
      time.sleep(1)
    if os.path.isfile(name):
      current = open(name, "r")
      curino = os.fstat(current.fileno()).st_ino
      while True:
        while True:
          line = current.readline()
          if not line:
              break
          yield line

        try:
            if os.stat(name).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
          #time.sleep(1)
    else:
       raise ValueError("%s isn't a file!" % name)


if __name__ == '__main__':
    fname = "test.log"
    #fieldnames = ("timestamp","msg","sig_id","proto","src","srcport","dst","dstport")
    for l in follow("/var/log/snort/alert.csv"):
    	data = {"timestamp":"","msg":"","sig_id":"","proto":"","src":"","srcport":"","dst":"","dstport":""}
    	words = l.split(",")
    	count =0
    	t=datetime.fromtimestamp(time.time())
    	t.strftime('%Y-%m-%d')
    	for index, item in enumerate(words):
    		if (item == "" or item == "\n"):
    			words[index]="Empty"
    	#print(words)
    	data["timestamp"]=str(t.strftime('%Y-%m-%d %H:%M:%S'))
    	data["msg"]=words[1]
    	data["sig_id"]=words[2]
    	data["proto"]=words[3]
    	data["src"]=words[4]
    	data["srcport"]=words[5]
    	data["dst"]=words[6]
    	data["dstport"]=words[7]
    	#print(data)
    	data1 = json.dumps(data)
    	data2 = json.loads(data1)
    	data2.update({'idpi':1})
    	#db.alert.insert_one(data2)
    	print(data2)
      print("Done")
    	"""data = json.loads(l)
            #data2=json.dumps(data)
            #data2["type"].append({'b':'2'})
            #data2=json.dumps(data)
            timet=str(datetime.now())
            data.update({'time':timet})
            #print(data)
            db.alert.insert_one(data)
            print("Done")"""
