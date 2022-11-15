f = open("text.txt","r")
wordsList = f.read().split()


characterList = {}
for x in wordsList:
	if x in characterList:
		characterList[x] +=1
	else:
		characterList[x] =1
print("Character frequency is")
print(characterList)





f.close()