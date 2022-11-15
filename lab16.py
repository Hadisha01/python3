f = open("text.txt","r")
r = f.readlines()

print([a.rstrip('\n')for a in r]) 
print(type(r))
