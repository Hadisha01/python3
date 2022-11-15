
f = open("text.txt", "a")
f.write("We have added more contents to the file.")
f.close()
f = open("text.txt", "r")
print(f.read())
