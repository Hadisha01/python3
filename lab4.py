N = int(input("enter value:"))
f = open("text.txt", "r")

last_n_lines = f.readlines()

for line in (last_n_lines[-N:]):
    print(line, end ='')
    
f.close()
    

    
    