mobile=['samsung','redmi','oneplus','apple']

file=open('test.txt','w')
for items in mobile:
    file.writelines([items + "\n"])


file.close()