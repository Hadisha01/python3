testsite_array = []
with open('text.txt') as my_file:
   for line in my_file:
       testsite_array.append(line)
print(testsite_array)