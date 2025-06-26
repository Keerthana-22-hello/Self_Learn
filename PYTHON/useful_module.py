import math as m
print(m.sqrt(16))
print(m.factorial(5))
print(m.pi)
print()

#random 
import random as r
print(r.randint(1, 10))
print(r.choice(['apple','mango']))
print()

#date and time
import datetime as d
now=d.datetime.now()
print(now)
print(now.strftime("%d-%m-%Y"))
print()

# os
import os
print(os.getcwd())      # Current working directory
#os.mkdir("newFolder")   # Create a directory  and it is commmented after running it on time to avoid creating multiple file in the same name
print(os.listdir())     # List files and folders
print()

#sys
import sys
print(sys.platform)
print(sys.version)
print()

# regular expressions
import re
pattern=r"\d+"
text="My number is 8838336588"
print(re.findall(pattern,text))
print()

#handling json
import json
data = {"name" : "Keerthana", "age" : 17}
json_str  = json.dumps(data) 
print(json_str)
print()
