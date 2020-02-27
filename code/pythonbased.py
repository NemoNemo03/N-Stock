import pickle
d = dict(name='李小虎', age=29, score=80)
str = pickle.dumps(d)
print(str)
file2 = open("out5.txt","w")

import json
d1 = dict(name='李小虎', age=29, score=80)
str = json.dumps(d1)
print(str)
d2 = json.loads(str)
print(d2)
x=3
print(x)

#for line in open("input.txt"):
#    file2.write('"'+line+'"'+",")
#   pass

#with open('input.txt' , 'r') as f:
 #   for line in f:
  #      print(line)
#import os
#print(os.environ)
#print(os.path.abspath('.'))



