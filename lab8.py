f = open("text.txt","r")
wordsList = f.read().split()


longestWord = len(max(wordsList, key=len))
result = [word for word in wordsList if len(word) == longestWord]


print("The following are the longest words from a text file:")
print(result)


f.close()