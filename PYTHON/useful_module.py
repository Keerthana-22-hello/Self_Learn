import math as m

print(m.sqrt(16))
print(m.factorial(5))
print(m.pi)

#random 
import random as r
print(r.randint(1, 10))
print(r.choice(['apple','mango']))

#date and time
import datetime as d

now=d.datetime.now()
print(now)
print(now.strftime("%d-%m-%Y"))