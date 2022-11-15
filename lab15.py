import random

f = open("text.txt","r")
s = f.readlines()
l = random.choice(s)

print("random words:"+"\n",l)