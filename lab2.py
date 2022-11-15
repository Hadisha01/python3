N = int(input("enter value:"))
f = open("text.txt", "r")
p = f.readlines()
for line in (p[:N]):
    print(line, end ='')
    
f.close()
    
    
    